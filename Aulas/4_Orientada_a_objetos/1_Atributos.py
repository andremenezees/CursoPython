"""

Classe -> Modelo do objeto de um mundo real sendo representado conmputacionalmente.
Atributo -> Características do objeto.
Método -> Comportamento do objeto (funções).
Construtor -> Método especial utilizado para criar os objetos.
Objeto -> Instancia da classe.

"""

"""
Classes  -> São odelos de um objeto do mundo real sendo representado conmputacionalmente.

Por exemplo se voce quiser representar uma lampada computacionalmente, isso e feito atraves de uma classe

Por exemplo idade = 32 (a classe de idade é int)

Classes podem conter:
    - Atributos: Representam a caracteristica do objeto. No nosso exemplo seriam por exemplo
    a voltagem da lampada ou a cor da lampada, seria alguma caracteristica da lampada.

    - Métodos(funções): Representam os comportamentos do objeto. Ou seja as açoes que este objeto
    pode realizar no seu sistema. No nosso exemplo um metodo seria a ação de ligar e desligar.


OBS: Utilizamos a palavra 'pass' em python quando temos um bloco de codigo que ainda nao esta
implementado.

OBS: Quando nomeamos nossas classes em python utilizamos letra inicial maiscula.

"""
# A classe de idade é o tipo de dado dela, no caso int como podemos ver.
idade = 32
print(type(idade))



class Lampadateste:
    pass

#Acabamos de criar lamp que possui o tipo de dado lampada.
lamp = Lampadateste()

print('\n')
print(type(lamp))

"""
Atributos -> Representam as caracteristicas do objeto. Como na lampada sua cor, voltagem é uma caracteristica.

    Tipos de atributos:
        - Atributos de instacia.
        - Atributos de classe.
        - Atributos dinamicos.
        
#Atributos de instacia: São atributos declarados dentro do metodo construtor.


"""

#Exemplo de classes com atributos publicos

class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligado = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo



class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


#Exemplo classes com atributos PRIVADOS

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        return self.__senha

    def mostra_email(self):
        return self.email

# o duplo _ é mais uma conveção pois em python e possivel acessar os atributos privados fora da classe

user = Acesso('mapache@gmail.com', '23231')

#E possivel acessar atributo privado porem é diferente do publico

#Atributos de instancia

#Publico
print(user.email)

#Privado
print(user._Acesso__senha)

print(user.mostra_senha())
print(user.mostra_email())


#Atributos de classe

class Produto:

    #Atributo de classe
    imposto = 1.05 #0.05 de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        self.imposto = (valor * 0.05)
        Produto.contador = self.id


p1 = Produto('PlayStation 4', 'Video game', 2300)
p2 = Produto('Xbox S', 'Video game', 4500)

print(Produto.imposto)
print(p1.imposto)
print(p1.valor)

print(p1.id)
print(p2.id)


#Atributos Dinamicos -> é um atributo de instacia que pode ser criado durante a execucao.
# o atributo dinamico sera exclusivo da instancia que o criou.

#Ex: Atributo dinamico

p2.peso = '5kg' #Atributo criado durante a execução porem não é recomendado.

print(f'Produto:{p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

#Printando estutura dos nossos produtos

print(p1.__dict__)
print(p2.__dict__) #é possivel ver que o atributo peso foi adicionado

#deletando atributo dinamicamente

print('\n')
del p2.peso
print(p1.__dict__)
print(p2.__dict__) #Peso foi deletado.

