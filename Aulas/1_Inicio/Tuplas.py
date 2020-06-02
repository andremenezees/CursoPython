"""
Tuplas(tuple)

Tuplas são representadas por () diferente das listas q são []

Tuplas são imutáveis: Isso significa que ão criar uma tupla ela não muda.

Não existem tuplas de um elemento -> T = (4) --> não é uma tupla.

As tuplas são definidas pela virgula ou seja --> T =(4,) --> é uma tupla.

Diferença de uma lista e uma tupla é na lista pode-se retirar e adicionar elementos,
na tupla não pode adicionar nem retirar elementos, a unica forma de mudar uma tupla é
sobreescrevendo ela.

"""
#Forma de criar uma tupla:

tupla = tuple(range(1,10,1))
print(tupla)

#Desempacotar tupla

tupla1 = ('Mapache', 'God')

nome, sobrenome = tupla1
print(nome)
print(sobrenome)

#Pegar os valores é igual a das listas:

print(sum(tupla)) #soma
print(max(tupla))
print(min(tupla))
print(len(tupla))



