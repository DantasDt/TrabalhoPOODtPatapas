import random
from Time import Time
from Jogador import Jogador
from Tecnico import Tecnico

class Contato:
    def __init__(self, tipo, contato, mensagens):
        self.__tipo = tipo
        self.__contato = contato
        self.__mensagens = []  


    def GetTipo(self):
        return self.__tipo 

    def GetContato(self):
        return self.__contato

    def salvar(self, tipo, mensagem):
        self.__mensagens.append((tipo, mensagem))
        return self.__mensagens

    def caixantrada(self):
        for mensagem in self.__mensagens:
            print(self.__mensagens[mensagem]) 



