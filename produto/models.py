from autoslug import AutoSlugField
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from stdimage import StdImageField


class Categoria(models.Model):
    nome = models.CharField(max_length=30)


class Marca(models.Model):
    nome = models.CharField(max_length=50)


class Especificacoes(models.Model):
    indicacao = models.CharField(max_length=30)
    raca = models.CharField(max_length=30)
    porte = models.CharField(max_length=30)
    idade = models.CharField(max_length=30)
    composicao = models.CharField(max_length=350)
    cor = models.CharField(max_length=350)
    fragrancia = models.CharField(max_length=20)
    peso = models.CharField(max_length=6)
    frequencia_recomendada = models.IntegerField()
    dimensoes = models.TextField()


class Produto(models.Model):
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")
    nome = models.CharField(max_length=250)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    imagem = StdImageField(upload_to='produto_imagens/%Y/%m/',
                           variations={'full': {'width': 500, 'height': 500},
                                       'medium': {'width': 212, 'height': 212},
                                       'thumbnail': {'width': 100, 'height': 100}})
    preco = models.FloatField(validators=[MinValueValidator(0.01)])
    preco_promocional = models.FloatField(validators=[MinValueValidator(0.01)], blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, blank=True, null=True)
    especificacoes = models.ForeignKey(Especificacoes, models.DO_NOTHING)
    marca = models.ForeignKey(Marca, models.DO_NOTHING)
