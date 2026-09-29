import random
import navios
import utils

FROTA = {
    "grande": 2,
    "pequeno": 3
    }


class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [
            ["~"] * utils.TAMANHO_TABULEIRO
            for _ in range(utils.TAMANHO_TABULEIRO)
        ]
        self.navios = []

    def _cabe(self, posicoes):  # interna
        for linha, coluna in posicoes:

            if linha < 0 or linha >= utils.TAMANHO_TABULEIRO:
                return False

            if coluna < 0 or coluna >= utils.TAMANHO_TABULEIRO:
                return False

            if self.tabuleiro[linha][coluna] != "~":
                return False

        return True

    def posicionar_navio(self, tipo):
        tamanho = navios.TAMANHOS[tipo]

        while True:
            linha = random.randint(0, utils.TAMANHO_TABULEIRO - 1)
            coluna = random.randint(0, utils.TAMANHO_TABULEIRO - 1)

            orientacao = random.choice(["horizontal", "vertical"])

            posicoes = navios.gerar_posicoes(linha,
                                             coluna, orientacao, tamanho)

            if self._cabe(posicoes):
                for linha, coluna in posicoes:
                    self.tabuleiro[linha][coluna] = "N"

                navio = navios.Navio(tipo, posicoes)
                self.navios.append(navio)

                break

    def posicionar_frota(self):
        for tipo, quantidade in FROTA.items():
            for _ in range(quantidade):
                self.posicionar_navio(tipo)

    def receber_tiro(self, linha, coluna):
        celula = self.tabuleiro[linha][coluna]
        if celula == "X" or celula == "O":
            return ("repetido", None)

        if celula == "~":
            self.tabuleiro[linha][coluna] = "O"
            return ("agua", None)

        if celula == "N":
            self.tabuleiro[linha][coluna] = "X"

            pos = (linha, coluna)

            for navio in self.navios:
                if navio.ocupa(pos):
                    navio.registrar_acerto(pos)

                    if navio.afundado():
                        return ("afundou", navio.tipo)

                    return ("acerto", None)

    def todos_afundados(self):
        for navio in self.navios:
            if not navio.afundado():
                return False

        return True

    def exibir(self, mostrar_navios):
        print("   " + " ".join("ABCDEFGHIJ"))

        for i, linha in enumerate(self.tabuleiro):
            linha_exibida = []

            for celula in linha:
                if celula == "N" and not mostrar_navios:
                    linha_exibida.append("~")
                else:
                    linha_exibida.append(celula)

            print(f"{i + 1:2} " + " ".join(linha_exibida))

        print()
        print("Legenda:")
        print("~ Água não jogada")
        print("N Navio")
        print("X Acerto")
        print("O Água jogada")
