from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Categoria

# Create your views here.

def home_categorias(request):
    return render(request, 'home_categorias.html')

def criar_categoria(request):
    erro = None

    if request.method == 'POST':
        nome_digitado = request.POST.get('nome')
        descricao_digitada = request.POST.get('descricao')
        ativo_marcado = request.POST.get('ativo') == 'on' 

        if Categoria.objects.filter(nome=nome_digitado).exists():
            erro = 'Já existe uma categoria cadastrada com este nome.'
        else:
            Categoria.objects.create(
                nome=nome_digitado,
                descricao=descricao_digitada,
                ativo=ativo_marcado
            )
            return redirect('/categorias')
        
    lista_categorias = Categoria.objects.all()

    contexto = {
        'categorias': lista_categorias,
        'label_nome': 'Nome da categoria',
        'label_descricao': 'Descrição da categoria',
        'label_ativo': 'Categoria Ativa?',
        'erro': erro,
    }

    return render(request, 'criar_categoria.html', contexto)

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

def editar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    erro = None

    if request.method == 'POST':
        nome_digitado = request.POST.get('nome')
        descricao_digitada = request.POST.get('descricao')
        ativo_marcado = request.POST.get('ativo') == 'on' 

        if Categoria.objects.filter(nome=nome_digitado).exclude(id_categoria=id_categoria).exists():
            erro = 'Já existe uma categoria cadastrada com este nome.'
        else:
            categoria.nome = nome_digitado
            categoria.descricao = descricao_digitada
            categoria.ativo = ativo_marcado
            categoria.save()
            return redirect('/categorias/listar')
    
    contexto = {
        'categoria': categoria,
        'label_nome': 'Nome da categoria',
        'label_descricao': 'Descrição da categoria',
        'label_ativo': 'Categoria Ativa?',
        'erro': erro,
    }

    return render(request, 'editar_categoria.html', contexto)


def excluir_categoria(request, id_categoria):
    # Busca usando o campo id_categoria que você definiu no models
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    
    if request.method == 'POST':
        categoria.delete()
        return redirect('/categorias/listar/')
        
    return render(request, 'excluir_categoria.html', {'categoria': categoria})