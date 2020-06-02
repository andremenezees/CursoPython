"""
Função

def nome_da_funcao(parametros_de_entrada):




# Exemplo de função:

def diz_oi():
    print('oi')


# Utilizando função

diz_oi()
"""

"""
Funções com retorno.

"""

"""
def quadrado_de_x(x):
    return x * x


ret = quadrado_de_x(6) + quadrado_de_x(3)
print(ret)
print(quadrado_de_x(6))
"""

# vamos criar uma função para jogar moeda

from random import random


# Random gera numeros entre 0 e 1


def joga_moeda():
    if random() > 0.5:
        return 'Cara'
    else:
        return 'Coroa'


print(joga_moeda())


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 3))

print(multiplica(2, 5))

print(outra(2, 3, 'Teste de função. '))


# Caso em que escolhe um valor opcional. No caso o valor potencia = 2 é opcional.
def exponencial(numero, potencia=2):
    return numero ** potencia


# Neste caso ira utilizar os valores informados.
print(exponencial(5, 3))

# Neste caso vai utilizar o valor opcional no lugar do valor potencial, ou seja 2.
print(exponencial(3))  # 3² = 9


def mostra_informacao(nome='mapache', instrutor=False):
    if nome == 'mapache' and instrutor:
        return 'Bem-vindo instrutor mapache'
    if nome == 'mapache' and instrutor == False:
        return 'Eu pensei que voce era o instrutor'
    return f'ola {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(nome='joao'))

# Como utilizar uma variavel global em uma função

total = 0  # Variavel  global.


def incrementa():
    global total  # Desta forma é possivel usar uma variável global em uma função.

    total = total + 1
    return total


print(incrementa())


# DOCSTRING

def diz_oi():
    """ Uma função simples que retorna a string 'oi' """
    return 'oi'


print(help(diz_oi))

"""
Docs string serve para criar uma documentação para a sua função que pode ser 
acessado através da função help. Seria como se fosse uma explicação de como
utilizar a sua função.

"""

"""
Entendendo o *args
O parametro *args utilizado em uma função, coloca os valores extras informados
como entrada em uma tupla. Então desde já lembre-se que tuplas sao imutáveis.

No args é possivel utilizar parametros obrigatorios (nome) no exemplo abaixo, e
parametros que são informados com o *args, os parametros *args podem ser informados
na hora de utilizar a função no exemplo foi utilizado no print.

Os parametros informados em *args são transformados em tupla.

"""


# Utilizando o *args  (explicação acima)


def soma_todos_numeros(nome, *args):
    return nome, sum(args)


print(soma_todos_numeros('mapache'))
print(soma_todos_numeros('mapache', 1))
print(soma_todos_numeros('mapache', 2, 3))
print(soma_todos_numeros('mapache', 2, 3, 4))
print(soma_todos_numeros('mapache', 2, 3, 4, 5))


#*kwargs é como o *args porem ao invez de criar tuplas cria dicionarios.
#UTILIZANDO **KWARGS (kwargs são dicionarios)

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

"""

Nas funçoes podemos utilizar (NESTA ORDEM):

- Parametros obrigatorios;
- *args;
- Parametros default(não obrigatorios)
- **Kwargs

"""

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Valentina', 4, 5, 6, solteiro=True)
minha_funcao(34, 'Felipe',eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)


def mostra_info(a, b, *args, instrutor='Michael', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobreome='Jordan', cargo='Deus'))

#Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


#Forma normal de printar
print(mostra_nomes(nome='Michael',sobrenome= 'Jordan'))

#Desempacotando
nomes = {'nome': 'Valentina', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))


#Outro exemplo(Mostrar que o desempacotamento nao serve apenas para **kwargs)
#Neste exemplo não um dicionario por isso vai so um *, seria o *args

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
soma_multiplos_numeros(*lista)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)


def soma_impares(a):
    soma = 0
    for i in a:
        if i % 2 != 0:
            soma = soma + i
    return soma



if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6,7]
    print(soma_impares(lista))
