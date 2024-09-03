import base_premises
import json

from datetime import date
from faker import Faker
from faker.providers import DynamicProvider
from faker_music import MusicProvider
from base_premises import areas_names_list, segmentos_names_list
import csv

def date_handler(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError("Type not serializable")

areas_names_provider = DynamicProvider(
     provider_name="area_name",
     elements=areas_names_list
)

segmentos_names_provider = DynamicProvider(
     provider_name="segmento_name",
     elements=segmentos_names_list
)

fake = Faker(['pt_BR'])

# then add new providers to faker instance
fake.add_provider(areas_names_provider)
fake.add_provider(segmentos_names_provider)
fake.add_provider(MusicProvider)

# now you can use:
fake.area_name()


# for _ in range(10):
#     print(fake.area_name())

def generate_fake_salic_project():
    return {
        "nome_projeto": fake.music_subgenre()+" "+fake.music_instrument(),
        "ano_projeto": fake.year(),
        "area_projeto": fake.area_name(),
        "uf_projeto": fake.state_abbr(),
        "municipio_projeto": fake.city(),
        "segmento": fake.segmento_name(),
        "palavra": fake.word(),
        "produtora": fake.company(),
        "proponente": fake.name(),
        "objetivos": fake.sentence(nb_words=10, variable_nb_words=True),
        "ficha_tecnica": fake.sentence(nb_words=15, variable_nb_words=True),
        "justificativa": fake.paragraph(nb_sentences=7, variable_nb_sentences=True),
        "data_inicio": fake.date_this_year(before_today=False, after_today=True),
        "data_termino": fake.date_this_year(before_today=True, after_today=False),
        "valor_aprovado": fake.random_number(3),
        "valor_captado": fake.random_number(3),
        "valor_proposta": fake.random_number(3)
    }


def generate_list_of_fake_salic_projects(number_of_projects=10):
    return [generate_fake_salic_project() for _ in range(number_of_projects)]


list_of_projects = generate_list_of_fake_salic_projects(500)
## printe bonitinho do dict em formato json
# print(json.dumps(list_of_projects, indent=4, default=date_handler))

# ... existing code ...

# Save list_of_projects to a CSV file
filename = 'projects.csv'
fieldnames = list_of_projects[0].keys()

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list_of_projects)

print(f"Projects saved to {filename}")