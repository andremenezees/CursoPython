"""
Any e All

all() -> Retorna True se todos os elementos do iteravel forem verdadeiros ou
o se o iteravel estiver vazio.

"""

#Exemplo all()

print(all([0, 1, 2, 3, 4]))
print(all([1, 2, 3, 4]))
print(all([]))

#uma forma de utilizar o all
nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))

nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina', 'Abacate']
print(all([nome[0] == 'C' for nome in nomes]))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

"""
any() -> Retorna True se qulaquer elemento do iteravel for verdadeiro. Se o
iteravel estiver vazio retorna False.

"""
print(any([0, 1, 2, 3, 4, 5]))

nomes1 = ['Carlos', 'Camila', 'Cassiano', 'Cristina', 'Mpaache']

print(any([nome[0] == 'C' for nome in nomes]))

