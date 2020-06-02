"""
Polimorfismo

Poli -> Muitas
Morfis -> Formas

O overwriting (sobreescrita) é o poliformismo.
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este metodo')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau') #Polimorfismo

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala miau") #Polimorfismo

class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala algo..")  #Polimorfismo

#testes

felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()

