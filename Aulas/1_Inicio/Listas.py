"""
As listas em python são representadas por colchetes: []

"""

#comando list é uma ferramente para criar listas mais facil

lista1 = [3, 1, 5, 9, 7]
print(f'Lista1:{lista1}')

lista2 = list(range(1,10,2))
print(f'Lista2:{lista2}')

lista3 = ['m', 'a', 'p', 'a', 'c', 'h', 'e']
print(f'lista3:{lista3}')

lista4 = list('mapache')
print(f'lista4:{lista4}')

num = 9
if num in lista1:
    print(f'O numero {num} foi encontrado')
else:
    print(f"O numero {num} nao foi encontrado")


#Ferramentas de python para listas

print(f'Lista2:{lista2}')
print(f'Soma dos elementos da lista 2:{sum(lista2)}') #Soma os elementos da lista 2
print(f'Maximo valor da lista2:{max(lista2)}')
print(f'Minimo valor da lista2:{min(lista2)}')
print(f'Tamanho da lista 2: {len(lista2)}')
print(f'Elemento de indice 3: {lista2.index(3)}')

#Ordenar listas

lista5 = [1,3,10,2,5,19,6,22,15,10,10,10]
lista5.sort()
print(lista5)

lista3.sort()
print(lista3)

#contar elementos em um lista
print(f'O numero de elementos 10 na lista é de:{lista5.count(10)}')
listcount3 = (lista3.count('a'))
print(f'O numero de elementos a na lista é de:{listcount3}')


#Adicionar elementos a lista
lista5.extend([10000])
print(f'lista 5 com o elemento 10000 adicionado ao fim:{lista5}')

#adicionar mais de um elemento por vez em uma lista
lista5.extend([1, 10, 100, 10000])
print(f'lista 5 com mais de um elemento adicionado de um so vez:{lista5}')

#Adicionando lista em uma lista
lista5.append([1000, 10, 50])
print(f'lista 5 com um elemento lista adicionado a lista::{lista5}')

#adicionar elemento escolhendo a posição

lista6 = [1, 2, 3, 4, 5, 6]
lista6.insert(2, 'Novo valor')
print(f'Lista 6 com elemento adicioado em posição escolhida{lista6}')

#inverter listas

lista6.reverse()
print(f'Lista 6 inversa:{lista6}')

#outra forma de inverter(ou seja vai voltar a ser a lista criada inicialmente)
print(f"Lista 6 inversa novamente: {lista6[:: -1]}")

#Copiar lista
lista7 = lista6.copy()
print(f'Lista 6: {lista6}')
print(f'Lista 7 copia da 6:{lista7}')

#contar numero total de elemenetos na lista
contlist6=(len(lista6))
print(f'O numero de elementos da lista6 é:{contlist6}')

#Remover ultimo elemento da lista
lista8 = [1, 10, 33, 15, 10, 9999]
print(f'Lista 8:{lista8}')
lista8.pop()
print(f'Lista 8 com elemento removido:{lista8}')

#Remover elemento pelo indice
lista8.pop(3)
print(f'Lista 8 com elemento indice 3 removido:{lista8}')

#Separar elementos da lista
lista9 = 'testando a lista'
print(lista9)
lista9 = lista9.split()
print(lista9)

"""
#Iteração com listas, o elemento é referente a cada elemento da lsita

#Exemplo 1:

soma = 0
for elemento in lista8:
    print(elemento)
    soma = soma + elemento;
print(f'A soma de elementos da lista 8 é:{soma}')

#Exemplo 2: Simulando um carrinho de compras.

carrinho = []
produto = ''

while produto != 'sair':

    produto = str(input("Adicione produtos no carrinho ou digite sair para sair:"))
    if produto != 'sair':
        carrinho.append(produto)
    if (carrinho == []):
        print("Carrinho vazio")

for produto in carrinho:
    print(f'Produtos adicionados:{ produto}')
"""

#Deep copy, a lista copiada é independente da original.
listao = [1,5,6,7]
newnumeros = listao.copy()
print(f'Lista independente copiada:  {newnumeros}')

#shallow copy: as listas sao dependentes, se uma é modificada a outra tbm é.

lista10 = [1, 2, 3]
print(lista10)

nova = lista10
print(nova)

nova.append(10)
print(lista10)
print(nova)

lista10.append(120)
print(lista10)
print(nova)

"""



                                PARTE DE INDICE 



"""

#Gerar indice em um for

for indice, elements in enumerate(lista8):
    print(indice)

#Encontrar o indice de um elemento de forma mais facil

print(f'Em qual indice esta o elemento 10 da lista 8: {lista8.index(10)}')

#Fazer busca dentro de um range

numeros = [5, 6, 7, 5, 8, 9, 10]
print(f'Lista numeros:{numeros} ')
print(f'Buscando indice do elemento 5 da lista numeros a partir do indice 1: {numeros.index(5, 1)}')

#Slicing

#lista[inicio:fim:passo] igual ao range

print(numeros[1:6:1]) #Neste caso comecou no elemento de indice 1 foi ate o de indice 6.

