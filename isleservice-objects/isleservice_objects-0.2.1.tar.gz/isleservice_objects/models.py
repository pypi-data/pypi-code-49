# Custom Models gd here.

from dataclasses import dataclass


@dataclass
class Name:
    """Name Info"""

    first: str
    """Cannot contain spaces"""

    last: str
    """Cannot Contain spaces"""

    @property
    def full_name(self) -> str:
        """First and last name"""
        return f"{self.first} {self.last}"


@dataclass
class Enemy:
    """Information about an adversary"""

    rank: str
    """Military Rank"""

    name: Name
    """The Enemy's name"""

    @property
    def addressable(self) -> str:
        """Title and last name."""
        return f"{self.rank} {self.name.last}"
