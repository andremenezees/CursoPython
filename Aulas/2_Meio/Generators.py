"""
Generators

Tuple comprehension são chamadas de generators.

"""

#Exemplo

nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina', 'Abacate']

#List comprehension
print(any([nome[0] == 'C' for nome in nomes]))

#Generator
print(any(nome[0] == 'C' for nome in nomes))

"""
A diferença entre os dois está na performance, o generator não salva a lista 
de true or false ele apenas a utiliza no any já o list comprehension salva
a lista com todos os testes feitos, ou seja toda a lista de true or false.
O generator não gera nada antes de utilizar e logo apos utilizar ele exclui.

"""

#testes

from sys import getsizeof

#mostra quantos bytes a string 'Geek' está ocupando em memoria.

#Gerando uma lista de números com list comprehension

list_comp = getsizeof([x * 10 for x in range(1000)])

#Gerando uma lista de números com set comprehension

set_comp = getsizeof({x * 10 for x in range(1000)})

#Gerando uma lista de números com dictionary comprehension

dict_comp = getsizeof({x: x * 10 for x in range(1000)})

#Gerando uma lista de numeros com generator

gen = getsizeof(x * 10 for x in range(1000))

print(f'list:{list_comp}')
print(f'list:{set_comp}')
print(f'list:{dict_comp}')
print(f'list:{gen}')

#Ocupa tão pouco pq ele não gera antes de utilizar, e logo apos utilizar ja apaga.

