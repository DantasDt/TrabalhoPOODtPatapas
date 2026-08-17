class Contato:
    def __init__(self, tipo, contato):
        self.__tipo = tipo
        self.__contato = contato

    def Ligar(self):
        return f"Contato do time: {self.__contato}"

    def GetTipo(self):
        return self.__tipo 

    def GetContato(self):
        return self.__contato
