import unittest
from tests.test_tools import return_local_test_data, convert_to_json
from acronyms.acronym_filter import Filter
from acronyms.acronyms import Acronyms
import panflute
import io


class TestAcronymFilter(unittest.TestCase):
    def test_one_acronym(self):
        doc = self._loadJSONDocument("one_acronym.md")
        filter = Filter()
        filter.acronyms = self._createAcronymsDictionary(
            "two_basic_acronyms.json")
        filter.process_document(doc)
        self.assertEqual(filter.index.occurences('bba'), 1)
        self.assertEqual(filter.index.occurences('aba'), 0)

    def test_return_acronym_match(self):
        filter = Filter()
        self.assertTrue(filter.return_acronym_match("[!BBA]"))
        self.assertFalse(filter.return_acronym_match("[!]"))
        self.assertFalse(filter.return_acronym_match("[]"))
        self.assertFalse(filter.return_acronym_match("[[!BBA]]"))
        self.assertFalse(filter.return_acronym_match("[@BBA]"))

    def test_replace_acronym(self):
        filter = Filter()
        filter.acronyms = self._createAcronymsDictionary(
            "two_basic_acronyms.json")
        acronym = filter.acronyms.get('bba')
        test_sets = {
            # key (descriptive) : (input, first use?, expected result)
            "first use of acronym": ["[!bba]", True, "beer brewing attitude (BBA)"],
            "repeated use of acronym": ["[!bba]", False, "BBA"]
            # TODO Not Implemented:
            # "repeated use, plural form": ["[!bba+]", False, "BBAs"],
            # "use-with-word": ["[!bba]-related", False, "BBA-related"],

        }
        for key, test_set in test_sets.items():
            matchtext = test_set[0]
            firstuse = test_set[1]
            expected_result = test_set[2]
            result = filter.replace_acronym(matchtext, acronym, firstuse)
            self.assertEqual(result, expected_result, key)

    def test_process_string_token(self):
        # This replacer checks that the patterns are identified correctly:
        def maybe_replace_tester(pattern):
            return "###{}###".format(pattern)

        filter = Filter()
        filter.acronyms = self._createAcronymsDictionary(
            "two_basic_acronyms.json")

        tokens = {
            # a simple pattern
            "[!bba]": "###[!bba]###",
            # a pattern with no match
            "test": "test",
            # a multi-word pattern with no match
            "test-test test": "test-test test",
            # a pattern with multiple matches
            "[!bba]-related/[!aba]-based": "###[!bba]###-related/###[!aba]###-based"
        }
        for token, expected_result in tokens.items():
            result = filter.process_string_token(token, maybe_replace_tester)
            self.assertEqual(result, expected_result)

    def test_run_method(self):
        doc = self._loadJSONDocument("one_acronym.md")
        acronyms = return_local_test_data("two_basic_acronyms.json")
        filter = Filter()
        try:
            filter.run([acronyms], doc)
        except:
            self.fail("calling the run method should not fail")
        self.assertEqual(filter.index.occurences('bba'), 1)

    def test_run_method_no_acronymns(self):
        doc = self._loadJSONDocument("one_acronym.md")
        filter = Filter()
        try:
            filter.run([], doc)
        except:
            self.fail("calling the run method should not fail")
        self.assertEqual(filter.index.occurences('bba'), 0)

    def test_run_method_undefined_acronym(self):
        doc = self._loadJSONDocument("sample-text.md")
        acronyms = return_local_test_data("two_basic_acronyms.json")
        filter = Filter()
        filter.run([acronyms], doc)
        # try:
        #     filter.run([acronyms], doc)
        # except:
        #     self.fail("calling the run method should not fail")
        self.assertEqual(filter.index.occurences('bba'), 2)
        self.assertEqual(filter.index.occurences('undef'), 0)

    def test_check_for_suggestions(self):
        pattern = "A BBA is helpful, but BBA-requirements are not."
        doc = self._loadJSONDocument("sample-text.md")
        acronyms = return_local_test_data("two_basic_acronyms.json")
        filter = Filter()
        filter.run([acronyms], doc)
        result = filter.check_for_suggestions(pattern)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], 'NOTE: "BBA" in "A BBA is helpful, but BBA-requirements are not." could be an acronym. Consider replacing it with [!bba].')

    def _createAcronymsDictionary(self, filename):
        with open(return_local_test_data(filename), "r") as handle:
            return Acronyms.Read(handle)

    def _loadJSONDocument(self, filename):
        data = convert_to_json(return_local_test_data(filename))
        doc = panflute.load(io.StringIO(data))
        return doc


if __name__ == '__main__':
    unittest.main()
