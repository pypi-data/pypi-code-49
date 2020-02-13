import unittest

from features_factory.dependencies_error import DependenciesError


class TestDependenciesError(unittest.TestCase):

    def test_initially_the_error_is_empty(self):
        de = DependenciesError()
        self.assertTrue(de.is_empty())

    def test_add_missing_dependency(self):
        de = DependenciesError()
        de.add_missing_dependencies(victim='Joe', missing_dependencies=['Jimi', 'Jane'])
        de.add_missing_dependencies(victim='Gunther', missing_dependencies=['Reinhold', 'Mutter'])
        de.add_missing_dependencies(victim='Gunther', missing_dependencies=['Reinhold', 'Elena'])

        self.assertFalse(de.is_empty())
        self.assertTrue(de.has_missing_dependencies())

        self.assertCountEqual(('Joe', 'Gunther'), de.get_missing_dependencies_victims())
        self.assertCountEqual(('Jimi', 'Jane'), de.get_missing_dependency_of_victim('Joe'))
        self.assertCountEqual(('Reinhold', 'Mutter', 'Elena'), de.get_missing_dependency_of_victim('Gunther'))

    def test_add(self):
        de1 = DependenciesError()
        de1.add_missing_dependencies(victim='Joe', missing_dependencies=['Jimi', 'Jane'])
        de1.add_missing_dependencies(victim='Gunther', missing_dependencies=['Reinhold', 'Mutter'])
        de1.add_missing_dependencies(victim='Gunther', missing_dependencies=['Reinhold', 'Elena'])

        de2 = DependenciesError()
        de2.add_missing_dependencies(victim='Paolo', missing_dependencies=('Francesca', ))
        de2.add_missing_dependencies(victim='Gunther', missing_dependencies=['Reinhold', 'Reinhold'])

        de = de1 + de2

        self.assertFalse(de.is_empty())
        self.assertTrue(de.has_missing_dependencies())

        self.assertCountEqual(('Joe', 'Gunther', 'Paolo'), de.get_missing_dependencies_victims())
        self.assertCountEqual(('Jimi', 'Jane'), de.get_missing_dependency_of_victim('Joe'))
        self.assertCountEqual(('Reinhold', 'Mutter', 'Elena'), de.get_missing_dependency_of_victim('Gunther'))
        self.assertCountEqual(('Francesca', ), de.get_missing_dependency_of_victim('Paolo'))

        # --- verify that de1 and de2 are unchanged
        self.assertCountEqual(('Joe', 'Gunther'), de1.get_missing_dependencies_victims())
        self.assertCountEqual(('Jimi', 'Jane'), de1.get_missing_dependency_of_victim('Joe'))
        self.assertCountEqual(('Reinhold', 'Mutter', 'Elena'), de1.get_missing_dependency_of_victim('Gunther'))

        self.assertCountEqual(('Paolo', 'Gunther'), de2.get_missing_dependencies_victims())
        self.assertCountEqual(('Francesca', ), de2.get_missing_dependency_of_victim('Paolo'))
        self.assertCountEqual(('Reinhold', ), de2.get_missing_dependency_of_victim('Gunther'))

    def test_to_string_contains_involved_names(self):
        de = DependenciesError()
        de.add_missing_dependencies(victim='Joe', missing_dependencies=['Jimi', 'Jane'])
        self.assertTrue('Joe' in de.to_string())
        self.assertTrue('Jimi' in de.to_string())
        self.assertTrue('Jane' in de.to_string())

    def test_to_string_of_empty_error_contains_word_empty(self):
        de = DependenciesError()
        self.assertTrue('empty' in de.to_string())

    def test_to_string_does_not_report_empty_victims(self):
        de = DependenciesError()
        de.add_missing_dependencies(victim='Joe', missing_dependencies=[])
        self.assertNotIn('Joe', de.to_string())
