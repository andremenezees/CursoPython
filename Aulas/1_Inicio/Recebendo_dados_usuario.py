"""

Recebendo dados do usuário

input() -> todo dado recebido via input vira string.

"""


#Recebendo dados de forma antiga (igual em C)

print("Qual seu nome? ")
nome = input()   #input = entrada

print('Qual sua idade?')
idade = input()

#Recebendo dados de forma nova

nome = input('Qual seu nome? ')
idade = input('Qual sua idade?')


#Printar a resposta

#Exemplo antigo semelhante a programação em C
print('A %s tem %s anos' % (nome, idade))

#Exemplo um pouco mais novo

print('A {0} tem {1} anos'.format(nome, idade))

#Exemplo utilizado atualmente

print(f'A {nome} tem {idade} anos')

#Como utilizar esta nova forma

print(f'{nome} nasceu em {2020 - int(idade)}')

