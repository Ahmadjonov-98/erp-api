from django.db import models
from django.db.models import Model, TextField, DateTimeField,CharField

from apps.common.models import TimeStampedModel


class Event(TimeStampedModel):
    name = CharField(max_length=128)
    decription = TextField()
    date = DateTimeField()

    class Meta:
        db_table = 'event'

    def __str__(self):
        return self.name
