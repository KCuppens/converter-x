from django.db import models

from apps.base.models import BaseModel, SeoModel, StateModel
from apps.translations.models import Translatable


class Page(BaseModel, SeoModel, Translatable, StateModel):
    key_name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.key_name

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ["-date_created"]

    class TranslatableMeta:
        fields = [
            "key_name",
            "title",
            "content",
            "meta_title",
            "meta_description",
            "meta_keywords",
        ]
