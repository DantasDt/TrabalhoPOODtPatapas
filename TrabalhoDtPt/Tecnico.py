import random

 
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


    def DarInstrucao(self, instrucao1, instrucao2, instrucao3, instrucao4, instrucao5):

        instrucoes = [
            instrucao1,
            instrucao2,
            instrucao3,
            instrucao4,
            instrucao5
        ]

        instrucao = random.choice(instrucoes)

        print(f"{self.__nome}: {instrucao}")

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


tecnico = Tecnico(
    "Luan",
    5,
    10,
    45,
    "Brasil",
    "4-3-3"
    )


tecnico.DarInstrucao(
    "Encaixa no canto.",
    "Controle o movimento.",
    "Cruza no alto.",
    "Acalma o jogo.",
    "Toque mais."
    )
