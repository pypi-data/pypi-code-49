import unittest
from milanlp.cleaning import utilities


class CleaningTest(unittest.TestCase):
    def test_something(self):
        text = "I like Pizza"
        cleaner = utilities.SimpleSpacyCleaner("en_core_web_sm")
        cleaned_text = cleaner.clean(text)

        self.assertEqual(cleaned_text, "like pizza")


if __name__ == '__main__':
    unittest.main()
