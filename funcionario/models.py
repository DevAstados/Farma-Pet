from django.db import models

# Create your models here.
from usuario.models import CustomUser


class Funcionario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    usuario = models.ForeignKey(CustomUser, models.CASCADE)

    @classmethod
    def popular(cls, json, usuario):
        funcionario = Funcionario()
        funcionario.nome = json['nome']
        funcionario.usuario = usuario

        return funcionario

    @classmethod
    def popularAlteracao(cls, json, funcionario):
        if funcionario.nome != json['nome']:
            funcionario.nome = json['nome']

        return funcionario
