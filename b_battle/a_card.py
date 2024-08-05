#a_card.py in b_battle (folder)

"""
title: card class
author: Marco Ou
date: March 15th 2024
"""

class Card:
    """
    Single playing card
    """
    SUITS = {
        1: "Diamonds",
        2: "Clubs",
        3: "Hearts",
        4: "Spades"
    }

    FACES = {
        1: "Ace",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Jack",
        12: "Queen",
        13: "King"
    }

    def __init__(self, SUIT, VALUE):
        """
        constructs a Card
        """
        self.__SUIT = SUIT
        self.__VALUE = VALUE

    # --- MODIFIER --- #


    # --- ACCESSOR --- #

    def getCardValue(self):
        return self.__VALUE

    def getCardSuit(self):
        return self.__SUIT

    def __str__(self):
        if 1 < self.__VALUE < 11:
            return f"{self.__VALUE} of {Card.SUITS[self.__SUIT]}"
        else:
            return f"{Card.FACES[self.__VALUE]} of {Card.SUITS[self.__SUIT]}"

    def __repr__(self):
        return f"<-- {self.__str__()} -->"

if __name__ == "__main__":
    CARD = Card(1, 12)
    print(CARD.getCardValue(), CARD.getCardSuit())

    DECK = []
    for i in range(1, 5):
        for j in range(1, 14):
            DECK.append(Card(i, j))
    print(DECK[0].getCardValue())
    print(DECK)