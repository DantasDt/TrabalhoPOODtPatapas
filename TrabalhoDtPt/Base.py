from Time import Time

class Base(Time):
    def __init__(self, nome, anoF, titulos, categoria):
        super().__init__(nome, anoF, titulos)
        self.__categoria = categoria

    def JogadorDestaque(self):
        self.__categoria

    def Promover(self):
        self.__categoria
