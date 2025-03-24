import secrets

from django.db import models


class ClientStatusModel (models.Model):
    name = models.CharField(unique=True, verbose_name="Nombre del estado")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción", help_text="Campo opcional")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="Slug del estado")

    class Meta:
        db_table = 'clients_status'
        verbose_name = 'Estado del cliente'
        verbose_name_plural = 'Estados de los clientes'

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_urlsafe(16)
            while ClientStatusModel.objects.filter(slug=prov).exists:
                prov = secrets.token_urlsafe(16)
            self.slug = prov
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

class ClientModel(models.Model):
    company_name = models.CharField(max_length=150, unique=True, verbose_name='Nombre de compañia', help_text='Campo obligatorio')
    contact_name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Persona de contacto', help_text='Campo obligatorio')
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name='Correo de contacto', help_text='Campo obligatorio')
    phone = models.CharField(blank=True, null=True, verbose_name='Teléfono de contacto', help_text='Campo opcional')
    status = models.ForeignKey("ClientStatusModel", on_delete=models.RESTRICT, null=True, blank=True, related_name='clients', verbose_name="Estado del cliente", help_text="Campo opcional")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="Slug del cliente")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        db_table = 'clients'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_urlsafe(16)
            while ClientModel.objects.filter(slug=prov).exists:
                prov = secrets.token_urlsafe(16)
            self.slug = prov
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.company_name}'

