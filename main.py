import menu
import estatisticas
import replay


def main():
    while True:
        opcao = menu.menu_principal()

        if opcao == 1:
            modo = menu.selecionar_modo()

            if modo == 0:
                continue

            jogador1, jogador2 = menu.preparar_partida(modo)

            resultado = menu.executar_partida(jogador1, jogador2, modo)

            venceu = resultado["vencedor"] is jogador1

            estatisticas.registrar_partida(jogador1, venceu)

            replay.salvar_replay(resultado["historico"])

            opcao_fim = menu.tela_fim_jogo(resultado)

            if opcao_fim == 1:
                replay.reproduzir_replay()

            elif opcao_fim == 2:
                modo = menu.selecionar_modo()

                if modo == 0:
                    continue

                jogador1, jogador2 = menu.preparar_partida(modo)

                resultado = menu.executar_partida(jogador1, jogador2, modo)

                venceu = resultado["vencedor"] is jogador1

                estatisticas.registrar_partida(jogador1, venceu)

                replay.salvar_replay(resultado["historico"])

            elif opcao_fim == 3:
                continue

            input("Pressione Enter para continuar.")

        elif opcao == 2:
            estatisticas.exibir_estatisticas()
            input("Pressione Enter para continuar.")

        elif opcao == 3:
            replay.reproduzir_replay()
            input("Pressione Enter para continuar.")

        elif opcao == 4:
            print("================================")
            print("                  CREDITOS")
            print("================================")
            print()
            print("BATALHA NAVAL - GPTECH GAMES")
            print()
            print("Desenvolvido por:")
            print("Arthur Oliveira Bonifacio")
            print()
            print("Orientador:")
            print("Prof. Guido Pantuza")
            print()
            print("Projeto desenvolvido em Python")
            print()
            print("================================")

            input("Pressione Enter para voltar ao menu.")

        elif opcao == 5:
            print("Saindo...")
            break


main()
