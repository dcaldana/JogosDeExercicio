# 6.11. Jogo de Forca.
#
# Desenvolva um jogo da forca. O programa terá uma lista de palavras
# lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador poderá errar 6 vezes antes de ser enforcado.
#
# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!
#
# Digite uma letra: O
# A palavra é: _ _ _ _ O
#
# Digite uma letra: E
# A palavra é: _ E _ _ O
#
# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!
#
# Retirado de: https://wiki.python.org.br/ExerciciosComStrings

import random

def main():
    jogo_forca()

def jogo_forca():
    contador = 0
    misterio = []
    novam = ""
    letraserradas = []
    palavraserradas = []

    print("\n********BEM-VINDO AO JOGO DA FORCA********")
    print("\nREGRAS:\nSerá sorteada uma palavra aleatória. \nVocê tem 6 vidas para tentar acertar uma das letra que essa palavra possui (uma letra por tentativa).\nCaso erre 6 vezes, você perde o jogo!")
    print("\nOBSERVAÇÃO: O jogo não funciona com caracteres especiais. Utilize os equivalentes.\nEx: 'Ç' = 'C', 'Á' = 'A'")
    continuar = input("\nVamos lá (S/N)? ")
    if continuar in 'Nn':
        exit()
    else:
        pass

    palavras = ['ABOBORA','TALCO','NITEROI','ILHA','VENTILADOR']
    dicas1 = ['Pode ser tanto um legume, quanto uma cor...', 'Utilizado para remover mau-cheiros...', 'Cidade do Estado do Rio de Janeiro...', 'O que Japão, Fernando de Noronha e Haiti têm em comum?',  'Útil em dias muito quentes...']
    dicas2 = ['Usada no Halloween...', 'Geralmente, se passa no bebê...', 'O Museu de Arte Contemporânea (MAC) fica aqui...', 'Ao redor só existe água...', 'Às vezes seria melhor ter um ar-condicionado a ter isso...']

    palavra = str(random.choice(palavras))

    n = palavras.index(palavra)
    dica = dicas1[n]
    dica2 = dicas2[n]

    for i in palavra:
        misterio += "_"

    print("\nPalavra escolhida: {}".format(" ".join(misterio)))

    while contador < 6:
        letra = str(input("\nDigite uma letra ou arrisque a palavra{}: ".format(novam))).upper()  # Pede uma letra
        novam = " novamente"
        if len(letra) > 1:
            if letra == palavra:
                print("\nA palavra é: {}".format(" ".join(misterio)))
                print("\n********Parabéns, você acertou!********")
                exit()
            else:
                contador += 1
                palavraserradas.append(letra)
                print("\n\nA palavra não é '{}'... Você errou pela {}ª vez! Você possui {} tentativas restantes...".format(letra, contador, 6-contador))
                print("Letras erradas: {}\nPalavras erradas: {}".format(" ".join(letraserradas),
                                                                          ", ".join(palavraserradas)))
                print("\nA palavra é: {}".format(" ".join(misterio)))
                if contador == 4:
                    print("\n(Dica 1: {})".format(dica))
                elif contador == 5:
                    print("\n(Dica 2: {})".format(dica2))
        else:
            if letra in palavra:
                for i in range(len(palavra)):
                    if letra == palavra[i]:
                        misterio[i] = letra
                if palavra == "".join(misterio):
                    print("\nA palavra é: {}".format(" ".join(misterio)))
                    print("\n********Parabéns, você acertou!********")
                    break
                else:
                    print("\nA palavra é: {}".format(" ".join(misterio)))
            else:
                contador += 1
                print("\n\nLetra errada... Você errou pela {}ª vez! Você possui {} tentativas restantes...".format(contador, 6-contador))
                letraserradas += letra
                print("Letras erradas: {}\nPalavras erradas: {}".format(" ".join(letraserradas),", ".join(palavraserradas)))
                print("\nA palavra é: {}".format(" ".join(misterio)))
                if contador == 4:
                    print("\n(Dica 1: {})".format(dica))
                elif contador == 5:
                    print("\n(Dica 2: {})".format(dica2))

    else:
        print("\nA palavra era: '{}'".format(palavra))
        print("\n********Você perdeu!********")

if __name__ == '__main__':
    main()