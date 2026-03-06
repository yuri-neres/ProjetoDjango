from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(unique=True, primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False, unique = True)
    descricao = models.TextField(blank = True, null = True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
