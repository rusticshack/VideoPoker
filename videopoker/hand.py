from collections import Counter


class Hand:
    def __init__(self, hand):
        if len(hand) != 5:
            raise ValueError("Hand must be 5 cards, got {}".format(len(hand)))
        self.cards = sorted(hand)

    def __repr__(self):
        return self.cards.__repr__()

    def is_royal_flush(self):
        return self.cards[0].rank == 10 and self.is_straight_flush()

    def is_straight_flush(self):
        return self.is_straight() and self.is_flush()

    def is_flush(self):
        suits = [card.suit for card in self.cards]
        return len(set(suits)) == 1

    def is_straight(self):
        cur_rank = self.cards[0].rank
        for card in self.cards[1:]:
            if card.rank != cur_rank + 1:
                return False
            cur_rank = card.rank
        return True

    def is_four_of_a_kind(self):
        return 4 in self.count_ranks().values()

    def is_three_of_a_kind(self):
        return 3 in self.count_ranks().values()

    def is_pair(self):
        return 2 in self.count_ranks().values()

    def is_two_pair(self):
        ranks = self.count_ranks()
        pairs = 0
        for rank in ranks.keys():
            if ranks[rank] == 2:
                pairs += 1
        return pairs == 2

    def is_full_house(self):
        return self.is_three_of_a_kind() and self.is_pair()

    def is_jacks_or_better(self):
        ranks = self.count_ranks()
        for rank in ranks.keys():
            if rank >= 11 and ranks[rank] == 2:
                return True
        return False

    def is_set(self, x, min_rank=None):
        ranks = self.count_ranks()
        for rank in ranks.keys():
            if min_rank is not None and rank < min_rank:
                continue
            if ranks[rank] >= x:
                return True
        return False

    def count_ranks(self):
        return Counter([card.rank for card in self.cards])
