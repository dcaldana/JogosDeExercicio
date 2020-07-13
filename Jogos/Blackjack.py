# Valor das cartas:
#
# A = 1 ou 11 pontos
# J, Q e K = 10 pontos
# Demais cartas = seu próprio valor. Ex: 7 = 7 pontos
#
# No seu turno, cada jogador tem várias opções sempre e quando não tenha “blackjack”:
#
# 1. Pedir carta.
# O dealer distribui uma carta mais ao jogador. Se as cartas somarem mais de 21 pontos,
# automaticamente perde e passa a vez.
#
# 2. Parar.
# O jogador fica com as cartas que tiver e passa a vez ao seguinte jogador.
#
# Outras opções:
#
# 3. Desistir.
# O jogador pode desistir antes de realizar qualquer outra ação. Recupera a metade do que apostou.
#
# 4. Dobrar.
# Um jogador pode dobrar a aposta se tiver 9, 10 ou 11 pontos. Se dobrar, o dealer distribuirá uma carta
# a mais ao jogador e terminará o turno.
#
# 5. Dividir.
# Quando as 2 primeiras cartas tiverem o mesmo valor, poderão ser divididas em 2 jogadas independentes e
# cada uma com a sua própria aposta.
# Se um par de As for dividido, somente é distribuída uma carta a cada jogada e o turno se acaba.
# Não se pode ter “blackjack” depois de dividir.
# Nesta modalidade, somente é possível dividir uma única vez.
#
# 6. Seguro.
# Quando a carta virada para cima do dealer for um ás, pode-se apostar que o dealer tem blackjack.
# O jogador deve fazer uma aposta adicional com a metade do valor que havia apostado.
# Esta jogada é decidida no mesmo instante. Caso acerte, o dealer pagará esta aposta 2 a 1;
# caso contrário perde-se o seguro e a ordem normal do jogo é seguida.
#
# Quando todos os jogadores terminarem seu turno, o dealer fará sua jogada.
# Está obrigado a dar-se cartas até que a sua jogada some 17 pontos ou mais.
# Não pode dobrar, dividir, desistir e nem apostar seguro.
#
# Finalmente a aposta de cada jogador é decidida dependendo de que tenha superado ou não o dealer.
# Se houver empate, o jogador recuperará a aposta. Também considera-se empate se tanto o dealer quanto o jogador
# conseguirem blackjack.
#
# A mão ganhadora se paga 1 para 1.
# A aposta do seguro se paga 2 para 1.
# O blackjack se paga 3 para 2.
#
# Retirado de: https://www.ludijogos.com/multiplayer/blackjack/regras/

import random

NAIPES = ['♥', '♣', '♦', '♠']
POSTOS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'D', 'J', 'Q', 'K']
VALOR = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'D': 10,
'J': 10, 'Q': 10, 'K': 10}


def main():
    blackjack()

class Baralho(naipe, posto):
    def carta(self):
        naipe = random(NAIPES)
        posto = random(POSTOS)
        return naipe, posto

def blackjack():
    print("Embaralhando...")
    random.shuffle(baralho)


print("*** BLACKJACK (21) ***")
input("Pressione Enter para jogar... ")
blackjack()

if __name__ == '__main__':
    main()