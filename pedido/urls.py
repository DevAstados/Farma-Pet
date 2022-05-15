from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [

    path('checkout/', views.checkout.as_view(), name='checkout'),
    path('pagar/', views.pagar.as_view(), name='pagar'),
    path('resumo/<id>', views.resumo.as_view(), name='resumo'),

]