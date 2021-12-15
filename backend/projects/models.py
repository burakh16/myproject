from django.db import models

from common.models import TimestampMixin, UserMixin


class Project(TimestampMixin, UserMixin):
    STATUS_CHOICE = [
        (1, 'Open'),
        (2, 'Closed'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICE, default=1)
