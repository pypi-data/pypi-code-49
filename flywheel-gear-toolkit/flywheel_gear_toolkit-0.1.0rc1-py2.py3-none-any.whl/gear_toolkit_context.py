"""Provides gear helper functions"""
import argparse
import copy
import json
import logging
import os
import pathlib
import tempfile
import sys

import flywheel

from gear_toolkit.constants import FILE_OBJECT_DICT
from gear_toolkit.logging.templated import configure_logging


def convert_config_type(input_str):
    """
    Converts strings in the format <value>:<type> (i.e. '4:integer') to a type consistent with the string preceded by
        the last `:`

    Args:
        input_str (str): a string in <value>:<type> format

    Raises:
        ValueError: if input_str is not a string or the type is not recognized

    Returns:
        a value consistent with the type specified

    """
    if not isinstance(input_str, str):
        raise ValueError(f'input_str {input_str} is not str')

    if ':' not in input_str:
        input_str = input_str + ':'

    input_str, type_str = input_str.rsplit(':', maxsplit=1)

    type_str = type_str.lower()

    if type_str in ['boolean', 'bool'] and input_str.lower() == 'true':
        output = True

    elif type_str in ['boolean', 'bool'] and input_str.lower() == 'false':
        output = False

    elif type_str in ['boolean', 'bool'] and input_str.lower() not in ['false', 'true']:
        raise ValueError(f'Cannot convert {input_str} to a boolean')

    elif type_str in ['str', '', 'string']:
        output = input_str

    elif type_str == 'number':
        if '.' in input_str:
            output = float(input_str)
        else:
            output = int(input_str)

    elif type_str == 'float':

        output = float(input_str)

    elif type_str in ['integer', 'int']:
        output = int(input_str)

    else:
        raise ValueError(f'Unrecognized type_str: {type_str}')

    return output


def parse_context_args(input_args=None):
    """Parses sys.argv (or input args if provided).

    Argument names that are not prefixed with ``--`` or ``-`` will be ignored. Destination can be specified with
        -d <destination_id>:<destination_type> at the command line or as ``input_args`` as
        ``['-d', '<destination_id>:<destination_type>']``

    Args:
      input_args(list, optional): an optional list of arguments to provide to argparse. If not provided,
            sys.argv will be used instead. (Default value = None)

    Returns:
      argparse.Namespace: parsed arguments

    """

    if not isinstance(input_args, list):
        input_args = sys.argv
    else:
        # coerce to strings if they were passed as an argument
        input_args = [str(item) for item in input_args]

    # fromfile_prefix_chars allows parsing of file containing newline-delimited arguments with @<path to file>
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
    parser.add_argument('--destination', '-d', help='<fw container id>:<fw container type>', default='aex:acquisition')
    parser.add_argument('--api-key', '-key', help='Flywheel API key', default='')
    _, unknown = parser.parse_known_args(input_args)
    # allows arbitrary arguments to be passed, such as config and file inputs
    for arg in unknown:
        if arg.startswith(("-", "--")):
            # you can pass any arguments to add_argument
            parser.add_argument(arg)
    args, unknown = parser.parse_known_args(input_args)
    return args


class GearToolkitContext:
    """Provides helper functions for gear development, namely for accessing the gear's `config.json` and `manifest.json`

    Args:
        gear_path (str, optional): a path to use, default behavior will use the current working directory
            (`os.getcwd()`)
        manifest_path (str, optional): a path to the gear's manifest.json file, defaults to
            `self.path/'manifest.json'`
        config_path (str, optional): a path to the gear's config.json file, defaults to
            `self._path/'config.json'`
        input_args (list, optional): list of arguments to parse to generate a `config.json` file. If not provided,
            `sys.argv` will be parsed instead.
        tempdir (bool, optional): whether to use tempfile.TemporaryDirectory() for `_path`, defaults to False. Useful
            for testing.

    Attributes:
        _path (pathlib.Path): the result of `pathlib.Path(gear_path or os.getcwd()).resolve()`
        _client (flywheel.Client): an instance of the Flywheel client if a valid API key was provided or a user is
            currently logged into the Flywheel CLI
        _metadata (dict): dictionary that stores updates to be dumped to `.metadata.json`
        _temp_dir (tempfile.TemporaryDirectory): None unless initialized with `tempdir=True`
        log (logging.Logger): a log initialized with logging.getLogger(__name__)
        manifest (dict): dictionary representation of `manifest.json`
        config_json (dict): dictionary representation of `config.json`

    """

    def __init__(self, gear_path=None, manifest_path=None, config_path=None, input_args=None, tempdir=False):
        self._temp_dir = None
        if tempdir:
            self._temp_dir = tempfile.TemporaryDirectory()
            gear_path = self._temp_dir.name

        self._path = pathlib.Path(gear_path or os.getcwd()).resolve()
        self._client = None
        self._out_dir = None
        self._work_dir = None
        self._metadata = {}
        self.log = logging.getLogger(__name__)
        self.manifest = self._load_json(manifest_path or self._path / 'manifest.json')
        self.config_json = self._load_json(config_path or self._path / 'config.json')
        self.config_from_args(input_args=input_args)

    def init_logging(self, default_config_name=None, update_config=None):
        """Configures logging via `gear_toolkit.logging.templated.configure_logging`.

        If no `default_config_name` is provided, will get `debug_gear` from the configuration options. If `debug_gear`
            is False or not defined in the gear configuration options, `default_config_name` will be set to info.

        If `update_config` is not provided, manifest['custom']['log_config'] will be used (if defined in the manifest)

        Args:
            default_config_name (str, optional): A string, 'info' or 'debug', indicating the default template to use.
                Defaults to 'info'.
            update_config (dict, optional): A dictionary containing the keys, subkeys, and values of the templates to
                update. Defaults to None.
        """
        if not default_config_name:
            if self.config.get('debug_gear'):
                default_config_name = 'debug'
            else:
                default_config_name = 'info'
        if not update_config:
            if self.manifest:
                if isinstance(self.manifest.get('custom'), dict):
                    update_config = self.manifest['custom'].get('log_config', None)

        configure_logging(default_config_name=default_config_name, update_config=update_config)
        return default_config_name, update_config

    @property
    def config(self):
        """Get the config dictionary from config.json.

        Returns:
          dict: The configuration dictionary.

        """
        return self.config_json['config']

    @property
    def destination(self):
        """Get the destination reference.

        Returns:
          dict: The destination dictionary.

        """
        return self.config_json['destination']

    @property
    def work_dir(self):
        """Get the absolute path to a work directory

        Returns:
          pathlib.Path: The absolute path to work.

        """
        if self._work_dir is None:
            self._work_dir = self._path / 'work'
            if not self._work_dir.exists():
                self._work_dir.mkdir(parents=True)
        return self._work_dir

    @property
    def output_dir(self):
        """Get the absolute path to the output directory.

        Returns:
          pathlib.Path: The absolute path to outputs.

        """
        if self._out_dir is None:
            self._out_dir = self._path / 'output'
            if not self._out_dir.exists():
                self._out_dir.mkdir(parents=True)
        return self._out_dir

    @property
    def client(self):
        """Get the SDK client, if an api key input exists or CLI client exists.

        Returns:
          Client: The SDK client

        """
        if self._client is None:
            api_key = None
            for inp in self.config_json['inputs'].values():
                if inp['base'] == 'api-key' and inp['key']:
                    api_key = inp['key']
                    try:
                        self._client = flywheel.Client(api_key)
                    except Exception as exc:  # pylint: disable=broad-except
                        self.log.error('An exception was raised when initializing client: %s', exc, exc_info=True)
                        self._client = None
            if api_key is None:
                try:
                    self._client = flywheel.Client()
                except Exception as exc:  # pylint: disable=broad-except
                    self.log.error(
                        'No api_key was provided and exception was raised when attempting to log in via CLI %s',
                        exc,
                        exc_info=True
                    )
                    self._client = None

        return self._client

    def log_config(self):
        """Print the configuration and input files to the logger"""
        # Log destination
        self.log.info('Destination is %s=%s', self.destination.get('type'), self.destination.get('id'))

        # Log file inputs
        for inp_name, inp in self.config_json['inputs'].items():
            if inp['base'] != 'file':
                continue

            container_type = inp.get('hierarchy', {}).get('type')
            container_id = inp.get('hierarchy', {}).get('id')
            file_name = inp.get('location', {}).get('name')

            self.log.info('Input file "%s" is %s from %s=%s', inp_name, file_name,
                          container_type, container_id)

        # Log configuration values
        for key, value in self.config.items():
            self.log.info('Config "%s=%s"', key, value)

    def get_input(self, name):
        """Get the input for name.

        Args:
          name (str): The name of the input
        Returns:
          dict: The input dictionary, or None if not found.

        """
        return self.config_json['inputs'].get(name)

    def get_input_path(self, name):
        """Get the full path to the given input file.

        Args:
          name (str): The name of the input

        Raises:
          ValueError: if the input exists, but is not a file.

        Returns:
          str: The path to the input file if it exists, otherwise None

        """
        inp = self.get_input(name)
        if inp is None:

            return None
        if inp['base'] != 'file':
            raise ValueError(f'The specified input {name} is not a file')
        return inp['location']['path']

    def open_input(self, name, mode='r', **kwargs):
        """Open the named input file.

        Args:
          name (str): The name of the input
          mode (str): The open mode (Default value = 'r')
          **kwargs: keyword arguments for `open`

        Raises:
             ValueError: if input ``name`` is not defined in config_json.
             FileNotFoundError: if the path in the config_json for input ``name`` is not a file
        Returns:
          file: The file object

        """
        path = self.get_input_path(name)
        if path is None:
            raise ValueError(f'Input {name} is not defined in the config.json')
        if not os.path.isfile(path):
            raise FileNotFoundError(f'Input {name} does not exist at {path}')
        return open(path, mode, **kwargs)

    def open_output(self, name, mode='w', **kwargs):
        """Open the named output file.

        Args:
          name (str): The name of the output
          mode (str): The open mode (Default value = 'w')
          **kwargs: keyword arguments for `open`

        Returns:
          file: The file object

        """
        path = self.output_dir / name
        return path.open(mode, **kwargs)

    def get_context_value(self, name):
        """Get the context input for name.

        Args:
          name (str): The name of the input

        Returns:
          dict: The input context value, or None if not found.

        """
        inp = self.get_input(name)
        if not inp:
            return None
        if inp['base'] != 'context':
            raise ValueError(f'The specified input {name} is not a context input')
        return inp.get('value')

    def update_container_metadata(self, container_type, *args, **kwargs):
        """Update metadata for the given container name in the hierarchy.

        Dictionaries and/or a set of key=value args can be passed to this function.

        The metadata will be written when write_metadata() is called, or if
            using this as a context manager, when the context is exited.

        Args:
            container_type (str): The container type (e.g. session or acquisition)
            *args: arbitrary dictionaries
            **kwargs: arbitrary keyword arguments

        Note:
            \\*args must be of type dictionary and if these dictionaries share keys, then a warning will be logged and
                only the first instance of the key will be used to update the resulting dictionary

        Return:
            dict: the update dictionary

        """
        update = self._create_update_dict(*args, **kwargs)
        self._update_metadata(container_type, update)
        return update

    def update_file_metadata(self, file_name, *args, **kwargs):
        """Update metadata for the given file on the destination.

        Dictionaries and/or a set of key=value args can be passed to this function.

        The metadata will be written when write_metadata() is called, or
        if using this as a context manager, when the context is exited.

        Args:
            file_name (str): The name of the file
            *args: arbitrary dictionaries
            **kwargs: arbitrary keyword arguments

        Note:
            \\*args must be of type dictionary and if these dictionaries share keys, then a warning will be logged and
                only the first instance of the key will be used to update the resulting dictionary. \\**kwargs has
                precedence over \\*args

        Return:
            dict: the update dictionary

        """
        container_type = self.destination['type']
        update = self._create_update_dict(*args, **kwargs)
        self._update_metadata(container_type, update, file_name=file_name)
        return update

    def update_destination_metadata(self, *args, **kwargs):
        """Update metadata for the destination container.

        Dictionaries and/or a set of key=value args can be passed to this function.

        The metadata will be written when write_metadata() is called, or
        if using this as a context manager, when the context is exited.

        Args:
            *args: arbitrary dictionaries
            **kwargs: arbitrary keyword arguments

        Note:
            \\*args must be of type dictionary and if these dictionaries share keys, then a warning will be logged and
                only the first instance of the key will be used to update the resulting dictionary. \\**kwargs has
                precedence over \\*args

        Return:
            dict: the update dictionary
        """
        container_type = self.destination['type']
        update = self._create_update_dict(*args, **kwargs)
        self._update_metadata(container_type, update)
        return update

    def write_metadata(self):
        """Write the metadata json file to the output folder"""
        if not self._metadata:
            return

        with self.open_output('.metadata.json') as f:
            json.dump(self._metadata, f, indent=2)

    def download_session_bids(self, target_dir=None, **kwargs):
        """Download the session in bids format to target_dir.

        Args:
          target_dir (str): The destination directory (otherwise work/bids will be used)
            (Default value = 'work/bids')
          **src_data (bool):  Whether or not to include src data (e.g. dicoms) (Default value = False)
          **folders (list):  The list of folders to include (otherwise all folders) e.g. ['anat', 'func']
            (Default value = None)
          **kwargs: kwargs for ``flywheel_bids.export_bids.download_bids_dir``

        Returns:
          pathlib.Path: The absolute path to the downloaded bids directory

        """
        parent_id, target_dir, download_bids_dir, kwargs = self._validate_bids_download(
            container_type='session', target_dir=target_dir, **kwargs
        )
        download_bids_dir(self.client, parent_id, 'session', target_dir, **kwargs)
        return target_dir

    def download_project_bids(self, target_dir=None, **kwargs):
        """Download the project in bids format to target_dir.

        Args:
          target_dir(str): The destination directory (otherwise work/bids will be used)(Default value = 'work/bids')
          **src_data(bool): Whether or not to include src data (e.g. dicoms)(Default value = False)
          **subjects(list): The list of subjects to include (via subject code) otherwise all subjects
          **sessions(list): The list of sessions to include (via session label) otherwise all sessions
          **folders(list): The list of folders to include (otherwise all folders) e.g. ['anat', 'func']
          **kwargs: kwargs for ``flywheel_bids.export_bids.download_bids_dir``

        Returns:
          pathlib.Path: The absolute path to the downloaded bids directory

        """
        parent_id, target_dir, download_bids_dir, kwargs = self._validate_bids_download(
            container_type='project', target_dir=target_dir, **kwargs
        )
        download_bids_dir(self.client, parent_id, 'project', target_dir, **kwargs)
        return target_dir

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.write_metadata()
        if self._temp_dir:
            self._temp_dir.cleanup()

    def _validate_bids_download(self, container_type, target_dir, **kwargs):
        """Prepare and validate `flywheel_bids.export_bids.download_bids_dir` arguments

        Args:
          container_type (str): the container type for which to download BIDs (i.e. "session", "project")
          target_dir (pathlib.Path or str or None): the path to which to download the BIDs hierarchy
          kwargs: kwargs for ``flywheel_bids.export_bids.download_bids_dir``
        Returns:
            (tuple): tuple containing:
                parent_id (str): id of the destinations container's parent of type `container_type`
                target_dir (pathlib.Path): path to which BIDS will be downloaded
                download_bids_dir (function): flywheel_bids.export_bids.download_bids_dir
                kwargs (dict): keyword arguments to be passed to download_bids_dir
        """
        # Raise a specific error if BIDS not installed
        download_bids_dir = self._load_download_bids()

        if not target_dir:
            target_dir = self.work_dir / 'bids'
        elif isinstance(target_dir, pathlib.Path):
            pass
        elif isinstance(target_dir, str):
            target_dir = pathlib.Path(target_dir)
        else:
            raise TypeError(f'BIDs target_dir {target_dir} is of unexpected type ({type(target_dir)})')
        # create target_dir if it doesn't exist
        if not target_dir.exists():
            target_dir.mkdir(parents=True)

        # Cleanup kwargs
        for key in ('subjects', 'sessions', 'folders'):
            if key in kwargs and kwargs[key] is None:
                kwargs.pop(key)

        # Resolve container type from parents
        dest_container = self.client.get(self.destination['id'])

        parent_id = dest_container.get(container_type)
        if parent_id is None:
            parent_id = dest_container.get('parents', {}).get(container_type)

        if parent_id is None:
            raise RuntimeError('Cannot find {} from destination'.format(container_type))

        self.log.info('Using source container: %s=%s', container_type, parent_id)

        return parent_id, target_dir, download_bids_dir, kwargs

    def _load_download_bids(self):
        """Load the download_bids_dir function from flywheel_bids"""
        try:
            from flywheel_bids.export_bids import download_bids_dir   # pylint: disable=import-outside-toplevel
            return download_bids_dir
        except ImportError:
            self.log.error('Cannot load flywheel-bids package.')
            self.log.error('Make sure it is installed with "pip install flywheel-bids"')
            raise RuntimeError('Unable to load flywheel-bids package, make sure it is installed!')

    def _update_metadata(self, container_type, metadata, file_name=None):
        """

        Args:
          container_type (str): the container type that needs updating (i.e. "session", "project")
          metadata (dict):
          file_name (str):  (Default value = None)


        """
        dest = self._metadata.setdefault(container_type, {})
        if file_name:
            files = dest.setdefault('files', [])
            file_entry = None
            for fe in files:
                if fe.get('name') == file_name:
                    file_entry = fe
                    break
            if file_entry is None:
                file_entry = {'name': file_name}
                files.append(file_entry)
            dest = file_entry

        dest.update(metadata)

    def _create_update_dict(self, *args, **kwargs):
        """
        Creates dictionary from **kwargs which is updated with *args. If keys are shared between any args* dicts, a
            warning is logged and only the first arg update is applied.
        Args:
            *args: arbitrary dictionaries
            **kwargs: arbitrary keyword arguments
        Raises:
            TypeError: if any arg in *args is not a dictionary
        Returns:
            dict: a dictionary representation of ``**kwargs`` updated by ``*args``
        """
        result = copy.deepcopy(kwargs) or {}
        arg_keys = list(kwargs.keys())
        for arg in args:
            if not isinstance(arg, dict):
                raise TypeError(f'*args must be of type dict, got {type(arg)} for {arg}')
            for key in list(arg.keys()):
                if key in arg_keys:
                    self.log.warning('%s has already been provided in result %s', key, result)
                    arg.pop(key)
                else:
                    arg_keys.append(key)
            result.update(arg)
        return result

    @staticmethod
    def _load_json(filepath):
        """

        Args:
          filepath (str): path to a JSON file

        Returns:
            (dict): the dictionary representation of the JSON file at filepath
        """
        json_dict = dict()
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'r') as f:
                    json_dict = json.load(f)
            except json.JSONDecodeError:
                raise RuntimeError(f'Cannot parse {filepath} as JSON.')

        return json_dict

    def config_from_args(self, input_args=None):
        """ Updates config_json dictionary using input_args (or sys.argv if input_args are not provided)

        If config.json exists at the path provided when the GearTookitContext was instantiated, sys.argv (or input_args
            if provided) will be used to update the config options and inputs.

        Inputs are discerned on the basis that ``os.path.isfile(<config value or input path>)`` evaluates as
            ``True``.

        If no config.json exists, a config_json object will be created with the following as the default (and
            updated where config/inputs are provided):
            `{'config': {}, 'inputs': {}, 'destination': {'id': 'aex', 'type': 'acquisition'}}`

        Args:
            input_args(list, optional): an optional list of arguments to provide to argparse. If not provided,
                sys.argv will be used instead. (Default value = None)

        Returns:
            dict: a dictionary representation of a Flywheel gear's config.json

        Examples:

            .. code-block:: python

                gt_context = GearToolkitContext()
                gt_context.config_from_args([])
                > {'config': {}, 'inputs': {}, 'destination': {'id': 'aex', 'type': 'acquisition'}}
                gt_context.config_from_args(input_args=['-d', '5e0612a6f999360027e1aa9d:project'])
                > {'config': {}, 'inputs': {}, 'destination': {'id': '5e0612a6f999360027e1aa9d', 'type': 'project'}}
                gt_context.config_from_args(input_args=['-config_key1', 'config_value1'])
                > {'config': {'config_key1': 'config_value1'}, 'inputs': {}, 'destination': {
                    'id': '5e0612a6f999360027e1aa9d', 'type': 'project'}}
                gt_context.config_from_args(['-file_input1', '/path/to/file_input_1'])
                > {'config': {
                        'config_key1': 'config_value1'},
                   'inputs': {
                        'file_input1': {
                            'base': 'file',
                            'hierarchy': {'acquisition', 'aex'},
                            'location': {'name': 'parse_args1.txt', 'path': '/path/to/file_input_1'},
                            'object': {
                                'classification': {'Intent': [], 'Measurement': []},
                                'info': {},
                                'measurements': [],
                                'mimetype': '',
                                'modality': '',
                                'size': <file size>,
                                'tags': [],
                                'type': ''
                            }
                        }},
                    'destination': {'id': '5e0612a6f999360027e1aa9d', 'type': 'project'}}

        """
        args = parse_context_args(input_args=input_args)
        arg_dict = args.__dict__
        destination = arg_dict.pop('destination')
        if not self.config_json:
            config_dict = {
                'config': {},
                'inputs': {}
            }
        else:
            config_dict = self.config_json

        if not config_dict.get('destination') or destination != 'aex:acquisition':
            config_dict['destination'] = dict(zip(['id', 'type'], destination.split(':')))
        api_key = arg_dict.pop('api_key')
        if api_key:
            config_dict['inputs']['api-key'] = {'base': 'api-key', 'key': api_key}

        for key, value in arg_dict.items():
            if os.path.isfile(str(value)):
                if not config_dict['inputs'].get(key):
                    config_dict['inputs'][key] = {
                        'base': 'file',
                        'hierarchy': {'aex', 'acquisition'},
                        'location': {
                            'name': os.path.basename(value),
                            'path': value
                        },
                        'object': FILE_OBJECT_DICT
                    }
                    config_dict['inputs'][key]['object']['size'] = os.stat(value).st_size
            else:
                if not config_dict['config'].get(key):
                    config_dict['config'][key] = convert_config_type(value)

        self.config_json = config_dict
        return self.config_json
