import factory

from ..models import InitialFile


class InitialFileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InitialFile
