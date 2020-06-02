"""
Herança (inheritance)

A ideia de herança é a de reaproveitar codigos. Também extender nossas classes.

Basicamente uma classe herda atributos e métodos de outra classe.


"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):  # Dessa forma a class cliente ta herdando os atributos da classe pessoa
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herdou de pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):  # Sobrescrita de méotodo.
        return f"Funcionario: {self.__matricula} Nome: {self._Pessoa__nome}"


cliente1 = Cliente('Mapache', 'God', '123.232.332-52', 5000)
funcionario1 = Funcionario('Maicon', 'Jordan', '132.232.543-33', 9000)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
