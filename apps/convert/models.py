from django.db import models

import apps.data.constants as C
from apps.conversion_file.models import ConversionFile
from apps.initial_file.models import InitialFile

from apps.base.models import Base


class Convert(Base):
    # The storage of files in session
    initial_file = models.ForeignKey(InitialFile, on_delete=models.CASCADE)
    conversion_files = models.ManyToManyField(ConversionFile, blank=True)
    # The from and to of the action
    from_action = models.CharField(max_length=255, null=True, blank=True)
    to_action = models.CharField(max_length=255, null=True, blank=True)

    status = models.CharField(max_length=255, choices=C.STATUSES_FILE, default=C.STATUS_OPEN)
