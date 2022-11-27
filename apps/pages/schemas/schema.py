import logging

import graphene
from graphene_django import DjangoObjectType

from apps.base.utils import model_to_dict
from apps.pages.models import Page


logger = logging.getLogger(__name__)


class PageType(DjangoObjectType):
    class Meta:
        model = Page
        fields = ["key_name", "title", "content"]


class Query(graphene.ObjectType):
    get_page = graphene.Field(PageType, key_name=graphene.String(), lng=graphene.String())

    def resolve_get_page(self, info, key_name=None, lng=None, **kwargs):
        page = Page.objects.filter(key_name=key_name).first()
        if not page or not key_name:
            page = Page.objects.filter(key_name="general").first()
        if lng:
            page = page.translate(lng)
            logger.info(f"Get translated page detail: {model_to_dict(page)}")
        return page
