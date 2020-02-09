import json
from abc import abstractmethod, ABCMeta, ABC
from typing import Any, List

from django.core.management import call_command
from django.db import DEFAULT_DB_ALIAS

from django_fixtures.dataset import CommonDatasetMixin
from django_fixtures.utilities import snake_case, get_fixture_filepath, get_fixture


class FixturesData(list, object):
    def __init__(self, fixtures):
        super().__init__(fixtures)

        for index, fixture in enumerate(fixtures):
            self[index] = fixture

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


class RequiredFixturesMixin:
    fixtures = None

    @classmethod
    def _load_required_fixtures(cls):
        cls.fixtures = FixturesData(cls.fixtures or [])

        for fixture_class_or_accessor in cls.fixtures:
            if isinstance(fixture_class_or_accessor, str):
                fixture = get_fixture(fixture_class_or_accessor)
            else:
                fixture = fixture_class_or_accessor(fixture_class_or_accessor.__module__)

            if (fixture_data := fixture.load()):
                if not hasattr(cls, fixture.app_label):
                    setattr(cls.fixtures, fixture.app_label, app_data := FixturesData([]))
                else:
                    app_data = getattr(cls.fixtures, fixture.app_label)

                cls.fixtures[fixture.name] = fixture_data
                cls.fixtures[fixture.__class__.__name__] = fixture_data

                setattr(cls.fixtures, fixture.__class__.__name__, fixture_data)
                setattr(cls.fixtures, snake_case(fixture.__class__.__name__, '_'), fixture_data)

                app_data[fixture.__class__.__name__] = fixture_data

                setattr(app_data, fixture.__class__.__name__, fixture_data)
                setattr(app_data, snake_case(fixture.__class__.__name__, '_'), fixture_data)


class BaseFixture(RequiredFixturesMixin, CommonDatasetMixin, metaclass=ABCMeta):
    def __init__(self, app_label: str):
        super().__init__()

        self.app_label, self.name = app_label, f'{app_label}.{self.__class__.__name__}'
        self.filepath = get_fixture_filepath(app_label, snake_case(self.__class__.__name__))

    def process_dataset_entry(self, *args, **kwargs) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def load(self):
        pass


class JSONFixture(BaseFixture, ABC):
    def serialize_dataset_entry(self, entry: dict) -> dict:
        return entry

    def create(self):
        self._load_required_fixtures()
        serialized_entries = []

        for entry in self.dataset:
            args, kwargs = self.prepare_dataset_entry(entry)
            entry = self.process_dataset_entry(*args, **kwargs)

            serialized_entries.append(entry)

        with open(self.filepath, 'w+') as file:
            file.write(json.dumps(serialized_entries))

    def load(self) -> List[dict]:
        with open(self.filepath, 'r+') as file:
            return json.loads(file.read())


class ModelFixture(BaseFixture, ABC):
    database, models = DEFAULT_DB_ALIAS, None

    def create(self):
        self._load_required_fixtures()

        for entry in self.dataset:
            args, kwargs = self.prepare_dataset_entry(entry)
            entry = self.process_dataset_entry(*args, **kwargs)

            entry.save(using=self.database)

        models_list = [f'{model._meta.app_label}.{model._meta.object_name}' for model in self.models]
        call_command('dumpdata', *models_list, verbosity=0, database=self.database, output=self.filepath)

    def load(self):
        call_command('loaddata', self.filepath, verbosity=0, database=self.database)
