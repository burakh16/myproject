from django.db import models

from common.models import TimestampMixin


class Organization(TimestampMixin):
    name = models.CharField(max_length=30, unique=True)
    trial = models.BooleanField(default=True)
