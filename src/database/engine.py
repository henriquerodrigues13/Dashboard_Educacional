from pathlib import Path
from datetime import datetime

from sqlalchemy import create_engine, String, Integer, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

pastal_atual = Path(__file__).parent
caminho_DB = pastal_atual / 'BancoDeDados.sqlite'

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

engine = create_engine(f'sqlite:///{caminho_DB}')
Base.metadata.create_all(bind=engine)

def criando_usarario(
        matricula: int,
        genero: str,
        periodo: str,
        polo: str,
        cor_etnia: str,
        pdc: str,
        tipo_deficiencia: str,
        renda: str,
        deslocamento: str,
        trabalho: str,
        assistencia_estudantil: str,
        saude_mental: str,
        estresse: str,
        acompanhamento: str,
        escolaridade_pai: str,
        escolaridade_mae: str,
        qtd_computador: int,
        qtd_celular: int,
        computador_proprio: str,
        gasto_internet: str,
        acesso_internet: str,
        tipo_moradia: str,
        data_hora: datetime,
):

    with Session(bind=engine) as session:
        usuario = Usuarios(
            matricula=matricula,
            genero=genero,
            periodo=periodo,
            polo=polo,
            cor_etnia=cor_etnia,
            pdc=pdc,
            tipo_deficiencia=tipo_deficiencia,
            renda=renda,
            deslocamento=deslocamento,
            trabalho=trabalho,
            assistencia_estudantil=assistencia_estudantil,
            saude_mental=saude_mental,
            estresse=estresse,
            acompanhamento=acompanhamento,
            escolaridade_pai=escolaridade_pai,
            escolaridade_mae=escolaridade_mae,
            qtd_computador=qtd_computador,
            qtd_celular=qtd_celular,
            computador_proprio=computador_proprio,
            gasto_internet=gasto_internet,
            acesso_internet=acesso_internet,
            tipo_moradia=tipo_moradia,
            data_hora=data_hora
        )
        session.add(usuario)
        session.commit()