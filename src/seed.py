from sqlalchemy import select
from src.database import engine
from src.models import Talhao

def cadastrar_talhao (nome, area_hectares, cultura):
    with engine.begin() as conexao:
        existente = conexao.execute(
            select(Talhao).where(Talhao.nome == nome)
        ).first()

        if existente:
            print( f"Talhao {nome} ja existe")
            return
        
        talhao = Talhao(
            nome = nome,
            area_hectares=area_hectares,
            cultura=cultura,
        )

        conexao.execute(Talhao.__table__.insert().values(
        nome=talhao.nome,
        area_hectares=talhao.area_hectares,
        cultura=talhao.cultura,))

        print(f"talhao {nome} cadatrado")

if __name__ == "__main__":
    cadastrar_talhao("area experimental", 0.23, "milho")