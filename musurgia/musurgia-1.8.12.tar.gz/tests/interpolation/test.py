from unittest import TestCase

from musurgia.interpolation import Interpolation, InterpolationSection


class Test(TestCase):
    def setUp(self) -> None:
        self.interpolation = Interpolation()

    def test_1(self):
        # self.interpolation.add_section(InterpolationSection(0, 100, 10))
        # self.interpolation.add_section(InterpolationSection(100, 50, 20))
        # self.interpolation.add_section(InterpolationSection(50, 200, 10))
        self.interpolation.add_section(0, 100, 10)
        self.interpolation.add_section(100, 50, 20)
        self.interpolation.add_section(50, 200, 10)

        test_case = [float(self.interpolation.get_value(x)) for x in range(0, 41)]
        expected = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 97.5, 95.0, 92.5, 90.0, 87.5, 85.0,
                  82.5, 80.0, 77.5, 75.0, 72.5, 70.0, 67.5, 65.0, 62.5, 60.0, 57.5, 55.0, 52.5, 50.0, 65.0, 80.0, 95.0,
                  110.0, 125.0, 140.0, 155.0, 170.0, 185.0, 200.0]

        self.assertEqual(expected, test_case)
