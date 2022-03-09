from django.contrib import admin

# Register your models here.
from produto.models import Produto, Categoria, Marca


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome',]

class CategoriAdmin(admin.ModelAdmin):
    list_display = ['nome',]

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nome',]




admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriAdmin)
admin.site.register(Marca, MarcaAdmin)