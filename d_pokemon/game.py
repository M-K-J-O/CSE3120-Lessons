# game.py in folder d_pokemon folder

"""
title: pokemon battle game engine
author: marco ou
date: march 21st 2024
"""
from pokemon import *
from trainer import *

class Game:

    def __init__(self):
        self.__attacking_trainer = Trainer("Ash")
        self.__defending_trainer = Trainer("Gary")
        self.__arena = [] # attacking and defending pokemon when the battle starts


    def setup(self):
        self.__attacking_trainer.addPokemon(BULBASAUR)
        self.__defending_trainer.addPokemon(CHARMANDER)


    def run(self):
        if self.__attacking_trainer.canBattle():
            self.__arena.append(self.__attacking_trainer.selectPokemon())
        if self.__defending_trainer.canBattle():
            self.__arena.append(self.__defending_trainer.selectPokemon())
        self.pokemonFight()

        while True:
            self.pokemonFight()

    def pokemonFight(self):
        # Attacking Pokemon
        self.pokemonDamageCalculation(0, 1)
        print(f"{self.__arena[0]} attacks! {self.__arena[1]} has {self.__arena[1].getHP()} remaining")
        if self.__arena[1].isFainted():
            print(f"{self.__arena[1]} Fainted!")
        else:
            # Defending Pokemon
            self.pokemonDamageCalculation(1, 0)
            print(f"{self.__arena[1]} attacks! {self.__arena[0]} has {self.__arena[0].getHP()} remaining")
            if self.__arena[0].isFainted():
                print(f"{self.__arena[0]} Fainted!")



    def pokemonDamageCalculation(self, attacking, defending):
        # Attacking Pokemon
        move_damage = self.__arena[attacking].useMove()
        if self.__arena[attacking].isSuperEffective(self.__arena[defending].getType()):
            move_damage *= 2
        if self.__arena[attacking].isNotVeryEffective(self.__arena[defending].getType()):
            move_damage //= 2
        self.__arena[defending].takeDamage(move_damage)



if __name__ == "__main__":
    GAME = Game()
    GAME.setup()
    GAME.run()