# -*- encoding: utf-8 -*-

"""
Conhecendo o pickle

A função do pickle é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

#O modulo pickle não é seguro contra dados maliciosos. Portanto não e recomendado
trabalhar com pickle em arquivos vindos de estranhos.

"""

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} esta latindo...')


felix = Gato('Felix')
pluto = Cachorro('Pluto')

"""
#Fazendo a escrita em arquivos pickle, ou seja binario

with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)


"""
#Fazer as leitura de dados em arquivos pickle

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
