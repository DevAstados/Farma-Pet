from django.contrib import admin
from .models import Pedido, ItemPedido, FormaDePagamento


class FormaPagamentoInLine(admin.TabularInline):
    model = FormaDePagamento
    extra = 1


class ItemPedidoInLine(admin.TabularInline):
    model = ItemPedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInLine
    ]

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(FormaDePagamento)
admin.site.register(ItemPedido)