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
├── Categoria/                    # Domínio principal 
│   ├── templates/                # Permite inserir variáveis e usar estruturas no HTML
│   │   ├── criar_categoria.html
|   |   ├── editar_categoria.html
|   |   ├── home_categoria.html
|   |   └── listar_categoria.html

│   ├── migrations/
│   ├── admin.py           # Configuração do admin
│   ├── authentication.py  # (Legado) classe de autenticação custom
│   ├── models.py          # Modelos de dados
│   ├── serializers.py     # Serializers DRF
│   ├── views.py           # Views/ViewSets
│   └── urls.py            # Rotas da API
├── Produto/                 # Domínio de usuários (auth, perfil, histórico)
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── ProjetoProduto_Categoria/            # Configurações do projeto
│   ├── settings.py        # Configurações Django
│   └── urls.py            # URLs principais
├── .venv/                 # Ambiente virtual
├── db.sqlite3             # Banco de dados SQLite
├── 
└── manage.py              # CLI do Django
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


**Produto**
