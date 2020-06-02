# -*- encoding: utf-8 -*-
"""
1) Crie uma classe para representar uma pessoa, com atributos privados
de nome, idade e altura. Crie os métodos públicos necessarios para sets
e gets e também um método para imprimir os dados de uma pessoa.

"""


class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def altura(self):
        return self.__altura

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade

    @altura.setter
    def altura(self, nova_altura):
        self.__altura = nova_altura


contador = 0
while 1:
    nome = input('Digite o nome:')
    if nome == 'sair':
        break
    idade = input('Digite a idade:')
    if idade == 'sair':
        break
    altura = input('Digite a altura:')
    if altura == 'sair':
        break
    contador = contador + 1
    p1 = Pessoa(nome, idade, altura)
    #setando um nome
    p1.nome = 'mapache'
    print(f'Numero da pessoa: {contador} nome:{p1.nome} idade: {p1.idade} altura: {p1.altura} de altura ')
    print(f'Existem {contador} pessoa cadastradas')



"""
3) Crie uma classe denominada Elevador para armazenar as informações de
um elevador dentro de um prédio. A classe deve aramzenar o andar atual
(térreo = 0), total de andares no prédio, excluindo o térreo, capacidade
do elevador, e quantas pessoas estão presentes nele.

A classe deve também disponibilizar os seguintes métodos:

    * Inicializa: que deve receber como parametros a capacidade do 
elevador e o total de andares do prédio(os elevadores sempre comecam
no terreo e vazio); 

    * Sai: para remover uma pessoa do elevador (so deve remover se houver
alguem dentro dele);
    
    * Sobe: para subir um andar (não deve subir se já estiver no último andar)
    
    * Desce: para descer um andar (não deve descer se já estiver no terreo)
    
    * Encapsular todos os atributos da classe(criar os métodos set e get).
       

"""


class Elevador:
    def __init__(self, andar_atual, total_andares, capacidade_elevador, numero_de_pessoas):
        self.__andar_atual = andar_atual
        self.__total_andares = total_andares
        self.__capacidade_elevador = capacidade_elevador
        self.__numero_de_pessoas = numero_de_pessoas

    @property
    def andar_atual(self):
        return self.__andar_atual

    @property
    def total_andares(self):
        return self.__total_andares

    @property
    def capacidade_elevador(self):
        return self.__capacidade_elevador

    @property
    def numero_de_pessoas(self):
        return self.__numero_de_pessoas

    def inicializa(self):
        print(f"Capacidade_elevador: {self.__capacidade_elevador}.")
        print(f"Total de andares: {self.__total_andares}.")

    # self.__andar_atual = 0
    # self.__numero_de_pessoas = 0

    def sai(self):
        if self.__numero_de_pessoas == 0:
            print(f'O numero de pessoas é {self.__numero_de_pessoas} portanto não é possivel remover.')

        if self.__numero_de_pessoas > 0:
            self.__numero_de_pessoas = self.__numero_de_pessoas - 1
            print(f'Pessoa removida, o numero de pessoas agora é {self.__numero_de_pessoas}.')

    def subir(self):
        if self.__andar_atual == self.__total_andares:
            print('O elevador já está no ultimo andar.')

        if self.__andar_atual < self.__total_andares:
            self.__andar_atual = self.__andar_atual + 1
            print(f"O elevador subiu um andar portanto o andar atual é {self.__andar_atual}.")

    def desce(self):
        if self.__andar_atual == 0:
            print(f"O elevador está no terreo, portanto não é possivel descer.")

        elif self.__andar_atual > 0:
            self.__andar_atual = self.__andar_atual - 1
            print(f"O elevador desceu um andar, portanto o andar atual é {self.__andar_atual}.")

    def adicionar_pesoas(self, pessoas_adicionadas):
        if self.__numero_de_pessoas == self.__capacidade_elevador:
            print(f'Não é possivel embarcar mais pessoas pois o elevador está cheio.')

        elif (self.__numero_de_pessoas + pessoas_adicionadas) < self.__capacidade_elevador:
            self.__numero_de_pessoas = self.__numero_de_pessoas + pessoas_adicionadas
            print(f'{pessoas_adicionadas} pessoas embarcaram no elevador, agora o elevador está com'
                  f' {self.__numero_de_pessoas} pessoas.')
        else:
            print(f'O numero de pessoas embarcadas escedeu o limite.')
            print(f'So embarcaram {(self.__capacidade_elevador) -(self.__numero_de_pessoas)} pessoas no elevador '
                  f'que agora possui {self.__capacidade_elevador} pessoas.')


#elevador(andar_atual, total_andares, capacidade_elevador, numero_de_pessoas)

e1 = Elevador(5, 5, 6, 4)
e1.inicializa()
e1.sai()
print(f"Andar atual : {e1.andar_atual}")
e1.subir()
e1.desce()
e1.adicionar_pesoas(2)


"""
4) Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o
volume e trocar os canais da televisão.

    * O controle de volume permite aumentar ou diminuir a potencia do volume
de som em uma unidade de cada vez;

    * O controle de canal também permite aumentar e diminuir o número do canal
em uma unidade, porém, também possibilita trocar para um canal indicado;

    * Também devem existir métodos para consultar o valor do volume de som e o
canal selecionado.
"""


class Televisao:

    def __init__(self, volume, canal):
        self.__volume = volume
        self.__canal = canal

    @property
    def volume(self):
        return self.__volume

    @property
    def canal(self):
        return self.__canal


televisao_volume = self.volume


class ControleRemoto(Televisao):

    def __init__(self, volume, canal):
        super().__init__(volume, canal)

    def aumentar_volume(self):
        self.volume = self.volume + 1
        print(f'Aumentou um numero no volume.')

    def diminuir_volume(self):
        self._Televisao__volume = self._Televisao__volume - 1
        print(f'Diminuiu um numero no volume.')

    def aumentar_canal(self):
        self._Televisao__canal = self._Televisao__canal + 1
        print(f'Aumentou um canal.')

    def diminuir_canal(self):
        self._Televisao__canal = self._Televisao__canal - 1
        print(f'Diminuiu um canal.')

    def trocar_canal(self, novo_canal):
        self._Televisao__canal = novo_canal
        print(f'Ocorreu uma troca de canal.')


# Televisao (volume, canal) //
t1 = Televisao(10, 33)
c1 = ControleRemoto

print(f'O volume é : {t1.volume}')
c1.aumentar_volume(t1)
c1.aumentar_volume(t1)
c1.aumentar_volume(t1)
c1.aumentar_volume(t1)
print(f'O volume agora é: {t1.volume}')

c1.diminuir_volume(t1)
c1.diminuir_volume(t1)
print(f'O volume agora é: {t1.volume}')

print('\n')
print(f'O canal é : {t1.canal}')
c1.aumentar_canal(t1)
c1.aumentar_canal(t1)
c1.aumentar_canal(t1)
c1.aumentar_canal(t1)

print(f'O canal é : {t1.canal}')
c1.diminuir_canal(t1)
c1.diminuir_canal(t1)
print(f'O canal é : {t1.canal}')

print('\n')
print(f'O canal é : {t1.canal}')
c1.trocar_canal(t1, 50)
print(f'O canal foi mudado para: {t1.canal}')
