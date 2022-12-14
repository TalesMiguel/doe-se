import json

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from .models import Acoes
import datetime
import geocoder

@csrf_exempt
def add_acao(request):
    if request.method == "POST":
        g = geocoder.osm(request.POST['endereco'])
        data = datetime.datetime(2022, 12, 5, 11, 11)
        #data_inicio=data, data_fim=data
        l1 = g.lat
        l2 = g.lng
        acao = Acoes(tipo=request.POST['tipo'], dataInicio=data, endereco=request.POST['endereco'], concluido=False, lat=l1, lng=l2)
        acao.save()
        res = acao.to_dict_json()
        return JsonResponse(res) 

    else:
        return HttpResponse("falhou")

def add_inst(request): #ai e com vc Felipe
    if request.method == "POST":
        
    else:
        return HttpResponse(request)

def login_user(request): #vc denovo Felipe

def login_inst(request): #vc denovo Felipe
