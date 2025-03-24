from django.contrib import admin
from clients.models import ClientModel


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'contact_name', 'email', 'status')
    search_fields = ("company_name", "contact_name", "email")
    list_filter = ('status',)

    list_editable = ('status',)

    ordering = ('company_name',)

    readonly_fields = ("slug",)


    fieldsets = (
        ("Información del cliente", {
            "fields": ("company_name", "contact_name", "email", 'slug', "status")
        }),
    )

    add_fieldsets = (
        ("Creación del cliente", {
            "classes": ("wide",),
            "fields": ("company_name", "contact_name", "email", "status",)
        }),
    )


admin.site.register(ClientModel, ClientAdmin)


