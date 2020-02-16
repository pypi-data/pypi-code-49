from numpy.random import randint
import numpy


class Dice:
    def __init__(self, sides: str, rolls: int) -> None:
        dice_bag = {
            "d4": 4,
            "d6": 6,
            "d8": 8,
            "d10": 10,
            "d12": 12,
            "d20": 20,
            "d100": 100,
        }
        try:
            self.sides = dice_bag[sides]
        except KeyError:
            self.sides = dice_bag["d4"]
        self.sides += 1
        self.rolls = rolls >= 1 and rolls or 1

    def roll(self) -> numpy.ndarray:
        """Returns random array purged_values between low and high at size."""
        return randint(low=1, high=self.sides, size=self.rolls)
