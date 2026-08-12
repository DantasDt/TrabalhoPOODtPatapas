class Contato:
    def __init__(self, tipo, contato):
        self.__tipo = tipo
        self.__contato = contato

    def MostraContato(self):
        return f"Contato do time: {self.__contato}"
