#

import random

NAIPES = ['♥', '♣', '♦', '♠']
POSTOS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'D', 'J', 'Q', 'K']
VALOR = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'D': 10,
'J': 10, 'Q': 10, 'K': 10}


def main():
    blackjack()

class baralho(naipe, posto):
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