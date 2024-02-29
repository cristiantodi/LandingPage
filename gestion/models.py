from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    contrasena = models.CharField(max_length=128)

    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    # Otros campos del modelo...
    def __str__(self):
        return str(self.nombre)