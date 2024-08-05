"""
title: Pokemon class
author marco ou
date: march 20th 2024
"""

from type import *
from move import *
class Pokemon:
    """
    This class will consolidate all information needed to create a pokemon that can battle another pokemon
    :param: name str
    :param: type object
    :param: max_health int
    :param: current_health int
    :param: known_moves: list[Move()]
    """

    def __init__(self, name, element_type, max_health,ID=None):
        self.__name = name
        self.__id = ID
        self.__type = element_type
        self.__max_health = max_health
        self.__current_health = max_health
        self.__known_moves = []

    def __str__(self):
        return self.__name


    # methods
    def learnMove(self, new_move: object):
        self.__known_moves.append(new_move)



    def useMove(self) -> int:
        """
        select a move and return a damage value
        :return: int
        """
        print(f"Select a move for {self.__name}")
        for i in range(len(self.__known_moves)):
            print(f"{i+1} {self.__known_moves[i]}")
        selection = int(input("> ")) - 1
        return self.__known_moves[selection].getDamage()



    def takeDamage(self, damage: int) -> None:
        """
        :param damage: int
        :return: None
        """
        self.__current_health -= damage
        if self.__current_health < 0:
            self.__current_health = 0


    def getHP(self):
        return self.__current_health

    def isSuperEffective(self, incoming_type):
        """
        :param incoming_type: str
        :return: bool
        """
        return self.__type.getSuperEffective(incoming_type)

    def isNotVeryEffective(self, incoming_type):
        """
        :param incoming_type: str
        :return: bool
        """
        return self.__type.getNotVeryEffective(incoming_type)

    def getType(self):
        return str(self.__type)

    def isFainted(self):
        if self.__current_health == 0:
            return True
        else:
            return False


# --- Pokemon Objects --- #

BULBASAUR = Pokemon("Bulbasaur", GRASS, 23)
BULBASAUR.learnMove(TACKLE)
CHARMANDER = Pokemon("Charmander", FIRE, 32)
CHARMANDER.learnMove(SCRATCH)

if __name__ == "__main__":
    print(BULBASAUR.useMove())
