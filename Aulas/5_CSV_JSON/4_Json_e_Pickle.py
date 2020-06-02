# -*- encoding: utf-8 -*-

"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> Meios de comunicação entre os serviços oferecidos por empresas e desenvolvedores.


"""

import json

#Dumps serve para fazer as modificaçoes necessarias para poder trabalhar com JSON.

"""
ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))
print(ret)
"""

"""
class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca



#Mostrando a utilizadade do dumps, lembrando q json só le arquivos com aspas duplas.
louie = Gato('Louie', 'Vira-lata')

print(louie.__dict__)

ret = json.dumps(louie.__dict__)
print('\n')
print(ret)
"""


#EScrevendo o arquivo

"""
import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


louie = Gato('Louie', 'Vira-lata')

with open('louie.json', 'w') as arquivo:
    ret = jsonpickle.encode(louie)
    arquivo.write(ret)

"""

#lendo o arquivo em json

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open('louie.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(ret.nome)
    print(ret.raca)