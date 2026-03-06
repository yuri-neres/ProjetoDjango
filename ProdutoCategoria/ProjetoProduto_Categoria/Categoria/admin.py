from django.contrib import admin
from Categoria.models import Categoria
from Produto.models import Produto

# Register your models here.

@admin.register(Produto)
@admin.register(Categoria)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nome", "descricao",]
    list_per_page = 25

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["Nome", "Descrição", "Preço", "Estoque", "Categoria", "Ativo", "Data_Criacao"]
    list_filter = ["Nome"]

    
