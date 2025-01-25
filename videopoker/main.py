from videopoker.card import Card, SPADE, HEART, DIAMOND, CLUB
import random


def main():
    cards = []
    for rank in range(1, 14):
        for suit in range(0, 4):
            cards.append(Card(rank, suit))

    random.shuffle(cards)

    hand = cards[:5]
    print(hand)


if __name__=="__main__":
    main()