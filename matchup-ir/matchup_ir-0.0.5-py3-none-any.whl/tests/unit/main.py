import unittest

from tests.unit import model_test, sanitizer_test, occurrence_test, query_test, vocabulary_test


def create_suite(t_lst, t_load):
    t_lst.append(t_load.loadTestsFromTestCase(model_test.ModelTest))
    t_lst.append(t_load.loadTestsFromTestCase(sanitizer_test.SanitizerTest))
    t_lst.append(t_load.loadTestsFromTestCase(occurrence_test.OccurrenceTest))
    t_lst.append(t_load.loadTestsFromTestCase(query_test.QueryTest))
    t_lst.append(t_load.loadTestsFromTestCase(vocabulary_test.VocabularyTest))


test_list = []
test_loader = unittest.TestLoader()

# add test suites
create_suite(test_list, test_loader)

suite = unittest.TestSuite(test_list)
runner = unittest.TextTestRunner()
runner.run(suite)
