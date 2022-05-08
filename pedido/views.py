from django.shortcuts import render

# Create your views here.
from django.views import View

from produto.models import Categoria


class checkout(View):
    def post(self, request, *args, **kwargs):
        context = {}
        context['categorias'] = Categoria.objects.all().order_by('nome')
        return render(request, 'checkout.html', context)


class pagar(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['categorias'] = Categoria.objects.all().order_by('nome')
        return render(request, 'pagamento.html', context)

