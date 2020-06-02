"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

filter(função que filtrara, iteravel a ser filtrado)
"""

#Filtrar os dados para valores acima da media

import statistics

#dados coletados de algum sensor
valores = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]


media = statistics.mean(valores)
#vai usar valores no lugar do x, e o filter filtra os valores conforme a função.
res = filter(lambda x: x > media, valores)
print(list(res))

#Outra utilização do filter é através da remoção de itens faltantes.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '']
print(paises)

#Neste caso quando o caracter é 0 ele é false e entao é removido.
res = filter(lambda pais: len(pais), paises)
print(list(res))

print(list(filter(lambda pais: pais != '', paises)))

#Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "lais", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "dog", "tweets": ["Eu adoro dogs", "Eu adoro mapaches"]},
    {"username": "gal", "tweets": []}
]

#Filtrar os usuarios que estão inativos no twitter

lista_inativos = filter(lambda usuario: len(usuario['tweets']) == 0, usuarios)
print(list(lista_inativos))
lista_ativos = filter(lambda usuario: not len(usuario['tweets']) == 0, usuarios)
print(list(lista_ativos))

#Combinar filter e map ()

nomes = ['Vanessa', 'Ana', 'Maria']

#Criar lista contendo 'Sua instrutora é '' + nome, desde que o nome tenha - de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome1: len(nome1) < 5, nomes)))
print(lista)
