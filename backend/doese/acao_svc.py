from .models import Acoes
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import get_object_or_404


def create_acao(acao):
    new_inst = Acoes(**acao)
    new_inst.save()


def list_all_acoes():
    return Acoes.objects.all()


def update_acao(acao):
    try:
        inst = Acoes.objects.get(key=acao["key"])
    except ObjectDoesNotExist as e:
        raise ValidationError("A ação não existe.")
    
    inst = { **acao }
    inst.save()


def delete_acao(acao):
    acao = get_object_or_404(Acoes, key=acao["key"])
    acao.delete()
