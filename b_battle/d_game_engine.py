#d_game_engine.py in folder b_battle

"""
title: game engine of battle
author: Marco
date: March 18th 2024
"""

from b_deck import Deck
from c_player import Player
from a_card import Card

class Game:
    """
    runs the main program code
    """

    def __init__(self):
        self.__PLAYER1 = Player(input("Player 1 Name: "))
        self.__PLAYER2 = Player(input("Player 2 Name: "))
        self.__DECK = Deck()
        self.__LOOTDECK = []


    def setup(self):
        self.__DECK.shuffleDeck()
        for i in range(26):
            self.__PLAYER1.takeCard(self.__DECK.drawCard())
            self.__PLAYER2.takeCard(self.__DECK.drawCard())


    def run(self):
        while True:
            self.__PLAYER1.isHandEmpty()
            self.__PLAYER2.isHandEmpty()
            print(f" Player {self.__PLAYER1}'s Card: {self.__PLAYER1.showCard()}, Player {self.__PLAYER2}'s Card: {self.__PLAYER2.showCard()} ")
            print("Which Player has the Higher Value 1 or 2 or draw")
            WINNER = int(input("> "))
            if WINNER == 1:
                self.__PLAYER1.takeCard(self.__PLAYER2.giveCard())
                self.__PLAYER1.takeCard((self.__PLAYER1.giveCard()))
                print("Player 1 takes both cards")
            elif WINNER == 2:
                self.__PLAYER2.takeCard(self.__PLAYER1.giveCard())
                self.__PLAYER2.takeCard((self.__PLAYER2.giveCard()))
                print("Player 2 takes both cards")
            elif WINNER == 3:
                print(f"Player {self.__PLAYER1}'s Loot: ")
                TEMP = 0
                for i in range(0, self.__PLAYER1.getHandLen() - 1):
                    TEMP += 1
                    if TEMP > 10:
                        break
                    print(self.__PLAYER1.showCard(INDEX=i))
                    self.__LOOTDECK.append(self.__PLAYER1.giveCard())
                print(f"Player {self.__PLAYER2}'s Loot: ")
                TEMP = 0
                for i in range(0, self.__PLAYER1.getHandLen() - 1):
                    TEMP += 1
                    if TEMP > 10:
                        break
                    print(self.__PLAYER2.showCard(INDEX=i))
                    self.__LOOTDECK.append(self.__PLAYER2.giveCard())

                print(f" Player {self.__PLAYER1}'s Card: {self.__PLAYER1.showCard()}, Player {self.__PLAYER2}'s Card: {self.__PLAYER2.showCard()} ")
                print("Which Player has the Higher Value 1 or 2 or 3")
                WINNER = int(input("> "))

                if WINNER == 1:
                    for i in range(len(self.__LOOTDECK)):
                        self.__PLAYER1.takeCard(self.__LOOTDECK[i])
                    print("Player 1 takes all")
                if WINNER == 2:
                    for i in range(len(self.__LOOTDECK)):
                        self.__PLAYER2.takeCard(self.__LOOTDECK[i])
                    print("Player 2 takes all")
                else:
                    pass
                self.__LOOTDECK = []


            self.__PLAYER1.isHandEmpty()
            self.__PLAYER2.isHandEmpty()



if __name__ == "__main__":
    GAME = Game()
    print("")
    GAME.setup()
    print("")
    GAME.run()