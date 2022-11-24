from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.model):
    nome = models.CharField(max_length=50)
    CEP = models.IntegerField
    data_de_nascimento = models.DateField
    def __str__(self):
        return self.nome

class Historico(models.model):
    tipo = models.IntegerField
    local = models.CharField(max_length=128)
    CEP_local = models.IntegerField
    data_inicio = models.DateField
    data_termino = models.DateField
    valor = models.IntegerField
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Instituicoes(models.Model):
    nome = models.CharField(max_length=256)
    CNPJ = models.CharField(max_length=32)
    telefone = models.CharField(max_length=32)
    email = models.EmailField(max_length=256)
    endereco = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Acao(models.model):
    intistuicao = models.ForeignKey(Instituicoes, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=32)
    endereco = models.CharField(max_length=128)
    CEP_local = models.IntegerField
    data_inicio = models.DateTimeField
    data_termino = models.DateTimeField
    concluido = models.BooleanField
    lat = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    lng = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)

    def to_dict_json(self):
        return {
            'tipo': self.tipo,
            'endereco': self.endereco,
            'lat': self.lat,
            'lng': self.lng,
        }
