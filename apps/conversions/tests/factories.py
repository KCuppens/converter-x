import factory

from ..models import Conversion


class ConversionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Conversion
