from abc import ABC, abstractmethod

from gym_grashoppers.lawn_mower.lawn_mower import LawnMower


class Action(ABC):
    """This class is part of the Command Pattern for lawn mower actions and represents the base class Action."""

    def __init__(self, lawn_mower: LawnMower) -> None:
        self._lawn_mower = lawn_mower

    @property
    def lawn_mower(self) -> LawnMower:
        return self._lawn_mower

    @abstractmethod
    def execute(self) -> None:
        pass
