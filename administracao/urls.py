from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path


from administracao import views
app_name = 'adm'

urlpatterns = [
                  path('login/', views.login.as_view(), name='login'),
                  path('logout/', views.Logout, name='logout'),
                  path('', login_required(views.administracao, login_url= 'adm:login'), name='administracao'),
                  path('listagemProduto/', views.listagem_produto.as_view(), name='listagem_produto'),
                  path('listagemFuncionario/', views.listagem_funcionario.as_view(), name='listagem_funcionario'),
                  path('listagemPedido/', views.listagem_pedido.as_view(), name='listagem_pedido'),
                  path('listagemCliente/', views.listagem_cliente.as_view(), name='listagem_cliente'),
                  path('adicionaProduto/', views.adicionar_produto.as_view(), name='adiciona_produto'),
                  path('adicionaFuncionario/', views.adicionar_funcionario.as_view(), name='adiciona_funcionario'),

                  path('alteraProduto/<id>', views.update_produto.as_view(), name='alterar_produto'),
                  path('alteraFuncionario/<id>', views.update_funcionario.as_view(), name='alterar_funcionario'),
                  path('deletarProduto/<id>', views.excluirProduto, name='deletar_produto'),
                  path('deletarFuncionario/<id>', views.excluirFuncionario, name='deletar_funcionario'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
