from Time import Time
from Jogador import Jogador
from random import *

class Base(Time):
    def __init__(self, nome, anoF, titulos, tecnico, contato, categoria):
        super().__init__(nome, anoF, titulos, tecnico, contato)
        self.__categoria = categoria
        self.__jogadores = []

    def JogadorDestaque(self):
        return f"Jogador Destaque: {self.__jogadores[randint(len(self.__jogadores))]}"


    def GetCategoria(self):
        return self.__categoria

    def GetJogadores(self):
        return self.__jogadores

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

    def diasParaProf(self):
        for jogador in self.__jogadores:
            if jogador.GetIdade() < 20:
                print(f"{jogador.GetNome()} ainda não subiu para o profissional!!!!!!!")
            else:
                print(f"{jogador.GetNome()} já é profissional!!!!!")
