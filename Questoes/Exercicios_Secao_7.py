"""
#Exercicio 1

A = [1, 0, 5, -2, -5, 7]
print(type(A))
print(A)

#Soma de A[0] A[1] A[5]
soma = A[0] + A[1] + A[5]
print(soma)

#Modificar o elemento da posição 4 para 100
A.pop(4)
A.insert(4,100)
print(A)

for indice, valor in enumerate(A):
    print(indice, valor)

"""
from typing import List

"""
#Leia um vetor de 10 possiçoes e conte quantos valores pares ele possui.

Vetor = [5, 4, 2, 1, 7, 9, 15, 13, 11, 10]

for i,valor in enumerate(Vetor):
    if(Vetor[i] % 2 == 0):
        print(valor)
"""

"""
#Escreva um programa q leia 10 numeros em um vetor e imprima o maior elemento e seu indice.

Vetor = [5, 4, 2, 1, 7, 9, 15, 13, 11, 10]

print(f'O maior valor é {max(Vetor)} e seu indice é {Vetor.index(max(Vetor))}')

"""

"""
#Programa que mostra a quantidade de numeros negativos e a soma dos positivos

vetor = [5, -4, -2, -1, -7, -9, 15, 13, 11, -10]
soma = 0
for i, valor in enumerate(vetor):
    if(vetor[i] < 0):
        print(f"Numeros negativos:{vetor[i]}")
    else:
        soma = soma + vetor[i]

print(f'A soma dos numeros positivos são: {soma}')
"""

"""
#Programa que le vetor e verifica se existem valores iguais e os escreve na tela

vetor = [5, 5, -4, -4, -1, -9, -9, 15, 13, 11, -10]
lista = []

for v in vetor:
    if v not in lista:
        lista.append(v)
    else:
        print(v)
print(lista)

"""

# Exercico 22
"""
#Programa q le dois vetores e calcular outro vetor contendo, nas posiçoes pares os valores do
#primeiro vetor e nas posiçoes impares os valores do segundo vetor.

v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
v3 = []

v = 0
x = 0

for i, valor in enumerate(range(0, 20)):

    if i % 2 == 0:
        #for j, val in enumerate(v1):
        v3.append(v1[v])
        v = v + 1
    if i % 2 != 0:
        #for k, val1 in enumerate(v2):
        v3.append(v2[x])
        x = x + 1
print(v3)

"""

# Exercicio 24

"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o
numero do aluno e o segundo representando a sua altura em metros. Encontre o aluno mais
baixo e o mais alto. Mostre o numero do aluno mais baixo e do mais alto, juntamento com
suas alturas.

"""

"""
alt = []
maltu = 0
num = 0
minalt = 9999
num1 = 0
for i,v in enumerate(range(0, 10)):
    altura = float(input('Digite a altura:'))
    alt.append(altura)

for ind,val in enumerate(range(0, 10)):
    if(alt[ind] > maltu):
        maltu = alt[ind]
        num = ind
    if(alt[ind] < minalt):
        minalt = alt[ind]
        num1 = ind

print(f'Aluno mais alto -> Numero:{num+1} altura: {maltu} ')
print(f'Aluno mais baixo -> Numero:{num1+1} altura: {minalt} ')

"""

# Exercicio 25

"""
Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que
são multiplos de 7 ou que terminam com 7.

"""

"""
vetor = []

for num in range(0, 70000):
    if len(vetor) == 100:
        break
    if num % 7 != 0 or (num - 7) % 10 == 0:
        vetor.append(num)
print(vetor)
"""

# Exercicio 28

"""
Leia 10 numeros inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2.
Copie os valores impares de v para v1, e os valores pares de v para v2. Note que cada
um dos vetores v1 e v2 tem no maximo 10 elementos, mas nem todos os elementos são
utilizados. No final escreva os elementso utilizados em v1 e v2.

"""

"""
v = []
v1 = []
v2 = []

for val in range(0, 10):
    num = int(input('Digite um numero:'))
    v.append(num)

for ind,val1 in enumerate(range(0,10)):
    if v[ind] % 2 != 0:
        v1.append(v[ind])

    if v[ind] % 2 == 0:
        v2.append(v[ind])

print(f'Numeros de v1(impares):{v1}')
print(f'Numeros de v2(pares):{v2}')
"""
1
"""
Faça um programa para ler 10 numeros diferentes a serem armazenados em um vetor. Os
dados deverão ser armazenados no vetor na ordem que forem sendo lidos, sendo que caso
o usuario digite um numero que ja foi digitado anteriormente, o programa devera pedir
para ele digitar outro numero. Note que cada valro digitado pelo usuario deve ser
pesquisado no vetor, verificando se ele existe entre os numeros que ja foram fornecidos.
Exibir na tela o vetor final que foi digitado.

"""


"""
vetor = []
v = 0
for valu in range(0, 100):
    num = int(input('Digite o numero:'))
    if num not in vetor:
        vetor.append(num)
    else:
        print('Numero ja existente!Digite outro.')
    if len(vetor) == 4:
        break
print(vetor)


"""

"""

Faça um programa que leia dois numeros a e b (positivos menores que 10000) e :

    Crie um vetor onde cada posição é um algarismo do número. A primeira posição é o
    algarismo menos sigificativo;
    
    Crie um vetor que seja a soma de a e b, mas faça-o usando apenas os vetores
    construidos anteriormente.
    
"""

"""

a = float(input("Digite o numero a:")) #9123
b = float(input("Digite o numero b:"))

vetora = []
vetorb = []

if a <= 9 and a >= 0:
    a1int = int(a / 1)
    vetora.append(a1int)

if a <= 99 and a >= 10:

    a2int = int(a / 10)
    a2t = a2int * 10
    a1f = a - a2t
    a1int = int(a1f / 1)

    vetora.append(a1int)
    vetora.append(a2int)

if a <= 999 and a >= 100:

    a3int = int(a / 100)
    a3t = a3int * 100
    a2f = a - a3t
    a2int = int(a2f / 10)
    a2t = a2int * 10
    a1f = a2f - a2t
    a1int = int(a1f / 1)

    vetora.append(a1int)
    vetora.append(a2int)
    vetora.append(a3int)

if a <= 9999 and a >= 1000:

    a4int = int(a / 1000)
    a4t = a4int*1000
    a3f = a - a4t
    a3int = int(a3f/100)
    a3t = a3int*100
    a2f = a3f - a3t
    a2int = int(a2f/10)
    a2t = a2int*10
    a1f = a2f - a2t
    a1int = int(a1f/1)

    vetora.append(a1int)
    vetora.append(a2int)
    vetora.append(a3int)
    vetora.append(a4int)

#Vetor b

if b <= 9 and b >= 0:
    a1int = int(b / 1)
    vetorb.append(a1int)

if b <= 99 and b >= 10:

    a2int = int(b / 10)
    a2t = a2int * 10
    a1f = b - a2t
    a1int = int(a1f / 1)
    vetorb.append(a1int)
    vetorb.append(a2int)

if b <= 999 and b >= 100:

    a3int = int(b / 100)
    a3t = a3int * 100
    a2f = b - a3t
    a2int = int(a2f / 10)
    a2t = a2int * 10
    a1f = a2f - a2t
    a1int = int(a1f / 1)

    vetorb.append(a1int)
    vetorb.append(a2int)
    vetorb.append(a3int)


if b <= 9999 and b >= 1000:

    a4int = int(b / 1000)
    a4t = a4int*1000
    a3f = b - a4t
    a3int = int(a3f/100)
    a3t = a3int*100
    a2f = a3f - a3t
    a2int = int(a2f/10)
    a2t = a2int*10
    a1f = a2f - a2t
    a1int = int(a1f/1)

    vetorb.append(a1int)
    vetorb.append(a2int)
    vetorb.append(a3int)
    vetorb.append(a4int)

print(f'Numero a em  vetor: {vetora}')
print(f'Numero b em  vetor: {vetorb}')

if len(vetora) >= 4:
    vetora.append(0)

if len(vetora) >= 3:
    vetora.append(0)
    vetora.append(0)

if len(vetora) >= 2:
    vetora.append(0)
    vetora.append(0)
    vetora.append(0)

if len(vetorb) >= 4:
    vetorb.append(0)

if len(vetorb) >= 3:
    vetorb.append(0)
    vetorb.append(0)

if len(vetorb) >= 2:
    vetorb.append(0)
    vetorb.append(0)
    vetorb.append(0)
#soma

soma = []
for i, v in enumerate(range(0, 4)):
    somat = vetora[i] + vetorb[i]
    soma.append(somat)


lens = len(soma)


for ind, val in enumerate(range(0,lens)):
    if soma[ind] >= 10:
        soma[ind] = soma[ind] - 10
        indice = ind + 1
        soma[indice] = soma[indice] + 1

print(f'Somatorio dos dois numeros em vetor:{soma}')

"""

"""
Escreva um programa que leia um numero inteiro positivo n em seguida imprima n linhas
do chamado triangulo de pascal.

"""

"""
Peça ao usuario para digitar dez valores numericos e ordene por ordem crescente esses
valores, guardando-os num vetor. Ordene o valor assim que ele for digitado. Mostre ao
final na tela os valores em ordem.

"""

"""
vetor = []

for i, v in enumerate(range(0,10)):
    num = float(input('Digite um numero:'))
    vetor.append(num)
    vetor.sort()
    print(vetor)
"""

"""
leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.

"""

"""
matriz = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
print()
for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]}]', end=' ')
    print()

print(matriz)
"""

"""
Escreva uma matriz 5x5 com a diagonal principal 1 e os elementos restantes 0.

"""

"""
matriz = [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]
for l in range(0, 5):
    for c in range(0, 5):
        print(f'[{matriz[l][c]}]', end=' ')
        if l == 0 and c == 4:
            print()
        if l == 1 and c == 4:
            print()
        if l == 2 and c == 4:
            print()
        if l == 3 and c == 4:
            print()

"""

"""
Faça um programa que leia uma matriz 6x6 com valores reais.
a)Imprima a soma de todos os elementos das colunas impares.
b)Imprima a media aritimetica dos elementos da segunda e quarta coluna.
c)Substitua os valores da sexta coluna pela soma dos valores das colunas 2 e 4.
d)Imprima a matriz modificada.

"""


matriz = [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]
soma = 0
numerodelinhas = 3
NumeroDeColunas = 6
media = 0
somam = 0
smatriz = [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]

for l in range(3):
    for c in range(6):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
        if c % 2 == 0:
            soma = soma + matriz[l][c]
        if c == 1 or c == 3:
            somam = somam + matriz[l][c]
        if c == 0 or c == 1:
            smatriz[l][5] = matriz[l][0] + matriz[l][1]


media = somam/(6)
print()
for l in range(3):
    for c in range(6):
        print(f'[{matriz[l][c]}]', end=' ')
    print()

print()

print('Matriz modificada:')
for l in range(3):
    for c in range(6):
        matriz[l][5] = smatriz[l][5]
        print(f'[{matriz[l][c]}]', end=' ')
    print()


print(f'A soma de todos os elementos das colunas impares é :{soma}')
print(f'Media aritimetica dos elementos da segunda e quarta coluna:{media}')



#Exercicio 25

"""
Faça um programa para determinar a próxima jogada em um jogo da velha. Assumir que
o tabuleiro é representado por uma matriz de 3 x 3, onde cada posição representa uma
das casas do tabuleiro. A matriz pode conter os seguintes valores -1, 0, 1
representando respectivamente uma casa contendo uma peça minha (-1), uma casa vazia
do tabuleiro (0), e uma casa contendo uma peça do meu oponente(1).
Ex:
        -1  1 1
        -1 -1 0
         0  1 0

"""

