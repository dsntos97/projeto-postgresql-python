from sqlalchemy.orm import sessionmaker

from src.database import engine

from src.repository import cadastrar_talhao, listar_talhoes

SessionLocal  = sessionmaker(bind=engine)

def main():
    with SessionLocal() as sessao:
        with sessao.begin():
            talhoes = listar_talhoes(sessao)
        
            if not talhoes:
                cadastrar_talhao(
                    sessao = sessao,
                    nome="area 23",
                    area_hectares=0.24,
                    cultura="sorgo",
                )

                talhoes = listar_talhoes(sessao)
        


        print("\n--- Talhões cadastrados ---")
        # Exibe os dados de cada talhão.
        for talhao in talhoes:
            # print(talhoes)
            print(
                f"ID: {talhao.id} | "
                f"Nome: {talhao.nome} | "
                f"Área: {talhao.area_hectares} ha | "
                f"Cultura: {talhao.cultura}"
            )


                
if __name__ == "__main__":
    main()