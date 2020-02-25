from quicktions import Fraction
from unittest import TestCase

from musurgia.basic_functions import xToD, dToX
from musurgia.quantize import get_quantized_values


class Test(TestCase):

    def test_1(self):
        input = [0.2, 0.333, 0.6, 0.99, 0.1, 0.5]
        example = get_quantized_values(input, 0.6)
        result = [Fraction(0, 1), Fraction(3, 5), Fraction(3, 5), Fraction(6, 5), Fraction(0, 1), Fraction(0, 1)]
        self.assertEqual(result, example)

    def test_2(self):
        midis = [60, 61.5, 58.5, 56.5, 63]
        intervals = xToD(midis)
        quantized_intervals = get_quantized_values(intervals, 1)
        quantized_midis = [int(x) for x in dToX(quantized_intervals, first_element=midis[0])]
        result = [60, 61, 58, 57, 63]
        self.assertEqual(result, quantized_midis)
