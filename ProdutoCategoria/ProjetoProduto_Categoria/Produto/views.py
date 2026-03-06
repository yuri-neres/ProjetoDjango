from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Produto
# Create your views here.

def _get_produto_form_labels():
    """Retorna os verbose_name dos campos do formul?rio de Pessoa."""
    meta = Produto._meta
    return {
        'label_nome': meta.get_field('nome').verbose_name,
        'label_descricao': meta.get_field('descricao').verbose_name,
        'label_preco': meta.get_field('preco').verbose_name,
        'label_estoque': meta.get_field('estoque').verbose_name,
        'label_categoria': meta.get_field('categoria').verbose_name,
        'label_data_criacao': meta.get_field('data_criacao').verbose_name,
        'label_ativo': meta.get_field('ativo').verbose_name,
    }


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
    if request.POST:
        nome = request.POST.get('nome', '').strip()
        preco = request.POST.get('preco', '').strip()
        estoque = request.POST.get('estoque', '').strip() or None
        descricao = request.POST.get('descricao') or None
        categoria = request.POST.get('categoria', '').strip() or None
        ativo = request.POST.get('ativo') == 'on'
        
        # Verificar se email j? existe
        if Produto.objects.filter(nome=nome).exists():
            messages.error(request, 'Este produto ja esta cadastrado.')
            return render(request, 'criar.html', {'titulo': 'Nova Pessoa', **_get_produto_form_labels()})
        
        try:
            produto = Produto.objects.create(
                nome=nome,
                preco=preco,
                estoque=estoque,
                descricao=descricao,
                categoria=categoria,
                ativo=ativo
            )
            messages.success(request, f'Produto: "{produto.nome}" criado com sucesso!')
            return redirect('detalhe.html', id=produto.id)
        except Exception as e:
            messages.error(request, f'Erro ao criar produto: {str(e)}')
            return render(request, 'pessoas/form.html', {'titulo': 'Nova Pessoa', **_get_produto_form_labels()})
    
    context = {
        'titulo': 'Nova Pessoa',
        **_get_produto_form_labels(),
    }
    return render(request, 'criar.html', context)


def editar_produto(request):
    HttpResponse

def excluir_produto(request):
    HttpResponse

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
