"""
Utilizando este metodo podemos gera novas listas com dados processados a partir
de outro iteravel.

#sintaxe de list comprehension

[ dado for dado in iteravel ]

"""

# Exemplo

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

# Utilizando loop para fazer o mesmo

numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# Utilizando list comprehension

print([numero * 2 for numero in numeros])

# Outros exemplos

nome = 'Maicon Jordan'

print([letra.upper() for letra in nome])


# Exemplo 3

def caixa_alta(nome):  # Replace troca o nome[0] por nome[0].upper
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro', 'carlos']

print([caixa_alta(amigo) for amigo in amigos])

#Exemplo 4

print([numero * 3 for numero in range(1,4)])

#Exeplo 5

print([bool(valor) for valor in [0, [], '', True, 1, 3, 4.15]])

#Exemplo 6

num = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in num if numero % 2 == 0]  #numero é o q vai pra variavel
impares = [numero for numero in num if numero % 2 != 0]

print(pares)
print(impares)


res = [numero * 2 if numero % 2 == 0 else numero/2 for numero in num]
print(res)

