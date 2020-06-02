class Equipamentos:
    def __init__(self, mouse, teclado):
        self.__mouse = mouse
        self.__teclado = teclado

    @property
    def mouse(self):
        return self.__mouse

    @property
    def teclado(self):
        return self.__teclado

    def exibe(self):
        print(f'Atributos Equipamentos  ->  Mouse: {self.__mouse}  Teclado: {self.__teclado}')

class Computador(Equipamentos):
    def __init__(self, mouse, teclado, placa_de_video, processador):
        super().__init__(mouse, teclado)
        self.__placa_de_video = placa_de_video
        self.__processador = processador

    @property
    def placa_de_video(self):
        return self.__placa_de_video

    @property
    def processador(self):
        return self.__processador

    def exibe(self):
        print(f' Atributos computador -> Mouse: {self.mouse}  Teclado: {self.teclado} Placa de video: {self.__placa_de_video} Processador: {self.__processador}')


class TestaEquipamento(Computador):
    def __init__(self, mouse, teclado, placa_de_video, processador):
        super().__init__(mouse, teclado, placa_de_video, processador)

    def main(self):
        #e1 = Equipamentos('Death Adder', 'Black widow')
        #c1 = Computador(e1.mouse, e1.teclado, 'gtx 1060', 'i9')
        #informacoes
        print(f"Equipamento -> Mouse: {self.mouse}  Teclado: {self.teclado}")
        print(f'Computador -> Mouse: {self.mouse}, Teclado: {self.teclado}, palaca: {self.placa_de_video}, processador: {self.processador}')

e1 = Equipamentos('Death Adder', 'Black widow')
c1 = Computador(e1.mouse, e1.teclado, 'gtx 1060', 'i9')
t1 = TestaEquipamento
t1.main(c1)
print('\n')
c1.exibe()
print('\n')
e1.exibe()