from gym_grasshoppers.exception.invalid_action_exception import InvalidActionException
from gym_grasshoppers.lawn_mower.action.action import Action
from gym_grasshoppers.lawn_mower.lawn_mower import LawnMower


class Turn(Action):
    """This class is part of the Command Pattern for lawn mower actions and represents the action Turn."""

    def __init__(self, lawn_mower: LawnMower, new_angle: float) -> None:
        super().__init__(lawn_mower)

        self._new_angle = new_angle
        if self._new_angle is None:
            raise InvalidActionException('The new angle of the lawn mower is missing!')
        elif not isinstance(self._new_angle, float):
            raise InvalidActionException('The new angle of the lawn mower is not a float!')
        elif self._new_angle < -180:
            raise InvalidActionException('The new angle of the lawn mower must be higher than -180°!')
        elif self._new_angle > 180:
            raise InvalidActionException('The new angle of the lawn mower must be lower than 180°!')

    def execute(self) -> None:
        """This method is used to change the angle of the lawn mower."""
        self._lawn_mower.angle = self._new_angle
