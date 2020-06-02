"""
Similar a função reverse porem reverse só funciona em listas
"""

#exemplo

lista = [1, 2, 3, 4, 5]


print(list(reversed(lista)))

print(tuple(reversed(lista)))

for letra in reversed('god god'):
    print(letra, end='')

#podemos utilizar o reversed() para fazer um loop de for reverso

for n in reversed(range(0, 10)):
    print(n)

#Outra forma de fazer este for

for n in range(-10,0):
    print(n)