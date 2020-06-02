"""
Métodos

 Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
 que este objeto pode realizar no seu sistema.

 2 tipos de métodos: Métodos de instancia e métodos de classe.

"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligado = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuarios no sistema.')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    # Não é aconselhavel criar funções com dunder (__) como abaixo.
    def __correr__(self, metros):
        print(f'{self.__nome}Esta correndo {metros} metros')


p1 = Produto('Playstation', 'Video game', 2300)

print(p1.desconto(50))
# Printando atributo privado(Porem não recomendado, pois esta fora de class)
print(p1._Produto__nome)

print("\n")

"""
nome = input('Informe o nome:')
sobrenome = input('Informe o sobrenome:')
email = input('Informe o email:')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senhas não conferem')
    exit(1)

print('Usuario criado com sucesso')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

# O metodo criptografado é o q é salvo em banco de dados de senhas.
print(f'Senha user criptografada: {user._Usuario__senha}')

"""

# Métodos de classe (checar Class Usuario para entender)

user1 = Usuario('Mapache', 'God', 'mapachegod@gmail.com', '12345')
user2 = Usuario('Mapache1', 'God', 'mapache1god@gmail.com', '123345')

Usuario.conta_usuarios()


