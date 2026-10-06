from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://thinkerguy@localhost:5432/thinkerguy"

engine = create_engine(DATABASE_URL)