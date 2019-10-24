from django.contrib import admin

from .models import Office, Company


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
