import enum


class DotaMedal(enum.Enum):
    HERALD = 1
    GUARDIAN = 2
    CRUSADER = 3
    ARCHON = 4
    LEGEND = 5
    ANCIENT = 6
    DIVINE = 7
    IMMORTAL = 8

    def __str__(self):
        return self.name.capitalize()

    def __repr__(self):
        return f"{self.__class__.__qualname__}.{self.name}"

    def __gt__(self, other):
        return self.value > other.value
