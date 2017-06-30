from django.contrib import admin

from . import models


@admin.register(models.HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('time', 'type', 'latitude', 'longitude', 'resolved')
    list_filter = ('type', 'resolved')
    ordering = ('-time',)
