"""
Utilizando lambdas

Conhecidas por expressões Lambdas, ou simplesmente Lambdas, são funções sem nome,
ou seja, funçÕes anonimas.

"""

def funcao(x):
    return 3 * x + 1

print(funcao(4))

#Expressão lambda

lambda x: 3 * x + 1

#E como utilizar a empressão lambda?

calc = lambda x: 3 * x + 1

print(calc(4))

#Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

#O strip serve para tirar os espaços do começo e do final
#O title serve para colocar em maisculo as iniciais das palavras e em minusculo o resto.

print(nome_completo('maicon', 'jordan'))
print(nome_completo('           maicon', 'jordan                   '))
print(nome_completo('maicon', 'JORDAN'))

#Em funções python podemos ter varias entradas ou nenhuma. Portanto em lambda tbm.

amar = lambda: 'Como não amar python?'
uma = lambda x: 3* x + 1
duas = lambda x, y: 3*x + 2*y
tres = lambda x, y, z: (3 + z) + 2*x + 4*y

print(amar())
print(uma(2))
print(duas(3, 1))
print(tres(4, 1, 2))

#Outro exemplo

nomes = ['Maicon Jordan', 'Mapache X. God', 'Cristiano Ronaldo', 'Lionel Messi',
         'Neymar Jr', 'Gabriel Toledo']

print(nomes)

#Foi feito uma ordenação da lista pelo sobrenome
nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1])
print(nomes)

#Função quadratica com lambda (ax2 + bx + c)

def gerador_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

teste = gerador_funcao_quadratica(2, 3, 5)

print(teste(0))
print(teste(1))
print(teste(2))

#Outra forma de printar.
print(gerador_funcao_quadratica(2, 4, 5)(2))
