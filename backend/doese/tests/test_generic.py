import pytest

# Dummy Test pra servir de molde pros outros testes

"""
    Uma fixture é uma função que será rodada várias vezes nos testes. Geralmente, ela é
    usada pra setup de testes ou alguma implementação mock de um service ou endpoint.
    Podemos declarar uma fixture local (que será usada apenas no arquivo em que ela foi criada)
    ou criar um arquivo fixtures.py (dentro da pasta /tests/) para fixtures que serão usadas
    em vários arquivos de teste.
    Leia a doc: https://docs.pytest.org/en/6.2.x/fixture.html
"""
@pytest.fixture
def project_name():
    return "Doe-se"


# As fixtures são passadas como parâmetro pros testes
def test_wrong_project_name(project_name):
        assert project_name != "Projeto genérico"


def test_project_name(project_name):
      assert project_name == "Doe-se"
