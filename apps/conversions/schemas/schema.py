import graphene
from graphene_django import DjangoObjectType

from apps.action.models import Action
from apps.conversions.models import Conversion
from apps.convert.services.ConvertEngine import ConvertEngine


class ConversionType(DjangoObjectType):
    class Meta:
        model = Conversion


class RemoveConversion(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        conversion_id = graphene.String()

    def mutate(self, info, **kwargs):
        conversion_id = kwargs.get("conversion_id")
        conversion_obj = Conversion.objects.get(id=conversion_id)
        # Remove initial file and conversion file from s3
        if conversion_obj.initial_file:
            conversion_obj.initial_file.delete()
        if conversion_obj.converted_file:
            conversion_obj.converted_file.delete()
        # Delete from action
        action_obj = Action.objects.get(conversions__id=str(conversion_obj.id))
        action_obj.conversions.remove(conversion_obj)
        # Delete object
        conversion_obj.delete()
        return RemoveConversion(message="Conversion is removed.")


class SetConversionToAction(graphene.Mutation):
    conversion = graphene.Field(ConversionType)
    message = graphene.String()

    class Arguments:
        conversion_id = graphene.String(required=True)
        to_action = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        conversion_id = kwargs.get("conversion_id")
        to_action = kwargs.get("to_action")
        conversion_obj = Conversion.objects.get(id=conversion_id)
        if conversion_obj.from_action:
            conversion_exists = ConvertEngine().check_conversion_exists(
                conversion_obj.from_action, to_action
            )
            if conversion_exists:
                conversion_obj.to_action = to_action
                conversion_obj.save(update_fields=["to_action"])
                message = "The to action in the conversion has been successfully set."
            else:
                message = "This conversion does not exist yet in our system."
        else:
            message = "Please set a from action first in your conversion."
        return SetConversionToAction(message=message, conversion=conversion_obj)


class Mutation(graphene.ObjectType):
    set_conversion_to_action = SetConversionToAction.Field()
    remove_conversion = RemoveConversion.Field()
