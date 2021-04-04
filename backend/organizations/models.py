from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from rest_framework.exceptions import ValidationError

from common.models import TimestampMixin


class OrganizationManager(models.Manager):
    def create_organization(self, name):
        is_exist = self.filter(name=name).exists()
        if is_exist:
            raise ValidationError("This organization already exist!")


class Organization(TenantMixin):
    name = models.CharField(max_length=30, unique=True)
    paid_until = models.DateField()
    on_trial = models.BooleanField(default=True)
    craeted_at = models.DateTimeField(auto_now_add=True)

    auto_create_schema = True

    objects = OrganizationManager()


class Domain(DomainMixin):
    pass
