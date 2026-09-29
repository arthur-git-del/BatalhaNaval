from pathlib import Path

import utils

PASTA_DATA = Path(__file__).parent / "data"
ARQUIVO_REPLAY = PASTA_DATA / "ultima_partida.txt"


def salvar_replay(historico):
    PASTA_DATA.mkdir(exist_ok=True)

    with open(ARQUIVO_REPLAY, "w", encoding="utf-8") as arquivo:
        for numero, nome, coordenada, resultado in historico:
            if isinstance(coordenada, tuple):
                coordenada = utils.coordenada_para_texto(
                    coordenada[0], coordenada[1])

            arquivo.write(f"{numero};{nome};{coordenada};{resultado[0]}\n")


def carregar_replay():
    historico = []

    try:
        with open(ARQUIVO_REPLAY, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if not linha:
                    continue

                partes = linha.split(";")

                if len(partes) != 4:
                    return []

                numero = int(partes[0])
                nome = partes[1]
                coordenada = partes[2]
                resultado = partes[3]

                historico.append((numero, nome, coordenada, resultado))

    except (FileNotFoundError, ValueError, IndexError):
        return []

    return historico


def reproduzir_replay():
    historico = carregar_replay()

    if not historico:
        print("Nenhuma partida gravada para reproduzir.")
        return

    print("Reproduzindo replay da ultima partida...")
    print()

    total = len(historico)

    mensagens = {"agua": "Agua", "acerto": "Acerto",
                 "afundou": "Navio afundado"}
    for numero, nome, coordenada, resultado in historico:
        resultado_formatado = mensagens.get(resultado.lower(),
                                            resultado.capitalize())
        print(
            f"Jogada {numero:02d}/{total} - "
            f"{nome} - {coordenada} - {resultado_formatado}"
        )

        try:
            resposta = input("[ENTER] Proxima jogada [Q] Sair do replay: ")

        except (EOFError, KeyboardInterrupt):
            return

        if resposta.strip().upper() == "Q":
            return

    print("Fim do replay")
