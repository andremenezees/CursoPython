"""
Min e Max

max() -> Retorna o maior valor em um iteravel ou o maior de dois ou mais elemento.

#ver o maior valor entre duas variaveis

val1 = int(input('Digite um valor:'))
val2 = int(input('Digite um valor:'))
val3 = int(input('Digite um valor:'))
val4 = int(input('Digite um valor:'))

print(max(val1, val2, val3, val4))

"""

#Maior entre os 3, é feito por ordem alfabetica ou seja o d é o maior.
print(max('a', 'b', 'd', 'c'))

#Outros exemplos

nomes = ['Arya', 'Sansa', 'Ned', 'Catelyn']

#Neste caso é feito por ordem alfabetica da primeira letra
print(max(nomes))
print(min(nomes))

#Para pegar o nome com maior e menor quantidade de letras

print(max(nomes, key=lambda nome: len(nome)))


#Outro exemplo

musicas = [
    {"titulo": "Reuniao dos cria", "tocou": 3},
    {"titulo": "glock do vasco", "tocou": 5},
    {"titulo": "Poesia acustica 3", "tocou": 3},
    {"titulo": "Dias de luta dias de gloria", "tocou": 43},
    {"titulo": "Não me sinto mal mais", "tocou": 999999}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

#Imprimir apenas o titulo da musica mais tocada e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

#Fazer a mesma coisa sem utilizar max min e lambda

num = 0
for musica in musicas:

    if num < musica['tocou']:
        num = musica['tocou']
        titulo = musica['titulo']
print(titulo)

num1 = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
for musica in musicas:

    if num > musica['tocou']:
        num = musica['tocou']
        titulo2 = musica['titulo']
print(titulo2)