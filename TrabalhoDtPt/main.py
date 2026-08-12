import os
from Jogador import Jogador
from Base import Base
from Time import Time
from Tecnico import Tecnico
from dadosJson import SalvarTime
from dadosJson import SalvarBase
from dadosJson import CarregarBase
from dadosJson import CarregarTime
try:
    objTime = CarregarTime()
    objBase = CarregarBase()
except:
    print("Nada a carregar")

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
            NomeT = input("Informe o nome do tecnico: ")
            TitulosT = input("Informe os titulos do técnico: ")
            AnosT = int(input("Informe os anos trabalhados: "))
            IdadeT = input("Informe a idade do tecnico: ")
            Esquema = input("Informe o esquema tatico: ")
            objTec = Tecnico(NomeT, TitulosT, AnosT, IdadeT, Nome, Esquema)
            objTime = Time(Nome, AnoF, Titulos, NomeT)
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
            NomeT = input("Informe o nome do tecnico: ")
            TitulosT = input("Informe os titulos do técnico: ")
            AnosT = int(input("Informe os anos trabalhados: "))
            IdadeT = input("Informe a idade do tecnico: ")
            Esquema = input("Informe o esquema tatico: ")
            objTec = Tecnico(NomeT, TitulosT, AnosT, IdadeT, Nome, Esquema)
            objBase = Base(Nome, AnoF, Titulos, NomeT, Categoria)
            SalvarBase(objBase)
            os.system("cls") 

        elif y == "contratar":
            objBase.Contratar()
            SalvarBase(objBase)
            os.system("cls")

    elif x == "sair":
        break