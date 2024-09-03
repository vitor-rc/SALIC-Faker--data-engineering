import requests
import json
import pandas as pd

# Função para executar o comando curl e retornar o resultado como um objeto JSON
def execute_curl_command_projetos():
    url = "http://api.salic.cultura.gov.br/v1/projetos/"
    params = {
        'limit': 100,
        'area': 1,
        'sort': 'ano_projeto:desc',
        'format': 'json'
    }
    response = requests.get(url, params=params)
    json_output = response.json()
    return json_output

def execute_curl_command_basic_listing(method_name):
    url = f"http://api.salic.cultura.gov.br/v1/projetos/{method_name}"
    params = {'format': 'json'}
    response = requests.get(url, params=params)
    json_output = response.json()
    return json_output

# Função para extrair os campos do objeto JSON e armazenar em colunas separadas
def extract_fields(sub_array_json_infos):
    fields = {}
    for element in sub_array_json_infos:
        for key, value in element.items():
            if key not in fields:
                fields[key] = []
            fields[key].append(value)
    return fields

# Função para criar um DataFrame a partir dos campos extraídos
def create_dataframe(fields):
    df = pd.DataFrame(fields)
    return df



areas_output = execute_curl_command_basic_listing("areas")
areas = extract_fields(areas_output["_embedded"]["areas"])
areas_names_list = areas["nome"]

segmentos_output = execute_curl_command_basic_listing("segmentos")
segmentos = extract_fields(segmentos_output["_embedded"]["segmentos"])
segmentos_names_list = segmentos["nome"]