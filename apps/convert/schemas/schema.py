import graphene
from apps.s3.file_handling import delete_object
from graphene_django import DjangoObjectType

from apps.action.models import Action
from apps.action.schemas.schema import ActionType
from apps.convert.models import Convert
from apps.convert.services.ConvertEngine import ConvertEngine


class ConvertType(DjangoObjectType):
    class Meta:
        model = Convert


class RemoveConvert(graphene.Mutation):
    convert = graphene.Field(ConvertType)
    message = graphene.String()

    class Arguments:
        convert = graphene.String()

    def mutate(self, info, **kwargs):
        convert = kwargs.get("convert")
        convert_obj = Convert.objects.filter(id=convert).first()
        if convert_obj:
            # Remove initial file and conversion file from s3
            if convert_obj.initial_file:
                delete_object("converterx", str(convert_obj.initial_file.file))
            if convert_obj.conversion_files.exists():
                for conversion_file in convert_obj.conversion_files.all():
                    delete_object("converterx", str(conversion_file.file))
            # Delete from action
            action_obj = Action.objects.filter(converts__id=convert_obj.id).first()
            action_obj.converts.remove(convert_obj)
            # Delete object
            convert_obj.delete()
            message = "Convert is removed."
        else:
            message = "Convert does not exist."
        return RemoveConvert(convert=convert_obj, message=message)


class ConvertAction(graphene.Mutation):
    action = graphene.Field(ActionType)
    errors = graphene.List(graphene.String)
    successes = graphene.List(graphene.String)

    def mutate(self, info, **kwargs):
        request = info.context
        action_obj = Action.objects.new_or_get(request)
        errors = []
        successes = []
        if not action_obj.converts.exists():
            errors.append("You don't have any files to convert.")

        # Loop through initial files and filter on status
        for convert in action_obj.converts.filter(status="open"):
            if convert.initial_file.status == "open" and convert.from_action and convert.to_action:
                if ConvertEngine.check_correct_file_type(
                    convert.from_action, convert.initial_file.mimetype
                ):
                    ConvertEngine.convert(convert)
                    successes.append(
                        f"We are converting ({convert.initial_file.file.name})"
                        f"to {convert.initial_file.mimetype}."
                    )
                else:
                    errors.append(
                        f"The uploaded ({convert.initial_file.file.name}) file"
                        "doesn't have the correct type "
                        f"{convert.initial_file.mimetype}"
                        f" instead of {convert.from_action}"
                    )
            else:
                errors.append("Please make sure your desired file type is set.")
        return ConvertAction(action=action_obj, successes=successes, errors=errors)


class SetConvertToTypeAction(graphene.Mutation):
    convert = graphene.Field(ConvertType)
    message = graphene.String()

    class Arguments:
        convert_id = graphene.String(required=True)
        to_action = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        convert_id = kwargs.get("convert_id", None)
        to_action = kwargs.get("to_action", None)
        convert_obj = Convert.objects.filter(id=convert_id).first()
        if convert_obj and to_action:
            convert_obj.to_action = to_action
            if convert_obj.from_action:
                conversion_exists = ConvertEngine.check_conversion_exists(
                    convert_obj.from_action, to_action
                )
                if conversion_exists:
                    convert_obj.save(update_fields=["to_action"])
                    message = "To action has been set successfully."
                else:
                    convert_obj.to_action = ""
                    message = "This conversion does not " "exist yet in our system."
            else:
                convert_obj.save(update_fields=["to_action"])
                message = "To action has been set successfully."
        return SetConvertToTypeAction(message=message, convert=convert_obj)


class Mutation(graphene.ObjectType):
    convert_action = ConvertAction.Field()
    remove_convert = RemoveConvert.Field()
    set_convert_to_type_action = SetConvertToTypeAction.Field()
