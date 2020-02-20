import unittest
from acronyms.index import Index
from acronyms.acronym import Acronym


class TestIndex(unittest.TestCase):
    def test_register(self):
        index = Index()
        a = Acronym('aba', 'ABA', 'A better acronym')
        count = index.register(a)
        self.assertEqual(count, 1)
        count = index.register(a)
        self.assertEqual(count, 2)
        self.assertEqual(index.occurences(a.key), 2)
        self.assertEqual(index.occurences('bba'), 0)


if __name__ == '__main__':
    unittest.main()
