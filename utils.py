import os

TAMANHO_TABULEIRO = 10
LETRAS_COLUNAS = "ABCDEFGHIJ"


def texto_para_coordenada(texto):
    if len(texto) < 2:
        return None

    if len(texto) > 3:
        return None

    letra = texto[0].upper()
    numero = texto[1:]

    if not numero.isdigit():
        return None

    numero = int(numero)

    if numero < 1 or numero > 10:
        return None

    if letra < "A" or letra > "J":
        return None

    coluna = ord(letra) - ord("A")

    linha = numero - 1

    return (linha, coluna)


def coordenada_para_texto(linha, coluna):
    numero = linha + 1

    letra = chr(coluna + ord("A"))

    coordernada = letra + str(numero)

    return coordernada


def formatar_tempo(segundos):
    horas = segundos // 3600
    segundos = segundos % 3600

    minutos = segundos // 60
    segundos = segundos % 60

    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"


def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
