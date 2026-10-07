from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg://thinkerguy@localhost:5432/thinkerguy"

engine = create_engine(DATABASE_URL)

with engine.begin() as conn:
    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS pessoas (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER)"""))

    conn.execute(
        text("INSERT INTO pessoas (nome, idade) VALUES (:nome, :idade)"),
        {"nome":"TARS", "idade":30})    

    resultado = conn.execute(
        text("SELECT id, nome, idade FROM pessoas"))

    for pessoa in resultado:
        print(pessoa)

print ("PostgreSQL conectado com sucesso")