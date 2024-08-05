#game.py in dice_folder

"""
Title: Game Engine for FArkel
Author: Marco
Date: March 12th 2024
"""

from player import Player

class Game:

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()


    def setup(self):
        """
        When data within the constructors needs modification before the game starts
        :return:
        """
        print("Welcome to Farkel")

    def run(self):
        """
        The majority of the game will happen
        :return:
        """
        while self.player1.getScore() < 10000 and self.player2.getScore() < 10000:
            # --- PLAYER 1 TURN --- #
            print("player 1 Turn")
            while self.player1.getCanRoll():
                self.player1.rollDice()
                self.player1.holdDie()
            new_points = int(input("Points: "))
            self.player1.addToScore(new_points)
            print(f"Player 1's Score: {self.player1.getScore()}.")
            self.player2.can_roll = True
            # --- PLAYER 2 TURN --- #
            print("player 2 Turn")
            while self.player2.getCanRoll():
                self.player2.rollDice()
                self.player2.holdDie()
            new_points = int(input("Points: "))
            self.player2.addToScore(new_points)
            print(f"Player 2's Score: {self.player2.getScore()}.")
            self.player1.can_roll = True
        if self.player2.getScore() > self.player2.getScore():
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")

if __name__ == "__main__":
    GAME = Game()
    GAME.setup()
    GAME.run()