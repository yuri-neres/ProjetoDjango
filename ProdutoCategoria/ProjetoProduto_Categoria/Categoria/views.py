from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categoria

# Create your views here.

def home_categorias(request):
    return render(request, 'home_categorias.html')

def criar_categoria(request):
    if request.method == 'POST':
        nome_digitado = request.POST.get('nome')
        descricao_digitada = request.POST.get('descricao')
        ativo_marcado = request.POST.get('ativo') == 'on' 

        try:
            categoria_obj = Categoria.objects.get(id_categoria=categoria_id)
        except Categoria.DoesNotExist:
             return redirect('alguma_url_de_erro') 

        Categoria.objects.create(
            nome=nome_digitado,
            descricao=descricao_digitada,
            categoria=categoria_obj,
            ativo=ativo_marcado
        )

        return redirect('/categorias')

    lista_categorias = Categoria.objects.all()

    contexto = {
        'categorias': lista_categorias,
        'label_nome': 'Nome do Produto',
        'label_preco': 'Preço',
        'label_estoque': 'Quantidade em Estoque',
        'label_descricao': 'Descrição do Produto',
        'label_categoria': 'Categoria',
        'label_ativo': 'Produto Ativo?',
    }

    return render(request, 'criar.html', contexto)

def listar_categorias(request):
    categorias = Categoria.objects.all()
    meta = Categoria._meta
    
    context = {
        'categorias': categorias,
        'label_id': meta.get_field('id_categoria').verbose_name,
        'label_nome': meta.get_field('nome').verbose_name,
        'label_preco': meta.get_field('descricao').verbose_name,
        'label_estoque': meta.get_field('ativo').verbose_name,
    }
    
    return render(request, 'listar_categorias.html', context)
