from django.contrib import admin
from clients.models import ClientStatusModel

class ClientStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)

    readonly_fields = ("slug",)

admin.site.register(ClientStatusModel, ClientStatusAdmin)


