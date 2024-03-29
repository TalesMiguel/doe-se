from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from djgeojson.fields import PointField
from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=50)
    CEP = models.IntegerField
    data_de_nascimento = models.DateField
    def __str__(self):
        return self.nome

class Historico(models.Model):
    tipo = models.IntegerField
    local = models.CharField(max_length=128)
    CEP_local = models.IntegerField
    #data_inicio = models.DateField
    #sdata_termino = models.DateField
    valor = models.IntegerField
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Instituicoes(models.Model):
    nome = models.CharField(max_length=256)
    CNPJ = models.CharField(max_length=32)
    telefone = models.CharField(max_length=32)
    email = models.EmailField(max_length=256)
    endereco = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #acoes = models.ForeignKey('doese.Acoes', on_delete=models.CASCADE, related_name='acao')
    def __str__(self):
        return self.nome


class Acoes(models.Model):
    #instituicao = models.ForeignKey(Instituicoes, on_delete=models.CASCADE, related_name='instituicao')
    nome = models.CharField(max_length=256)
    tipo = ArrayField(models.CharField(max_length=32), size = 3)
    endereco = models.CharField(max_length=256)
    geom = PointField()

    def to_dict_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'tipo': self.tipo,
            'endereco': self.endereco,
            'geom': self.geom,
        }
