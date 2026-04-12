from pathlib import Path
from src.database.engine import Usuarios
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session


caminho_DB = Path(__file__).parent / 'BancoDeDados.sqlite'
engine = create_engine(f'sqlite:///{caminho_DB}')

def crg_medio():
    with Session(engine) as session:
        comando_sql = select(Usuarios.matricula,Usuarios.CRG).group_by(Usuarios.matricula).having(Usuarios.CRG > 0)
        resposta = session.execute(comando_sql).all()
        return resposta

def matriculas_unicas():
    with Session(bind=engine) as session:
        comando_sql = select(func.count(Usuarios.matricula.distinct()))
        resposta = session.execute(comando_sql).all()
        return resposta[0][0]

def consulta_por_argumento(argumento):
    argumento = parametros_do_select(argumento)
    with Session(bind=engine) as session:
        comando_sql = select(argumento)
        resposta = session.execute(comando_sql).all()
        return resposta

def consulta_longitudinal(argumento):
    if argumento != 'perido':
        argumento = parametros_do_select(argumento)
        with Session(bind=engine) as session:
            comando_sql = select(argumento, Usuarios.matricula, Usuarios.periodo)
            resposta = session.execute(comando_sql).all()
            return resposta
    return Exception

def consulta_bidimensional(primeiro_arg,segundo_arg):
    primeiro_arg = parametros_do_select(primeiro_arg)
    segundo_arg = parametros_do_select(segundo_arg)
    with Session(bind=engine) as session:
        comando_sql = select(primeiro_arg, segundo_arg,
                             func.count(Usuarios.id).label('total'))
        resposta = session.execute(comando_sql).all()
    return resposta

def parametros_do_select(parametro):
    match parametro:
        case 'genero':
            return Usuarios.genero
        case 'cor/etnia':
            return Usuarios.cor_etnia
        case 'pcd':
            return Usuarios.pcd
        case 'tipo deficiencia':
            return Usuarios.tipo_deficiencia
        case 'renda':
            return Usuarios.renda
        case 'descolamento':
            return Usuarios.descolamento
        case 'trabalho':
            return Usuarios.trabalho
        case 'assistencia estudante':
            return Usuarios.assistencia_estudante
        case 'saude mental':
            return Usuarios.saude_mental
        case 'estresse':
            return Usuarios.estresse
        case 'acompanhamento':
            return Usuarios.acompanhamento
        case 'escolaridade pai':
            return Usuarios.escolaridade_pai
        case 'escolaridade mae':
            return Usuarios.escolaridade_mae
        case 'qtd computador':
            return Usuarios.qtd_computador
        case 'qtd celular':
            return Usuarios.qtd_celular
        case 'computador proprio':
            return Usuarios.computador_proprio
        case 'gasto internet':
            return Usuarios.gasto_internet
        case 'acesso internet':
            return Usuarios.acesso_internet
        case 'tipo moradia':
            return Usuarios.tipo_moradia
    return None

