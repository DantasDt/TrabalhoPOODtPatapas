import json
from Time import Time
from Base import Base
from Jogador import Jogador


def SalvarTime(obj):
    dados = {
        "time": {
            "nome": obj.GetNome(),
            "anoF": obj.GetAnoF(),
            "titulos": obj.GetTitulos(),
            "tecnico": obj.GetTecnico()
        },

        "jogadores": []
    }

    for jogador in obj.GetJogadores():
        dados["jogadores"].append({
            "nome": jogador.GetNome(),
            "idade": jogador.GetIdade(),
            "posicao": jogador.GetPosicao(),
            "numero": jogador.GetNumero(),
            "contrato": jogador.GetContrato()
        })

    with open("Time.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def CarregarTime():
    with open("Time.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

        obj = Time(
            dados["time"]["nome"],
            dados["time"]["anoF"],
            dados["time"]["titulos"],
            dados["time"]["tecnico"])

    for dadosJogador in dados["jogadores"]:
        jogador = Jogador(
            dadosJogador["nome"],
            dadosJogador["idade"],
            dadosJogador["posicao"],
            dadosJogador["numero"],
            dadosJogador["contrato"])

        obj.AdicionarJogador(jogador)
    return obj

def SalvarBase(obj):
    dados = {
            "time": {
            "nome": obj.GetNome(),
            "anoF": obj.GetAnoF(),
            "titulos": obj.GetTitulos(),
            "tecnico": obj.GetTecnico(),
            "categoria": obj.GetCategoria()
            },
    
            "jogadores": []
        }
    
    for jogador in obj.GetJogadores():
        dados["jogadores"].append({
            "nome": jogador.GetNome(),
            "idade": jogador.GetIdade(),
            "posicao": jogador.GetPosicao(),
            "numero": jogador.GetNumero(),
            "contrato": jogador.GetContrato()
        })
    
    with open("Base.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def CarregarBase():
    with open("Base.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    
    obj = Time(
        dados["time"]["nome"],
        dados["time"]["anoF"],
        dados["time"]["titulos"],
        dados["time"]["tecnico"],
        dados["time"]["categoria"])
    
    for dadosJogador in dados["jogadores"]:
        jogador = Jogador(
        dadosJogador["nome"],
        dadosJogador["idade"],
        dadosJogador["posicao"],
        dadosJogador["numero"],
        dadosJogador["contrato"])
    
        obj.AdicionarJogador(jogador)
    return obj
