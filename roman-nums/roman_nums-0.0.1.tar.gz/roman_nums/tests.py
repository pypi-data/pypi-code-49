
import unittest
from roman_nums.roman_nums import to_roman, from_roman
from roman_nums.roman_nums.utils import RText, rn_validator

RN_NUMBERS_VALID = (
    (3, 'III'), (123, 'CXXIII'), (234, 'CCXXXIV'), (78, 'LXXVIII'), (34, 'XXXIV'), (23, 'XXIII')
)

RN_NUMBERS_INVALID = (
    'IIII', 'VVI', 'MMMCLLIV'
)

ORIGINAL = """С IX—VIII веков до н. э. в Британию активно переселялись кельты. Под давлением государства гуннов и 
ослаблением Римской империи к 410 году с острова ушли римляне и вторглись волнами англосаксы, сформировавшие здесь 7 
своих королевств"""


class TestRomanNums(unittest.TestCase):
    def test_to_roman(self):
        for n, rn in RN_NUMBERS_VALID:
            self.assertEqual(to_roman(n), rn)

    def test_from_roman(self):
        for n, rn in RN_NUMBERS_VALID:
            self.assertEqual(from_roman(rn), n)

    def test_rn_validator_true(self):
        for _, rn in RN_NUMBERS_VALID:
            self.assertTrue(rn_validator(rn))
        for _, rn in RN_NUMBERS_VALID:
            self.assertTrue(rn_validator(rn.lower(), case=-1))

    def test_rn_validator_false(self):
        for rn in RN_NUMBERS_INVALID:
            self.assertFalse(rn_validator(rn))
        for rn in RN_NUMBERS_INVALID:
            self.assertFalse(rn_validator(rn.lower(), case=-1))

    def test_rtext_rn(self):
        self.assertEqual(RText(ORIGINAL).rnb(), ['IX', 'VIII'])

    def test_rtext_n(self):
        self.assertEqual(RText(ORIGINAL).nb(), ['410', '7'])


if __name__ == '__main__':
    unittest.main()
