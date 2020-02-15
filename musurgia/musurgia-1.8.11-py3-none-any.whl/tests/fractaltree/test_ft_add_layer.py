import os
from unittest import TestCase
from quicktions import Fraction

from musurgia.fractaltree.fractaltree import FractalTree

path = os.path.abspath(__file__).split('.')[0]


class Test(TestCase):
    def test_1(self):
        ft = FractalTree(proportions=(1, 2, 3), tree_permutation_order=(3, 1, 2))
        ft.tempo = 60
        ft.value = 10
        ft.add_layer()
        ft.add_layer()
        self.assertEqual([node.fractal_order for node in ft.traverse_leaves()], [1, 2, 3, 3, 1, 2, 2, 3, 1])

    def test_2(self):
        ft = FractalTree(proportions=(1, 2, 3), tree_permutation_order=(3, 1, 2))
        ft.tempo = 60
        ft.value = 10
        ft.add_layer()
        ft.add_layer()
        self.assertEqual([node.value for node in ft.traverse_leaves()],
                         [Fraction(5, 6), Fraction(5, 3), Fraction(5, 2), Fraction(5, 6), Fraction(5, 18),
                          Fraction(5, 9),
                          Fraction(10, 9), Fraction(5, 3), Fraction(5, 9)])
