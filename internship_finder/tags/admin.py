from django.contrib import admin
from django.contrib.admin import register

from .models import Tag


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
