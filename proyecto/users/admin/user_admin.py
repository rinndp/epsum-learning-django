from django.contrib import admin
from users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "password", "is_active", "is_superuser")
    list_filter = ("is_superuser", "is_active",)
    search_fields = ("email",)

    list_editable = ("is_superuser", "is_active",) #Editar campos directamente en el panel

    readonly_fields = ("email", "password",)
    ordering = ("email",)

    fieldsets = (
        ("Información del usuario", {
            "fields": ("email", "password", "role")
        }),

        ("Permisos del usuario", {
            "fields": ("is_active", "is_staff", "is_superuser")
        })
    )

    add_fieldsets = (
        ("Creación de usuario", {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_active", "is_staff")
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)