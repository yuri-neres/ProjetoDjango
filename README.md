# BOLSA FUTURO DIGITAL - BACKEND COM PYTHON 🐍
## Projeto Django: Sistema de Gestão de Produtos e de Categorias

### Integrantes do Grupo
* Iandra Santos Lacerda
* Maria Clara dos Santos Pires
* Tarcísio Côrtes Viana
* Yuri Lima Neres

**Orientador**: Prof. Cláudio Rodolfo Sousa de Oliveira

## 🗃 Estrutura do Projeto
```
ProjetoProduto_Categoria/
├── Categoria/                    # Domínio de categorias
│   ├── templates/                # Permite inserir variáveis e usar estruturas no HTML
│   │   ├── criar_categoria.html      # Renderiza o HTML para a função de criação de categoria
|   |   ├── editar_categoria.html     # Renderiza o HTML para a função de edição de categoria
|   |   ├── home_categoria.html       # Renderiza o HTML para a página inicial de categoria
|   |   └── listar_categoria.html     # Renderiza o HTML para a função de listar categorias
│   ├── migrations/
│   ├── admin.py               # Configuração do admin
│   ├── apps.py
│   ├── models.py              # Modelos de dados
│   ├── tests.py
│   ├── urls.py                # Rotas da API
│   └── views.py               # Views/ViewSets
├── Produto/                     # Domínio de produtos (id, nome, descrição, preço...)
│   ├── templates/                # Permite inserir variáveis e usar estruturas no HTML
│   │   ├── base.html                 # Tela inicial do projeto
|   |   ├── criar.html                # Renderiza o HTML para a função de criação de produto
|   |   ├── detalhe.html              # Renderiza o HTML para a função de detalhar produto
│   │   ├── editar.html               # Renderiza o HTML para a função de edição de produto
│   │   ├── excluir.html              # Renderiza o HTML para a função de exclusão de produto
│   │   ├── home_produtos.html        # Renderiza o HTML para a página inicial de produto
|   |   └── listar.html               # Renderiza o HTML para a função de listar produtos
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── ProjetoProduto_Categoria/            # Configurações do projeto
│   ├── __init__.py
│   ├── asgi.py            # Entrada para servidores ASGI.
│   ├── settings.py        # Configurações Django
│   ├── urls.py            # Mapeia URLs para views.
│   ├── views.py           # Views/ViewSets
│   └── wsgi.py            # Entrada para servidores WSGI.
├── .venv/             # Ambiente virtual
├── db.sqlite3         # Banco de dados SQLite
├── 
└── manage.py          # Executa comandos do Django.
```

## 🛍 Projeto Loja Virtual

### 1. Requisitos Técnicos Obrigatórios: Modelagem
**Categoria**
* id_categoria = models.AutoField(unique=True, primary_key=True)
* nome = models.CharField(max_length=255, null=False, blank=False, unique = True)
* descricao = models.TextField(blank = True, null = True)
* ativo = models.BooleanField(default=True)

**Produto**
* id = models.AutoField(unique=True, primary_key=True)
* nome = models.CharField(max_length=255)
* descricao = models.TextField()
* preco = models.DecimalField(decimal_places=2, max_digits=10)
* estoque = models.IntegerField()
* categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
* ativo = models.BooleanField(default=True)
* data_criacao = models.DateTimeField(auto_now_add=True)

### 2. Funcionalidade CRUD
**Categoria**
CREATE: Criação de categorias
```
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
```

READ: Listar categorias
```
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
```

UPDATE: Editar categorias
```
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
```

DELETE: Excluir categorias
```
def excluir_categoria(request, id_categoria):
    # Busca usando o campo id_categoria que você definiu no models
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    
    if request.method == 'POST':
        categoria.delete()
        return redirect('/categorias/listar/')
        
    return render(request, 'excluir_categoria.html', {'categoria': categoria})
```

**Produto**
CREATE: Criação de produto
```
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
```

READ: Listar produto(s)
```
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
```
**Detalhar produtos:**
```
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
```

UPDATE: Editar produto
```
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
```

DELETE: Excluir produto
```
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':
        produto.delete()
        return redirect('/produtos/listar/')
        
    return render(request, 'excluir.html', {'produto': produto})
```
