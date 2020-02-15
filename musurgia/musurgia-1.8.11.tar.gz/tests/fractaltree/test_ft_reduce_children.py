import os
from unittest import TestCase
from quicktions import Fraction

from musurgia.fractaltree.fractaltree import FractalTree

path = os.path.abspath(__file__).split('.')[0]


class Test(TestCase):

    def test_1(self):
        ft = FractalTree(proportions=(1, 2, 3), tree_permutation_order=(3, 1, 2), value=10)
        ft.add_layer()
        ft.add_layer()
        for node in ft.get_layer(1):
            node.reduce_children(condition=lambda node: node.fractal_order == 1)
        self.assertEqual([node.fractal_order for node in ft.traverse_leaves()], [2, 3, 3, 2, 2, 3])

    def test_2(self):
        ft = FractalTree(proportions=(1, 2, 3), tree_permutation_order=(3, 1, 2), value=10)
        ft.add_layer()
        ft.add_layer()
        for node in ft.get_layer(1):
            node.reduce_children(condition=lambda node: node.fractal_order == 1)
        self.assertEqual([node.value for node in ft.traverse_leaves()],
                         [Fraction(25, 12), Fraction(35, 12), Fraction(35, 36), Fraction(25, 36), Fraction(25, 18),
                          Fraction(35, 18)])
