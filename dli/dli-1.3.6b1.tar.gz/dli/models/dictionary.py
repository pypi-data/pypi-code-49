import warnings

from dli.models.paginator import Paginator
from dli.client.aspects import analytics_decorator, logging_decorator
from dli.client.components.urls import dataset_urls
from dli.models import log_public_functions_calls_using, AttributesDict


@log_public_functions_calls_using(
    [analytics_decorator, logging_decorator], class_fields_to_log=['dictionary_id']
)
class DictionaryModel(AttributesDict):

    @property
    def id(self):
        return self.dictionary_id

    @property
    def schema_id(self):
        """This method is deprecated. Please use DictionaryModel.id"""
        warnings.warn(
            'This method is deprecated. Please use DictionaryModel.id',
            DeprecationWarning
        )
        return self.id

    @property
    def fields(self):
        if 'fields' not in self.__dict__:
            self.__dict__['fields'] = list(self._paginator)

        return self.__dict__['fields']

    def __init__(self, json, client=None):
        self._client = client

        super().__init__(
            json['attributes'],
            dictionary_id=json['id'],
        )

        def append_flattened_to_cache(x, cache):
            for v in x["attributes"]["fields"]:
                cache.append(Field(v))

        self._paginator = Paginator(
            dataset_urls.dictionary_fields.format(id=self.dictionary_id),
            self._client._DictionaryV2,
            instantiation_override=append_flattened_to_cache,
            total_field="total_count"
        )


        if 'fields' not in json['attributes']:
            # DLIv2 doesn't put the fields on the attributes
            # when getting
            self.__dict__['fields'] = list(self._paginator)


class Field(AttributesDict):
    """
    Represents a dictionary Field. Exists
    to provide a basic class with a name.
    """