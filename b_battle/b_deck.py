#b_deck.py in folder b_battle (folder)

"""
Title: Deck class
Author: Marco
Date: March 18th 2024
"""

from a_card import Card
from random import shuffle

class Deck:
    """
    Create a deck of 52 playing cards that interact with individual cards
    """


    def __init__(self):
        self.__DECK = []
        for i in range(1,5):
            for j in range(1, 14):
                self.__DECK.append(Card(i, j))

    # --- MODIFIER --- #

    def shuffleDeck(self):
        """
        shuffles the cards in the deck
        """
        shuffle(self.__DECK)

    def drawCard(self):
        """
        return the top card of the deck
        """
        if len(self.__DECK) > 0:
            return self.__DECK.pop(0)


if __name__ == "__main__":
    DECK = Deck()
    DECK.shuffleDeck()
    print(DECK)

    PLAYER_HAND = []
    for i in range(5):
        PLAYER_HAND.append(DECK.drawCard())
    print(PLAYER_HAND)

