from django.db import models


class MeetingModel(models.Model):
    purpose = models.TextField(max_length=150, null=False, blank=False, verbose_name='Proposito de reunión', help_text="Campo obligatorio - máximo 150 caractéres")
    date = models.DateTimeField(verbose_name='Fecha de reunión')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        db_table = 'meetings'
        verbose_name = 'Reunión'
        verbose_name_plural = 'Reuniones'

    def __str__(self):
        return f"{self.purpose}"
