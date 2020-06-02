"""
Conjuntos

No python, os conjutos são chamados de Sets.

    - Sets(Conjuntos) não possuem valores duplicados.
    - Sets(conjuntos) não possuem valores não ordenados, os valores são sempre ordenados.
    - Os elementos dos sets não são acessados via indice, não são indexados.

Os conjuntos são referenciados como {}.
Diferença entre Conjuntos(sets) e Mapas(dicionarios):
    - Um dicionario possui chave/valor.
    - Um conjunto tem apenas valor.

Conjuntos são usados quando queremos armazenar elementos sem que existam elementos repetidos
e a ordenação deles não é importante.

"""

#Testando

#Listas aceitam tudo.
lista = [99, 23, 34, 2, 12, 1, 44, 5, 34]
print(type(lista))
print(f'Lista:{lista} com {len(lista)} elementos')

#Tuplas são quase iguais as listas, a unica diferença é não permitem modificação.
tupla = (99, 2, 34, 2, 12, 1, 44, 5, 34)
print(type(tupla))
print(f'Lista:{tupla} com {len(tupla)} elementos')

#Dicionarios não aceitam chaves duplicadas.
dicionario = {}.fromkeys([99, 2, 34, 2, 12, 1, 44, 5, 34], 'dict')
print(type(dicionario))
print(f'Lista:{dicionario} com {len(dicionario)} elementos')

#Conjuntos não aceitam valores duplicados e ordenam seus valores.
conjunto = {99, 2, 34, 2, 12, 1, 44, 5, 34}
print(type(conjunto))
print(f'Lista:{conjunto} com {len(conjunto)} elementos')

#Em sets também é permitido colocar qualquer tipo de dado, assim como em tudo no python.

#Uso interessantes com sets.

#Formulario de cadastro, os visitantes informam a cidade e onde vieram.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande','Cuiaba', 'Campo grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

#Sets são usados para neste caso saber quantas diferentens cidades (não repetidas) foram preenchidas.

s = set(cidades)
print(type(s))
print(s)
print(len(s))

#Adicionando elementos em um set.

s1 = {1, 2, 3, 4}
print(s1)
s1.add(5)
print(s1)

#Removendo elementos em um set

s1.remove(3)
print(s1)

#Metodos matematicos de conjuntos

conjunto1 = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
conjunto2 = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

#Conjunto com nomes iguais.
#Precisamos gerar conjuntos com nomes unicos.

#forma 1 :

unicos1 = conjunto1.union(conjunto2)
print(unicos1)

#Forma 2 - Utilizando o caractere pipe

unicos2 = conjunto1 | conjunto2
print(unicos2)

#Gerar um conjunto de nomes que estão em ambos os conjuntos.

ambos1 = conjunto1.intersection(conjunto2)
print(ambos1)

#Forma 2

ambos2 = conjunto1 & conjunto2
print(ambos2)

#Agora gerar um conjunto com nomes que estão apenas no conjunto1.

soconj1 = conjunto1.difference(conjunto2)
print(soconj1)

