from .models import Instituicoes
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import get_object_or_404


def create_instituicao(instituicao):
    new_inst = Instituicoes(**instituicao)
    new_inst.save()


def list_all_instituicoes():
    return Instituicoes.objects.all()


def update_instituicao(instituicao):
    try:
        inst = Instituicoes.objects.get(key=instituicao["key"])
    except ObjectDoesNotExist as e:
        raise ValidationError("A instituição não existe.")
    
    inst = { **instituicao }
    inst.save()


def delete_instituicao(instituicao):
    instituicao = get_object_or_404(Instituicoes, key=instituicao["key"])
    instituicao.delete()
