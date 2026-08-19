import random
from Time import Time

class Contato:
    def __init__(self, tipo, contato,tecnico, jogador):
        self.__tipo = tipo
        self.__contato = contato
        self.tecnico = tecnico
        self.jogador = jogador

    def Ligar(self):
        return f"Contato do time: {self.__contato}"

    def GetTipo(self):
        return self.__tipo 

    def GetContato(self):
        return self.__contato


    def Dialogo(self):
        dialogos =[
                (f"{self.tecnico}: Você está pronto para a partida?", f"{self.jogador}: Sim, professor. Estou preparado!"), 
                (f"{self.tecnico}: Como você está se sentindo hoje?", f"{self.jogador}: Estou bem e motivado para jogar."), 
                (f"{self.tecnico}: Preciso que você tenha mais confiança.", f"{self.jogador}: Pode deixar, vou dar o meu melhor."), 
                (f"{self.tecnico}: Você treinou muito bem esta semana.", f"{self.jogador}: Obrigado, professor. Estou me esforçando."), 
                (f"{self.tecnico}: Qual posição você prefere jogar?", f"{self.jogador}: Prefiro jogar como atacante."),
                (f"{self.tecnico}: Hoje precisamos vencer.", f"{self.jogador}: Vamos lutar pela vitória!"), 
                (f"{self.tecnico}: Não se preocupe com os erros.", f"{self.jogador}: Vou continuar tentando."),
                (f"{self.tecnico}: Você está evoluindo bastante.", f"{self.jogador}: Fico feliz em ouvir isso."), 
                (f"{self.tecnico}: Está preparado para entrar em campo?", f"{self.jogador}: Estou pronto!"),
                (f"{self.tecnico}: Mostre tudo o que aprendeu nos treinos.", f"{self.jogador}: Pode confiar em mim!")
                ]

dialogo= random.choice(dialogos) 
print(dialogo[0])
print(dialogo[1])
dialogo1 = Contato( "Treinador", "Carlos", "Carlos", "Lucas" )

dialogo1.Dialogo()
