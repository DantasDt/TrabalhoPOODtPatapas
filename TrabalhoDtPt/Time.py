from Jogador import Jogador
from Contato import Contato
from random import *

class Time:
    def __init__(self, nome, anoF, titulos, tecnico, contato):
        self.__nome = nome
        self.__anoF = anoF
        self.__titulos = titulos
        self.__tecnico = tecnico
        if isinstance(contato, Contato):
            self.__contato = contato
        else:
            self.__contato = Contato(contato[0], contato[1])
        self.__jogadores = []

    def DisputarPartida(self):

        q = ["pt", "dt", "galo"]
        golsfavor= random.randint(1,10)
        golscontra= random.randint(0,5)
        
        return f"{self.__nome} {golsfavor} X {golscontra} {choice(q)}"

    def Escalacao(self):
        if len(self.__jogadores) < 11:
            return "Não há jogadores suficientes no time. Contrate!!!!!!!!!!!!!"
        else:
            for jogador in range(0,11):
                print(f"{self.__jogadores[jogador]}")

    def Contratar(self):
        NomeJ = input("Informe o nome do jogador: ")
        IdadeJ = int(input("Informe a idade do jogador: "))
        PosicaoJ = input("Informe a posicao do jogador: ")
        NumeroJ = int(input("Informe o numero do jogador: "))
        ContratoJ = input("Informe o contrato do jogador: ")
        jogador = Jogador(NomeJ, IdadeJ, PosicaoJ, NumeroJ, ContratoJ)
        self.__jogadores.append(jogador)

    def AdicionarJogador(self, jogador):
        self.__jogadores.append(jogador)

    def JogadorDestaque(self):
        return f"Jogador Destaque: {self.__jogadores[randint(len(self.__jogadores))]}"

    def GetNome(self):
        return self.__nome
    
    def GetAnoF(self):
        return self.__anoF
    
    def GetTitulos(self):
        return self.__titulos
    
    def GetJogadores(self):
        return self.__jogadores

    def GetTecnico(self):
        return self.__tecnico

    def GetContato(self):
        return self.__contato



    def GetContato(self):
        return self.__contato
