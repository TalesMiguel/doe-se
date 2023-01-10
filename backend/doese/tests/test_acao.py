import acao_svc

from model_bakery import baker
import pytest


@pytest.fixture
def acao():
    return baker.make(
        "Acoes",
        key="1",
        tipo=["teste"],
        endereco="123456",
        dataInicio="2022/12/12",
        concluido=True,
        lat=0,
        lng=0
    )


def clear_model():
    return Acoes.objects.all().delete()


def test_create_acao():
    acao = {
        "tipo": ["teste"],
        "endereco": "123456",
        "dataInicio": "2022/12/12",
        "concluido": True,
        "lat": 0,
        "lng": 0
    }
    acao_svc.create_acao(acao)
    assert Acoes.objects.all().count() == 1
    clear_model()


def test_list_Acoes(acao):
    acao_svc.list_acao()
    assert Acoes.objects.all().count() == 1


def test_update_acao(acao):
    new_inst = acao
    new_inst["concluido"] = False
    acao_svc.update_acao(new_inst)
    assert Acoes.objects.filter(concluido=False).all().count() == 1


def test_delete_acao(acao):
    acao_svc.delete_acao(acao)
    assert Acoes.objects.filter(key=acao["key"]).all().count() == 0
