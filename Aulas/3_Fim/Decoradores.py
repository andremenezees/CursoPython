"""
Funções de maior grandeza - Higher ordem functions(HOF)

Quando uma linguagem suporta HOF, significa que podemos ter funçoes que retornam outras
funcoes como resultado ou mesmo que podemos passar funcoes como argumentos para outras
funcoes.

"""

#Exemplos de higher ordem function:

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a -  b

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    return a/b

#higher ordem function


def calcular(num1, num2, funcao):
    return funcao(num1, num2)

#Testando

print(calcular(1, 3, somar))
print(calcular(5, 2 , diminuir))
print(calcular(2, 3, multiplicar))
print(calcular(10, 3, dividir))


#Nested functions - Funcoes aninhadas (Funcoes dentro de funcoes)

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de vc '))
    return humor() + pessoa

print(cumprimento('mapache '))

#Retornando funcoes de outras funcoes

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahaha', 'kkkk', 'jajaja'))
    return rir

rindo = faz_me_rir()
print(rindo())

"""
Decoradores (decorators) (é um aprimorador de função)

Decoradores são funções que envolvem outras funções e aprimoram seus comportamentos.


"""

#Exemplo de decorator(recebe uma funcao sempre)
#Sintaxe não recomendado


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhece-lo')
        funcao()
        print('Tenha um bom dia')
    return sendo

def saudacao():
    print('Seja bem vindo')



teste = seja_educado(saudacao)
print('\n')
teste()


#Exemplo com sintaxe recomendada.

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer voce')
        funcao()
        print('Tenha um execelente dia!')
    return sendo_mesmo

@seja_educado_mesmo   #Isso é um decorator com sintaxe recomendada
def apresentando():
    print('Meu nome é Pedro')


#Teste
print('\n')
apresentando()


#Outro exemplo
@seja_educado_mesmo
def dormir():
    print('Quero dormir')

print('\n')
dormir()


"""

Decorators com diferentes assinaturas


"""
#Desta forma é possivel fazer um decorator com diferentes assinaturas, no caso com 1 ou mais parametros
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'ola, eu sou o {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'ola eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor '


print('\n')
print(saudacao('mapache'))


print('\n')
print(ordenar('picanha', 'maionese'))


"""
Preservando metadatas com wraps

metadatas -> São dados que existem nos arquivos mas estão intrisecos (internos).

wraps -> São funções que envolvem elementos com diversas finalidades.

"""

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        """é uma funcao logar dentor de outra"""
        print(f'Voce está chamando: {funcao.__name__}')
        print(f'Aqui a documentacao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """soma dois numeros."""
    return a + b

print("\n")

#Problema
print(soma.__name__)
print(soma.__doc__)

#Resolução do problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)  #Assim resolve o problema
    def logar(*args, **kwargs):
        """é uma funcao logar dentor de outra"""
        print(f'Voce está chamando: {funcao.__name__}')
        print(f'Aqui a documentacao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """soma dois numeros."""
    return a + b

print("\n")

#resolvido
print(soma.__name__)
print(soma.__doc__)


"""

Forçando tipos de dados com decoradores

"""

