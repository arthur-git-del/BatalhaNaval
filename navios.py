TAMANHOS = {"pequeno": 2, "grande": 4}


class Navio:
    def __init__(self, tipo, posicoes):
        self.tipo = tipo
        self.posicoes = set(posicoes)
        self.atingidas = set()

    def ocupa(self, pos):
        if pos in self.posicoes:
            return True
        else:
            return False

    def registrar_acerto(self, pos):
        if self.ocupa(pos):
            self.atingidas.add(pos)

    def afundado(self):
        if self.atingidas == self.posicoes:
            return True
        else:
            return False


def gerar_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for i in range(tamanho):
        if orientacao == "horizontal":
            posicoes.append((linha, coluna + i))
        else:
            posicoes.append((linha + i, coluna))

    return posicoes
