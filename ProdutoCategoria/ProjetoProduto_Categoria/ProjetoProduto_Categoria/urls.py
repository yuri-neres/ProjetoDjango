from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path('produtos/', include('Produto.urls')),
    path('categorias/', include('Categoria.urls'))
]