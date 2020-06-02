"""
Manipulando data e hora

Python tem um modulo para se trabalha com data e hora chamado
datetime

"""

"""
import datetime

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

#Retorna a data e hora corrente
print(datetime.datetime.now())  #(2020-05-28 23:36:33.334100)


#Replace() serve para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

#Alterando o horario para 16 horas, 0 munutos, 0 segundos, 0 microseconds

inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print('\n')

#Pode ser usado como cronometro
print(inicio)

"""

"""
import datetime

#Criando um horario

evento = datetime.datetime(2020, 1, 1, 10, 3, 4, 33)

print(evento)

nascimento = input('Informe sua data de nascimento (dd/ mm/ yyyy) : ')
print(nascimento)
print('\n')


nascimento = nascimento.split('/') #Pegando os valores da data que foram separados por /

#Transformando em um datatime em ingles as datas geradas a cima.
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
"""

import datetime

evento = datetime.datetime.now()

#Acessa individual dos elementos de data e hora

print(evento.year) #Ano
print(evento.month) #Mes
print(evento.day) #Dia
print(evento.minute) #minutos
print(evento.second) #Secundo
print(evento.microsecond) #Microsegundo

