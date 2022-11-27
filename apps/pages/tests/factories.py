import factory.fuzzy

from apps.pages.models import Page


class PageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Page

    key_name = factory.fuzzy.FuzzyText(length=12)
    title = factory.fuzzy.FuzzyText(length=48)
    content = factory.fuzzy.FuzzyText(length=36)
