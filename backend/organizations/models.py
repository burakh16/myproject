from datetime import timedelta, date

from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from rest_framework.exceptions import ValidationError

from common.models import TimestampMixin
from users.models import User


class OrganizationManager(models.Manager):
    def create_organization(self, organization_name, username, name, email, password):
        is_exist = self.filter(name=organization_name).exists()
        if is_exist:
            raise ValidationError("This organization already exist!")
        tenant = Organization(schema_name=organization_name,
                              name=organization_name,
                              paid_until=date.today() + timedelta(days=30),
                              on_trial=False)
        # tenant.save()

        domain = Domain(domain=organization_name + '.localhost',
                        tenant=tenant,
                        is_primary=False)

        domain.domain = 'my-domain.com'
        domain.tenant = tenant
        domain.is_primary = True
        # domain.save()

        # user = User.objects.create_user(
        #   username=username, email=email, password=password, name=name, is_active=False)


class Organization(TenantMixin):
    name = models.CharField(max_length=30, unique=True)
    paid_until = models.DateField()
    on_trial = models.BooleanField(default=True)
    craeted_at = models.DateTimeField(auto_now_add=True)

    auto_create_schema = True

    objects = OrganizationManager()


class Domain(DomainMixin):
    pass


class OrganizationToken(TimestampMixin, TenantMixin):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    token = models.CharField(max_length=35)
