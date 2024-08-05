"""
title: pokemon type class
author: marco Ou
date: march 20th 2024
"""

class Type:
    """
    This will organize while types are super effective or not very effective
    """

    def __init__(self, name: str, strong: list[str], resist: list[str]):
        """
        The perspective of the attacking pokemon and the defending pokemon type
        pokemon move is super effective towards "water"
        pokemon move is not very effective towards "fire"
        :param name: str, grass
        :param weak: list(str), ["water", "ground", "rock"]
        :param resist: list(str). ["fire", "grass", "poison", "flying", "bug", "dragon", "steel"]
        """

        self.__name = name
        self.__strong = strong
        self.__resist = resist

    def __str__(self):
        return self.__name

    def getSuperEffective(self, pokemon_type):
        if pokemon_type in self.__strong:
            return True
        else:
            return False

    def getNotVeryEffective(self, pokemon_type):
        if pokemon_type in self.__resist:
            return True
        else:
            return False


# --- TYPES --- #
GRASS = Type("Grass", ["Water", "Ground", "Rock"], ["Fire", "Poison", "Flying", "Bug", "Ice"])
FIRE = Type("Fire", ["Bug", "Steel", "Ice", "Grass"], ["Ground", "Rock", "Water", "Fire"])

if __name__ == "__main__":
    print(GRASS)
    print(GRASS.getSuperEffective("Ground"))
    print(GRASS.getSuperEffective("Fairy"))
    print(GRASS.getNotVeryEffective("Fire"))