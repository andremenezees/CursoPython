"""
Set comprehension

listas = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}  #Set é uma lista que não permite elementos repetidos
e os valores no set são ordenados automaticamente.


"""

#Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

#Exemplo 2

numeros = {x ** 2 for x in range(10)}
print(numeros)

#GERANDO UM DICIONARIO

numeros = {x: x** 2 for x in range(10)}
print(numeros)

#Com strings

letras = {letra for letra in 'Mapache God'}
print(letras)