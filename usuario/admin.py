from django.contrib import admin

# Register your models here.
from usuario.models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['login',]




admin.site.register(Usuario, UsuarioAdmin)