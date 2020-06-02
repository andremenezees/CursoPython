"""

Propriedades

"""

# Essa é a ideia de propriedades com JAVA, com get e set

"""
class Conta:
    contador = 0
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = Conta.contador + 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo = self.__saldo + valor

    def sacar(self, valor):
        self.__saldo = self.__saldo - valor

    def tranferir(self, valor, destino):
        self.__saldo = self.__saldo - valor
        destino.__saldo = destino.__saldo + valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):   #Get é apenas para pegar o valor de uma variavel de forma mais facil
        return self.__titular

    def set_titular(self, titular):  #O set é mais periogoso pois com ele é possivel altera o valor de uma variavel
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Mapache', 3000, 5000)
conta2 = Conta('Jordan', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.get_saldo() + conta2.get_saldo()  #get pega o valor e armazena nesta variavel
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.set_limite(9999999)
print(conta1.__dict__)
"""


# Ideia de propriedades em python

class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = Conta.contador + 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo = self.__saldo + valor

    def sacar(self, valor):
        self.__saldo = self.__saldo - valor

    def tranferir(self, valor, destino):
        self.__saldo = self.__saldo - valor
        destino.__saldo = destino.__saldo + valor


conta1 = Conta('Mapache', 3000, 5000)
conta2 = Conta('Jordan', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo  # get pega o valor e armazena nesta variavel
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 765432  # Atraves do property.setter
print(conta1.__dict__)
print(conta1.limite)

"""
Método SUPER

O método super() se refere a super classe.

"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        super().faz_som('Miau')
        self.__raca = raca

print('\n')
felix = Gato('Felix', 'Gato Gordo', 'Persa')


