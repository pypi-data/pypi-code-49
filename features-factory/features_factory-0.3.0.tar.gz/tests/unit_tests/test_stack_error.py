import unittest

from features_factory.dependencies_error import DependenciesError
from features_factory.input_data_error import InputDataError
from features_factory.stack_error import StackError


class TestStackError(unittest.TestCase):

    def test_initially_the_error_is_empty(self):
        bbe = StackError()
        self.assertTrue(bbe.is_empty())

    def test_add(self):
        ie = InputDataError()
        ie.add_column_with_wrong_format('stone')

        de = DependenciesError()
        de.add_missing_dependencies(victim='Joe', missing_dependencies=['Jimi', 'Jane'])

        se1 = StackError()
        se1.add_input_data_error(ie)
        se1.add_dependency_error(de)

        ie = InputDataError()
        ie.add_missing_column('bubble')

        de = DependenciesError()
        de.add_missing_dependencies(victim='Gunther', missing_dependencies=['Reinhold', 'Mutter'])

        se2 = StackError()
        se2.add_input_data_error(ie)
        se2.add_dependency_error(de)

        se_sum = se1 + se2

        self.assertEqual(('stone', ),
                         se_sum.get_input_data_error().get_columns_with_wrong_format())
        self.assertEqual(('bubble', ),
                         se_sum.get_input_data_error().get_missing_columns())
        self.assertCountEqual(('Joe', 'Gunther'),
                         se_sum.get_dependencies_error().get_missing_dependencies_victims())
        self.assertCountEqual(('Jimi', 'Jane'),
                         se_sum.get_dependencies_error().get_missing_dependency_of_victim('Joe'))
        self.assertCountEqual(('Reinhold', 'Mutter'),
                         se_sum.get_dependencies_error().get_missing_dependency_of_victim('Gunther'))

    def test_to_string_contains_both_input_and_dependencies_info_messages(self):
        ie = InputDataError()
        ie.add_column_with_wrong_format('stone')

        de = DependenciesError()
        de.add_missing_dependencies(victim='Joe', missing_dependencies=['Jimi', 'Jane'])

        se = StackError()
        se.add_input_data_error(ie)
        se.add_dependency_error(de)

        message = se.to_string()
        self.assertTrue(ie.to_string() in message)
        self.assertTrue(de.to_string() in message)
