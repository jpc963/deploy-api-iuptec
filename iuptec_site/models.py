from django.db import models
from django.contrib.auth.models import User


class Veiculos(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.CharField(max_length=10)
    placa = models.CharField(max_length=10)
    cor = models.CharField(max_length=20)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)