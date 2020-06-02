"""
Heraca Multipla

Como nome ja diz é a habilidade de uma classe herdar atributos e metodos de
outras multiplas classes.

"""


# Exemplo 1 - Multiderivacao direta

class Base1:
    pass


class Base2:
    pass


class MultiDerivada(Base1, Base2):
    pass


# Exemplo 2 - Multiderivacao indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):  # E possveil perceber que herdando a base 3 a classe esta herdando todas as outras tbm.
    pass


# Exemplo

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando"

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} do mar"


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} esta andando'

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} da terra"


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


# Testando

print('\n')
baleia = Aquatico("Wally")
print(baleia.nadar())
print(baleia.cumprimentar())

print('\n')
tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

print('\n')
ping = Pinguim('Tux')
print(ping.andar())
print(ping.nadar())
print(ping.cumprimentar())  # Method resolution Order - MRO, executa a primeira super classe escrita na classe pinguim

"""

MRO = Method Resolution Order (Resolução de Ordem de Métodos)

Basicamente escolhe qm será executado primeiro.

É possivel conferir a ordem de execução através de alguns metodos:
Através de propriedade da classe __mro__
via mro()
via Help
"""
#from mro import Pinguim

print(Pinguim.__mro__) #É possivel ver qual execução sera antes.