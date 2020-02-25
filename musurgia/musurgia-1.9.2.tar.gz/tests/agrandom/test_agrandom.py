from unittest import TestCase

from musurgia.agrandom import AGRandom


class Test(TestCase):
    def test_1(self):
        pool = [1, 3, 2, 4, 5, 1, 1]
        r = AGRandom(pool=pool, periodicity=2, seed=20)
        output = [r.__next__() for i in range(20)]
        expected = [3, 2, 1, 5, 3, 1, 4, 3, 2, 4, 5, 3, 2, 4, 1, 5, 4, 1, 3, 5]
        self.assertEqual(expected, output)

    def test_2(self):
        pool = [1, 3, 2, 4, 5, 1, 1, 1, 1, 1, 1]
        r = AGRandom(pool=pool, periodicity=0, seed=20)
        expected = [1, 3, 2, 4, 5]
        self.assertEqual(expected, r.pool)

    def test_3(self):
        pool = [1, 3, 2, 4, 5, 6]
        r = AGRandom(pool=pool, periodicity=0, seed=20)
        output = [r.__next__() for i in range(20)]
        expected = [6, 6, 3, 2, 6, 6, 1, 2, 5, 3, 1, 4, 4, 1, 1, 3, 2, 4, 5, 4]
        self.assertEqual(expected, output)
