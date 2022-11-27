from django.db import models

from apps.action.managers import ActionManager
from apps.base.models import BaseModel
#from apps.compression.models import Compression


class Action(BaseModel):
    # The storage of files in session
    #conversions = models.ManyToManyField(Conversion, blank=True)

    objects = ActionManager()

    def __str__(self):
        return str(self.id)
