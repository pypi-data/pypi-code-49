import enum


class DotaStars(enum.Enum):
    I = 1
    II = 2
    III = 3
    IV = 4
    V = 5
    VI = 6
    VII = 7

    def __str__(self):
        return self.name.upper()

    def __repr__(self):
        return f"{self.__class__.__qualname__}.{self.name}"

    def __gt__(self, other):
        return self.value > other.value
