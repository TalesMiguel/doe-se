from models import Instituicoes
import instituicao_svc

from model_bakery import baker
import pytest



@pytest.fixture
def instituicao():
    return baker.make(
        "Instituicoes",
        key="1",
        nome="teste",
        CNPJ="123456",
        telefone="987654321",
        email="teste@teste.com",
        endereco="Rua teste",
    )


def clear_model():
    return Instituicoes.objects.all().delete()


def test_create_instituicao():
    instituicao = {
        "nome": "teste",
        "CNPJ": "123456",
        "telefone": "987654321",
        "email": "teste@teste.com",
        "endereco": "Rua teste",
    }
    instituicao_svc.create_instituicao(instituicao)
    assert Instituicoes.objects.all().count() == 1
    clear_model()


def test_list_instituicoes(instituicao):
    instituicao_svc.list_instituicao()
    assert Instituicoes.objects.all().count() == 1


def test_update_instituicao(instituicao):
    new_inst = instituicao
    new_inst["nome"] = "Novo nome de teste"
    instituicao_svc.update_instituicao(new_inst)
    assert Instituicoes.objects.filter(nome="Novo nome de Teste").all().count() == 1


def test_delete_instituicao(instituicao):
    instituicao_svc.delete_instituicao(instituicao)
    assert Instituicoes.objects.filter(nome=instituicao["nome"]).all().count() == 0
