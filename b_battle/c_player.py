# c_player.py in folder b_battle

"""
title: player class for b_battle
author: Marco
date: March 18th 2024
"""

class Player:
    """
    player class for the game battle
    """

    def __init__(self, NAME):
        self.__NAME = NAME
        self.__HAND = []


    # --- MODIFIER --- #

    def takeCard(self, CARD: object) -> None:
        """
        adds a card to the hand
        :param CARD: object - Card
        """
        self.__HAND.append(CARD)

    def giveCard(self) -> object:
        """
        take the top card from the hand
        :return:
        """
        if len(self.__HAND) > 0:
            return self.__HAND.pop(0)

    def showCard(self, INDEX=0):
        """
        shows card value and suit
        :return:
        """
        return self.__HAND[INDEX]


    # --- ACCESSOR --- #

    def __str__(self):
        return self.__NAME

    def isHandEmpty(self):
        if len(self.__HAND) > 0:
            return False
        else:
            return True

    def getHandLen(self):
        return len(self.__HAND)

if __name__ == "__main__":
    from b_deck import Deck

    DECK = Deck()
    DECK.shuffleDeck()

    PLAYER1 = Player("Mr. Zhang")
    PLAYER2 = Player("Mr. Patterson")

    for i in range(26):
        PLAYER1.takeCard(DECK.drawCard())
        PLAYER2.takeCard((DECK.drawCard()))

    print(PLAYER1.isHandEmpty())

    TABLE = []
    TABLE.append(PLAYER1.giveCard())
    TABLE.append(PLAYER2.giveCard())
    print(TABLE)