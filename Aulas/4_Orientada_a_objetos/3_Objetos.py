"""
Objetos em programacao orientada a objetos.

Objetos -> São instancias da classe.

"""


class Lampada: #Classe
    def __init__(self, cor, voltagem, luminosidade):  #Metodo construtor
        self.__cor = cor     #Atributos(neste caso privados)
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):   #Metodo
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True



class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero


    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

class Usuario: #Classe

    def __init__(self, nome, sobrenome, email, senha):  #Metodo cronstutor
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


#instancias/Objetos

lamp1 = Lampada('branca', 110, 60)  #Objeto

#lamp1.ligar_desligar()

lamp1.ligar_desligar()

print(f'A lampada está ligada? {lamp1.checa_lampada()}')


#Testes com ContaCorrente e Cliente

cli1 = Cliente('Mapache', '123.123.123-44')
cc = ContaCorrente(500, 10000, cli1)

cc.mostra_cliente()


cli1.diz()

cc._ContaCorrente__cliente.diz()