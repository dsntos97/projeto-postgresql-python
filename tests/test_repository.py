import pytest

from src.repository import cadastrar_talhao

def test_rejeita_nome_vazio():
    with pytest.raises(ValueError, match="nome do talhao"):
        cadastrar_talhao(
            sessao=None,
            nome="   ",
            area_hectares=1.0,
            cultura="milho",

        )
def test_rejeita_area_zero():
    with pytest.raises(ValueError, match="area deve ser maior que zero"):
        cadastrar_talhao(
            sessao=None,
            nome="talhao de teste",
            area_hectares=0,
            cultura="MIlho",
        )


def test_rejeita_cultura_vazia():
    with pytest.raises(ValueError, match="cultura nao pode ficar vazia"
    ):
        cadastrar_talhao(
            sessao=None,
            nome="talhao de teste",
            area_hectares=1.0,
            cultura="   ",)