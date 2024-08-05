#player.py in a_dice folder

"""
Title: Player Program
Author: Marco Ou
Date: March 12th 2024
"""
from a_dice import Die

class Player:
    """
    The player for the game Farkle
    """

    def __init__(self):
        """
        Attributes for the player
        :return:
        """
        self.score = 0
        self.dice = []
        for i in range(5):
            self.dice.append(Die())
        self.dice_held = []
        self.can_roll = True


    # Methods --> Behaviours

    def holdDie(self):
        """
        select a die and hold onto it.
        :return:
        """
        # --- Creates the list of Dice values for the user to select a dice to store
        for i in range(len(self.dice)):
            print(f"{i+1}. Dice Value: {self.dice[i].getDieValue()}")
        print(f"{len(self.dice) + 1}. No selection")
        print(f"{len(self.dice)+2}. End Turn and add Points")
        print("Please select the list number not the dice value")
        self.displayHeldDice()
        dice_num = int(input("> ")) - 1
        # --- This section determines the action after the user selects and item from the menu
        if dice_num < len(self.dice):
            self.dice_held.append(self.dice.pop(dice_num))
            # --- if all dice are selected move dice back into self.dice and re-roll
            if len(self.dice) == 0:
                for i in range(len(self.dice_held)):
                    self.dice.append(self.dice_held.pop())
                for dice in self.dice:
                    dice.rollDie()
            self.can_roll = True
            self.holdDie()
        elif dice_num == len(self.dice):
            self.can_roll = True
            # --- If not storing a dice and re-rolling
        else:
            # --- If not storing a dice and ending the turn
            self.can_roll = False

    def rollDice(self):
        """
        roll all available dice
        :return:
        """
        for i in range(len(self.dice)):
            self.dice[i].rollDie()

    def addToScore(self, NEW_POINTS):
        self.score += NEW_POINTS

    def displayRolledDie(self):
        """
        :return:
        """
        for cube in self.dice:
            cube.displayDie()

    def displayScore(self):
        print(self.score)

    def displayHeldDice(self):
        dice_in_held = ""
        for cube in self.dice_held:
            dice_in_held += str(cube.getDieValue())
            dice_in_held += ", "
            print(f"Held Dice: {dice_in_held}")
        if len(self.dice_held) > 0:
           pass

    def getScore(self):
        return self.score

    def getCanRoll(self):
        return self.can_roll

if __name__ == "__main__":
    MARCO = Player()
    MARCO.rollDice()
    MARCO.holdDie()
    MARCO.displayRolledDie()
    MARCO.addToScore(100)
    MARCO.displayScore()
