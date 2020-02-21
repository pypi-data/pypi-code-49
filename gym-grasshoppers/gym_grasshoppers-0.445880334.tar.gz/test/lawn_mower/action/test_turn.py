from unittest import TestCase

from gym_grashoppers.lawn_mower.action.turn import Turn
from gym_grashoppers.lawn_mower.lawn_mower import LawnMower


class TestTurn(TestCase):
    def setUp(self) -> None:
        self._LawnMower = LawnMower(0., 0., 0., 0., 0., False)

    def test_execute(self):
        Turn(self._LawnMower, 90.).execute()
        self.assertEqual(self._LawnMower.angle, 90.)
