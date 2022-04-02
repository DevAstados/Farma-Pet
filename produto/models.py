from autoslug import AutoSlugField
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from django.urls import reverse
from stdimage import StdImageField


class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    @classmethod
    def popular(cls, nome):
        cat = Categoria()
        cat.nome = nome
        return cat


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    @classmethod
    def popular(cls, nome):
        cat = Marca()
        cat.nome = nome
        return cat


class Especificacoes(models.Model):
    indicacao = models.CharField(max_length=30, blank=True, null=True)
    raca = models.CharField(max_length=30, blank=True, null=True)
    porte = models.CharField(max_length=30, blank=True, null=True)
    idade = models.CharField(max_length=30, blank=True, null=True)
    composicao = models.CharField(max_length=350, blank=True, null=True)
    cor = models.CharField(max_length=350, blank=True, null=True)
    fragrancia = models.CharField(max_length=20, blank=True, null=True)
    peso = models.FloatField(max_length=6, blank=True, null=True)
    frequencia_recomendada = models.IntegerField(blank=True, null=True)
    dimensoes = models.TextField(blank=True, null=True)

    @classmethod
    def popular(cls, json, categoria=None, marca=None):
        especificacoes = Especificacoes()
        especificacoes.indicacao = json['indicacao']
        especificacoes.raca = json['raca']
        especificacoes.porte = json['porte']
        especificacoes.idade = json['idade']
        especificacoes.composicao = json['composicao']
        especificacoes.cor = json['cor']
        especificacoes.fragrancia = json['fragrancia']
        especificacoes.peso = float(json['peso'].replace(',', '.'))

        return especificacoes

    @classmethod
    def popular_alterar(cls, json, especificacoes):
        if especificacoes.indicacao != json['indicacao']:
            especificacoes.indicacao = json['indicacao']
        if especificacoes.raca != json['raca']:
            especificacoes.raca = json['raca']
        if especificacoes.porte != json['porte']:
            especificacoes.porte = json['porte']
        if especificacoes.idade != json['idade']:
            especificacoes.idade = json['idade']
        if especificacoes.composicao != json['composicao']:
            especificacoes.composicao = json['composicao']
        if especificacoes.cor != json['cor']:
            especificacoes.cor = json['cor']
        if especificacoes.fragrancia != json['fragrancia']:
            especificacoes.fragrancia = json['fragrancia']
        if especificacoes.peso != float(json['peso'].replace(',', '.')):
            especificacoes.peso = float(json['peso'].replace(',', '.'))

        return especificacoes


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

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("produtos:detalhe", kwargs={"slug": self.slug})

    def getDesconto(self):
        if self.preco_promocional:
            return self.preco - self.preco_promocional

    @classmethod
    def popular(cls, json, categoria=None, marca=None, especificacoes=None):
        produto = Produto()

        produto.categoria = categoria
        produto.marca = marca

        produto.nome = json['nome']
        produto.descricao = json['descriacao']
        produto.quantidade = json['quantidade']
        produto.imagem = json['Imagen']
        produto.preco = json['preco']
        if (json['preco_promocional'] != ''):
            produto.preco_promocional = json['preco_promocional']

        produto.especificacoes = especificacoes

        return produto

    @classmethod
    def popular_alterar(cls, json, produto):
        if produto.nome != json['nome']:
            produto.nome = json['nome']

        if produto.descricao != json['descriacao']:
            produto.descricao = json['descriacao']

        if produto.quantidade != json['quantidade']:
            produto.quantidade = json['quantidade']

        if produto.preco != json['preco']:
            produto.preco = json['preco']
        if (json['preco_promocional'] != ''):
            if produto.preco_promocional != json['preco_promocional']:
                produto.preco_promocional = json['preco_promocional']

        return produto
    @classmethod
    def split(cls, lista, tamanho):
        return [lista[i:i + tamanho] for i in range(0, len(lista), tamanho)]

    @classmethod
    def getListProdutInColun(cls, categoria=None, nome_produto=None):
        listProduct = []

        if categoria is None:
            if nome_produto is None:
                listProduct = Produto.objects.all()
            else:

                for produto in Produto.objects.filter(nome__contains=nome_produto):
                    listProduct.append(produto)

        else:
            if nome_produto is not None:
                for produto in Produto.objects.filter(categoria=categoria, nome__contains=nome_produto):
                    listProduct.append(produto)
            else:

                for produto in Produto.objects.filter(categoria=categoria):
                    listProduct.append(produto)

        if listProduct.__len__() < 1:
            return None

        return Produto.split(listProduct, 3)