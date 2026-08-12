from Time import Time
from Jogador import Jogador
from random import *

class Base(Time):
    def __init__(self, nome, anoF, titulos, tecnico, categoria):
        super().__init__(nome, anoF, titulos, tecnico)
        self.__categoria = categoria
        self.__jogadores = []

    def JogadorDestaque(self):
        return f"Jogador Destaque: {self.__jogadores[randint(len(self.__jogadores))]}"

    def Promover(self):
        self.__categoria

    def GetCategoria(self):
        return self.__categoria

    def Contratar(self):
        NomeJ = input("Informe o nome do jogador: ")
        IdadeJ = input("Informe a idade do jogador: ")
        PosicaoJ = input("Informe a posicao do jogador: ")
        NumeroJ = input("Informe o numero do jogador: ")
        ContratoJ = input("Informe o contrato do jogador: ")
        jogador = Jogador(NomeJ, IdadeJ, PosicaoJ, NumeroJ, ContratoJ)
        self.__jogadores.append(jogador)

    def AdicionarJogador(self, jogador):
        self.__jogadores.append(jogador)
