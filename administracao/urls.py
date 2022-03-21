from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from administracao import views

urlpatterns = [
                  path('login/', views.login, name='login'),
                  path('logout/', views.Logout, name='logout'),
                  path('', views.administracao, name='administracao'),
                  path('listagemProduto/', views.listagem_produto.as_view(), name='listagem_produto'),
                  path('listagemFuncionario/', views.listagem_funcionario.as_view(), name='listagem_funcionario'),
                  path('listagemPedido/', views.listagem_pedido.as_view(), name='listagem_pedido'),
                  path('listagemCliente/', views.listagem_cliente.as_view(), name='listagem_cliente'),
                  path('adicionaProduto/', views.adicionar_produto.as_view(), name='adiciona_produto'),

                  path('alteraProduto/<id>', views.update_produto.as_view(), name='alterar_produto'),
                  path('deletarProduto/<id>', views.excluirProduto, name='deletar_produto'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
