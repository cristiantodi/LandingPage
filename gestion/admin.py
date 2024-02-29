from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

from import_export.admin import ImportExportModelAdmin

class CustomUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # personaliza la representación del modelo en el administrador si es necesario
    list_display = ['id','nombre','contrasena']
    readonly_fields= ('created','updated')

# admin.site.register(CustomUser, CustomUserAdmin)

