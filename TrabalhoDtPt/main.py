import os
from Jogador import Jogador
from Base import Base
from Time import Time
from Tecnico import Tecnico
from Contato import Contato
from dadosJson import SalvarTime
from dadosJson import SalvarBase
from dadosJson import CarregarBase
from dadosJson import CarregarTime
objTime = CarregarTime()
objBase = CarregarBase()

while True:
    x = input("Oque vai alterar: ").lower()
    os.system("cls")

    if x == "time":
        y = input("Oque deseja fazer? ").lower()
        os.system("cls")

        if y == "contratar":
            objTime.Contratar()
            SalvarTime(objTime)
            os.system("cls")

        elif y == "criar":
            Nome = input("Informe o nome do time: ")
            AnoF = int(input("Informe o ano de fundacao: "))
            Titulos = input("Informe os titulos: ")
            print("")
            NomeT = input("Informe o nome do tecnico: ")
            TitulosT = input("Informe os titulos do técnico: ")
            AnosT = int(input("Informe os anos trabalhados: "))
            IdadeT = input("Informe a idade do tecnico: ")
            Esquema = input("Informe o esquema tatico: ")
            print("")
            TipoC = input("Informe o tipo de contato: ")
            ContatoC = input("Informe o contato: ")
            contato = (TipoC, ContatoC)
            objTec = Tecnico(NomeT, TitulosT, AnosT, IdadeT, Nome, Esquema)
            objTime = Time(Nome, AnoF, Titulos, objTec, contato)
            SalvarTime(objTime)
            os.system("cls")

    elif x == "base":
        y = input("Oque deseja fazer? ").lower()
        os.system("cls")
        if y == "criar":
            Nome = input("Informe o nome do time: ")
            AnoF = int(input("Informe o ano de fundacao: "))
            Titulos = input("Informe os titulos: ")
            Categoria = input("Informe a categoria: ")
            print("")
            NomeT = input("Informe o nome do tecnico: ")
            TitulosT = input("Informe os titulos do técnico: ")
            AnosT = int(input("Informe os anos trabalhados: "))
            IdadeT = input("Informe a idade do tecnico: ")
            Esquema = input("Informe o esquema tatico: ")
            print("")
            TipoC = input("Informe o tipo de contato: ")
            ContatoC = input("Informe o contato: ")
            contato = (TipoC, ContatoC)
            objTec = Tecnico(NomeT, TitulosT, AnosT, IdadeT, Nome, Esquema)
            objBase = Base(Nome, AnoF, Titulos, objTec, contato, Categoria)
            SalvarBase(objBase)
            os.system("cls") 

        elif y == "contratar":
            objBase.Contratar()
            SalvarBase(objBase)
            os.system("cls")

    elif x == "sair":
        break
