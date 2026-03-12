from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Produto
from Categoria.models import Categoria

# Create your views here.

def home_produtos(request):
    return render(request, 'home_produtos.html')

def listar_produtos(request):
    produtos = Produto.objects.all()
    meta = Produto._meta
    
    context = {
        'produtos': produtos,
        'label_nome': meta.get_field('nome').verbose_name,
        'label_preco': meta.get_field('preco').verbose_name,
        'label_estoque': meta.get_field('estoque').verbose_name,
    }
    
    return render(request, 'listar.html', context)

def criar_produto(request):
    if request.method == 'POST':
        nome_digitado = request.POST.get('nome')
        preco_digitado = request.POST.get('preco')
        estoque_digitado = request.POST.get('estoque')
        descricao_digitada = request.POST.get('descricao')
        
        categoria_id = request.POST.get('categoria') 
        
        ativo_marcado = request.POST.get('ativo') == 'on' 

        if not categoria_id:
            lista_categorias = Categoria.objects.all()
            contexto = {
                'categorias': lista_categorias,
                'erro': 'Por favor, selecione uma categoria obrigatória.',
                'label_nome': 'Nome do Produto',
                'label_preco': 'Preço',
                'label_estoque': 'Quantidade em Estoque',
                'label_descricao': 'Descrição do Produto',
                'label_categoria': 'Categoria',
                'label_ativo': 'Produto Ativo?',
            }
            return render(request, 'criar.html', contexto)

        try:
            categoria_obj = Categoria.objects.get(id_categoria=categoria_id)
        except Categoria.DoesNotExist:
             return redirect('alguma_url_de_erro') 

        Produto.objects.create(
            nome=nome_digitado,
            preco=preco_digitado,
            estoque=estoque_digitado,
            descricao=descricao_digitada,
            categoria=categoria_obj,
            ativo=ativo_marcado
        )

        return redirect('/produtos/')

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


def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    lista_categorias = Categoria.objects.all()
    erro = None

    if request.method == 'POST':
        nome_digitado = request.POST.get('nome')
        preco_digitado = request.POST.get('preco')
        estoque_digitado = request.POST.get('estoque')
        descricao_digitada = request.POST.get('descricao')
        id_categoria_selecionada = request.POST.get('categoria')
        ativo_marcado = request.POST.get('ativo') == 'on'

        if Produto.objects.filter(nome=nome_digitado).exclude(id=id).exists():
            erro = 'Já existe um produto cadastrado com este nome.'
        else:
            try:
                categoria_obj = Categoria.objects.get(id_categoria=id_categoria_selecionada)
                produto.nome = nome_digitado
                produto.preco = preco_digitado
                produto.estoque = estoque_digitado
                produto.descricao = descricao_digitada
                produto.categoria = categoria_obj
                produto.ativo = ativo_marcado
                produto.save()
                
                return redirect('/produtos/listar/')
            except Categoria.DoesNotExist:
                erro = 'A categoria selecionada é inválida.'

    contexto = {
        'produto': produto,
        'categorias': lista_categorias,
        'label_nome': 'Nome do Produto',
        'label_preco': 'Preço (R$)',
        'label_estoque': 'Quantidade em Estoque',
        'label_descricao': 'Descrição',
        'label_categoria': 'Categoria',
        'label_ativo': 'Produto Ativo?',
        'erro': erro,
    }

    return render(request, 'editar.html', contexto)


def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':
        produto.delete()
        return redirect('/produtos/listar/')
        
    return render(request, 'excluir.html', {'produto': produto})

def detalhar_produto(request, id):
    produto = Produto.objects.get(id=id)
    meta = Produto._meta
    context = {
        'produto': produto,
        'label_nome': meta.get_field('nome').verbose_name,
        'label_preco': meta.get_field('preco').verbose_name,
        'label_estoque': meta.get_field('estoque').verbose_name,
        'label_descricao': meta.get_field('descricao').verbose_name,
        'label_categoria': meta.get_field('categoria').verbose_name,
        'label_ativo': meta.get_field('ativo').verbose_name,
        'label_data_criacao': meta.get_field('data_criacao').verbose_name,
    }
    return render(request, 'detalhe.html', context)
