"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista:
lista = [1, 2, 3, 4, 5]

Uma tupla:
tupla = (1, 2, 3, 4, 5)

Um set:
conjunto = {1, 2, 3, 4, 5}

Um dicionario
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

"""

#Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

numero1 = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numero1}
print(quadrados)

#Neste caso temos valores repetidos, porem em dicionarios não e possivel repetir.
numero1 = [1, 2, 3, 4, 5, 1,2]

quadrados = {valor: valor ** 2 for valor in numero1}
print(quadrados)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5, 6]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

#Exemplo com logica condicional

nume = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in nume}
print(res)

