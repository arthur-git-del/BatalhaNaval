import random

import jogador
import utils


class Computador(jogador.Jogador):
    def __init__(self, nome):
        super().__init__(nome)

        self.jogadas_disponiveis = []

        for linha in range(utils.TAMANHO_TABULEIRO):
            for coluna in range(utils.TAMANHO_TABULEIRO):
                self.jogadas_disponiveis.append((linha, coluna))

        random.shuffle(self.jogadas_disponiveis)

    def escolher_jogada(self):
        return self.jogadas_disponiveis.pop()
