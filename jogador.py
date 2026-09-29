import tabuleiro
import utils


class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.tabuleiro = tabuleiro.Tabuleiro()
        self.tabuleiro.posicionar_frota()

        self.tiros = 0
        self.acertos = 0

    def escolher_jogada(self):
        while True:
            try:
                texto = input(f"{self.nome}, digite uma coordenada"
                              "(letra|número): ")
            except (EOFError, KeyboardInterrupt):
                return None

            coordenada = utils.texto_para_coordenada(texto)

            if coordenada is None:
                print("Coordenada inválida. Use o formato como A1, B5 ou J10.")
                continue

            return coordenada

    def registrar_resultado(self, coordenada, resultado):
        if resultado == "repetido":
            return

        self.tiros += 1

        if resultado == "acerto" or resultado == "afundou":
            self.acertos += 1
