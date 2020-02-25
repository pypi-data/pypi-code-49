from gym_grasshoppers.lawn_mower.action.action import Action
from gym_grasshoppers.lawn_mower.lawn_mower import LawnMower


class Empty(Action):
    """This class is part of the Command Pattern for lawn mower actions and represents the action Empty."""

    def __init__(self, lawn_mower: LawnMower) -> None:
        super().__init__(lawn_mower)

    def execute(self) -> None:
        self._lawn_mower.current_volume = self._lawn_mower.INITIAL_VOLUME
