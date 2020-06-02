# -*- encoding: utf-8 -*-

"""
Assertions (Afirmações/ Checagens)

Utilizamos o 'assert' em uma expressao que queremos checar se é valida ou não.
Se a expressao for verdadeira, retorna None e se for falsa ocorre um erro tipo
AssertionError.

"""

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos numeros precisam ser positivos'
    return a + b

ret = soma_numeros_positivos(2, 4)
print(ret) #Como não apareceu a mensagem o assert foi verdadeiro.
print('\n')


#Se a comida digitada estiver dentro do assert a mensagem sera retornada.
def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'Sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'

comida = input('Informe a comida:')
print(comer_fast_food(comida))

#Alerta cuidado ao usar 'Assert' pois uma flag -o pode faze-lo parar de funcionar



