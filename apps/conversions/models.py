from django.db import models

from apps.base.models import BaseModel
from apps.converted_files.models import ConvertedFile
from apps.initial_files.models import InitialFile

from .constants import STATUS_OPEN, STATUSES_FILE


class Conversion(BaseModel):
    initial_file = models.ForeignKey(InitialFile, blank=True, null=True, on_delete=models.CASCADE)
    converted_file = models.ForeignKey(
        ConvertedFile, blank=True, null=True, on_delete=models.CASCADE
    )

    # The from and to of the action
    from_action = models.CharField(max_length=255, null=True, blank=True)
    to_action = models.CharField(max_length=255, null=True, blank=True)

    status = models.CharField(max_length=255, choices=STATUSES_FILE, default=STATUS_OPEN)
