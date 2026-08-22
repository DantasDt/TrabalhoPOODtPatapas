class Jogador:
    def __init__(self, nome, idade, posicao, numero, contrato):
        self.__nome = nome
        self.__idade = idade
        self.__posicao = posicao
        self.__numero = numero
        self.__contrato = contrato

    def AlterarNumero(self, num):
        self.__numero = num
        return self.__numero

    def GetNome(self):
        return self.__nome
    
    def GetIdade(self):
        return self.__idade
    
    def GetPosicao(self):
        return self.__posicao
    
    def GetNumero(self):
        return self.__numero
    
    def GetContrato(self):
        return self.__contrato
