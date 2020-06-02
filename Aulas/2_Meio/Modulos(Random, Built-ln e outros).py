"""
O que são módulos?
    Modulos são nada mais nada menos que arquivos Python. Ou seja é um arquivo normal
que pode ser compartilhado.

Módulo random -> Possui várias funções para geração de números pseudo-aleatorios.

"""

"""
                M Ó D U L O         R A N D O M
"""

#Para importar todo o modulo
import random

#gera um valor aleatorio entre 0 e 1
print(random.random())

#Para importar apenas a função random

from random import uniform

#Valores aleatorios entre 3 e 7, ou seja maior q 3 e menor q 7
for i in range(10):
    print(uniform(3,  7))

#Para gerar valores inteiros

from random import randint
for i in range(5):
    print(randint(1, 5))

#Choice() -> Mostra um valor aleatório entre um iterável.
#Escolhe um elemento aleatorio de uma lista, tupla, etc que voce especificou.

from random import choice

jogadas =['pedra', 'papel', 'tesoura']

print(choice(jogadas))

#shuffle() -> Tem a função de embaralhar dados.

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)

shuffle(cartas) #Shuffle serve para embaralhar, neste caso embaralhar a lista cartas.

print(cartas)

#Forma de import utilizada para varios imports.
from random import(
    random,
    shuffle,
    randint,
    choice
)

fila = ['Geek', 'University', 'Python']
filas = [1, 2, 3, 4, 5]
print(random())
print(randint(1,3))
print(choice(fila)) #Escolhe aleatoriamente um dos elementos.
shuffle(filas)
print(filas)

"""

Módulos Externos

Utilizamos o gerenciador de pacotes python chamado Pip - Python Installer Package

http://pypi.org

colorama -> É utilizado para impressão de textos coloridos.

"""

from colorama import init, Fore

init()
print(Fore.BLUE + 'Mapache')

import pydf
pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)