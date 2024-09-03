# SALIC-Faker--data-engineering
First challenge from the bootcamp "Data Engineering - How Bootcamps"


# Projeto: Geração de Dados Falsos para Projetos SALIC

Este repositório contém dois arquivos principais que utilizam a API do SALIC para gerar e salvar dados falsos de projetos culturais em formato CSV.

## Arquivos

### `base_premises.py`

Este arquivo contém funções para interagir com a API do SALIC e manipular os dados recebidos.

#### Funções:

- **`execute_curl_command_projetos()`**: Executa um comando `curl` para a API do SALIC, retornando os dados dos projetos como um objeto JSON.

- **`execute_curl_command_basic_listing(method_name)`**: Executa um comando `curl` básico para listar informações de uma entidade específica (ex: áreas, segmentos).

- **`extract_fields(sub_array_json_infos)`**: Extrai campos de um objeto JSON e os armazena em um dicionário com listas separadas por campo.

- **`create_dataframe(fields)`**: Cria um DataFrame do Pandas a partir de um dicionário de campos.

#### Variáveis:

- **`areas_names_list`**: Lista de nomes de áreas extraída da API.
- **`segmentos_names_list`**: Lista de nomes de segmentos extraída da API.

### `faker_test.py`

Este arquivo utiliza o pacote `Faker` para gerar dados falsos de projetos culturais, baseando-se nos dados extraídos via `base_premises.py`.

#### Funções:

- **`date_handler(obj)`**: Função auxiliar para serializar objetos de data no formato JSON.

- **`generate_fake_salic_project()`**: Gera um dicionário com os dados falsos de um projeto cultural.

- **`generate_list_of_fake_salic_projects(number_of_projects=10)`**: Gera uma lista de dicionários, cada um representando um projeto falso.

#### Variáveis:

- **`areas_names_provider`**: Provedor dinâmico para gerar nomes de áreas.
- **`segmentos_names_provider`**: Provedor dinâmico para gerar nomes de segmentos.
- **`fake`**: Instância do `Faker` configurada com os provedores personalizados.

#### Exportação para CSV:

- Os projetos gerados são salvos em um arquivo `projects.csv` com os campos definidos em `generate_fake_salic_project()`.

## Dependências

- `requests`
- `pandas`
- `faker`
- `faker_music`

## Como Usar

1. Execute o script `base_premises.py` para obter as listas de áreas e segmentos da API do SALIC.
2. Execute o script `faker_test.py` para gerar e salvar os projetos falsos no arquivo `projects.csv`.
