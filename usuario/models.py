from django.db import models

# Create your models here.
class Usuario(models.Model):
    login = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)
    email = models.CharField(max_length=250)
