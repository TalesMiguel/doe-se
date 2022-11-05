from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Instituicoes(models.Model):
    nome = models.CharField(max_length=256)
    CNPJ = models.CharField(max_length=32)
    telefone = models.CharField(max_length=32)
    email = models.EmailField(max_length=256)
    endereco = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
