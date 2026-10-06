from sqlalchemy import create_engine, text

engine = create_engine(
        "postgresql+psycopg://thinkerguy@localhost:5432/thinkerguy"
        )

with engine.connect() as conexao:
    resultado = conexao.execute(text("SELECT version()"))
    print(resultado.fetchone())
