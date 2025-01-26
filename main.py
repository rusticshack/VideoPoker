import time

from videopoker.deck import Deck
from videopoker.hand import Hand


def main():
    coins = 100
    deck = Deck()

    while True:
        print("Total Coins: {}   Cost to Play: 1".format(coins))
        input("Ready?")
        coins -= 1
        deck.shuffle()

        hand = deck.deal_hand()
        print(hand)

        hand = select_holds(deck, hand)
        print(hand)

        score = score_hand(hand)
        print("Hand Scores: {}".format(score))
        print()

        coins += score
        time.sleep(1)


def select_holds(deck, hand):
    val = input("Select Cards to Hold: ")
    hold_cards = [hand.cards[int(hold) - 1] for hold in list(val)]
    return deck.deal_hand(hold_cards)


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

if __name__=="__main__":
    main()