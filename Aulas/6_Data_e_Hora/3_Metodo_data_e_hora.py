# -*- encoding: utf-8 -*-

"""
Métodos de data e hora

"""

"""
import datetime

#Com now() podemos especificar um timezone (Fuso Horario)
agora = datetime.datetime.now()  #Now = agora
print(agora)

hoje = datetime.datetime.today()  #Today == hoje
print(hoje)
print('\n')

#Mudancas a meia noite

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print('\n')

#Encontrar o dia da semana, weekday()

#Os dias da semana no metodo weekday(), começam em 0, sendo esta a segunda-feira

# Dia 0 -> Segunda
# Dia 1 -> terca
# Dia 2 -> quarta
# Dia 3 -> quinta
# Dia 4 -> Sexta
# Dia 5 -> Sabado
# Dia 6 -> Domingo

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
#Pega o dia que ira ocorrer o evento manutenção, como estamos somando +1 sera um dia apos o dia de hoje.

print(manutencao.weekday()) #No dia em que fiz o codigo era sexta, portanto ira aparecer sabado(5)

"""
# Encontrar o dia em que nasceu
"""
import datetime

aniversario = input('Qual sua data de nascimento (dd/mm/yyyy) :')

aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

#Encontrar o dia em que nasceu.
if aniversario.weekday() == 0:
    print('Voce nasceu em uma segunda feira')
elif aniversario.weekday() == 1:
    print('Voce nasceu em uma terca feira')
elif aniversario.weekday() == 2:
    print('Voce nasceu em uma quarta feira')
elif aniversario.weekday() == 3:
    print('Voce nasceu em uma quinta feira')
elif aniversario.weekday() == 4:
    print('Voce nasceu em uma sexta feira')
elif aniversario.weekday() == 5:
    print('Voce nasceu em um sabado')
elif aniversario.weekday() == 6:
    print('Voce nasceu em um domingo')

"""


def formata_data(data):
    if data.month == 1:
        return f'{data.day} de janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de marco de {data.year}'
    elif data.month == 4:
        return f'{data.day} de abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de dezembro de {data.year}'


import datetime

# Formatando datas/horas com strtime()
"""
hoje = datetime.datetime.today()

print(hoje)

hoje_formato = hoje.strftime('%d/%m/%y')  #Padrao brasileiro

print(hoje_formato)
"""

hoje = datetime.datetime.today()

print(formata_data(hoje))

from textblob import TextBlob


def formata_data2(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()

print(formata_data2(hoje))

import datetime

print('\n')
# strptime('data', 'modelo escolhido') entao converte a data para o modelo tradicional
nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')
print(nascimento)
print('\n')

# nascimento = input('Qual sua data de nascimento:')
nascimento = '05/06/1996'
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)
print('\n')

"""
TRABALHANDO COM APENAS HORA

"""

# Marcando tempo de execução do nosso codigo com timeit

import timeit

# Timeit recebe uma string e o numero de vezes que essa string será executada, e aparece o tempo de execução.

# loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comphension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)

import timeit, functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print('\n')
print(teste(5))
print('\n')

print(timeit.timeit(functools.partial(teste, 2), number=10000))

