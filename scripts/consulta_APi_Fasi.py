from datetime import datetime
from src.database.engine import criando_usuario
import os
import requests
import dotenv


dotenv.load_dotenv()

token = os.getenv("token_fasi")

base_url = "https://www.fasitech.com.br/api/v1/_dev/raw-social-data"
headers = {
    "Authorization": f"Bearer {token}"
}
for i in range(1,6):
    params = {
        "pagina": i,
        "por_pagina": 100
    }
    response = requests.get(base_url, headers=headers, params=params)

    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no request: {e}')
    else:
        response_json = response.json()
        todos_os_dados = response_json['dados']
        if todos_os_dados is not None:
            for registros in todos_os_dados:
                registros['data_hora'] = datetime.fromisoformat(registros['data_hora'])
                criando_usuario(
                    matricula=registros['matricula'],
                    periodo=registros['periodo'],
                    genero=registros['genero'],
                    polo=registros['polo'],
                    cor_etnia=registros['cor_etnia'],
                    pcd=registros['pcd'],
                    tipo_deficiencia=registros['tipo_deficiencia'],
                    renda=registros['renda'],
                    deslocamento=registros['deslocamento'],
                    trabalho=registros['trabalho'],
                    assistencia_estudantil=registros['assistencia_estudantil'],
                    saude_mental=registros['saude_mental'],
                    estresse=registros['estresse'],
                    acompanhamento=registros['acompanhamento'],
                    escolaridade_pai=registros['escolaridade_pai'],
                    escolaridade_mae=registros['escolaridade_mae'],
                    qtd_computador=registros['qtd_computador'],
                    qtd_celular=registros['qtd_celular'],
                    computador_proprio=registros['computador_proprio'],
                    gasto_internet=registros['gasto_internet'],
                    acesso_internet=registros['acesso_internet'],
                    tipo_moradia=registros['tipo_moradia'],
                    data_hora=registros['data_hora'],
                        )
