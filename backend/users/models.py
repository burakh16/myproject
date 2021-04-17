from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    first_name = None
    last_name = None
    name = models.CharField(_("Name of user"), max_length=50)
