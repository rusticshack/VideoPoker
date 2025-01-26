SPADE = 0
HEART = 1
DIAMOND = 2
CLUB = 3

class Card:
    SUITS = ["\u2660", "\u2661", "\u2662", "\u2663"] # Spade, heart, diamond, club
    RANKS = {14: "A", 11: "J", 12: "Q", 13: "K"}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        suit = self.SUITS[self.suit]
        rank = self.RANKS.get(self.rank, self.rank)
        return "{} {}".format(rank, suit)

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        return self.rank < other.rank

    def __gt__(self, other):
        if self.rank == other.rank:
            return self.suit > other.suit
        return self.rank > other.rank