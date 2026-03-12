from django.urls import path
from Categoria import views

urlpatterns = [
    path("", views.home_categorias, name='home_categoria'),
    path("criar/", views.criar_categoria),
    path("listar/", views.listar_categorias, name='listar_categorias'),
]