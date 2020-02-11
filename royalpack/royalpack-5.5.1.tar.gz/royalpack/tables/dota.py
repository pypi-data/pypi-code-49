from typing import *
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr
from ..utils.dotamedal import DotaMedal
from ..utils.dotastars import DotaStars
from ..utils.dotarank import DotaRank
import steam


class Dota:
    __tablename__ = "dota"

    @declared_attr
    def _steamid(self):
        return Column(BigInteger, ForeignKey("steam._steamid"), primary_key=True)

    @declared_attr
    def steam(self):
        return relationship("Steam", backref=backref("dota", uselist=False))

    @property
    def steamid(self):
        return steam.SteamID(self._steamid)

    @declared_attr
    def _rank_tier(self):
        return Column(Integer)

    @property
    def medal(self) -> Optional[DotaMedal]:
        if self._rank_tier is None:
            return None
        return DotaMedal(self._rank_tier // 10)

    @medal.setter
    def medal(self, value: DotaMedal):
        if not isinstance(value, DotaMedal):
            raise AttributeError("medal can only be set to DotaMedal objects.")
        self._rank_tier = value.value * 10 + self.stars.value

    @property
    def stars(self) -> Optional[DotaStars]:
        if self._rank_tier is None:
            return None
        return DotaStars(self._rank_tier % 10)

    @stars.setter
    def stars(self, value: DotaStars):
        if not isinstance(value, DotaStars):
            raise AttributeError("stars can only be set to DotaStars objects.")
        self._rank_tier = self.medal.value * 10 + value.value

    @property
    def rank(self) -> Optional[DotaRank]:
        if self._rank_tier is None:
            return None
        return DotaRank(self.medal, self.stars)

    @rank.setter
    def rank(self, value: Optional[DotaRank]):
        if value is None:
            self._rank_tier = None
            return
        if not isinstance(value, DotaRank):
            raise AttributeError("rank can only be set to DotaRank objects (or None).")
        self._rank_tier = value.rank_tier

    @declared_attr
    def wins(self):
        return Column(Integer)

    @declared_attr
    def losses(self):
        return Column(Integer)

    def __repr__(self):
        return f"<Dota account {self._steamid}>"

    def __str__(self):
        return f"[c]dota:{self._steamid}[/c]"
