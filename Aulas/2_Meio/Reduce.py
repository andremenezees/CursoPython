"""
Reduce

Para utilizar a função reduce é necessario utilizar o modulo 'functools'

Entendendo reduce()

#Imagine que voce tem uma coleção de dados:

dados = [a1, a2, a3,..., an]

#E voce tem uma função que recebe dois parametros:

def funcao(x,y):
    return x * y

Assim como map() e filter(), a funcao reduce() recebe dois parametros, a funcao e o iteravel.
A função reduce(), funciona da seguinte forma:
    passo 1: res1 = f(a1, a2) #Aplica a função nos dois primeiros elementos da coleção e guarda os resultados.
    passo 2: res2 = f(res1, a3) #Aplica a função utilizando o resultado anterior mais o proximo elemento dos dados.

"""

#exemplo (utilizar reduce para multiplicar todos os valores de uma lista)

from functools import reduce

dados = [1, 1, 1, 1, 2, 3, 4, 5, 6]

#para utilizar reduce() precisamos de uma função que receba dois parametros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

#Com for
res = 1
for n in dados:
    res = res * n

print(res)