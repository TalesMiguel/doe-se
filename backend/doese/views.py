import json

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from .models import Acoes
from .models import User
from django.contrib.auth import login

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        #user = User(nome=request.POST['nome'], senha=request.POST['senha'])
        if User is not None:
            #login(request, user)
            return 
        else:
            return HttpResponse("Usuário não encontrado")


@csrf_exempt
def add_acao(request):
    if request.method == "POST":
        l1 = -42
        l2 = 23
        acao = Acoes(tipo=request.POST['tipo'], endereco=request.POST['endereco'], lat=l1, lng=l2)
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