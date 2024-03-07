from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from django.conf import settings


class InformacionModelo(models.Model):
    observacion     = models.CharField(max_length=300, blank=True, null=True)
    comentario      = models.CharField(max_length=300, blank=True, null=True)

    # def __str__(self):
    #     return f"{self.observacion} - {self.comentario}"
    
