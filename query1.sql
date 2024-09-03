select produtora, try(sum(try(CAST(valor_captado AS INTEGER)))/sum(try(CAST(valor_aprovado AS INTEGER)))) perc_captado
from salic_faker.vrc_how_desafio1_salic_faker
group by 1
order by 2 desc
