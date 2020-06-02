"""
Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso codigo dentro de um grupo logico e
hierarquico utilizando classes.

Abstração é o ato de expor apenas dados relevantes de uma classe, escondendo atributos
e métodos privados de usuario.


"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = Conta.contador + 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo = self.__saldo + valor
        else:
            print('O valor do saldo não é positivo.')

    def sacar(self, valor):
        if valor > self.__saldo:
            print("O valor sacado é maior que o saldo. Não foi possivel sacar")
        else:
            self.__saldo = self.__saldo - valor

        if valor < 0:
            print('O valor deve ser positivo.')

    def transferir(self, valor, conta_destino):
        self.__saldo = self.__saldo - valor
        self.__saldo = self.__saldo - 10

        conta_destino.__saldo = conta_destino.__saldo + valor



#Testando

conta1 = Conta('Mapache', 200.00, 2000.00)


"""
#Podemos perceber que atributos publicos possibilitam a mudança dos valores de forma facil.
conta1.numero = 42
conta1.titular = 'xuxa'
conta1.saldo = 999999999999999999
conta1.limite = 999999999999999999999999999999999999999999999999

print(conta1.saldo)

"""
#Atributos mudados para privado

"""
#Testes
conta1.depositar(- 200)
print(conta1.__dict__)

conta1.sacar(-200)
print(conta1.__dict__)

"""

#teste
conta1 = Conta('Mapache', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Raffa Moreira', 777, 10000)
conta2.extrato()

conta2.transferir(100, conta1)

print("\n")

conta1.extrato()
conta2.extrato()