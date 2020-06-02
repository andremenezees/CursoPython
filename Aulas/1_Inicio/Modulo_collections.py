"""
São utilizados para alta performance, ou seja otimizar o codigo

Modulo collections - counter

O counter conta quantos caracteres iguais existem na lista/tupla/etc..
"""

#Utilizando counter
#Importe
from collections import Counter

lista = [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 4, 144, 45, 55, 33]

res = Counter(lista)
print(type(res))
print(res)

#Exemplo 2

#Neste caso é possivel contar quantas palavras iguais existem no texto.

texto = """ Podemos imaginar o computador como uma super calculadora, capaz de fazer cálculos muito mais rápido que nós, mas para isso devemos dizer para o computador o que deve ser calculado e como deve ser calculado. A função das linguagens de programação é exatamente essa, ou seja, servir de um meio de comunicação entre computadores e humanos.

Existem dois tipos de linguagens de programação: as de baixo nível e as de alto nível. Os computadores interpretam tudo como números em base binária, ou seja, só entendem zero e um. As linguagens de baixo nível são interpretadas diretamente pelo computador, tendo um resultado rápido, porém é muito difícil e incômodo se trabalhar com elas. Exemplos de linguagens de baixo nível são a linguagem binária e a linguagem Assembly. """

palavras = texto.split()
res = Counter(palavras)
print(res)

#Encontra as 5 palavras com mais ocorrencias no texto
print(res.most_common(5))

"""
Modulo collections - Default Dict

Neste caso a unica diferença para um dicionario é que ao tentar printar uma chave
que não existe ao invés de apresentar um erro, o default dict cria esta nova chave, o q
traz uma grande utilidade para algumas coisas.

"""

#Fazendo import

from collections import defaultdict


dicionario = defaultdict(lambda: 0)
print(dicionario)

dicionario['god'] = 'mapache'
print(dicionario)

print(dicionario['outro']) #normalmente apareceria um erro, pois esta buscando uma chave q n existe
print(dicionario)


"""
Modulo collections - Ordered Dicit

Garante a ordem de inserção dos elementos.
"""

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'chave ={chave}:valor={valor}')

#Para o orderedDict a ordem de inserção dos elementos importa, enquanto em um dicionario
#comum a ordem não importa.

"""

Modulo collections - Named tuple

Tupla de alta performance

"""

from collections import namedtuple

#Precisamos definir o nome e parametros.

#Forma 1:

cachorro = namedtuple('cachorro', 'idade raca nome')

#Forma 2 = Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

#Forma 3 - Declaração Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#Usando

ray = cachorro(idade=2, raca='chow chow', nome='Ray')
print(ray)

#como printar por linha(indice)

print(ray.idade)
print(ray.raca)
print(ray.nome)

"""
Modulo collections - Deque

Deque é uma lista de alta performance

"""

#Criando deques

from collections import deque

deq = deque('mapacheson')
print(deq)

#Adicionando elementos no deque

deq.append('y') #Adiciona elemento no final

print(deq)

deq.appendleft('x') #Adiciona elemento no começo. Essa é uma das VANTAGENS do deq.
print(deq)

deq.pop() #Remove o ultimo elemento da lista
print(f'a:{deq}')

deq.popleft()  #Remove o primeiro elemento da lista
print(deq)

