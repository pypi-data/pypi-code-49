"""This module provide classes and functions for reading/writing DataFrameDirectory."""
import os
import pandas as pd

from azureml.studio.core.data_frame_schema import DataFrameSchema
from azureml.studio.core.utils.jsonutils import dump_to_json_file, load_json_file
from azureml.studio.core.io.data_frame_utils import data_frame_to_parquet, data_frame_from_parquet, data_frame_to_csv
from azureml.studio.core.io.any_directory import AnyDirectory
from azureml.studio.core.io.any_directory import DirectoryLoadError, DirectorySaveError
from azureml.studio.core.io.data_frame_visualizer import DataFrameVisualizer

_SCHEMA_FILE_PATH = 'schema/_schema.json'
_DEFAULT_DATA_PATH = '_data.parquet'
PARQUET_FORMAT = 'Parquet'
CSV_FORMAT = 'CSV'
_DEFAULT_FORMAT = PARQUET_FORMAT


_DUMPERS = {
    PARQUET_FORMAT: data_frame_to_parquet,
    CSV_FORMAT: data_frame_to_csv,
}
_LOADERS = {
    PARQUET_FORMAT: data_frame_from_parquet,
}


class DataFrameDirectory(AnyDirectory):
    """A DataFrameDirectory should store pandas.DataFrame data and related meta data in the directory."""
    TYPE_NAME = 'DataFrameDirectory'

    @classmethod
    def create(cls, data: pd.DataFrame = None, file_path=_DEFAULT_DATA_PATH, file_format=_DEFAULT_FORMAT,
               schema=None, compute_schema_if_not_exist=True,
               compute_visualization=True, compute_stats_in_visualization=False,
               visualizers=None, extensions=None):
        """A DataFrameDirectory is created by a pandas DataFrame, the schema of the DataFrame and other metas.

        :param data: A pandas DataFrame.
        :param file_path: The relative path to store the data.
        :param file_format: The format to dump the data.
        :param schema: The schema is a jsonable dict to describe the detailed info in data.
        :param compute_schema_if_not_exist: Compute schema with data when schema is missing.
        :param compute_visualization: Compute visualization with data and schema when visualizer is missing.
        :param compute_stats_in_visualization: Compute statistics when computing visualization.
        :param visualizers: See AnyDirectory
        :param extensions: See AnyDirectory
        """
        if not schema and compute_schema_if_not_exist and data is not None:
            schema = DataFrameSchema.data_frame_to_dict(data)
        if not visualizers and compute_visualization and data is not None and schema is not None:
            visualizers = [DataFrameVisualizer(data, schema, compute_stats=compute_stats_in_visualization)]
        meta = cls.create_meta(visualizers, extensions)
        meta['format'] = file_format
        meta['data'] = file_path
        if schema:
            meta['schema'] = _SCHEMA_FILE_PATH
        return cls(meta, data=data, schema_data=schema, visualizers=visualizers)

    def dump(self, save_to, meta_file_path=None, overwrite_if_exist=True, validate_if_exist=False):
        """Dump the DataFrame to the directory and and store the yaml file for meta.

        :param save_to: See AnyDirectory
        :param meta_file_path: See AnyDirectory
        :param overwrite_if_exist: If overwrite_if_exist, overwrite the data if the file already exists.
        :param validate_if_exist: If validate_if_exist, make sure the exist file at file_path is a valid DataFrame.
        """

        full_path = self.full_data_path(save_to)
        if overwrite_if_exist or not os.path.exists(full_path):
            DataFrameDirectory.dump_data(self.data, full_path, self.format)
        elif validate_if_exist:
            # When the file doesn't exist,
            # if validate_if_exist, try loading data to guarantee the directory is valid,
            DataFrameDirectory.load_data(full_path, self.format)
            # otherwise we trust that the file is a valid DataFrame file.

        if self.schema:
            dump_to_json_file(self.schema_data, os.path.join(save_to, self.schema))

        super().dump(save_to, meta_file_path=meta_file_path)

    def full_data_path(self, folder):
        if hasattr(self._meta, 'data'):
            return os.path.join(folder, self._meta.data)
        # For compatibility of the DFD in alghost-core<=0.0.16
        elif hasattr(self._meta, 'file_path'):
            return os.path.join(folder, self._meta.file_path)
        raise ValueError(f"File path is not provided in meta file.")

    def get_column_index(self, col_name):
        return self.data.columns.get_loc(col_name)

    def get_column_type(self, col_key):
        return self.schema_instance.get_column_type(col_key)

    def get_element_type(self, col_key):
        return self.schema_instance.get_element_type(col_key)

    def get_column_name(self, col_index):
        return self.data.columns[col_index]

    @property
    def schema_instance(self):
        # Currently, the attributes are stored in self._attrs, so we use this way to implement lazy computation.
        # This is not a good way to implement, will be changed after the logic of self._attrs is removed.
        # TODO: Change the logic of self._attrs to improve readability.
        if '_schema_instance' not in self._attrs:
            if self.schema_data is not None:
                self._schema_instance = DataFrameSchema.from_dict(self.schema_data)
            elif self.data is not None:
                self._schema_instance = DataFrameSchema.from_data_frame(self.data)
            else:
                raise ValueError("Neither schema nor data is provided, schema_instance cannot be computed.")
        return self._schema_instance

    @staticmethod
    def dump_data(data, full_path, file_format=_DEFAULT_FORMAT):
        """Dump the data to the specified full_path with file_format."""
        dumper = _DUMPERS.get(file_format, None)
        if not dumper:
            raise NotImplementedError(f"The dumper of file format '{file_format}' is not supported now.")
        if not isinstance(data, pd.DataFrame):
            raise TypeError(f"{pd.DataFrame.__name__} is required, got {data.__class__.__name__}")
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        dumper(data, full_path)

    @staticmethod
    def load_data(full_path, file_format=_DEFAULT_FORMAT, schema=None):
        """Load the data with the specified full_path with file_format."""
        loader = _LOADERS.get(file_format, None)
        if not loader:
            raise NotImplementedError(f"The loader of file format {file_format} is not supported now.")
        df = loader(full_path)
        if schema:
            pass  # Todo: Change categorial types
        return df

    @classmethod
    def load(cls, load_from_dir, meta_file_path=None, load_data=True):
        """Load the directory as a DataFrameDirectory.

        :param load_from_dir: See AnyDirectory
        :param meta_file_path: See AnyDirectory
        :param load_data: If load_data=True, the DataFrame and the schema will be loaded to the directory instance.
        :return: See AnyDirectory
        """
        directory = super().load(load_from_dir, meta_file_path)
        if not directory.format:
            raise ValueError(f"File format is not provided in meta file.")

        if not load_data:
            return directory

        if directory.schema:
            directory.schema_data = load_json_file(os.path.join(load_from_dir, directory.schema))
        data = DataFrameDirectory.load_data(
            directory.full_data_path(load_from_dir),
            directory.format,
            directory.schema_data,
        )
        directory.data = data
        return directory


def save_data_frame_to_directory(save_to, data: pd.DataFrame = None,
                                 file_path=_DEFAULT_DATA_PATH,
                                 file_format=_DEFAULT_FORMAT,
                                 schema=None,
                                 compute_schema_if_not_exist=True,
                                 compute_visualization=True,
                                 compute_stats_in_visualization=False,
                                 visualizers=None, extensions=None, meta_file_path=None,
                                 overwrite_if_exist=True, validate_if_exist=False,
                                 ):
    """Save a DataFrame to the specified folder 'save_to' with DataFrameDirectory.dump()."""
    try:
        DataFrameDirectory.create(
            data, file_path, file_format,
            schema, compute_schema_if_not_exist,
            compute_visualization, compute_stats_in_visualization,
            visualizers, extensions,
        ).dump(
            save_to,
            meta_file_path=meta_file_path,
            overwrite_if_exist=overwrite_if_exist,
            validate_if_exist=validate_if_exist,
        )
    except BaseException as e:
        raise DirectorySaveError(dir_name=save_to, original_error=e) from e


def load_data_path_from_directory(load_from_dir, meta_file_path=None):
    """Load a full data path in the specific folder."""
    try:
        return DataFrameDirectory.load(load_from_dir, meta_file_path, load_data=False).full_data_path(load_from_dir)
    except BaseException as e:
        raise DirectoryLoadError(dir_name=load_from_dir, original_error=e) from e


def load_data_frame_from_directory(load_from_dir, meta_file_path=None):
    """Load a DataFrame in the specified folder 'load_from_dir' with DataFrameDirectory.load()."""
    try:
        return DataFrameDirectory.load(load_from_dir, meta_file_path=meta_file_path)
    except BaseException as e:
        raise DirectoryLoadError(dir_name=load_from_dir, original_error=e) from e
