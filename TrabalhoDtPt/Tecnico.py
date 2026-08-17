class Tecnico:
    def __init__(self, nome, titulos, AnosDeTrabalho, idade, time, esquema):
        self.__nome = nome
        self.__titulos = titulos
        self.__AnosDeTrabalho = AnosDeTrabalho
        self.__idade = idade
        self.__time = time
        self.__esquema = esquema

    def DefinirEsquema(self):
        self.__esquema

    def DarInstrucao(self):
        self.__nome

    def GetNome(self):
        return self.__nome

    def GetTitulos(self):
        return self.__titulos

    def GetAnosDeTrabalho(self):
        return self.__AnosDeTrabalho

    def GetIdade(self):
        return self.__idade

    def GetTime(self):
        return self.__time

    def GetEsquema(self):
        return self.__esquema
