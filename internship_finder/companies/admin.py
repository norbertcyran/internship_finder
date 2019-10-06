from django.contrib import admin

from .models import Office, Company


class OfficeAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Office, OfficeAdmin)
admin.site.register(Company, CompanyAdmin)
