from django.contrib import admin
from django.db import models, transaction

from martor.widgets import AdminMartorWidget

from apps.pages.models import Page
from apps.translations.admin import TranslatableAdmin, TranslationInline
from apps.translations.tasks import translate_object


class PageAdmin(TranslatableAdmin, admin.ModelAdmin):
    actions = ["make_published", "make_draft"]
    search_fields = ("key_name", "title", "content")
    list_display = ("key_name", "title", "state", "content")
    list_editable = ("state",)

    formfield_overrides = {
        models.TextField: {"widget": AdminMartorWidget},
    }
    inlines = [
        TranslationInline,
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        transaction.on_commit(lambda: translate_object.delay("pages.Page", obj.id))
        super().save_model(request, obj, form, change)


admin.site.register(Page, PageAdmin)
