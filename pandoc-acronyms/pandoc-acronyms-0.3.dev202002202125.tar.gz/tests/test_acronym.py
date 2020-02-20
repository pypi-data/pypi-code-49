import unittest
from acronyms.acronym import Acronym

class TestAcronym(unittest.TestCase):
    def test_key(self):
        a = Acronym()
        self.assertEqual(a.key, '')
        a.key = 1
        self.assertIsInstance(a.key, str, "Acronym keys should be converted to strings.")
        self.assertEqual(a.key, '1')
        b = Acronym('b', 'B', 'Bravissimo')
        self.assertEqual(b.key, 'b')
        self.assertEqual(b.shortform, 'B')
        self.assertEqual(b.longform, 'Bravissimo')

    def test_shortform(self):
        a = Acronym()
        self.assertEqual(a.shortform, '')
        a.shortform = 123
        self.assertIsInstance(a.shortform, str, "Acronym keys should be converted to strings.")
        self.assertEqual(a.shortform, '123')

    def test_longform(self):
        a = Acronym()
        self.assertEqual(a.longform, '')
        a.longform = 123456789
        self.assertIsInstance(a.longform, str, "Acronym keys should be converted to strings.")
        self.assertEqual(a.longform, '123456789')

if __name__ == '__main__':
    unittest.main()
