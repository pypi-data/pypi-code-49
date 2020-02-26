"""Individual file/packfile profile for de-identification"""

import fnmatch
import re
import os
from abc import ABCMeta, abstractmethod
import logging
from dateutil.parser import parse

from .deid_field import DeIdField

log = logging.getLogger(__name__)


class FileProfile:
    # pylint: disable=too-many-public-methods
    """Abstract class that represents a single file/packfile profile"""
    __metaclass__ = ABCMeta

    # NOTE: If you derive from this class, set a unique name for the factory method to use
    name = None
    log_fields = []

    # NOTE: Date/Time formats are from dicom standard, override as necessary
    # http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_6.2.html

    uid_default_prefix_fields = 4
    uid_suffix_fields = 1  # How many suffix fields to keep in uid
    uid_max_suffix_digits = 6  # Maximum number of digits to keep from the suffix (trailing)
    uid_hash_fields = (6, 6, 6, 6, 6, 6)  # The number and length of parts to add to the hash

    hash_digits = 0  # How many digits are supported for 'hash' action
    hash_algorithm = 'sha256'
    date_format = '%Y%m%d'  # YYYYMMDD
    datetime_format = '%Y%m%d%H%M%S.%f'  # YYYYMMDDHHMMSS.FFFFFF&ZZXX
    datetime_has_timezone = True  # Whether or not optional timezone exists

    default_filenames = []
    filename_field_prefix = '_fwmtk'

    def __init__(self, packfile_type=None, file_filter=None):
        """Initialize the file profile"""
        self.packfile_type = packfile_type
        self.file_filter = file_filter
        self.fields = []
        self.field_map = {}
        self.log = None
        self.deid_name = None

        # Action configuration
        self.date_increment = None
        self.hash_salt = None

        self.uid_prefix_fields = self.uid_default_prefix_fields  # How many prefix fields to keep
        self.uid_numeric_name = None  # unique OID registered numeric name used as UID prefix if defined

        self.filenames = self.default_filenames

    def add_field(self, field):
        """Add a field to de-identify"""
        self.fields.append(field)
        self.field_map[field.fieldname] = field

    def set_log(self, log):
        # pylint: disable=redefined-outer-name
        """Set the log instance"""
        self.log = log

    def get_log_fields(self):
        """Return the full set of fieldnames that should be logged"""
        result = list(self.log_fields)
        for field in self.fields:
            result.append(field.fieldname)
        return result

    @classmethod
    def factory(cls, name, config=None, log=None):
        # pylint: disable=redefined-outer-name
        """Create a new file profile instance for the given name.

        Arguments:
            name (str): The name of the profile type
            config (dict): The optional configuration dictionary
            log: The optional de-id log instance
        """
        result = None

        for subclass in cls.__subclasses__():
            if subclass.name == name:
                result = subclass()
                break

        if not result:
            raise ValueError('Unknown file profile: "{}"'.format(name))

        if config is not None:
            result.load_config(config)

        if log is not None:
            result.set_log(log)

        return result

    @classmethod
    def profile_names(cls):
        """Get the list of profile names"""
        result = []
        for subclass in cls.__subclasses__():
            if subclass.name is not None:
                result.append(subclass.name)
        return result

    def to_config(self):
        """Get configuration as a dictionary"""

        result = {
            'fields': [field.to_config() for field in self.fields]
        }

        # Read action configuration
        if self.date_increment is not None:
            result['date-increment'] = self.date_increment

        if self.hash_salt is not None:
            result['salt'] = self.hash_salt

        if self.uid_prefix_fields != self.uid_default_prefix_fields:
            result['uid_prefix_fields'] = self.uid_prefix_fields

        if self.uid_numeric_name is not None:
            result['uid_numeric_name'] = self.uid_numeric_name

        if self.filenames is not self.default_filenames:
            result['filenames'] = self.filenames

        if self.file_filter:
            result['file-filter'] = self.file_filter

        return result

    def load_config(self, config):
        """Read configuration from a dictionary"""
        # Read fields
        for field in config.get('fields', []):
            self.add_field(DeIdField.factory(field))

        # Read file_filter
        self.file_filter = config.get('file-filter', None)

        # Read action configuration
        self.date_increment = config.get('date-increment', None)
        self.hash_salt = config.get('salt', None)
        self.uid_prefix_fields = config.get('uid-prefix-fields', self.uid_default_prefix_fields)
        self.uid_numeric_name = config.get('uid-numeric-name', None)

        # Add fields for filenames
        self.filenames = config.get('filenames', self.default_filenames)
        if self.filenames:
            for i, filename in enumerate(self.filenames):
                if 'groups' in filename:
                    for grp in filename.get('groups'):
                        grp_tmp = grp.copy()
                        grp_tmp['name'] = f'{self.filename_field_prefix}_filename{i}_{grp["name"]}'
                        self.add_field(DeIdField.factory(grp_tmp))

    def matches_file(self, filename):
        """Check if this profile can process the given file"""
        if self.file_filter:
            if isinstance(self.file_filter, list):
                return any([fnmatch.fnmatch(filename, ff) for ff in self.file_filter])
            if isinstance(self.file_filter, str):
                return fnmatch.fnmatch(filename, self.file_filter)
            raise TypeError(f'Unrecognized type for profile file_filter ({type(self.file_filter)})')
        return False

    def matches_packfile(self, packfile_type):
        """Check if this profile can process the given packfile"""
        return self.packfile_type and self.packfile_type == packfile_type

    def process_files(self, src_fs, dst_fs, files, callback=None):
        """Process all files in the file list, performing de-identification steps

        Args:
            src_fs: The source filesystem (Provides open function)
            dst_fs: The destination filesystem
            files: The set of files in src_fs to process
            callback: Function to call after writing each file
        """
        state = self.create_file_state()

        for path in files:
            # Load file
            record, modified = self.load_record(state, src_fs, path)

            # Record could be None if it should be skipped
            if not record:
                continue

            # Set filenames attributes on record
            self.set_filenames_attributes(record, path)

            # Get destination path
            dst_path = self.get_dest_path(state, record, path)

            # Destination could be None if it should be skipped
            if not dst_path:
                continue

            if modified or self.fields:
                # Create before entry, if log is provided
                if self.log:
                    self.write_log_entry(path, 'before', state, record)

                # De-identify
                for field in self.fields:
                    field.deidentify(self, state, record)

                # Create after entry, if log is provided
                if self.log:
                    self.write_log_entry(path, 'after', state, record)

                # Save to dst_fs if we modified the record
                self.save_record(state, record, dst_fs, dst_path)
            else:
                # No fields to de-identify, just copy to dst
                with src_fs.open(path, 'rb') as src_file:
                    dst_fs.upload(dst_path, src_file)

            if callable(callback):
                callback(dst_fs, dst_path)

    def get_value(self, state, record, fieldname):
        """Get the transformed value for fieldname"""
        field = self.field_map.get(fieldname)
        if field:
            return field.get_value(self, state, record)
        return self.read_field(state, record, fieldname)

    def create_file_state(self):  # pylint: disable=no-self-use
        """Create state object for processing files"""
        return None

    def get_dest_path(self, state, record, path):  # pylint: disable=no-self-use, unused-argument
        """Get destination path"""
        if self.filenames:
            dest_path = None
            for i, filename in enumerate(self.filenames):
                format_kws = {}
                if 'input-regex' in filename:
                    match = re.match(filename['input-regex'], path)
                    if not match:
                        continue
                    format_kws.update(match.groupdict())
                    key_mapping = {k: f'{self.filename_field_prefix}_filename{i}_{k}' for k in format_kws}
                    for k in format_kws:
                        format_kws[k] = self.get_value(state, record, key_mapping[k])
                kws = [x for x in re.findall(r'\{([^}]+)\}', filename['output']) if x not in format_kws]
                for k in kws:
                    format_kws[k] = self.get_value(state, record, k)
                dest_path = filename['output'].format(**format_kws)
                break
            if dest_path is None:
                log.warning('IGNORING %s. No filename input-regex matches', path)
        else:
            dest_path = os.path.basename(path)

        return dest_path

    def write_log_entry(self, path, entry_type, state, record):
        """Write a single log entry of type for path"""
        log_entry = {'path': path, 'type': entry_type}
        for fieldname in self.get_log_fields():
            log_entry[fieldname] = self.read_field(state, record, fieldname)
        self.log.write_entry(log_entry)

    def validate(self, enhanced=False):
        # pylint: disable=unused-argument
        """Validate the profile, returning any errors.

        Args:
            enhanced (bool): Performed a deeper validation if supported

        Returns:
            list(str): A list of error messages, or an empty list
        """
        errors = []
        if self.filenames:
            for filename in self.filenames:
                if filename.get('input-regex'):  # check regexp
                    try:
                        _ = re.compile(filename.get('input-regex', ''))
                    except re.error:
                        errors.append(f"Regex in deid profile is invalid: {filename.get('input-regex')}")
        return errors

    def _process_filename_groups(self, format_kws, groups):
        """Returning a processed group dict

        Args:
            format_kws (dict): Dictionary of group/value from a regex match
            groups (list): List of group (filename field-like) element

        Return:
            (dict): A processed group dict with key=<group name>/value=<processed value>
        """
        # convert group with increment-date action to expected date or datetime format
        for k, v in format_kws.items():
            for grp in groups:
                if grp['name'] == k:
                    if 'increment-date' in grp:
                        format_kws[k] = parse(v).strftime(self.date_format)
                    elif 'increment-datetime' in grp:
                        format_kws[k] = parse(v).strftime(self.datetime_format)
        return format_kws

    def set_filenames_attributes(self, record, path):
        r"""Update record object with private attributes based on filenames properties

        Record attributes are extended based on <groups> extracted from the <input-regex>.
        For instance the following filenames schema defines in profile:

            .. code-block:: json
            filenames:
                - output: {group1}.ext
                  input-regex=r'^(?P<group1>[\w]+).ext$'
                - output: {group1}-{group2}.ext
                  input-regex=r'^(?P<group1>[\w]+)-(?P<date1>[\d]+).ext$'

        will create attributes, depending on which input-regex matches, as:
            .. code-block:: python
            record.<self.filename_field_prefix>_filename0_group1 = 'test' # for `path` = test.ext

            record.<self.filename_field_prefix>_filename1_group1 = 'test'       # for `path` = test-20200130.ext
            record.<self.filename_field_prefix>_filename1_date1 = '20200130'    # for `path` = test-20200130.ext

        Args:
            record (object): A record
            path (str): basename of input file
        """
        if self.filenames:
            filenames_attrs = {}
            for i, filename in enumerate(self.filenames):
                if 'input-regex' in filename:
                    match = re.match(filename['input-regex'], path)
                    if not match:
                        continue
                    format_kws = match.groupdict()
                    if 'groups' in filename:
                        format_kws = self._process_filename_groups(format_kws, filename['groups'])
                    format_kws = {f'{self.filename_field_prefix}_filename{i}_{k}': v for k, v in format_kws.items()}

                    filenames_attrs.update(format_kws)

            # update record with filenames attributes
            if filenames_attrs:
                for k, v in filenames_attrs.items():
                    setattr(record, k, v)

    @abstractmethod
    def load_record(self, state, src_fs, path):
        """Load the record(file) at path, return None to ignore this file"""

    @abstractmethod
    def save_record(self, state, record, dst_fs, path):
        """Save the record to the destination path"""

    @abstractmethod
    def read_field(self, state, record, fieldname):
        """Read the named field as a string"""

    @abstractmethod
    def remove_field(self, state, record, fieldname):
        """Remove the named field from the record"""

    @abstractmethod
    def replace_field(self, state, record, fieldname, value):
        """Replace the named field with value in the record"""
