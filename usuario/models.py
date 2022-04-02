from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Usuario(models.Model):
    login = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)
    email = models.CharField(max_length=250)


    @classmethod
    def popular(cls, json):
        usuario = Usuario()
        usuario.login = json['login']
        usuario.email = json['email']
        usuario.senha = json['senha']

        return usuario

    @classmethod
    def popularalteracao(cls, json,usuario):
        if usuario.login != json['login']:
            usuario.login = json['login']

        if usuario.email != json['email']:
            usuario.email = json['email']

        if usuario.senha != json['senha']:

            usuario.senha = json['senha']

        return usuario