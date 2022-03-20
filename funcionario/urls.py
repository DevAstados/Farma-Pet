from django.urls import path
from funcionario.views import FuncionarioCreate, FuncionarioUpdate, FuncionarioDelete

urlpatterns = [

     path('cadastrar/funcionario/', FuncionarioCreate.as_view(), name='cadastrar-funcionario'),
     path('editar/funcionario/<int:pk>/', FuncionarioUpdate.as_view(), name='editar-funcionario'),
     path('excluir/funcionario/<int:pk>/', FuncionarioDelete.as_view(), name='excluir-funcionario'),



              ]
