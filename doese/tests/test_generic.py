import pytest

@pytest.fixture
def project_name():
    return "Doe-se"

def test_wrong_project_name(project_name):
        assert project_name != "Projeto genérico"


def test_project_name(project_name):
      assert project_name == "Doe-se"
