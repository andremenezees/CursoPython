# -*- encoding: utf-8 -*-

"""

Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 12:55:34 .993999
data_final = dd/mm/yyyy   12:34:23 .099343

"""

#Delta para dia do aniversario

"""
import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2020, 6, 5, 0)


#Calculando o delta

tempo_para_evento = aniversario - data_hoje

#O delta basicamente é a solução matematica de duas datas.
print(tempo_para_evento)

print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 3600} horas')

"""

import datetime


data_da_compra = datetime.datetime.now()
regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto)