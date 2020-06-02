"""
Sorted

Pode-se utilizar o sorted() com qualquer iterável.

Como o proprio nome diz, sorted() serve para ordenar.

#O sorted sempre retornar uma lista ordenada, ele não altera o elemento principal
no primeiro exemplo ordenados uma tupla, então os elementos da tupla foram
ordenados e adicionados a uma lista pelo sorted e o elemento principal que nesse
caso é uma tupla não foi alterado.
"""

#Exemplo

numeros = (6, 1, 8, 2) #Tupla
print(numeros)

print(sorted(numeros))
print(numeros)


#Adiocionando parametros ao sorted()

numeros = [6, 1, 8, 2]

#Neste caso ordenada e inverte a lista e printa como uma TUPLA.
print(tuple(sorted(numeros, reverse=True)))

#exemplo mais complexo.

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "lais", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "Amarelo"},
    {"username": "dog", "tweets": ["Eu adoro dogs", "Eu adoro mapaches"]},
    {"username": "gal", "tweets": []}
]

#Ordenar dicionario, neste caso foi ordenado em ordem alfabetica do username.

print(usuarios)

print(sorted(usuarios, key=lambda usuario: usuario["username"]))

print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))

#Ordenando pelo numeros de tweets

print(sorted(usuarios, key = lambda usuario: len(usuario["tweets"])))

#Outro exemplo

musicas = [
    {"titulo": "Reuniao dos cria", "tocou": 3},
    {"titulo": "glock do vasco", "tocou": 5},
    {"titulo": "Poesia acustica 3", "tocou": 3},
    {"titulo": "Dias de luta dias de gloria", "tocou": 43},
    {"titulo": "Não me sinto mal mais", "tocou": 999999}
]
#Ordenar da menos tocada para a mais tocada

print(sorted(musicas, key= lambda musica: musica["tocou"], reverse = True))

#Ordenar da mais tocada para a menos tocada

print(sorted(musicas, key = lambda musica: musica["tocou"]))



