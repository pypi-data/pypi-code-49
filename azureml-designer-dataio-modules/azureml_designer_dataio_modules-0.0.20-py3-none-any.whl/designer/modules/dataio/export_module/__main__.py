import re

from azureml.core import Datastore
from azureml.dataprep.api.dataflow import Dataflow
from azureml.studio.core.error import UserError
from azureml.studio.core.io.any_directory import DirectoryIOError
from azureml.studio.core.logger import logger, time_profile
from azureml.studio.core.io.data_frame_directory import DataFrameDirectory
from azureml.data.datapath import DataPath
from azureml.dataprep import read_pandas_dataframe
from pandas import DataFrame
from ..common.workspaceutil import get_workspace, get_time_as_string
from azureml.studio.internal.error import ErrorMapping, \
    UnsupportedOutputTypeError, TimeoutOccuredError, IncorrectAzureMLDatastoreError, ParameterParsingError, \
    InvalidDatasetError
from azureml.studio.internal.error_handler import error_handler
from azureml.dataprep import ColumnSelector
from azureml.dataprep.api.step import column_selection_to_selector_value
import argparse
import os
import azureml.core

logger.debug(f'Executing {os.path.abspath(__file__)}')
logger.debug(f"Azure ML SDK Version: {azureml.core.VERSION}")
logger.debug(f"DataPrep Version: {azureml.dataprep.__version__}")
logger.debug(
    f"azureml.designer.modules.dataio Version: {azureml.designer.modules.dataio.__version__}")


def check_url_format(url_str):
    """Check if input string is a url"""
    result = re.search('^(abfss|adl|https?)://.*$', url_str)
    return True if result else False


class ExportTabularDataModule:
    @classmethod
    def __init__(cls, input_dict):
        cls.output_datastore = input_dict['Output_data_store']
        cls.output_path = input_dict['Output_path']
        cls.file_type = input_dict['Output_file_type']
        cls.workspace = get_workspace()

    @classmethod
    @time_profile
    def write_to_csv(
            cls,
            data_flow,
            directory_path,
            separator=',',
            na='NA',
            error='ERROR',
            single_file=True) -> Dataflow:
        """
        Create a dataflow sequence for exporting as csv. It is almost a copy of Datafow.write_to_csv
        except adding singleFile parameter to it
        """
        from azureml.dataprep.api._datastore_helper import get_datastore_value
        logger.debug(
            f'Export as csv (datastore: {directory_path.datastore_name}; path: '
            f'{directory_path.path_on_datastore})')

        data_flow = data_flow.add_step('Microsoft.DPrep.WriteCsvToDatastoreBlock', {
            'datastore': get_datastore_value(directory_path)[1]._to_pod(),
            'separator': separator,
            'singleFile': single_file,
            'na': na,
            'error': error
        })
        return data_flow

    @classmethod
    # @ErrorHandler('./error_folder')
    @error_handler
    @time_profile
    def run(cls, input_port_dfd: DataFrameDirectory,
            input_dict: dict = None) -> None:
        """
        Export data to various datastore (blob, adls gen1 or adls gen2), dprep will handle the detail
        1. generate exporting dataflow sequence
        2. create output_path
        3. execute dataflow for exporter
        """
        try:
            null_keys = [key for key, value in input_dict.items()
                         if key in ['Output_data_store', 'Output_path', 'Output_file_type'] and value is None]
            if len(null_keys) > 0:
                ErrorMapping.throw(ParameterParsingError(arg_name_or_column=', '.join(null_keys)))
            cls.output_datastore = input_dict['Output_data_store']
            cls.output_path = input_dict['Output_path']
            cls.file_type = input_dict['Output_file_type']
            if cls.output_path.endswith('/') or cls.output_path.endswith('.') or check_url_format(cls.output_path):
                ErrorMapping.throw(ParameterParsingError(arg_name_or_column='Output_path'))

            if isinstance(input_port_dfd, DataFrameDirectory):
                data_frame = input_port_dfd.data
                logger.info(f"Input port is DFD type: {input_port_dfd}.")
            elif isinstance(input_port_dfd, DataFrame):
                data_frame = input_port_dfd
                logger.info(f"Input port is pandas data frame type.")
            else:
                logger.error(f"Unsupported input_port_dfd type.")
                raise NotImplementedError(
                    'Not support non-DataFrameDirectory or non-DataFrame type.')

            # check if a pandas DataFrame is empty first
            if len(data_frame.index) == 0 or len(data_frame.columns) == 0:
                ErrorMapping.throw(InvalidDatasetError())

            data_flow = read_pandas_dataframe(df=data_frame, in_memory=True)
            # drop all __index_level_* columns
            data_flow = data_flow.add_step(
                'Microsoft.DPrep.DropColumnsBlock', {
                    'columns': column_selection_to_selector_value(
                        ColumnSelector(
                            '__index_level_*', True, True))})

            data_store = Datastore.get(cls.workspace, cls.output_datastore)
            data_path = DataPath(data_store, cls.output_path)

            file_format = cls.file_type.lower()
            if file_format == 'csv':
                data_flow = cls.write_to_csv(
                    data_flow, data_path, single_file=True)
            elif file_format == 'tsv':
                data_flow = cls.write_to_csv(
                    data_flow, data_path, separator='\t', single_file=True)
            elif file_format == 'parquet':
                logger.debug(f"parquet file dtypes:\n{data_flow.dtypes}")
                data_flow = data_flow.write_to_parquet(
                    data_path, single_file=True)
            else:
                ErrorMapping.throw(UnsupportedOutputTypeError())

            logger.debug(f'Data flow:\n{data_flow.to_json()}')
            data_flow.run_local()
            logger.info(f"{get_time_as_string()} Export data is done.")
        except Exception as azureml_dataset_error:
            error_message = str(azureml_dataset_error)
            if 'Could not find datastore' in error_message:
                ErrorMapping.rethrow(azureml_dataset_error,
                                     IncorrectAzureMLDatastoreError(datastore_name=cls.output_datastore,
                                                                    workspace_name=cls.workspace))
            elif 'Access to Datastore denied with error response Forbidden' in error_message:
                ErrorMapping.rethrow(azureml_dataset_error,
                                     UserError('Please check datastore access permission.'))
            elif 'Cannot create file' in error_message:
                ErrorMapping.rethrow(azureml_dataset_error,
                                     UserError('Please check information for the file to be created.'))
            elif 'Cannot create folder/filesystem' in error_message:
                ErrorMapping.rethrow(azureml_dataset_error,
                                     UserError('Please check information for the folder/filesystem to be created.'))
            else:
                raise azureml_dataset_error


@time_profile
def main(args):
    """Initialize an export tabular data module and export data to the specified data store and data path"""
    logger.debug(f'Received argument --input_path: {args.input_path}.')
    logger.debug(
        f'Received argument --output_datastore: {args.output_datastore}.')
    logger.debug(f'Received argument --output_path: {args.output_path}.')
    logger.debug(f'Received argument --file_type: {args.file_type}.')

    input_dict = {
        'Output_data_store': args.output_datastore,
        'Output_path': args.output_path,
        'Output_file_type': args.file_type}

    export_tabular_module = ExportTabularDataModule(input_dict)

    try:
        input_data_frame_directory = DataFrameDirectory.load(args.input_path)
    except DirectoryIOError as dfd_error:
        ErrorMapping.rethrow(dfd_error, TimeoutOccuredError())

    logger.info(f"Get input data frame directory {input_data_frame_directory}")
    export_tabular_module.run(input_data_frame_directory, input_dict)


def configs(parser):
    parser.add_argument(
        "--input_path",
        type=str,
        help="Input port or path that data can be accessed")
    parser.add_argument(
        "--output_datastore",
        type=str,
        help="Output datastore name")
    parser.add_argument(
        "--output_path",
        type=str,
        help="The path that data to be exported")
    parser.add_argument(
        "--file_type",
        type=str,
        help="The file type to be exported")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    configs(parser)
    args, unknown = parser.parse_known_args()

    main(args)
