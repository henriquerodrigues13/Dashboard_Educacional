from datetime import datetime

from sqlalchemy import create_engine, String, Integer, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_engine('sqlite:///:meu_db')


class Base(DeclarativeBase):
    pass

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    matricula: Mapped[int] = mapped_column(Integer, nullable=False)
    genero: Mapped[str] = mapped_column(String(20))
    #crg: Mapped[float] = mapped_column(Float, nullable=False)
    periodo: Mapped[str] = mapped_column(String(15))
    polo: Mapped[str] = mapped_column(String(15))
    cor_etnia: Mapped[str] = mapped_column(String(10))
    pdc: Mapped[str] = mapped_column(String(5))
    tipo_deficiencia: Mapped[str] = mapped_column(String(100))
    renda: Mapped[str] = mapped_column(String(150))
    deslocamento: Mapped[str] = mapped_column(String(150))
    trabalho: Mapped[str] = mapped_column(String(150))
    assistencia_estudantil: Mapped[str] = mapped_column(String(5))
    saude_mental: Mapped[str] = mapped_column(String(10))
    estresse: Mapped[str] = mapped_column(String(50))
    acompanhamento: Mapped[str] = mapped_column(String(20))
    escolaridade_pai: Mapped[str] = mapped_column(String(20))
    escolaridade_mae: Mapped[str] = mapped_column(String(20))
    qtd_computador: Mapped[int] = mapped_column(Integer)
    qtd_celular: Mapped[int] = mapped_column(Integer)
    computador_proprio: Mapped[str] = mapped_column(String(5))
    gasto_internet: Mapped[str] = mapped_column(String(30))
    acesso_internet: Mapped[str] = mapped_column(String(5))
    tipo_moradia: Mapped[str] = mapped_column(String(10))
    data_hora: Mapped[datetime] = mapped_column(DateTime)