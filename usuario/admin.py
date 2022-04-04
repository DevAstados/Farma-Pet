from django.contrib import admin

# Register your models here.
from usuario.models import CustomUser


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['username',]




admin.site.register(CustomUser, UsuarioAdmin)