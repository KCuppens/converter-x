import graphene
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload

from apps.action.models import Action
from apps.action.schemas.schema import ActionType
from apps.initial_files.models import InitialFile
from apps.initial_files.utils import uploading_initial_file


class InitialFileType(DjangoObjectType):
    class Meta:
        model = InitialFile


class Query(graphene.ObjectType):
    get_initial_file = graphene.Field(InitialFileType, id=graphene.String(required=True))

    def resolve_get_initial_file(self, info, id, **kwargs):
        return InitialFile.objects.filter(id=id).first()


class UploadToInitialFiles(graphene.Mutation):
    action = graphene.Field(ActionType)
    message = graphene.String()

    class Arguments:
        file = Upload(required=True)

    def mutate(self, info, **kwargs):
        file = kwargs.get("file")
        request = info.context
        action_obj = Action.objects.new_or_get(request)
        # check_supported_file_type = CompressEngine().check_supported_file_type(file)
        if file:
            uploaded_file = uploading_initial_file(file, action_obj)
            if uploaded_file:
                message = "Initial file is uploaded"
            else:
                message = "File upload failed, Please try again!"
        elif not file:
            message = "We currently do not support this filetype. We will hurry!"
        else:
            message = "Please select file before upload ..."
        message = UploadToInitialFiles(message=message, action=action_obj)
        return message


class Mutation(graphene.ObjectType):
    upload_to_initial_files = UploadToInitialFiles.Field()
