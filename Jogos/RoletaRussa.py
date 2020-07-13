# Jogo da Roleta Russa.
#
# O canhão do revólver é carregado com uma bala e girado para embaralhar.
# A cada rodada, o jogador pode tentar um disparo para ver se sai vivo do jogo, um máximo de 5 vezes.
# Caso resista às 5 rodadas, o jogador vence.

import time
import random
import sys

def main():
    roleta_russa()


def roleta_russa():

    canhao = [0, 0, 0, 0, 0, 0]
    i = 0

    print("\nCarregando revolver...")
    time.sleep(1)
    canhao[random.randint(0, 5)] += 1

    while canhao[i] != 1:
        tiro = input("\nTentar a sorte? S/N\nR: ")
        if tiro.lower() not in 'sim':
            print("\nVolte quando tiver mais coragem!")
            sys.exit()
        else:
            print("\n**** Ufa, você escapou! :D ****\n")
        i += 1

        if i == 5:
            print("\n******** Parabéns, você ganhou! ********")
            exit()
    else:
        tiro = input("\nTentar a sorte? S/N\nR: ")
        if tiro.lower() not in 'sim':
            print("\nVolte quando tiver mais coragem!")
            sys.exit()
        else:
            print("\n**** Boom! Você morreu! :C ****\n")
            jogar_de_novo()

def jogar_de_novo():
    resp = input("Deseja jogar novamente? S/N\nR: ")
    while True:
        if resp.lower() in 'sim':
            roleta_russa()
        else:
            sys.exit()

print("\n******** ROLETA RUSSA ********")
x = input("\nVocê é corajoso o suficiente para jogar? S/N\nR: ")
if x.lower() not in 'sim':
    print("\nVolte quando tiver mais coragem!")
    sys.exit()

roleta_russa()

if __name__ == '__main__':
    main()