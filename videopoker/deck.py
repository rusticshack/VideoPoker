import random

from videopoker.card import Card
from videopoker.hand import Hand


class Deck:
    def __init__(self):
        self.cards = []
        self.index = 0
        for rank in range(2, 15):
            for suit in range(0, 4):
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        self.index = 0
        random.shuffle(self.cards)

    def deal_hand(self, cards=[]):
        while len(cards) < 5:
            cards.append(self.deal())
        return Hand(cards)

    def deal(self):
        dealt = self.cards[self.index]
        self.index += 1
        return dealt