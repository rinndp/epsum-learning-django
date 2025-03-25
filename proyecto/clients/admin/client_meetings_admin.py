from django.contrib import admin

from clients.models import MeetingModel


class MeetingAdmin(admin.ModelAdmin):
    list_display = ("id","purpose", "date",)
    search_fields = ("purpose", "date")

    ordering = ("-date",)

    list_filter = ("date",)

admin.site.register(MeetingModel, MeetingAdmin)
