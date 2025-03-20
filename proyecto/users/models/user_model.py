from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from users.models.role_model import Role


class CustomUserManager(BaseUserManager):
    # Datos de la clase por defevto de Django:
        # Username, password, is_active, is_staff, is_superUser

    # Crear usuario
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email')

        if not password:
            raise ValueError('Users must have a password')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    # Crear admin
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# AbstractUser --> Modificar estructura del user en la BD
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name="Correo electrónico")
    password = models.CharField(max_length=150, verbose_name="Contraseña")

    is_active = models.BooleanField(default=True, verbose_name="¿El usuario está activo?")
    is_superuser = models.BooleanField(default=False, verbose_name="¿Es administrador?")
    is_staff = models.BooleanField(default=False, verbose_name="Autorizado para ser staff")

    #Relación One-To-Many -> se hace con Foreign Key
    role = models.ForeignKey(Role, on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Seleccione el rol del usuario")

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'




