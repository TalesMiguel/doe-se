import json
import datetime

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from .models import Acoes

from service import instituicao_svc
from service import acao_svc

import geocoder
from .service import geocoder_svc, geojson_serializer_svc, acao_svc


@csrf_exempt
def add_acao(request):
    return JsonResponse(acao_svc.add_acao(request)) 


def get_acao(request):
    response = Acoes.objects.all()
    acoes = [acao.to_dict_json() for acao in response]
    return JsonResponse({'acoes': acoes})


def create_instituicao(request):
    instituicao = json.loads(request.POST.get("instituicao"))
    instituicao_svc.create_instituicao(instituicao)
    return JsonResponse({})


def list_instituicao(request):
    instituicoes = instituicao_svc.list_all_instituicoes()
    return JsonResponse([inst.to_dict_json() for inst in instituicoes], safe=False)


def update_instituicao(request):
    instituicao = json.loads(request.POST.get("instituicao"))
    instituicao_svc.update_instituicao(instituicao)
    return JsonResponse({})


def delete_instituicao(request):
    instituicao = json.loads(request.POST.get("instituicao"))
    instituicao_svc.delete_instituicao(instituicao)
    return JsonResponse({}, safe=False)


def create_acao(request):
    acao = json.loads(request.POST.get("acao"))
    acao_svc.create_acao(acao)
    return JsonResponse({})


def list_acao(request):
    acoes = acao_svc.list_all_acoes()
    return JsonResponse([inst.to_dict_json() for inst in acoes], safe=False)


def update_acao(request):
    acao = json.loads(request.POST.get("acao"))
    acao_svc.update_acao(acao)
    return JsonResponse({})


def delete_acao(request):
    acao = json.loads(request.POST.get("acao"))
    acao_svc.delete_acao(acao)
    return JsonResponse({}, safe=False)


def get_geojson(request):
    return HttpResponse(geojson_serializer_svc.serialize(), content_type='application/geo+json')


@csrf_exempt
def get_coord(request):
    coord = geocoder_svc.converter(request.POST['endereco'])
    return JsonResponse([coord[0], coord[1]], safe=False)
