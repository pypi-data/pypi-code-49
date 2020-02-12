import inspect
import os
import warnings
import contextlib
import shutil
import multiprocessing
from threading import Lock
from typing import List, Dict

import textwrap
import pyarrow
import humps
import json
import itertools

from urllib.parse import urljoin, urlparse
from collections.abc import Mapping, Iterable
from collections import UserDict, OrderedDict
from concurrent.futures import ThreadPoolExecutor

from dli.client.aspects import analytics_decorator, logging_decorator
from dli.client.components.urls import dataset_urls, consumption_urls, \
    me_urls, package_urls, search_urls
from dli.client.exceptions import DataframeStreamingException

THREADS = multiprocessing.cpu_count()


def log_public_functions_calls_using(decorators, class_fields_to_log=None):
    if not class_fields_to_log:
        class_fields_to_log = []

    def decorate(cls):
        functions_to_exclude = inspect.getmembers(AttributesDict, inspect.isfunction)
        functions_to_decorate = [
            func for func in inspect.getmembers(cls, inspect.isfunction)
            if func not in functions_to_exclude and not func[0].startswith('__')
        ]
        for function_meta in functions_to_decorate:
            function_name = function_meta[0]
            for decorator in decorators:
                setattr(
                    cls,
                    function_name,
                    decorator(getattr(cls, function_name),
                              class_fields_to_include=class_fields_to_log)
                )
        return cls
    return decorate


class AttributesDict(UserDict):

    def __init__(self, *args, **kwargs):
        # recursively provide the rather silly attribute
        # access
        data = {}

        for arg in args:
            data.update(arg)

        data.update(**kwargs)

        for key, value in data.items():
            if isinstance(value, Mapping):
                self.__dict__[key] = AttributesDict(value)
            else:
                self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def _asdict(self, *args, **kwargs):
        warnings.warn(
            'This method is deprecated as it returns itself.',
            DeprecationWarning
        )

        return self

    def __repr__(self):
        attributes = ' '.join([
            '{}={}'.format(k, v) for k,v in self.__dict__.items()
            if not k.startswith('_')
        ])

        return "{}({})".format(self.__class__.__name__, attributes)


class SampleData:
    def __init__(self, parent):
        self._parent = parent
        self._client = parent._client

    def schema(self):
        """
        Returns the schema data and first rows of sample data.

        :returns: attributes dictionary
        """
        response = self._client.session.get(
            dataset_urls.v2_sample_data_schema.format(id=self._parent.id)
        )

        return AttributesDict(**response.json()['data']['attributes'])

    @contextlib.contextmanager
    def file(self):
        """
        Provides a file like object containing sample data.

        Example usage:

        .. code-block:: python

            dataset = self.client.get_dataset(dataset_id)
            with dataset.sample_data.file() as f:
                dataframe = pandas.read_csv(f)
        """
        response = self._client.session.get(
            dataset_urls.v2_sample_data_file.format(id=self._parent.id),
            stream=True
        )
        # otherwise you get raw secure
        response.raw.decode_content = True
        yield response.raw
        response.close()


@log_public_functions_calls_using(
    [analytics_decorator, logging_decorator],
    class_fields_to_log=['datafile_id', 'path']
)
class FileModel(AttributesDict):

    @contextlib.contextmanager
    def open(self):
        response = self._client.session.get(
            urljoin(
                self._client._environment.consumption,
                consumption_urls.consumption_download.format(
                    id=self.datafile_id,
                    path=self.path
                )
            ),
            stream=True
        )
        # otherwise you get raw secure
        response.raw.decode_content = True
        yield response.raw
        response.close()

    def download(self, to='./'):
        to = os.path.join(
            to, urlparse(self.path).path.lstrip('/')
        )

        directory, _ = os.path.split(to)
        os.makedirs(directory, exist_ok=True)

        with self.open() as download_stream:
            with open(to, 'wb') as target_download:
                # copyfileobj is just a simple buffered
                # file copy function with some sane
                # defaults and optimisations.
                shutil.copyfileobj(
                    download_stream, target_download
                )

        return to


@log_public_functions_calls_using(
    [analytics_decorator, logging_decorator], class_fields_to_log=['datafile_id']
)
class InstanceModel(AttributesDict):

    def __init__(self, **kwargs):
        # Ignore the datafile's files
        kwargs.pop('files', [])
        super().__init__(**kwargs)

    def files(self):
        url = urljoin(
            self._client._environment.consumption,
            consumption_urls.consumption_manifest.format(
                id=self.datafile_id
            )
        )

        response = self._client.session.get(url)
        return [
            self._client._File(
                datafile_id=self.datafile_id,
                **d['attributes']
            )
            for d in response.json()['data']
        ]

    @classmethod
    def _from_v1_entity(cls, entity):
        properties = humps.decamelize(entity['properties'])
        return cls(**properties)

    def download_all(self, to='./'):
        warnings.warn(
            'This method will soon become deprecated. '
            'Please use `download` function instead.',
            PendingDeprecationWarning
        )
        return self.download(to)

    def download(self, to='./'):
        files = self.files()

        def _download(file_):
            return file_.download(to=to)

        threads = min(THREADS, len(files))
        with ThreadPoolExecutor(max_workers=threads) as executor:
            return list(executor.map(_download, files))

    def __str__(self):
        separator = "-"*80
        return f"\nINSTANCE {self.datafile_id}"


@log_public_functions_calls_using(
    [analytics_decorator, logging_decorator],
    class_fields_to_log=['_dataset.dataset_id']
)
class InstancesCollection(AttributesDict):

    def __init__(self, dataset=None):
        self._dataset = dataset
        self._paginator = Paginator(
            dataset_urls.datafiles.format(id=self._dataset.id),
            self._client.Instance, self._client.Instance._from_v1_entity
        )

    def latest(self):
        response = self._client.session.get(
            dataset_urls.latest_datafile.format(id=self._dataset.id)
        ).json()

        return self._client.Instance._from_v1_entity(response)

    def all(self):
        yield from self._paginator


@log_public_functions_calls_using(
    [analytics_decorator, logging_decorator], class_fields_to_log=['dataset_id']
)
class DatasetModel(AttributesDict):

    @property
    def sample_data(self):
        return SampleData(self)

    @property
    def id(self):
        return self.dataset_id

    def __init__(self, **kwargs):
        super().__init__(**kwargs,)
        self.instances = self._client._InstancesCollection(dataset=self)

    @classmethod
    def _from_v2_response(cls, response_json):
        return cls._construct_dataset_using(
            response_json['data']['attributes'], response_json['data']['id']
        )

    @classmethod
    def _from_v2_response_unsheathed(cls, response_json):
        return cls._construct_dataset_using(
            response_json['attributes'], response_json['id']
        )

    @classmethod
    def _from_v1_response_unsheathed(cls, response_json):
        response_json['properties']['location'] = None
        return cls._construct_dataset_using(
            response_json['properties'], response_json['properties']['datasetId']
        )

    @classmethod
    def _from_v2_list_response(cls, response_json):
        return [
            cls._construct_dataset_using(
                dataset['attributes'], dataset['id']
            )
            for dataset in response_json['data']
        ]

    @classmethod
    def _construct_dataset_using(cls, attributes, dataset_id):
        location = attributes.pop('location')
        # In the interests of not breaking backwards compatability.
        # TODO find a way to migrate this to the new nested API.

        if not location:
            location = None
        else:
            location = location[next(iter(location))]
        return cls(
            **attributes,
            location=location,
            dataset_id=dataset_id
        )

    def download(self, destination_path):
        """
        Downloads all files from the latest instance into the provided destination path.
        This is a short-cut function for:
        `Dataset.instances.latest().download(destination_path)`

        :param destination_path: The path on the system,
            where the files should be saved.
        :return: the list of downloaded files
        """
        return self.instances.latest().download(destination_path)

    def _dataframe(self, nrows=None, partitions: List[str] = None, raise_=True):
        """
        Returns a pandas dataframe of the dataset.

        :param int nrows: The max number of rows to return
        :param List[str] partitions: A dict of filters (partitions) to
            apply to the dataframe request in the form of: ["a=12","b>20190110"]
            - will permit whitespace and equality operators [<=, <, =, >, >=]
        :param bool raise_: raise if the dataframe stream stopped prematurely
        """
        params = {}

        if nrows is not None:
            params['filter[nrows]'] = nrows

        if partitions is not None:
            params['filter[partitions]'] = partitions

        dataframe_url = urljoin(
            self._client._environment.consumption,
            consumption_urls.consumption_dataframe.format(id=self.id)
        )

        response = self._client.session.get(
            dataframe_url, stream=True,
            params=params
        )

        # Don't decode content. We would like to keep the raw
        # probably gziped steam. Otherwise the stream.read(n) will
        # return a string of length != n.
        response.raw.decode_content = False

        native_file = pyarrow.PythonFile(response.raw, mode='rb')

        # If the response is gzip we need to wrap the
        # encoding in a decompressor.
        if response.headers['Content-Encoding'] == 'gzip':
            native_file = pyarrow.CompressedInputStream(
                native_file, 'gzip'
            )

        reader = pyarrow.ipc.open_stream(native_file)
        dataframe = reader.read_pandas()

        # The pyarrow buffered stream reader stops once it
        # reaches the end of the IPC message. Afterwards we
        # get the rest of the data which contains the summary
        # of what we've downloaded including an error message.
        summary_string = native_file.read()
        if summary_string:
            summary = json.loads(summary_string)

            if (summary['status'] >= 400):
                exception = DataframeStreamingException(
                    summary, dataframe_url
                )

                # Optionally ignore bad data
                if raise_:
                    raise exception
                else:
                    warnings.warn(
                        str(exception),
                        UserWarning
                    )

        return dataframe

    def _partitions(self):
        """
        Retrieves the list of available partitions for a given dataset
        """
        response = self._client.session.get(
            urljoin(
                self._client._environment.consumption,
                consumption_urls.consumption_partitions.format(id=self.id)
            )
        )

        return json.loads(response.content)

    def display(self):
        for p in self.instances.all():
            print(str(p))

    def __repr__(self):
        return self.id

    def __str__(self):
        separator = "-"*80
        splits = "\n".join(textwrap.wrap(self.description))

        return f"\nDATASET \"{self.short_code}\" [{self.data_format}]\n" \
               f">> Available Date Range: {self.first_datafile_at} to {self.last_datafile_at}\n" \
               f">> ID: {self.id}\n" \
               f">> Published: {self.publishing_frequency} by {self.organisation_name}\n" \
               f">> Accessible: {self.has_access}\n" \
               f"\n" \
               f"{splits}\n" \
               f"{separator}"


class Field(AttributesDict):
    """
    Represents a dictionary Field. Exists
    to provide a basic class with a name.
    """


@log_public_functions_calls_using(
    [analytics_decorator, logging_decorator], class_fields_to_log=['dictionary_id']
)
class DictionaryModel(AttributesDict):

    @property
    def id(self):
        return self.dictionary_id

    @property
    def schema_id(self):
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


class AccountModel(AttributesDict):
    @classmethod
    def _from_v2_response(cls, data):
        id_ = data.pop('id')
        attributes = data.pop('attributes')
        attributes.pop('ui_settings', None)
        return cls(id=id_, **attributes)


class PackageModel:
    """
    Represents a package pulled back from Me consumables
    """
    def __init__(self, json):
        self.id = json["properties"]["packageId"]
        self.name = json["properties"]["name"]
        if json["properties"].get("data", None):
            # we have a package_access_request json
            root = json["properties"]["data"]
        else:
            # we have a package json
            root = json["properties"]

        self.description = root["description"]
        self.sensitivity = root["dataSensitivity"]
        self.keywords = ", ".join(root["keywords"])
        self.documentation = root.get("documentation", "No documentation")
        self.hasAccess = root.get("has_access", "Unknown")
        self._paginator = Paginator(package_urls.v2_package_datasets.format(id=self.id),
                 self._client.Dataset,
                 self._client.Dataset._from_v2_response_unsheathed)

        self.shape = len(self.datasets())

    def datasets(self) -> Dict[str, DatasetModel]:
        return OrderedDict([(v.name, v) for v in self._paginator])

    def display(self):
        for p in self.datasets().items():
            print(str(p[1]))

    def __str__(self):
        separator = "-"*80
        split_description = "\n".join(textwrap.wrap(self.description, 80))
        split_keywords = "\n".join(textwrap.wrap(self.keywords, 80))
        split_documentation = "\n".join(textwrap.wrap(self.documentation, 80))
        return f"\nPACKAGE \"{self.name}\" (Contains: {self.shape} datasets)\n" \
               f">> ID: {self.id} \n" \
               f">> Sensitivity: {self.sensitivity} / Accessible: {self.hasAccess}\n"\
               f"\n" \
               f"{split_description}\n" \
               f"Documentation: {split_documentation}\n\n" \
               f"Keywords: {split_keywords}\n"\
               f"{separator}"

    def __repr__(self):
        return f"{self.id}"


class Paginator:

    def __init__(self, url, model,
         instantiation_method=None, instantiation_override=None,
         page=1, total_field=None
    ):
        self.page = page
        self.url = url
        self.model = model
        self.instantiation_factory = instantiation_method
        self.override = instantiation_override
        self.cache = []
        self.total_field = total_field
        self.lock = Lock()

    def _request(self, page=None):
        return self.model._client.session.get(
                self.url,
                params={
                    'page': self.page if not page else page,
                }
            ).json()

    def __iter__(self):
        if not self.cache:
            try:
                tp = ThreadPoolExecutor(max_workers=10)

                inst = self._request()
                if inst.get("entities", None):
                    # v1 route
                    key = "entities"
                    count = ("properties", "pages_count")
                else:
                    # v2 route
                    key = "data"
                    count = ("meta", "total_pages")

                def _get_and_instantiate(page):
                    inst = self._request(page)
                    self._iter_instance(inst, key)

                self._iter_instance(inst, key)

                total_pages = inst[count[0]][
                                  self.total_field if self.total_field
                                  else count[1]] + 1
                rng = range(2, total_pages)

                list(tp.map(_get_and_instantiate, rng))

            finally:
                tp.shutdown(wait=True)

        yield from self.cache

    def _iter_instance(self, inst, key):
        obj = inst if not key else inst[key]
        if key:
            obj = inst[key]

        # we use the __init__ method of the class unless
        # (or) provided instantiation method
        # ... useful to transform data first
        # (or) provided override to control cache insertion
        # ... useful to flatten multi-item

        if not self.override:
            for f in obj:
                if not self.instantiation_factory:
                    m = self.model(f)
                else:
                    m = self.instantiation_factory(f)

                with self.lock:
                    self.cache.append(m)
        else:
            self.override(obj, self.cache)


class PackageModule:

    def __call__(self, search_term=None, only_mine=True) \
            -> Dict[str, PackageModel]:
        """
               Returns a dictionary[id: str, PackageModel].

               :param str search_term: The search phrase to search the catalogue
               with, and to pull back packages based on name, description etc.
               :param bool only_mine: Specify whether to collect packages only
               accessible to you (user) or to discover packages that you may
               want to discover.
           """


        if only_mine:
            p = Paginator(me_urls.consumed_packages, self._client._Package)
        else:
            p = Paginator(search_urls.search_packages,  self._client._Package)

        # todo this should change to (v.shortcode, v) in future
        return OrderedDict([(v.name, v) for v in p])

    def _get(self, short_code) -> PackageModel:
        """
            Returns a PackageModel if it exists else None

            :param str package name: The name of the package to collect
        """
        warnings.warn(
            'Getting a dataset by name, and package name or package ID'
            'will be deprecated in future. Short-codes will replace this.',
            PendingDeprecationWarning
        )
        params = {}

        # todo this should be by short code but EP doesnt seem to exist for this yet
        # so pass p_id
        params["package_id"] = short_code
        response = self._client.session.get(
            package_urls.package_index, params=params
        )
        return self._client._Package(response.json())


class DatasetModule:

    def __call__(self, search_term=None, only_mine=True) \
            -> Dict[str, DatasetModel]:
        """
            Returns a dictionary[id: str, DatasetModel].

            :param str search_term: The search phrase to search the catalogue
            with, and to pull back datasets based on name, description etc.
            :param bool only_mine: Specify whether to collect datasets only
            accessible to you (True) or to discover packages that you may
            want to discover but may not have access to (False).

            If any combination of the two, then search term takes precedence
            of routing, followed by the application of only_mine flag.
        """
        p = Paginator(
            search_urls.search_datasets,
            self._client.Dataset,
            self._client.Dataset._from_v1_response_unsheathed
        )

        # todo this should change to (v.shortcode, v) in future
        return OrderedDict([(v.name, v) for v in p])

    def _get(self, short_code) -> DatasetModel:
        """
            Returns a DatasetModel if it exists else None

            :param str dataset name: The name of the dataset to collect
        """
        warnings.warn(
            'Getting a dataset by name, and package name or package ID'
            'will be deprecated in future. Short-codes will replace this.',
            PendingDeprecationWarning
        )
        params = {}

        # todo this should be by short code but EP doesnt seem to exist for this yet
        # so pass d_id
        params["dataset_id"] = short_code
        response = self._client.session.get(
            dataset_urls.v2_instance.format(id=short_code)
        )

        return self._client.Dataset._from_v2_response(response.json())



