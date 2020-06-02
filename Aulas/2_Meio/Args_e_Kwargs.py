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
