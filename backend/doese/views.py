import json

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from .models import Acoes
import datetime
#import geocoder

@csrf_exempt
def add_acao(request):
    if request.method == "POST":
        #g = geocoder.osm(request.POST['endereco'])
        #data = datetime.datetime.now()
        #data_inicio=data, data_fim=data
        l1 = -23.1639
        l2 = -45.7942
        acao = Acoes(tipo=request.POST['tipo'], endereco=request.POST['endereco'], concluido=False, lat=l1, lng=l2)
        acao.save()
        res = acao.to_dict_json()
        return JsonResponse(res) 

    else:
        return HttpResponse("falhou")

