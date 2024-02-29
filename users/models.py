from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
# Create your models here.


class User(AbstractUser):
    username  = models.CharField(max_length=150, unique=True)
    password  = models.CharField(max_length=128)

    def before_save_instance(self, instance, using_transactions, dry_run):
        # Asegúrate de aplicar make_password a la contraseña antes de guardar
        instance.password = make_password(instance.password)
        super().before_save_instance(instance, using_transactions, dry_run)

    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    # Otros campos del modelo...
    def __str__(self):
        return str(self.username )
    pass 