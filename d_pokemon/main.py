"""
Title: Pokemon Battle game
Author: Marco Ou
Date: April 2nd 2024
"""

from game import Game

class Main:

    def __init__(self):
        self.__game = Game()
        self.__game.setup()
        self.__game.run()

if __name__ == "__main__":
    Main()
