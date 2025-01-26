import random

from videopoker.card import Card


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

    def deal(self, num):
        dealt = self.cards[self.index:self.index+num]
        self.index += num
        return dealt