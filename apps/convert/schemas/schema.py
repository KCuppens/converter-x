import graphene

from apps.action.models import Action
from apps.action.schemas.schema import ActionType
from apps.convert.services.ConvertEngine import ConvertEngine
from apps.initial_files.constants import STATUS_OPEN


class ConvertAction(graphene.Mutation):
    action = graphene.Field(ActionType)
    errors = graphene.List(graphene.String)
    successes = graphene.List(graphene.String)

    def mutate(self, info, **kwargs):
        request = info.context
        action_obj = Action.objects.new_or_get(request)
        errors = []
        if not action_obj.conversions.exists():
            errors.append("You don't have any files to convert.")

        # Loop through initial files and filter on status
        for conversion in action_obj.conversions.filter(status=STATUS_OPEN):
            from_action = conversion.from_action
            to_action = conversion.to_action
            if conversion.initial_file.status == STATUS_OPEN and from_action and to_action:
                if ConvertEngine.check_conversion_exists(from_action, to_action):
                    ConvertEngine.convert(action_obj, conversion)
                else:
                    errors.append(
                        f"Conversion from {from_action} to {to_action} does not exist "
                        f"for conversion {conversion.id}."
                    )
            else:
                errors.append("Please make sure your desired file type is set.")
        return ConvertAction(action=action_obj, errors=errors)


class Mutation(graphene.ObjectType):
    convert_action = ConvertAction.Field()
