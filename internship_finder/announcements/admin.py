from django.contrib import admin

from .models import Announcement, Application


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    pass


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass
