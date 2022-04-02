from django.views.generic.edit import CreateView, UpdateView, DeleteView
from funcionario.models import Funcionario
from django.urls import reverse_lazy


class FuncionarioCreate(CreateView):
   model = Funcionario
   fields = ['id', 'nome', 'usuario']
   template_name = 'funcionario/form.html'
   success_url = reverse_lazy('listagem_produto')


class FuncionarioUpdate(UpdateView):
   model = Funcionario
   fields = ['id', 'nome', 'usuario']
   template_name = 'funcionario/form.html'
   success_url = reverse_lazy('listagem_produto')

class FuncionarioDelete(DeleteView):
   model = Funcionario
   template_name = 'funcionario/form.html'
   success_url = reverse_lazy('listagem_produto')