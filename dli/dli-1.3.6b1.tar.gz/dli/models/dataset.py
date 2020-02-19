import json
import textwrap
import warnings
from typing import List
from urllib.parse import urljoin

import pyarrow

from dli.models import log_public_functions_calls_using, SampleData, \
    AttributesDict
from dli.client.aspects import analytics_decorator, logging_decorator
from dli.client.components.urls import consumption_urls
from dli.client.exceptions import DataframeStreamingException


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
            response_json['properties'],
            response_json['properties']['datasetId']
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
        Downloads all files from the latest instance into the provided
        destination path.
        This is a short-cut function for:
        `Dataset.instances.latest().download(destination_path)`

        :param destination_path: The path on the system, where the files
        should be saved.

        :return: the list of the downloaded files
        """
        return self.instances.latest().download(destination_path)

    def _dataframe(self, nrows=None, partitions: List[str] = None, raise_=True):
        """
        Return the data from the files in the latest instance of the dataset
        as a pandas DataFrame.

        We currently support .csv and .parquet as our data file formats. The
        data files in the latest instance could all be .csv format or all be
        .parquet format. If there is a mix of .csv and .parquet or some other
        file format then we will not be able to parse the data and will
        return an error message.

        :param int nrows: Optional. The max number of rows to return.
            We use the nrows parameter to limit the amount of rows that are
            returned, otherwise for very large dataset it will take a long time
            or you could run out of RAM on your machine!
            If you want all of the rows, then leave this parameter set to the
            default None.

        :param List[str] partitions: Optional. A dict of filters (partitions) to
            apply to the dataframe request in the form of: ["a=12","b>20190110"]
            - will permit whitespace and equality operators [<=, <, =, >, >=]

        :param bool raise_: Optional. Raise exception if the dataframe stream
            stopped prematurely

        :returns: Pandas DataFrame.
        :rtype: pandas.DataFrame
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
        Retrieves the list of available partitions for a given dataset.

        The data onboarding team have structured the file paths on S3 with
        simple partitions e.g. `as_of_date` or `location`.

        Their aim was to separate the data to reduce the size of the
        individual files. For example, data that has a `location` column with
        the options `us`, `eu` and `asia` can be separated into S3 paths like
        so:

            package-name/dataset/as_of_date=2019-09-10/location=eu/filename.csv
            package-name/dataset/as_of_date=2019-09-10/location=us/filename.csv

        in this case the `partitions` will be returned as:

            {'as_of_date': ['2019-09-10'], 'location': ['eu', 'us]}
        """
        response = self._client.session.get(
            urljoin(
                self._client._environment.consumption,
                consumption_urls.consumption_partitions.format(id=self.id)
            )
        )

        return json.loads(response.content)

    def display(self):
        """
        Print IDs for all the instances in this dataset.

        Example output:

            INSTANCE 1111aaa-11aa-11aa-11aa-111111aaaaaa
        """
        for p in self.instances.all():
            print(str(p))

    def __repr__(self):
        return self.id

    def __str__(self):
        separator = "-" * 80
        splits = "\n".join(textwrap.wrap(self.description))

        return f"\nDATASET \"{self.short_code}\" [{self.data_format}]\n" \
               f">> Available Date Range: {self.first_datafile_at} to {self.last_datafile_at}\n" \
               f">> ID: {self.id}\n" \
               f">> Published: {self.publishing_frequency} by {self.organisation_name}\n" \
               f">> Accessible: {self.has_access}\n" \
               f"\n" \
               f"{splits}\n" \
               f"{separator}"
