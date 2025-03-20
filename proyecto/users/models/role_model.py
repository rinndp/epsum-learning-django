
from django.db import models
from django.utils.text import slugify


class Role(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name="Nombre del rol", help_text="Solo ADMIN y CLIENT")
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        db_table = "roles"
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            cont = 1
            while Role.objects.filter(slug=slug).exists():
                slug = f"{slug}-{cont}"
                cont += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


