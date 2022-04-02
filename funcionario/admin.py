from django.contrib import admin

# Register your models here.
from funcionario.models import Funcionario


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome',]


admin.site.register(Funcionario, FuncionarioAdmin)