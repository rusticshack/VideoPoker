SPADE = 0
HEART = 1
DIAMOND = 2
CLUB = 3

class Card:
    suits = ["\u2660", "\u2661", "\u2662", "\u2663"]
    ranks = {1: "A", 11: "J", 12: "Q", 13: "K"}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        suit = self.suits[self.suit]
        rank = self.ranks.get(self.rank, self.rank)
        return "{} {}".format(rank, suit)
