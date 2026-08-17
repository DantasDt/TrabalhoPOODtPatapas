import json
from Time import Time
from Base import Base
from Jogador import Jogador
from Tecnico import Tecnico
from Contato import Contato

def SalvarTime(obj):
    dados = {
        "time": {
            "nome": obj.GetNome(),
            "anoF": obj.GetAnoF(),
            "titulos": obj.GetTitulos(),
            "tecnico": {
                "nome": obj.GetTecnico().GetNome(),
                "titulos": obj.GetTecnico().GetTitulos(),
                "anosDeTrabalho": obj.GetTecnico().GetAnosDeTrabalho(),
                "idade": obj.GetTecnico().GetIdade(),
                "time": obj.GetTecnico().GetTime(),
                "esquema": obj.GetTecnico().GetEsquema()
            },
            "contato" : {
                "tipo": obj.GetContato().GetTipo(),
                "contato": obj.GetContato().GetContato()
            }
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
    try:
        with open("Time.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        tecnico = Tecnico("", "", 0, "", "", "")
        contato = Contato("", "")
        return Time("", 0, "", tecnico, contato)

    contato = Contato(
        dados["time"]["contato"]["tipo"],
        dados["time"]["contato"]["contato"]
    )

    tecnico = Tecnico(
        dados["time"]["tecnico"]["nome"],
        dados["time"]["tecnico"]["titulos"],
        dados["time"]["tecnico"]["anosDeTrabalho"],
        dados["time"]["tecnico"]["idade"],
        dados["time"]["tecnico"]["time"],
        dados["time"]["tecnico"]["esquema"]
    )

    obj = Time(
        dados["time"]["nome"],
        dados["time"]["anoF"],
        dados["time"]["titulos"],
        tecnico,
        contato
    )

    for dadosJogador in dados["jogadores"]:
        jogador = Jogador(
            dadosJogador["nome"],
            dadosJogador["idade"],
            dadosJogador["posicao"],
            dadosJogador["numero"],
            dadosJogador["contrato"]
        )

        obj.AdicionarJogador(jogador)

    return obj

def SalvarBase(obj):
    dados = {
        "base": {
            "nome": obj.GetNome(),
            "anoF": obj.GetAnoF(),
            "titulos": obj.GetTitulos(),
            "tecnico": {
                "nome": obj.GetTecnico().GetNome(),
                "titulos": obj.GetTecnico().GetTitulos(),
                "anosDeTrabalho": obj.GetTecnico().GetAnosDeTrabalho(),
                "idade": obj.GetTecnico().GetIdade(),
                "time": obj.GetTecnico().GetTime(),
                "esquema": obj.GetTecnico().GetEsquema()
            },
            "contato" : {
                        "tipo": obj.GetContato().GetTipo(),
                        "contato": obj.GetContato().GetContato()
            },
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
    try:
        with open("Base.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        tecnico = Tecnico("", "", 0, "", "", "")
        contato = Contato("", "")
        return Base("", 0, "", tecnico, contato, "")

    contato = Contato(
            dados["base"]["contato"]["tipo"],
            dados["base"]["contato"]["contato"]
        )

    tecnico = Tecnico(
        dados["base"]["tecnico"]["nome"],
        dados["base"]["tecnico"]["titulos"],
        dados["base"]["tecnico"]["anosDeTrabalho"],
        dados["base"]["tecnico"]["idade"],
        dados["base"]["tecnico"]["time"],
        dados["base"]["tecnico"]["esquema"]
    )

    obj = Base(
        dados["base"]["nome"],
        dados["base"]["anoF"],
        dados["base"]["titulos"],
        tecnico,
        contato,
        dados["base"]["categoria"]
    )

    for dadosJogador in dados["jogadores"]:
        jogador = Jogador(
            dadosJogador["nome"],
            dadosJogador["idade"],
            dadosJogador["posicao"],
            dadosJogador["numero"],
            dadosJogador["contrato"]
        )

        obj.AdicionarJogador(jogador)

    return obj
