# %%
## Importação das Bibliotecas
import pandas as pd
import requests
import time
import sqlite3

#%% 
## Extração de Dados de Licitação
BASE_SEARCH = "https://pncp.gov.br/api/search/"

params = {
    "tipos_documento": "edital",
    "ordenacao": "-data",
    "pagina": 1,
    "tam_pagina": 5,
    "status": "recebendo_proposta",
    "ufs": "PI"
}

resp = requests.get(BASE_SEARCH, params=params)
dados = resp.json()

linhas = []

for compra in dados.get("items", []):

    cnpj = compra.get("orgao_cnpj")
    ano = compra.get("ano")
    sequencial = compra.get("numero_sequencial")

    if not all([cnpj, ano, sequencial]):
        continue

    url = f"https://pncp.gov.br/api/pncp/v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/itens"

    print("URL:", url)

    r = requests.get(url)

    if r.status_code != 200:
        print("Erro:", r.status_code)
        continue

    itens = r.json()

    for item in itens:
        linha = {
            **{f"compra_{k}": v for k, v in compra.items()},
            **{f"item_{k}": v for k, v in item.items()}
        }

        linhas.append(linha)

df = pd.json_normalize(linhas)

#%%
## Subir os dados para o Banco SQlite
conn = sqlite3.connect("data/pncp.db")

df.to_sql("pncp_itens", conn, if_exists="replace", index=False)