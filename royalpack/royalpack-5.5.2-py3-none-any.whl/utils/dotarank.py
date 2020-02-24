from .dotamedal import DotaMedal
from .dotastars import DotaStars


class DotaRank:
    __slots__ = "medal", "stars"

    def __init__(self, medal: DotaMedal = None, stars: DotaStars = None, *, rank_tier: int = None):
        if rank_tier is not None:
            self.medal: DotaMedal = DotaMedal(rank_tier // 10)
            self.stars: DotaStars = DotaStars(rank_tier % 10)
        else:
            if medal is None or stars is None:
                raise AttributeError("Missing medal, stars or rank_tier.")
            self.medal = medal
            self.stars = stars

    def __gt__(self, other):
        if other is None:
            return True
        if not isinstance(other, DotaRank):
            raise TypeError(f"Can't compare {self.__class__.__qualname__} with {other.__class__.__qualname__}")
        if self.medal > other.medal:
            return True
        elif self.medal < other.medal:
            return False
        elif self.stars > other.stars:
            return True
        return False

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, DotaRank):
            raise TypeError(f"Can't compare {self.__class__.__qualname__} with {other.__class__.__qualname__}")
        return self.medal == other.medal and self.stars == other.stars

    def __repr__(self):
        return f"<{self.__class__.__qualname__}: {self.medal.name} {self.stars.name}>"

    def __str__(self):
        return f"{self.medal} {self.stars}"

    @property
    def rank_tier(self) -> int:
        return (self.medal.value * 10 + self.stars.value)