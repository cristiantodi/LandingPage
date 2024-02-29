from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User
from import_export.admin import ImportExportModelAdmin
from .resources import MiModeloResource
# Register your models here.

@admin.register(User)
class UserAdmin(ImportExportModelAdmin, BaseUserAdmin):
    resource_class = MiModeloResource
    list_display = ['id','username','password']
    
# admin.site.register(User, UserAdmin)

