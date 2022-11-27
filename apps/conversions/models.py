from django.db import models

from apps.base.models import BaseModel
from apps.converted_files.models import ConvertedFile
from apps.initial_files.models import InitialFile


class Conversion(BaseModel):
    initial_file = models.ForeignKey(InitialFile, blank=True, null=True, on_delete=models.CASCADE)
    converted_file = models.ForeignKey(
        ConvertedFile, blank=True, null=True, on_delete=models.CASCADE
    )
