# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Contains functionality for promoting an intermediate output to an Azure Machine Learning Dataset.

Intermediate data (output) in a pipeline by default will not become an Azure Machine Learning Dataset. To promote
intermediate data to an Azure Machine Learning Dataset, call the
:meth:`azureml.pipeline.core.builder.PipelineData.as_dataset` method on the PipelineData class to return
a :class:`azureml.pipeline.core.pipeline_output_dataset.PipelineOutputFileDataset` object. From a
PipelineOutputFileDataset object, you can then create an
:class:`azureml.pipeline.core.pipeline_output_dataset.PipelineOutputTabularDataset` object.
"""
from abc import ABCMeta
from copy import copy

from azureml.data._dataprep_helper import dataprep
from azureml.data._partition_format import handle_partition_format
from azureml.data.dataset_type_definitions import PromoteHeadersBehavior


class PipelineOutputAbstractDataset(object):
    """
    Represents the base class for promoting intermediate data to an Azure Machine Learning Dataset.

    Once an intermediate data is promoted to an Azure Machine Learning dataset, it will also be consumed as a
    :class:`azureml.core.Dataset` instead of a :class:`azureml.data.data_reference.DataReference` in subsequent
    steps.

    :param pipeline_data: The PipelineData that represents the intermediate output which will be promoted to
        a Dataset.
    :type pipeline_data: azureml.pipeline.core.PipelineData
    """

    __metaclass__ = ABCMeta

    def __init__(self, pipeline_data):
        """
        Create an intermediate data that will be promoted to an Azure Machine Learning Dataset.

        :param pipeline_data: The PipelineData that represents the intermediate output which will be promoted to
            a Dataset.
        :type pipeline_data: azureml.pipeline.core.PipelineData
        """
        self._pipeline_data = pipeline_data

        self._registration_name = None
        self._create_new_version = None
        self._input_mode = "mount"
        self._input_name = self._pipeline_data._output_name
        self._input_path_on_compute = None

    def register(self, name, create_new_version=True):
        """
        Register the output dataset to the workspace.

        :param name: The name of the registered dataset once the intermediate data is produced.
        :type name: str
        :param create_new_version: Whether to create a new version of the dataset if the data source changes. Defaults
            to True. By default, all intermediate output will output to a new location when a pipeline runs, so
            it is highly recommended to keep this flag set to True.
        :return:
        """
        other = self._clone()
        other._registration_name = name
        other._create_new_version = create_new_version
        return other

    def as_named_input(self, name):
        """Set the name of the dataset when it is used as input for subsequent steps.

        :param name: The name of the dataset for the input.
        :type name: str
        :return: The intermediate data with the new input name.
        :rtype: azureml.pipeline.core.pipeline_output_dataset.PipelineOutputFileDataset
                or azureml.pipeline.core.pipeline_output_dataset.PipelineOutputTabularDataset
        """
        other = self._clone()
        other._input_name = name
        return other

    @property
    def name(self):
        """
        Get the output name of the PipelineData.

        :return: The output name of the PipelineData.
        :rtype: str
        """
        return self._output_name

    def create_input_binding(self):
        """
        Create an input binding.

        :return: The InputPortBinding with this PipelineData as the source.
        :rtype: azureml.pipeline.core.graph.InputPortBinding
        """
        from azureml.pipeline.core import InputPortBinding

        if not self._input_mode:
            raise RuntimeError("Input mode cannot be None or empty.")

        return InputPortBinding(
            name=self.input_name,
            bind_object=self._pipeline_data,
            bind_mode=self._input_mode,
            path_on_compute=self._input_path_on_compute,
            overwrite=False,
        )

    @property
    def input_name(self):
        """
        Get the input name of the PipelineOutputDataset.

        You can use this name to retrieve the materialized dataset through environment environment variable or
        the :class:`azureml.core.Run` class ``input_datasets`` property.

        :return: Input name of the PipelineOutputDataset.
        :rtype: str
        """
        return self._input_name

    @property
    def _output_name(self):
        return self._pipeline_data._output_name

    @property
    def _data_type_short_name(self):
        return "AzureMLDataset"

    def _set_producer(self, producer):
        self._pipeline_data._set_producer(producer)

    @property
    def _producer(self):
        return self._pipeline_data._producer

    def _clone(self):
        return copy(self)


class PipelineOutputFileDataset(PipelineOutputAbstractDataset):
    """
    Represents intermediate pipeline data promoted to an Azure Machine Learning File Dataset.

    Once an intermediate data is promoted to an Azure Machine Learning Dataset, it will also be consumed as a Dataset
    instead of a DataReference in subsequent steps.

    :param pipeline_data: The PipelineData that represents the intermediate output which will be promoted to
        a Dataset.
    :type pipeline_data: azureml.pipeline.core.PipelineData
    """

    def __init__(self, pipeline_data):
        """
        Create an intermediate data that will be promoted to an Azure Machine Learning Dataset.

        :param pipeline_data: The PipelineData that represents the intermediate output which will be promoted to
            a Dataset.
        :type pipeline_data: azureml.pipeline.core.PipelineData
        """
        super(PipelineOutputFileDataset, self).__init__(pipeline_data=pipeline_data)

    def as_download(self, path_on_compute=None):
        """
        Set the consumption mode of the dataset to download.

        :param path_on_compute: The path on the compute to download the dataset to. Defaults to None, which means
            Azure Machine Learning picks a path for you.
        :type path_on_compute: str
        :return: The modified PipelineOutputDataset.
        :rtype: azureml.pipeline.core.pipeline_output_dataset.PipelineOutputFileDataset
        """
        return self._set_mode("download", path_on_compute=path_on_compute)

    def as_mount(self, path_on_compute=None):
        """
        Set the consumption mode of the dataset to mount.

        :param path_on_compute: The path on the compute to mount the dataset to. Defaults to None, which means
            Azure Machine Learning picks a path for you.
        :type path_on_compute: str
        :return: The modified PipelineOutputDataset.
        :rtype: azureml.pipeline.core.pipeline_output_dataset.PipelineOutputFileDataset
        """
        return self._set_mode("mount", path_on_compute=path_on_compute)

    def as_direct(self):
        """
        Set input the consumption mode of the dataset to direct.

        In this mode, you will get the ID of the dataset and in your script you can call Dataset.get_by_id to retrieve
        the dataset. run.input_datasets['{dataset_name}'] will return the Dataset.

        :return: The modified PipelineOutputDataset.
        :rtype: azureml.pipeline.core.pipeline_output_dataset.PipelineOutputFileDataset
        """
        return self._set_mode("direct", path_on_compute=None)

    def parse_delimited_files(self, include_path=False, separator=',',
                              header=PromoteHeadersBehavior.ALL_FILES_HAVE_SAME_HEADERS,
                              partition_format=None,
                              file_extension=None):
        """Transform the intermediate file dataset to a tabular dataset.

        The tabular dataset is created by parsing the delimited file(s) pointed to by the intermediate output.

        :param include_path: Boolean to keep path information as column in the dataset. Defaults to False.
            This is useful when reading multiple files, and want to know which file a particular record
            originated from, or to keep useful information in file path.
        :type include_path: bool
        :param separator: The separator used to split columns.
        :type separator: str
        :param header: Controls how column headers are promoted when reading from files. Defaults to assume
            that all files have the same header.
        :type header: azureml.data.dataset_type_definitions.PromoteHeadersBehavior
        :param partition_format: Specify the partition format of path. Defaults to None.
            The partition information of each path will be extracted into columns based on the specified format.
            Format part '{column_name}' creates string column, and '{column_name:yyyy/MM/dd/HH/mm/ss}' creates
            datetime column, where 'yyyy', 'MM', 'dd', 'HH', 'mm' and 'ss' are used to extract year, month, day,
            hour, minute and second for the datetime type. The format should start from the position of first
            partition key until the end of file path.
            For example, given the path '../USA/2019/01/01/data.csv' where the partition is by country and
            time, partition_format='/{Country}/{PartitionDate:yyyy/MM/dd}/data.csv' creates string column 'Country'
            with value 'USA' and datetime column 'PartitionDate' with value '2019-01-01'.
        :type partition_format: str
        :param file_extension: The file extension of the files to read. Only files with this extension will be read
            from the directory. Default value is '.csv' when the serperator is ',' and '.tsv' when the seperator
            is tab, and "" otherwise. If "" is passed, all files will be read regardless of their extension (or
            lack of extension).
        :type file_extension: str
        :return: Returns an intermediate data that will be a tabular dataset.
        :rtype: azureml.pipeline.core.pipeline_output_dataset.PipelineOutputTabularDataset
        """
        dprep = dataprep()
        dataflow = dprep.Dataflow(self._engine_api)

        if file_extension is None:
            if separator == ',':
                file_extension = '.csv'
            elif separator == '\t':
                file_extension = '.tsv'

        if file_extension is not None and len(file_extension) > 0:
            if file_extension[0] != '.':
                file_extension = '.' + file_extension
            dataflow = dataflow.filter(
                dprep.api.functions.get_stream_name(dataflow['Path']).ends_with(file_extension)
            )

        dataflow = dataflow.parse_delimited(
            separator=separator, headers_mode=header, encoding=dprep.FileEncoding.UTF8, quoting=False,
            skip_rows=0, skip_mode=dprep.SkipMode.NONE, comment=None
        )
        if partition_format:
            dataflow = handle_partition_format(dataflow, partition_format)
        dataflow = PipelineOutputFileDataset._handle_path(dataflow, include_path)
        return PipelineOutputTabularDataset(self, dataflow)

    def parse_parquet_files(self, include_path=False, partition_format=None, file_extension=".parquet"):
        """Transform the intermediate file dataset to a tabular dataset.

        The tabular dataset is created by parsing the parquet file(s) pointed to by the intermediate output.

        :param include_path: Boolean to keep path information as column in the dataset. Defaults to False.
            This is useful when reading multiple files, and want to know which file a particular record
            originated from, or to keep useful information in file path.
        :type include_path: bool
        :param partition_format: Specify the partition format of path. Defaults to None.
            The partition information of each path will be extracted into columns based on the specified format.
            Format part '{column_name}' creates string column, and '{column_name:yyyy/MM/dd/HH/mm/ss}' creates
            datetime column, where 'yyyy', 'MM', 'dd', 'HH', 'mm' and 'ss' are used to extract year, month, day,
            hour, minute and second for the datetime type. The format should start from the position of first
            partition key until the end of file path.
            For example, given the path '../USA/2019/01/01/data.parquet' where the partition is by country/region and
            time, partition_format='/{CountryOrRegion}/{PartitionDate:yyyy/MM/dd}/data.csv' creates a string column
            'CountryOrRegion' with the value 'USA' and a datetime column 'PartitionDate' with the value '2019-01-01'.
        :type partition_format: str
        :param file_extension: The file extension of the files to read. Only files with this extension will be read
            from the directory. Default value is '.parquet'. If this is set to None, all files will be read regardless
            their extension (or lack of extension).
        :type file_extension: str
        :return: Returns an intermediate data that will be a tabular dataset.
        :rtype: azureml.pipeline.core.pipeline_output_dataset.PipelineOutputTabularDataset
        """
        dprep = dataprep()
        dataflow = dprep.Dataflow(self._engine_api)

        if file_extension is not None and len(file_extension) > 0:
            if file_extension[0] != '.':
                file_extension = '.' + file_extension
            dataflow = dataflow.filter(
                dprep.api.functions.get_stream_name(dataflow['Path']).ends_with(file_extension)
            )

        dataflow = dataflow.read_parquet_file()
        if partition_format:
            dataflow = handle_partition_format(dataflow, partition_format)
        dataflow = PipelineOutputFileDataset._handle_path(dataflow, include_path)
        return PipelineOutputTabularDataset(self, dataflow)

    @staticmethod
    def _handle_path(dataflow, include_path):
        if not include_path:
            return dataflow.drop_columns('Path')
        return dataflow

    @property
    def _engine_api(self):
        return dataprep().api.engineapi.api.get_engine_api()

    def _set_mode(self, mode, path_on_compute):
        other = self._clone()
        other._input_mode = mode
        other._input_path_on_compute = path_on_compute
        return other


class PipelineOutputTabularDataset(PipelineOutputAbstractDataset):
    """
    Represent intermediate pipeline data promoted to an Azure Machine Learning Tabular Dataset.

    Once an intermediate data is promoted to an Azure Machine Learning Dataset, it will also be consumed as a Dataset
    instead of a DataReference in subsequent steps.

    :param pipeline_output_dataset: The file dataset that represents the intermediate output which will be transformed
        to a tabular Dataset.
    :type pipeline_output_dataset: azureml.pipeline.core.pipeline_output_dataset.PipelineOutputFileDataset
    :param additional_transformations: Additional transformations that will be applied on top of the file dataset.
    :type additional_transformations: azureml.dataprep.Dataflow
    """

    def __init__(self, pipeline_output_dataset, additional_transformations):
        """
        Create an intermediate data that will be promoted to an Azure Machine Learning Dataset.

        :param pipeline_output_dataset: The file dataset that represents the intermediate output which will be
            transformed to a tabular Dataset.
        :type pipeline_output_dataset: azureml.pipeline.core.pipeline_output_dataset.PipelineOutputFileDataset
        :param additional_transformations: Additional transformations that will be applied on top of the file dataset.
        :type additional_transformations: azureml.dataprep.Dataflow
        """
        if not additional_transformations:
            raise ValueError('Argument additional_transformation cannot be empty or None')

        self._pipeline_output_dataset = pipeline_output_dataset
        self._additional_transformations = additional_transformations

        super(PipelineOutputTabularDataset, self).__init__(pipeline_data=self._pipeline_output_dataset._pipeline_data)

        self._input_mode = "direct"

    def keep_columns(self, columns):
        """Keep the specified columns and drops all others from the dataset.

        :param columns: The name or a list of names for the columns to keep.
        :type columns: str or builtin.list[str]
        :return: Returns a new intermediate data with only the specified columns kept.
        :rtype: azureml.pipeline.core.pipeline_output_dataset.PipelineOutputTabularDataset
        """
        dataflow = self._additional_transformations.keep_columns(columns)
        return PipelineOutputTabularDataset(self._pipeline_output_dataset, dataflow)

    def drop_columns(self, columns):
        """Drop the specified columns from the dataset.

        :param columns: The name or a list of names for the columns to drop.
        :type columns: str or builtin.list[str]
        :return: Returns a new intermediate data with only the specified columns dropped.
        :rtype: azureml.pipeline.core.pipeline_output_dataset.PipelineOutputTabularDataset
        """
        dataflow = self._additional_transformations.drop_columns(columns)
        return PipelineOutputTabularDataset(self._pipeline_output_dataset, dataflow)

    def random_split(self, percentage, seed=None):
        """Split records in the dataset into two parts randomly and approximately by the percentage specified.

        :param percentage: The approximate percentage to split the dataset by. This must be a number between
            0.0 and 1.0.
        :type percentage: float
        :param seed: Optional seed to use for the random generator.
        :type seed: int
        :return: Returns a tuple of new TabularDataset objects representing the two datasets after the split.
        :rtype: (azureml.data.TabularDataset, azureml.data.TabularDataset)
        """
        dataflow1, dataflow2 = self._additional_transformations.random_split(percentage, seed)
        return PipelineOutputTabularDataset(self._pipeline_output_dataset, dataflow1), \
            PipelineOutputTabularDataset(self._pipeline_output_dataset, dataflow2)

    def create_input_binding(self):
        """
        Create an input binding.

        :return: The InputPortBinding with this PipelineData as the source.
        :rtype: azureml.pipeline.core.graph.InputPortBinding
        """
        from azureml.pipeline.core import InputPortBinding

        if self._input_mode != "direct":
            raise RuntimeError("Input mode for Tabular Dataset intermediate data can only be direct.")

        return InputPortBinding(
            name=self.input_name,
            bind_object=self._pipeline_data,
            bind_mode=self._input_mode,
            path_on_compute=self._input_path_on_compute,
            overwrite=False,
            additional_transformations=self._additional_transformations
        )


class DatasetRegistration:
    """
    Describes how the intermediate data in a pipeline should be promoted to an Azure Machine Learning dataset.

    If name is not provided, the dataset will be saved with no name and will not show up when listing all the datasets
    in the workspace.

    :param name: The name to register the dataset under.
    :type name: str
    :param create_new_version: Whether to create a new version of the dataset under the provided name.
    :type create_new_version: bool
    """

    def __init__(self, name, create_new_version):
        """
        Describe how the intermediate data in a pipeline should be promoted to an Azure Machine Learning dataset.

        If name is not provided, the dataset will be saved with no name and will not show up when listing all
        the datasets in the workspace.

        :param name: The name to register the dataset under.
        :type name: str
        :param create_new_version: Whether to create a new version of the dataset under the provided name.
        :type create_new_version: bool
        """
        self._name = name
        self._create_new_version = create_new_version

    @property
    def name(self):
        """
        Get the name to register the dataset to.

        :return: The name to register the dataset to.
        :rtype: str
        """
        return self._name

    @property
    def create_new_version(self):
        """
        Whether to create a new version of the dataset under the same name.

        :return: Whether to create a new version of the dataset under the same name.
        :rtype: bool
        """
        return self._create_new_version
