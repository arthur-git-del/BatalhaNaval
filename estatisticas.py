from pathlib import Path

PASTA_DATA = Path(__file__).parent / "data"
ARQUIVO_ESTATISTICAS = PASTA_DATA / "estatisticas.txt"


def carregar_estatisticas():
    try:
        with open(ARQUIVO_ESTATISTICAS, "r", encoding="utf-8") as arquivo:
            linha = arquivo.readline().strip()

        valores = linha.split(";")

        return {
            "partidas": int(valores[0]),
            "vitorias": int(valores[1]),
            "tiros": int(valores[2]),
            "acertos": int(valores[3]),
        }

    except (FileNotFoundError, ValueError, IndexError):
        return {"partidas": 0, "vitorias": 0, "tiros": 0, "acertos": 0}


def salvar_estatisticas(dados):
    PASTA_DATA.mkdir(exist_ok=True)

    with open(ARQUIVO_ESTATISTICAS, "w", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{dados['partidas']};"
            f"{dados['vitorias']};"
            f"{dados['tiros']};"
            f"{dados['acertos']}"
        )


def registrar_partida(jogador, venceu):
    dados = carregar_estatisticas()

    dados["partidas"] += 1

    if venceu:
        dados["vitorias"] += 1

    dados["tiros"] += jogador.tiros
    dados["acertos"] += jogador.acertos

    salvar_estatisticas(dados)


def calcular_aproveitamento(dados):
    if dados["tiros"] == 0:
        return 0

    return dados["acertos"] / dados["tiros"] * 100


def exibir_estatisticas():
    dados = carregar_estatisticas()

    if dados["partidas"] == 0:
        print("Nenhuma partida registrada ainda.")
        return

    aproveitamento = calcular_aproveitamento(dados)

    print("===============================")
    print("ESTATISTICAS")
    print("==============================")
    print(f"Partidas: {dados['partidas']}")
    print(f"Vitorias: {dados['vitorias']}")
    print(f"Tiros: {dados['tiros']}")
    print(f"Acertos: {dados['acertos']}")
    print(f"Aproveitamento: {aproveitamento:.2f}%")
