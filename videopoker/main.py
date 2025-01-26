from videopoker.card import Card, SPADE, HEART, DIAMOND, CLUB
from videopoker.hand import Hand

import random


def main():
    cards = []
    for rank in range(2, 15):
        for suit in range(0, 4):
            cards.append(Card(rank, suit))

    random.shuffle(cards)

    hand = [Card(10, SPADE),
            Card(10, SPADE),
            Card(11, SPADE),
            Card(11, SPADE),
            Card(11, SPADE)]

    scorer = Hand(hand)
    print(scorer.is_flush())
    print(scorer.is_straight())
    print(scorer.is_straight_flush())
    print(scorer.is_royal_flush())
    print(scorer.is_full_house())


if __name__=="__main__":
    main()