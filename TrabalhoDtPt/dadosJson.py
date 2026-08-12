import json
from Time import Time
from Jogador import Jogador

def Salvar(objTime):
    dados = {
        "time": {
            "nome": objTime.GetNome(),
            "anoF": objTime.GetAnoF(),
            "titulos": objTime.GetTitulos()
        },

        "jogadores": []
    }

    for jogador in objTime.GetJogadores():
        dados["jogadores"].append({
            "nome": jogador.GetNome(),
            "idade": jogador.GetIdade(),
            "posicao": jogador.GetPosicao(),
            "numero": jogador.GetNumero(),
            "contrato": jogador.GetContrato()
        })

    with open("JsonDoDtPt.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados,arquivo,indent=4,ensure_ascii=False)

def Carregar():
    with open("JsonDoDtPt.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    objTime = Time(
        dados["time"]["nome"],
        dados["time"]["anoF"],
        dados["time"]["titulos"]
    )

    for dadosJogador in dados["jogadores"]:

        jogador = Jogador(
            dadosJogador["nome"],
            dadosJogador["idade"],
            dadosJogador["posicao"],
            dadosJogador["numero"],
            dadosJogador["contrato"]
        )
        objTime.AdicionarJogador(jogador)

    return objTime