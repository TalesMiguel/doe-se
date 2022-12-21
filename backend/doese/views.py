import json

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from .models import Acoes
from .service import geocoder_svc, geojson_serializer_svc, acao_svc

@csrf_exempt
def add_acao(request):
    return JsonResponse(acao_svc.add_acao(request)) 

def get_acao(request):
    response = Acoes.objects.all()
    acoes = [acao.to_dict_json() for acao in acoes]
    return JsonResponse({'acoes': acoes})

def get_geojson(request):
    return HttpResponse(geojson_serializer_svc.serialize(), content_type='application/geo+json')

@csrf_exempt
def get_coord(request):
    coord = geocoder_svc.converter(request.POST['endereco'])
    return JsonResponse([coord[0], coord[1]], safe=False)