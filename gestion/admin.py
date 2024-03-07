from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import InformacionModelo

# Register your models here


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id',
                'observacion',
                'comentario',
                ]

admin.site.register(InformacionModelo, ContactAdmin)