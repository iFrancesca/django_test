from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .custom_site import custom_site

@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user',
                    'change_message']