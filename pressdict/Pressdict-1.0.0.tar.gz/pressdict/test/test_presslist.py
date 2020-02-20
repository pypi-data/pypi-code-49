import unittest

from pressdict import Presslist


class PresslistTests(unittest.TestCase):

    def test_basic_functionality(self):

        pl = Presslist()

        elem = {"key": "value", "key2": 2}

        pl.append(elem)

        self.assertTrue(elem in pl)

        self.assertEqual(pl[0], elem)

        for x in pl:
            self.assertEqual(x, elem)

        self.assertEqual(len(pl), 1)

        self.assertEqual(pl[0:1], [elem])

        pl[1:2] = [123]
        self.assertEqual(list(iter(pl)), [elem, 123])

        pl[1] = 456
        self.assertEqual(list(iter(pl)), [elem, 456])

        del pl[1]
        self.assertEqual(list(iter(pl)), [elem])

        self.assertEqual(pl.count(elem), 1)
        self.assertEqual(pl.index(elem), 0)

        self.assertEqual(pl.pop(), elem)
        self.assertEqual(len(pl), 0)

        pl.append(elem)
        self.assertTrue(elem in pl)
        pl.remove(elem)
        self.assertTrue(elem not in pl)
