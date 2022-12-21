from ..models import Acoes
from . import geocoder_svc

def add_acao(request):
    coord = geocoder_svc.converter(request.POST['endereco'])

    acao = (Acoes(nome=request.POST['nome'], tipo=request.POST['tipo'], endereco=request.POST['endereco'], 
           geom = {'type': 'Point', 'coordinates': [coord[1], coord[0]]}))

    acao.save()

    response = acao.to_dict_json()
    
    return response