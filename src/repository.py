from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models import Talhao

def cadastrar_talhao(
    sessao: Session,
    nome: str,
    area_hectares: float,
    cultura: str,
) -> Talhao:
    nome = nome.strip()

    if not nome:
        raise ValueError("o nome do talhao nao pode ser vazio")

    if area_hectares <= 0:
        raise ValueError(" a area deve ser maior que zero")

    cultura = cultura.strip()
    if not cultura:
        raise ValueError("a cultura nao pode ficar vazia")

    talhao = Talhao(
        nome=nome,
        area_hectares=area_hectares,
        cultura=cultura
        )
    sessao.add(talhao)
    sessao.flush()

    return talhao()

def listar_talhoes (sessao : Session) -> list[Talhao]:
    consulta = select(Talhao).order_by(Talhao.id)
    return list(sessao.scalars(consulta).all())
