from django.contrib import admin
from users.models import Role


class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "slug") #Elementos que apareceran en la pantalla
    list_filter = ("name",) #Filtro
    search_fields = ("name",) #Aparezca un buscador y busque items por nombre

    readonly_fields = ("slug",) #Campos de solo lectura

    ordering = ("name",) #Orden de la lista (alfabeticamente)

admin.site.register(Role, RoleAdmin)