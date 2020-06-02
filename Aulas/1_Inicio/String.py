"""
Um dado é considerado string sempre que:

Estiver em aspas simples -> 'string' '123' 'a'
Estiver em aspas duplas ->  "string" "123" "a"
Estiver em aspas simples triplas -> '''string''' '''123'''

"""

nome = 'string'
print(nome)

print(nome.upper())

nome1 = "s't'r'i'n'g"
print(nome1)

#printar atraves de uma lista

nome = 'string teste'

print(nome[0:6])
print(nome[7:15])

#outra forma de printar

print(nome.split()[0])
print(nome.split()[1])

#Inverter todos os elementos

print(nome[::-1])

#Substituir elementos na string

print(nome.replace('i','a'))

