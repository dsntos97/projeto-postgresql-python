from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Talhao(Base):
    __tablename__ = "talhoes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )
    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    area_hectares: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )
    cultura: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )