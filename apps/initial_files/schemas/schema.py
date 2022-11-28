import mimetypes

import graphene
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload

from apps.action.models import Action
from apps.action.schemas.schema import ActionType
from apps.convert.services.ConvertEngine import ConvertEngine
from apps.initial_files.models import InitialFile
from apps.initial_files.utils import uploading_initial_file


class InitialFileType(DjangoObjectType):
    class Meta:
        model = InitialFile


class UploadToInitialFiles(graphene.Mutation):
    action = graphene.Field(ActionType)
    message = graphene.String()

    class Arguments:
        file = Upload(required=True)
        from_action = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        file = kwargs.get("file")
        from_action = kwargs.get("from_action")
        request = info.context
        action_obj = Action.objects.new_or_get(request)
        mime_type = mimetypes.guess_type(file.name)[0]
        if not mime_type:
            message = "Please upload a valid file."
        check_correct_file_type = ConvertEngine().check_correct_file_type(from_action, mime_type)
        if not check_correct_file_type:
            message = f"This is not the correct file type. Please upload a {from_action} file."
        check_mime_type_supported = ConvertEngine().check_mime_type_supported(mime_type)
        if not check_mime_type_supported:
            message = "This file type is not yet suppported for conversion. We will hurry to add."
        if file and check_correct_file_type and check_mime_type_supported:
            uploaded_file = uploading_initial_file(file, action_obj, from_action)
            if uploaded_file:
                message = "Initial file is uploaded"
            else:
                message = "File upload failed, Please try again!"
        return UploadToInitialFiles(message=message, action=action_obj)


class Mutation(graphene.ObjectType):
    upload_to_initial_files = UploadToInitialFiles.Field()
