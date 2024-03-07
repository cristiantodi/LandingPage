from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User, gestionCustomer
from import_export.admin import ImportExportModelAdmin
from .resources import MiModeloResource
# Register your models here.

@admin.register(User)
class UserAdmin(ImportExportModelAdmin, BaseUserAdmin):
    resource_class = MiModeloResource
    list_display = ['id',
                    'username',
                    # 'password',
                    'fullName',
                    'obligacion',
                    'valor_proxima_cuota',
                    'nro_cuota_pagada',
                    'nro_cuota_pactada',
                    'banca',
                    'producto',
                    'destino_credito',
                    'fecha_desembolso',
                    'dias_mora',
                    'fecha_pago',
                    'frecuencia_pago',
                    'valor_original',
                    'saldo_capital',
                    'saldo_total',
                    'intereses_mora',
                    'otros_conceptos',
                    ]
    

    
class gestionCustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # personaliza la representación del modelo en el administrador si es necesario
    list_display = ['id',
                    'obligacion',
                    'fullNombre', 
                    'identificacion',
                    'acuerdo_pago',                    
                    'autorizacion',
                    'observacion',
                    'comentario',
                    'created',
                    'updated',
                ]
    readonly_fields= ('created','updated')

# admin.site.register(User, UserAdmin)
admin.site.register(gestionCustomer, gestionCustomerAdmin)
