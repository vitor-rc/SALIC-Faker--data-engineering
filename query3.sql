select uf_projeto, count(distinct nome_projeto) vol_projects
from salic_faker.vrc_how_desafio1_salic_faker
group by 1
order by 2 desc
