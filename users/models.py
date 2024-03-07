from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
# Create your models here.


class User(AbstractUser):
    username            = models.CharField(max_length=150, unique=True)
    password            = models.CharField(max_length=500)
    fullName            = models.CharField(max_length=128)
    obligacion          = models.CharField(max_length=128)
    valor_proxima_cuota = models.CharField(max_length=128, blank=True, null=True)
    nro_cuota_pagada    = models.CharField(max_length=128, blank=True, null=True)
    nro_cuota_pactada   = models.CharField(max_length=128, blank=True, null=True)
    banca               = models.CharField(max_length=128, blank=True, null=True)
    producto            = models.CharField(max_length=128, blank=True, null=True)
    destino_credito     = models.CharField(max_length=128, blank=True, null=True)
    fecha_desembolso    = models.DateField(blank=True, null=True)
    dias_mora           = models.CharField(max_length=128, blank=True, null=True)
    fecha_pago          = models.DateField(blank=True, null=True)
    frecuencia_pago     = models.CharField(max_length=128, blank=True, null=True)
    valor_original      = models.CharField(max_length=128, blank=True, null=True)
    saldo_capital       = models.CharField(max_length=128, blank=True, null=True)
    saldo_total         = models.CharField(max_length=128, blank=True, null=True)
    intereses_mora      = models.CharField(max_length=128, blank=True, null=True)
    otros_conceptos     = models.CharField(max_length=128, blank=True, null=True)

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

class gestionCustomer(models.Model):
    obligacion      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gestioncustomer_obligacion')
    fullNombre      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gestioncustomer_fullNombre')
    identificacion  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gestioncustomer_identificacion')
    acuerdo_pago    = models.CharField(max_length=300, blank=True, null=True)
    autorizacion    = models.BooleanField(default=True)
    observacion     = models.CharField(max_length=300, blank=True, null=True)
    comentario      = models.CharField(max_length=300, blank=True, null=True)
    created         = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated         = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # Otros campos del modelo...
    def __str__(self):
        return f"{self.observacion} - {self.comentario}"
