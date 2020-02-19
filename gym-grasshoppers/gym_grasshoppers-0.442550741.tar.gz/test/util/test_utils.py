from unittest import TestCase
from gym_grashoppers.util.utils import Utils


class TestUtils(TestCase):
    def test_get_scaled_radius(self):
        """Test that the radius of the lawn mower is scaled correctly to the scale of the garden."""
        latitude = 4.069490432739258
        radius = 0.5
        result = Utils.calculate_scaled_radius(latitude, radius)
        self.assertEqual(result, 4.49533796054169e-06)
