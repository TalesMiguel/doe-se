from ..models import Acoes
from . import geocoder_svc
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import get_object_or_404


#def create_acao(acao):
#    new_inst = Acoes(**acao)
#    new_inst.save()


def list_all_acoes():
    return Acoes.objects.all()


def update_acao(acao):
    try:
        inst = Acoes.objects.get(id=acao["id"])
    except ObjectDoesNotExist as e:
        raise ValidationError("A ação não existe.")
    
    inst = { **acao }
    inst.save()


def delete_acao(acao):
    acao = get_object_or_404(Acoes, id=acao["id"])
    acao.delete()


def add_acao(request):
    coord = geocoder_svc.converter(request.POST['endereco'])

    acao = (Acoes(nome=request.POST['nome'], tipo=request.POST['tipo'], endereco=request.POST['endereco'], 
           geom = {'type': 'Point', 'coordinates': [coord[1], coord[0]]}))

    acao.save()

    response = acao.to_dict_json()
    
    return response
