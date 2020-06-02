"""
Listas aninhadas

- Algumas linguagens de programação possuem estratura de dados chamadas arrays:
    - Unidimensionais (Arrays/ vetores)
    - Multidimensionais (Matrizes)

Em pyhthon nos temos as listas.

numeros = [1, 'b', 3.244, True, -5]

"""


#Exemplos(forma mais facil de manipular matrizes em python)

listas = [[1, 2, 3], [4, 5, 6], [7, 6, 9]]  #Matriz 3x3

print(listas[0][1])#printar um elemento da lista, porem para iterar é necessario loops

#iterar uma matriz

for lista in listas:
    for num in lista:
        print(num)

#list comprehension

[[print(valor) for valor in lista] for lista in listas]

#Outro exemplo de matrizes

#Gerando um tabuleiro/matriz 3x3

#numero = [1, 2, 3]
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

#Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

#Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range (1,4)])

