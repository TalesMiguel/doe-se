import json

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from .models import Acoes
import geocoder

def hello(request):
    return HttpResponse("Hello, World!")

@csrf_exempt
def add_acao(request):
    if request.method == "POST":
        g = geocoder.osm(request.POST['endereco'])
        l1 = g.latlng[0]
        l2 = g.latlng[1]
        acao = Acoes(nome=request.POST['nome'], tipo=request.POST['tipo'], endereco=request.POST['endereco'], lat=l1, lng=l2)
        acao.save()
        res = acao.to_dict_json()
        return JsonResponse(res) 

    else:
        return HttpResponse("falhou")

def get_acao(request):
    if request.method == "GET":
        res = Acoes.objects.all()
        teste = [ac.to_dict_json() for ac in res]
        return JsonResponse({'todos': teste})

    else:
        return HttpResponse("falhou")