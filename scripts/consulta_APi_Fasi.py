import os
import requests
import dotenv
import json

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
        print(response.status_code)

