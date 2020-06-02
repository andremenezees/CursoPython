"""
Crie uma função que recebe como parametro um numero inteiro e devolve o seu dobro.

"""


def dobro(num, elevado):
    return num ** elevado


print(dobro(5, 2))

"""
Faça uma função que recebe a data atual(dia, mes e ano em inteiro) e exiba-a na
tela no formato textual por extenso. Exemplo: Data: 01/01/2000, imprimir: 1 de
janeiro de 2000.

"""

cont = {1: 'janeiro', 2: 'fevereiro', 3: 'marco', 4: 'abril', 5: 'maio',
        6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro',
        11: 'novembro', 11: 'dezembro'}


def data_atual(dia, mes, ano):
    global cont
    return (f'Data: {dia} de {cont[mes]} de {ano}')


print(data_atual(1, 5, 2000))

"""
Faça uma função para verificar se um numero é positivo ou negativo. Sendo que o 
valor de retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0.

"""


def verificar_num(numero):
    if numero > 0:
        return 1
    if numero < 0:
        return -1
    if numero == 0:
        return 0


print(verificar_num(0))
print(verificar_num(10))
print(verificar_num(-3))

"""
Faça uma função que receba a altura e o raio de um cilindro circular e retorne o
volume do cilindro. O volume de um cilindro circular é calculado por meio da
seguinte formula: V = pi *raio² *altura, onde pi = 3.141592

"""


def volume_cilindro(altura, raio):
    pi = 3.141592
    return pi * altura * raio * raio


print(volume_cilindro(5, 3))

"""
Faça uma função que receba dois valores numéricos e um símbolo. Este símbolo 
representará a operação que se deseja efetuar com os números. Se o símbolo for
+ deverá ser realizada uma adição, se for - uma subtração, se for / uma divisão
e se for * sera efetuada uma multiplicação.

"""


def operacao(num1, num2, simb):
    if simb == '+':
        return num1 + num2
    if simb == '-':
        return num1 - num2
    if simb == '/':
        return num1 / num2
    if simb == '*':
        return num1 * num2


print(operacao(2, 3, '+'))
print(operacao(2, 3, '-'))
print(operacao(2, 3, '/'))
print(operacao(2, 3, '*'))

"""
Faça uma função que receba a distancia em Km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma
mensagem de acordo com a tabela abaixo:

            Consumo          Km/l           Mensagem
            menor que         8             Venda o carro!
            entre             8 a 14        Economico!
            maior que         12            Super economico!
"""


def consumo(distancia, quant):
    consumo = distancia / quant
    if consumo < 8:
        return 'Venda o carro!'
    if 8 < consumo < 14:
        return 'Economico!'
    if consumo > 12:
        return 'Super economico'


print(consumo(10, 1))
print(consumo(7, 1))
print(consumo(13, 1))


"""
Faça uma função que receba uma matriz 3x3 elementos. Calcule a soma dos elementos
que estão acima da diagonal principal

"""
"""
matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
soma = 0

def soma_elementos(matriz1):
    global soma
    for l in range(0,3):
        for c in range(0,3):
            soma = matriz1[0][1] + matriz1[0][2] + matriz1[1][2]
    return soma


for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))

print(soma_elementos(matriz))
"""

"""
Faça uma função que recebe por parametro, uma matriz A[7][6] e uma linha N e
retorne a soma dos elementos dessa linha.

"""

"""
matriz = [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]
soma = 0
def soma_elem_matriz7x6(matriz11,linha):
    global soma
    for l in range(7):
        for c in range(6):
            if l == (linha-1):
                soma = soma + matriz[linha-1][c]
    return soma


for l in range(7):
    for c in range(6):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
print(soma_elem_matriz7x6(matriz, 3))

"""

"""
Implemente a função a qual recebe duas strings, str1 e str2 e cocatena a string
apontada por str2 a string apontada por str1.

"""

"""
def concatena_str(str1,str2):
    return f'Strings:{str2} {str1}'

string1 = str(input('Digite a str1:'))
string2 = str(input('Digite a str2:'))

print(concatena_str(string1, string2))
"""


"""
Escreva uma função que gera um triangulo de altura e lados n e base 2*n-1. Por
exemplo, a saida para n = 6 seria:
                  *
                 ***
                *****
               *******
              *********
             ***********
"""
"""
def triangulo(n):

    for i in range(1, (n+1)):
        base = 2 * i - 1
        print('*'*base)

triangulo(6)

"""
"""
Considerando a estrutura:

def ponto:
    int x
    int y

Para representar um ponto em uma grade 2D, implemente uma função que indique se um
ponto p está localizado dentro ou fora de um retangulo. O retangulo é definido por
seus vetices inferior esquerdo v1 e superior direito v2. A função deve retornar 1
caso o ponto esteja localizado dentro do retangulo e 0 caso contrario. Essa função
deve obedecer ao prototipo:
int dentroret(struct ponto* v1, struct ponto* v2, struct ponto* p)
"""

def ponto(x, y):
    return x, y

def dentroret(v1, v2, p):   #V1 = vertice lateral  v2 = vertice grande
    (x, y) = p

    if x <= v2 and y <= v1:
        return 1
    return 0

print(dentroret(3, 5, ponto(2,4)))
print(dentroret(3, 5, ponto(4,2)))