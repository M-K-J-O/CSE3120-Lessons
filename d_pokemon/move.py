"""
title: Move class
author: marco ou
date: march 20th 2024
"""

class Move:
    """
    This class will organize the different moves a pokemon can select
    """

    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    def __str__(self):
        return self.__name

    def getDamage(self):
        return self.__damage


# --- Moves --- #

SCRATCH = Move("Scratch", 6)
TACKLE = Move("Tackle", 5)