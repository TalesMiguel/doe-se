from django.db import models
from django.contrib.auth.models import User

class Instituicoes(models.Model):
    nome = models.CharField(max_length=256)
    CNPJ = models.CharField(max_length=32)
    telefone = models.CharField(max_length=32)
    email = models.EmailField(max_length=256)
    endereco = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Instituicoes'

class User(models.Model):
    nome = models.CharField(max_length=25)
    cpf = models.IntegerField()
    UserID = models.IntegerField()
    DataNascimeto = models.DateField()

class Acoes(models.Model):
    nome = models.CharField(max_length=256)
    tipo = models.CharField(max_length=32)
    endereco = models.CharField(max_length=256)


