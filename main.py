import time

from videopoker.card import Card, SPADE, HEART, DIAMOND, CLUB
from videopoker.hand import Hand

import random


def main():
    cards = generate_deck()
    coins = 100

    while True:
        print("Total Coins: {}   Cost to Play: 1".format(coins))
        input("Ready?")
        coins -= 1
        random.shuffle(cards)

        deal_five = sorted(cards[:5])
        print(deal_five)
        val = input("Select Cards to Hold: ")
        holds = list(val)
        hold_cards = []
        for h in holds:
            hold_cards.append(deal_five[int(h)-1])

        to_draw = 5 - len(hold_cards)
        new_five = sorted(hold_cards + cards[5:5+to_draw])
        print(new_five)

        hand = Hand(new_five)
        score = score_hand(hand)
        print("Hand Scores: {}".format(score))
        print()
        coins += score
        time.sleep(1)

def score_hand(hand):
    if hand.is_royal_flush():
        return 250
    elif hand.is_straight_flush():
        return 50
    elif hand.is_four_of_a_kind():
        return 25
    elif hand.is_full_house():
        return 9
    elif hand.is_flush():
        return 6
    elif hand.is_straight():
        return 4
    elif hand.is_three_of_a_kind():
        return 3
    elif hand.is_two_pair():
        return 2
    elif hand.is_jacks_or_better():
        return 1
    else:
        return 0

def generate_deck():
    cards = []
    for rank in range(2, 15):
        for suit in range(0, 4):
            cards.append(Card(rank, suit))
    return cards

if __name__=="__main__":
    main()