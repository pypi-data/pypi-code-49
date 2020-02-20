from gym_grashoppers.lawn_mower.action.action import Action
from gym_grashoppers.lawn_mower.lawn_mower import LawnMower


class Empty(Action):
    """This class is part of the Command Pattern for lawn mower actions and represents the action Empty."""

    def __init__(self, lawn_mower: LawnMower) -> None:
        super().__init__(lawn_mower)

    # TODO
    def execute(self) -> None:
        pass
