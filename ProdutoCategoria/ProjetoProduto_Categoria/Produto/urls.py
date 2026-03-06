# Produto/urls.py
from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('criar/', views.criar_produto, name='criar'),
    path('listar/', views.listar_produtos, name='listar'),
    path('editar/<int:id>/', views.editar_produto, name='editar'),
    path('excluir/<int:id>/', views.excluir_produto, name='excluir'),
    path('detalhar/<int:id>/', views.detalhar_produto, name='detalhar'),
]