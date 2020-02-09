from django.test import TestCase

from .fixtures import RequiredFixturesMixin, FixturesData


class FixturesTestCase(TestCase, RequiredFixturesMixin):
    @classmethod
    def setUpClass(cls):
        initial_fixtures, cls.fixtures = FixturesData(cls.fixtures), []

        super().setUpClass()

        cls.fixtures = initial_fixtures
        cls._load_required_fixtures()
