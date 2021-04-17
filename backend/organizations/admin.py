from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Organization, Domain


@admin.register(Organization)
class OrganizationAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'paid_until',)


@admin.register(Domain)
class DomainAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('domain',)
