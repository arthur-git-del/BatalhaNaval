import jogador
import computador
import tabuleiro
import utils
import time


def menu_principal():
    while True:
        utils.limpar_tela()

        print("==============================")
        print("        BATALHA NAVAL - GPTECH GAMES")
        print("==============================")
        print()
        print("1. Nova partida")
        print("2. Ver estatisticas")
        print("3. Assistir replay da ultima partida")
        print("4. Creditos")
        print("5. Sair")
        print()
        print("==============================")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            return 1

        elif opcao == "2":
            return 2

        elif opcao == "3":
            return 3

        elif opcao == "4":
            return 4

        elif opcao == "5":
            return 5

        else:
            print("Opcao invalida.")
            input("Pressione Enter para continuar.")


def selecionar_modo():
    while True:
        utils.limpar_tela()
        print("Selecione o modo de jogo:")
        print("1.Jogador vs Computador")
        print("2.Dois Jogadores")
        print("0.Voltar ao menu")
        print()
        opcao = input("Digite sua opção: ")

        if opcao == "1":
            return 1

        elif opcao == "2":
            return 2

        elif opcao == "0":
            return 0

        else:
            print("Opcao invalida.")
            input("Pressione Enter para continuar.")


def conferir_frota(player):
    while True:
        player.tabuleiro.exibir(True)

        resposta = input("Aceita essa frota? [S/N]: ").strip().upper()

        if resposta == "S":
            return

        elif resposta == "N":
            player.tabuleiro = tabuleiro.Tabuleiro()
            player.tabuleiro.posicionar_frota()

        else:
            print("Opção inválida. Digite S ou N.")


def preparar_partida(modo):
    if modo == 1:
        nome = input("Digite o nome do jogador: ")

        jogador_humano = jogador.Jogador(nome)
        computador_jogador = computador.Computador("Computador")

        conferir_frota(jogador_humano)

        return jogador_humano, computador_jogador

    elif modo == 2:
        jogador1 = jogador.Jogador("Jogador 1")
        jogador2 = jogador.Jogador("Jogador 2")

        conferir_frota(jogador1)

        utils.limpar_tela()

        input("Jogador 2, pressione enter para continuar.")

        conferir_frota(jogador2)

        return jogador1, jogador2


def mostrar_resultado(nome, coordenada, resultado):
    tipo = resultado[0]

    if tipo == "agua":
        mensagem = "Agua! Nenhum navio atingido nessa posicao."

    elif tipo == "acerto":
        mensagem = "Acerto! Voce atingiu um navio inimigo."

    elif tipo == "afundou":
        navio = resultado[1]
        mensagem = "Navio afundado! Voce destruiu"
        f"um navio {navio} do adversario."
    print(f"{nome} jogou {coordenada}: {mensagem}")


def executar_partida(jogador1, jogador2, modo):
    historico = []
    inicio = time.time()

    atual = jogador1
    adversario = jogador2

    while True:
        if modo == 2:
            utils.limpar_tela()
            input(f"{atual.nome}, pressione enter tecla para continuar.")

        adversario.tabuleiro.exibir(False)

        coordenada = atual.escolher_jogada()

        linha, coluna = coordenada

        resultado = adversario.tabuleiro.receber_tiro(linha, coluna)

        if resultado[0] == "repetido":
            print("Você já jogou nessa posição. Tente novamente.")
            continue

        numero = len(historico) + 1

        historico.append(
            (numero, atual.nome, coordenada, resultado)
        )

        atual.registrar_resultado(coordenada, resultado[0])

        print()
        mostrar_resultado(atual.nome, utils.coordenada_para_texto(
            linha, coluna), resultado)
        print()

        if adversario.tabuleiro.todos_afundados():
            fim = time.time()

            return {
                "vencedor": atual,
                "historico": historico,
                "tempo": fim - inicio,
                "jogador1": jogador1,
                "jogador2": jogador2
            }

        atual, adversario = adversario, atual


def tela_fim_jogo(resultado):
    vencedor = resultado["vencedor"]
    historico = resultado["historico"]
    tempo = resultado["tempo"]

    print()
    print("================================")
    print("         FIM DE JOGO")
    print("================================")
    print(f"Vencedor: {vencedor.nome}")
    print(f"Total de jogadas: {len(historico)}")
    print(f"Tempo: {utils.formatar_tempo(int(tempo))}")
    print()
    print("1.Ver replay")
    print("2.Nova partida")
    print("3.Menu principal")

    while True:
        opcao = input("Escolha uma opcao: ")

        if opcao in ["1", "2", "3"]:
            return int(opcao)

        print("Opcao invalida.")
