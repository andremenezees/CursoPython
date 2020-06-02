
#Faça um programa q leia numeros inteiros e floats

'''
numero = 100.4343
nfloat = float(numero)
nint = int(numero)
print(f'Numero inteiro:{nint}')
print(f'Numero float:{nfloat}')
'''

#Peça ao usuario para digitar tres valores inteiros e imprima a soma deles.
import math

'''
soma = 0
for n in range(1,4):
    num = int(input(f"Digite o {n} numero:"))

    soma = soma + num
print(f'A soma é: {soma}')
'''

#Leia um numero real e imprima o quadrado dele

'''
nreal = float(input('Digite o numero real:'))
dobroreal = nreal**2
print(f'O dobro do numero real digitado é:{dobroreal}')
qreal = nreal/5
print(f'A quinta parte do numero real é:{qreal}')
'''

#Ler temperatura em graus celsius e converter para fahrenheit

'''
celsius = float(input(f'Digite a temperatura em celsius:'))
print(f"Temperatura a ser convertida:{celsius}")
fahrenheit = celsius*(9.0/5.0) + 32.0
print(f'Temperatura em fahrenheit:{fahrenheit}')
'''

#Ler velocidade em km/h e converter para m/s

'''
k = float(input(f'Digite a velocidade em km/h:'))
print(f'Velocidade digitada:{k}')
m = k/3.6
print(f'Valor em m/s:{m}')
'''

#Programa que le um valor de um produto e imprima o valor com desconto de 12%

'''
produto = float(input('Digite o valor do produto:'))
produtodesc = produto - produto*0.12
print(f'O valor do produto com desconto:{produtodesc}')
'''

#Enunciado questao 40
'''
Uma empresa contrata um encanador a 30 reais por dia. Fazer um programa que solicita
o numero de dias trabalhados pelo encanador e imprima a qunatia liquida que devera ser
paga, sabendo-se que são descontados 8% para imposto de renda.

precodia = 30
dias = int(input(('Numero de dias trabalhados pelo encanador:')))
quant =precodia*dias
print(f'Quantia ganha sem imposto:{quant}')
quantimp = quant - quant * 0.08
print(f'Quantidade ganha com imposto:{quantimp}')

'''

#Enunciado da questao 46
'''
Faça um programa que leia um numero inteiro positivo de tres digitos(de 1oo a 999).
Gere outro numero formado pelos digitos invertidos do numero lido.

numerolido = int(input('Digite um numero inteiro positivo de tres digitos:'))
numerogerado = int(str(numerolido)[::-1])
print(f'Numero gerado:{numerogerado}')

'''

#Leia um numero inteiro de 4 digitos (de 1000 a 9999) e imprima 1 digito por linha.

'''
n4digitos = int(input('Digite um numero inteiro de 4 digitos:'))
print(f'O numero digitado é:{n4digitos}')
num = str(n4digitos)
num1 = len(num)

print('Numeros separados:')
for n in range(0, num1):
    print(str(num[n]))
'''

'''
Escreva um programa que leia as cordenadas x e y de pontos no R² e calcule a
distancia da origem (0,0).

origemx = 0
origemy = 0
x = float(input('Digite a cordenada x:'))
y = float(input('Digite a cordenada y:'))
print(f'As cordenadas são-> x:{x} y:{y}')

#Formula da distancia
distancia = (((x - origemx) ** 2) + ((y - origemy) ** 2)) ** (1/2)

print(f'{distancia}')
'''

'''
Tres amigos jogaram na loteria. Caso eles ganhem, o premio deve ser repartido
proporcionalmente ao valor que cada um deu para a realizaçao da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do premio, e imprima quanto cada um
ganharia do premio com base no valor investido.
'''

premio = float(input("Digite o valor do premio:"))
apost1 = float(input("Valor que o primeiro amigo apostou:"))
apost2 = float(input("Valor que o segundo amigo apostou:"))
apost3 = float(input("Valor que o terceiro amigo apostou:"))
soma = apost1 + apost2 + apost3

porcent1 = apost1/soma
porcent2 = apost2/soma
porcent3 = apost3/soma

premio1 = premio*porcent1
premio2 = premio*porcent2
premio3 = premio*porcent3
print(f'Valor ganho do primeiro amigo:{premio1}')
print(f'Valor ganho do segundo amigo:{premio2}')
print(f'Valor ganho do terceiro amigo:{premio3}')


'''

Faça um programa para ler as dimensoes de um terreno(comprimento C e largura L), bem
como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com
tela.


C = float(input("Qual o comprimento do terreno:"))
L = float(input("Qual a largura do terreno:"))
P = float(input("Qual é o preço do metro da tela P:"))

area = C * L
custo = area * P
print(f'O custo para cercar a area é de :{custo}')
'''




