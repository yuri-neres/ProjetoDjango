from django.urls import path
from Categoria import views

urlpatterns = [
    path("", views.home_categorias, name='home_categoria'),
    path("criar/", views.criar_categoria),
    path("listar/", views.listar_categorias, name='listar_categorias'),
    path("editar/<int:id_categoria>", views.editar_categoria, name='editar_categoria'),
    path("excluir/<int:id_categoria>", views.excluir_categoria, name='excluir_categoria'),
]