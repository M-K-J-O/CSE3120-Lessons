"""
title: Trainer Class
author: marco ou
date: march 20th 2024
"""

from pokemon import *

class Trainer:
    """
    This class will hold the available pokemon for the battle
    """


    def __init__(self, name: str):
        self.__name = name
        self.__pokemon = []
        self.__battle_ready = False

    def __str__(self):
        return self.__name

    def addPokemon(self, pokemon:Pokemon):
        self.__pokemon.append(pokemon)
        if self.__battle_ready == False and self.__pokemon[-1].getHP() > 0:
            self.__battle_ready = True

    def selectPokemon(self) -> Pokemon:
        """

        :return:
        """
        print("Select a Pokemon to enter battle")
        for i in range(len(self.__pokemon)):
            print(f"{i+1}. {self.__pokemon[i]}")
        selection = int(input("> ")) - 1
        return self.__pokemon.pop(selection)

    def canBattle(self):
        return self.__battle_ready

if __name__ == "__main__":
    from pokemon import BULBASAUR

    ASH  = Trainer("Ash")
    ASH.addPokemon(BULBASAUR)
    ASH.addPokemon(CHARMANDER)
    print(ASH.selectPokemon())