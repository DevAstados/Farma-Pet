from django.contrib import admin
from .models import Cliente

'''
class EnderecoInLine(admin.TabularInline):
    model = Endereco
    extra = 1
'''

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'cpf', 'telefone']
'''
      inlines = [
        EnderecoInLine
    ]
'''

admin.site.register(Cliente, ClienteAdmin)

'''
admin.site.register(Endereco)
'''