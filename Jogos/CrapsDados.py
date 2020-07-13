# 5.10. Jogo de Craps.
#
# Faça um programa de implemente um jogo de Craps.
# O jogador lança um par de dados, obtendo um valor entre 2 e 12.
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
#
# Retirado de: https://wiki.python.org.br/ExerciciosFuncoes


import time
from random import randint


def main():
    dado_maluco()

print("\n*** APOSTA DE DADOS ***\n")
input("Pressione Enter para jogar... ")


def dado_maluco():

    n = input("\nQuantas vezes deseja lançar o dado?\nR: ")
    while True:
        try:
            int(n)
            break
        except ValueError:
            n = input("\nOps! Quantas vezes deseja lançar o dado?\nR: ")
    print("\nSorteando",n,"dados aleatoriamente... ")
    time.sleep(1)
    resultados = []
    cont = [0, 0, 0, 0, 0, 0]

    for x in range(int(n)):
        resultado = randint(1, 6)
        resultados += [resultado]
        cont[resultado - 1] += 1

    aposta = input("\nAposte qual número saiu mais vezes...\nR: ")
    print("\n")

    while aposta not in '123456':
        aposta = input("\nOps! Aposte qual número saiu mais vezes... (1 a 6)\nR: ")

    for t in range(1, 7):
        print("O número", t, "saiu", cont[t - 1], "vezes.")

    if int(aposta) == cont.index(max(cont)) + 1:
        print("\nParabéns, você ganhou!!!")
    else:
        print("\nInfelizmente você perdeu!!!")

    teste = input("\nDeseja jogar novamente? S/N\nR: ")
    while teste not in 'SsNn':
        teste = input("\nOps! Deseja jogar novamente? S/N\nR: ")
    if teste in 'Ss':
        dado_maluco()

if __name__ == '__main__':
    main()