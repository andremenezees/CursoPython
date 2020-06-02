"""
zip ()  -> Cria um iterável que agrega elementos de cada um dos iteraveis passados
como entrada em pares.

Junta os dois elementos Ex:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(list(zip(lista1, lista2)))

Resposta:
[(1, 4), (2, 5), (3, 6)]

"""



lista1 = [1, 2, 3, 1]
lista2 = [1, 4, 5, 6]


print(list(zip(lista1, lista2, 'abcd')))
print(tuple(zip(lista1, lista2, 'abcd')))
print(set(zip(lista1, lista2, 'abcd'))) #Em set não existe ordenação, ordem de elementos.
print(dict(zip(lista1, lista2)))    #Dicionarios nao aceitam valores repetidos.

lista3 = [7, 8, 9, 10, 11]

#O zip utiliza como tamanho o menor numero como iteravel, caso os tamanhos sejam diferentes.

print(list(zip(lista1, lista2, lista3)))

#podemos utilizar diferentes tipos de iteraveis com zip.

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario ={'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e':15}

zt = zip(tupla, lista, dicionario.values()) #dicionario.values para ser os valores do dicionario e nao suas chaves.
print(list(zt))

#lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados))) #Utilizar o * para fazer o desempacotamento dos dados.


#Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(dict(final))

