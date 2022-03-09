from django.db import models

# Create your models here.
from usuario.models import Usuario


class Funcionario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING)

