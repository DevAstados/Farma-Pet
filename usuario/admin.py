from django.contrib import admin

# Register your models here.
from usuario.models import CustomUser


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['email',]




admin.site.register(CustomUser, UsuarioAdmin)