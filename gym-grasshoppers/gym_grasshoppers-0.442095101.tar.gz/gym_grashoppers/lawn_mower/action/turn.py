from gym_grashoppers.lawn_mower.action.action import Action
from gym_grashoppers.lawn_mower.lawn_mower import LawnMower


class Turn(Action):
    """This class is part of the Command Pattern for lawn mower actions and represents the action Turn."""

    def __init__(self, lawn_mower: LawnMower, new_angle: float) -> None:
        super().__init__(lawn_mower)
        self._new_angle = new_angle

    def execute(self) -> None:
        """This method is used to change the angle of the lawn mower."""
        self._lawn_mower.angle = self._new_angle
