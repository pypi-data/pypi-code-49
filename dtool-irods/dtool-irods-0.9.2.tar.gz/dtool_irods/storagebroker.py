"""iRODS storage broker."""

import os
import sys
import json
import logging
import tempfile
import time
import datetime

from dtoolcore.utils import (
    generate_identifier,
    base64_to_hex,
    get_config_value,
    mkdir_parents,
    generous_parse_uri,
    DEFAULT_CACHE_PATH,
)
from dtoolcore.filehasher import FileHasher, sha256sum_hexdigest
from dtoolcore.storagebroker import StorageBrokerOSError, BaseStorageBroker

from dtool_irods import CommandWrapper, __version__, IinitRuntimeError

logger = logging.getLogger(__name__)

_STRUCTURE_PARAMETERS = {
    "data_directory": ["data"],
    "dataset_readme_relpath": ["README.yml"],
    "dtool_directory": [".dtool"],
    "admin_metadata_relpath": [".dtool", "dtool"],
    "structure_metadata_relpath": [".dtool", "structure.json"],
    "dtool_readme_relpath": [".dtool", "README.txt"],
    "manifest_relpath": [".dtool", "manifest.json"],
    "overlays_directory": [".dtool", "overlays"],
    "annotations_directory": [".dtool", "annotations"],
    "metadata_fragments_directory": [".dtool", "tmp_fragments"],
    "storage_broker_version": __version__,
}

_DTOOL_README_TXT = """README
======

This is a Dtool dataset stored in iRODS.

Content provided during the dataset creation process
----------------------------------------------------

Dataset descriptive metadata: README.yml
Dataset items: data/

The item identifiers are used to name the files in the data
collection/directory.

An item identifier is the sha1sum hexdigest of the relative path
used to represent the file on traditional file system disk.

Automatically generated files and directories
---------------------------------------------

This file: .dtool/README.txt
Administrative metadata describing the dataset: .dtool/dtool
Structural metadata describing the dataset: .dtool/structure.json
Structural metadata describing the data items: .dtool/manifest.json
Per item descriptive metadata: .dtool/overlays/
Dataset key/value pairs metadata: .dtool/annotations/
"""


#############################################################################
# iRODS helper functions.
#############################################################################

# The exit_on_failure argument should default to True!
# Otherwise bad things can happen, like a _cp command failing silently.
def _run_cmd(cmd, exit_on_failure=True):
    try:
        stdout = cmd(exit_on_failure=exit_on_failure)  # NOQA
        return cmd
    except IinitRuntimeError:
        print("There was an issue communicating with iRODS")
        print("Try running the iRODS command: iinit")
        sys.exit(800)


def _get_file(irods_path, local_abspath):
    cmd = CommandWrapper(["iget", irods_path, local_abspath])
    _run_cmd(cmd)


def _get_file_forcefully(irods_path, local_abspath):
    cmd = CommandWrapper(["iget", "-f", irods_path, local_abspath])
    _run_cmd(cmd)


def _get_text(irods_path):
    """Get raw text from iRODS."""
    # Command to get contents of file to stdout.
    cmd = CommandWrapper([
        "iget",
        irods_path,
        "-"
    ])
    return _run_cmd(cmd).stdout


def _put_text(irods_path, text):
    """Put raw text into iRODS."""
    with tempfile.NamedTemporaryFile() as fh:
        fpath = fh.name

        try:
            # Make Python2 compatible.
            text = unicode(text, "utf-8")
        except (NameError, TypeError):
            # NameError: We are running Python3 => text already unicode.
            # TypeError: text is already of type unicode.
            pass

        fh.write(text.encode("utf-8"))
        fh.flush()
        cmd = CommandWrapper([
            "iput",
            "-f",
            fpath,
            irods_path
        ])
        _run_cmd(cmd)
    assert not os.path.isfile(fpath)


def _get_obj(irods_path):
    """Return object from JSON text stored in iRODS."""
    return json.loads(_get_text(irods_path))


def _put_obj(irods_path, obj):
    """Put python object into iRODS as JSON text."""
    text = json.dumps(obj, indent=2)
    _put_text(irods_path, text)


def _path_exists(irods_path):
    cmd = CommandWrapper(["ils", irods_path])
    cmd = _run_cmd(cmd, exit_on_failure=False)
    return cmd.success()


def _mkdir(irods_path):
    cmd = CommandWrapper(["imkdir", irods_path])
    _run_cmd(cmd)


def _mkdir_if_missing(irods_path):
    if not _path_exists(irods_path):
        _mkdir(irods_path)


def _cp(fpath, irods_path):
    cmd = CommandWrapper(["iput", "-f", fpath, irods_path])
    _run_cmd(cmd)


def _rm(irods_path):
    cmd = CommandWrapper(["irm", "-rf", irods_path])
    _run_cmd(cmd)


def _rm_if_exists(irods_path):
    if _path_exists(irods_path):
        _rm(irods_path)


def _ls(irods_path):
    cmd = CommandWrapper(["ils", irods_path])
    cmd = _run_cmd(cmd)

    def remove_header_line(lines):
        return lines[1:]

    def remove_redundant_whitespace(lines):
        return [l.strip() for l in lines]

    def deal_with_collections(lines):
        fixed_lines = []
        for l in lines:
            if l.startswith("C"):
                _, path = l.split()
                l = os.path.basename(path)  # NOQA
            fixed_lines.append(l)
        return fixed_lines

    text = cmd.stdout.strip()
    lines = text.split("\n")
    return deal_with_collections(
        remove_redundant_whitespace(
            remove_header_line(lines)
        )
    )


def _ls_abspaths(irods_path):
    for f in _ls(irods_path):
        yield os.path.join(irods_path, f)


def _put_metadata(irods_path, key, value):
    cmd = CommandWrapper(["imeta", "set", "-d", irods_path, key, value])
    _run_cmd(cmd)


def _get_checksum(irods_path):
    # Get the hash.
    cmd = CommandWrapper(["ichksum", "-K", irods_path])
    cmd = _run_cmd(cmd)
    line = cmd.stdout.strip()
    info = line.split()
    compound_chksum = info[1]
    alg, checksum = compound_chksum.split(":")
    return checksum


#############################################################################
# iRODS storage broker.
#############################################################################


class IrodsNoMetaDataSetError(LookupError):
    pass


class IrodsStorageBroker(BaseStorageBroker):
    """
    Storage broker to interact with datasets in iRODS.
    """

    #: Attribute used to define the type of storage broker.
    key = "irods"

    #: Attribute used by :class:`dtoolcore.ProtoDataSet` to write the hash
    #: function name to the manifest.
    hasher = FileHasher(sha256sum_hexdigest)

    _structure_parameters = _STRUCTURE_PARAMETERS
    _dtool_readme_txt = _DTOOL_README_TXT

    def __init__(self, uri, config_path=None):

        parse_result = generous_parse_uri(uri)
        path = parse_result.path
        self._abspath = os.path.abspath(path)

        self._dtool_abspath = self._generate_abspath("dtool_directory")
        self._data_abspath = self._generate_abspath("data_directory")
        self._overlays_abspath = self._generate_abspath("overlays_directory")
        self._annotations_abspath = self._generate_abspath(
            "annotations_directory"
        )
        self._metadata_fragments_abspath = self._generate_abspath(
            "metadata_fragments_directory"
        )

        self._irods_cache_abspath = get_config_value(
            "DTOOL_CACHE_DIRECTORY",
            config_path=config_path,
            default=DEFAULT_CACHE_PATH
        )

        # Cache for optimisation
        self._use_cache = False
        self._ls_abspath_cache = {}
        self._metadata_cache = {}
        self._size_and_timestamp_cache = {}
        self._metadata_dir_exists_cache = None

    # Generic helper functions.

    def _generate_abspath(self, key):
        return os.path.join(self._abspath, *self._structure_parameters[key])

    def _ls_abspaths_with_cache(self, irods_path):
        if self._use_cache:
            if irods_path in self._ls_abspath_cache:
                return self._ls_abspath_cache[irods_path]

        abspaths = []
        for f in _ls(irods_path):
            abspaths.append(os.path.join(irods_path, f))

        if self._use_cache:
            self._ls_abspath_cache[irods_path] = abspaths

        return abspaths

    def _get_metadata_with_cache(self, irods_path, key):
        if self._use_cache:
            if irods_path in self._metadata_cache:
                if key in self._metadata_cache[irods_path]:
                    return self._metadata_cache[irods_path][key]

        cmd = CommandWrapper(["imeta", "ls", "-d", irods_path, key])
        cmd()
        text = cmd.stdout
        value_line = text.split('\n')[2]

        if ":" not in value_line:
            raise(IrodsNoMetaDataSetError())

        value = value_line.split(":")[1]
        value = value.strip()

        if self._use_cache:
            self._metadata_cache.setdefault(
                irods_path, {}).update({key: value})

        return value

    def _build_size_and_timestamp_cache(self):
        cmd = CommandWrapper(["ils", "-l", self._data_abspath])
        cmd()
        text = cmd.stdout.strip()
        for line in text.split("\n")[1:]:
            line = line.strip()
            info = line.split()
            size_in_bytes_str = info[3]
            size_in_bytes = int(size_in_bytes_str)
            time_str = info[4]
            dt = datetime.datetime.strptime(time_str, "%Y-%m-%d.%H:%M")
            utc_timestamp = int(time.mktime(dt.timetuple()))
            fname = info[6]
            fpath = os.path.join(self._data_abspath, fname)
            self._size_and_timestamp_cache[fpath] = (
                size_in_bytes,
                utc_timestamp
            )

    def _get_size_and_timestamp_with_cache(self, irods_path):
        if self._use_cache:
            if irods_path in self._size_and_timestamp_cache:
                return self._size_and_timestamp_cache[irods_path]

        cmd = CommandWrapper(["ils", "-l", irods_path])
        cmd()
        text = cmd.stdout.strip()
        first_line = text.split("\n")[0].strip()
        info = first_line.split()
        size_in_bytes_str = info[3]
        size_in_bytes = int(size_in_bytes_str)
        time_str = info[4]
        dt = datetime.datetime.strptime(time_str, "%Y-%m-%d.%H:%M")
        utc_timestamp = int(time.mktime(dt.timetuple()))

        return size_in_bytes, utc_timestamp

    def _get_item_key_from_handle(self, handle):
        fname = generate_identifier(handle)
        return os.path.join(self._data_abspath, fname)

    def _handle_to_fragment_absprefixpath(self, handle):
        stem = generate_identifier(handle)
        return os.path.join(self._metadata_fragments_abspath, stem)

    def _metadata_dir_exists(self):
        if self._use_cache:
            if self._metadata_dir_exists_cache is None:
                self._metadata_dir_exists_cache = \
                    _path_exists(self._metadata_fragments_abspath)
            return self._metadata_dir_exists_cache
        return _path_exists(self._metadata_fragments_abspath)

    # Class methods to override.

    @classmethod
    def list_dataset_uris(cls, base_uri, config_path):
        """Return list containing URIs in base_uri."""
        parsed_uri = generous_parse_uri(base_uri)
        irods_path = parsed_uri.path

        uri_list = []

        logger.info("irods_path: '{}'".format(irods_path))

        for dir_path in _ls_abspaths(irods_path):

            logger.info("dir path: '{}'".format(dir_path))

            base, uuid = os.path.split(dir_path)
            base_uri = "irods:{}".format(base)
            uri = cls.generate_uri(
                name=None,
                uuid=uuid,
                base_uri=base_uri
            )

            storage_broker = cls(uri, config_path)

            if storage_broker.has_admin_metadata():
                uri_list.append(uri)

        return uri_list

    @classmethod
    def generate_uri(cls, name, uuid, base_uri):
        prefix = generous_parse_uri(base_uri).path
        dataset_path = os.path.join(prefix, uuid)
        dataset_abspath = os.path.abspath(dataset_path)
        return "{}:{}".format(cls.key, dataset_abspath)

    # Methods to override.

    def get_text(self, key):
        return _get_text(key)

    def put_text(self, key, text):
        parent_dir = os.path.dirname(key)
        _mkdir_if_missing(parent_dir)
        _put_text(key, text)

    def get_admin_metadata_key(self):
        return self._generate_abspath("admin_metadata_relpath")

    def get_manifest_key(self):
        return self._generate_abspath("manifest_relpath")

    def get_readme_key(self):
        return self._generate_abspath("dataset_readme_relpath")

    def get_overlay_key(self, overlay_name):
        return os.path.join(self._overlays_abspath, overlay_name + '.json')

    def get_annotation_key(self, annotation_name):
        return os.path.join(
            self._annotations_abspath,
            annotation_name + '.json'
        )

    def get_structure_key(self):
        return self._generate_abspath("structure_metadata_relpath")

    def get_dtool_readme_key(self):
        return self._generate_abspath("dtool_readme_relpath")

    def has_admin_metadata(self):
        """Return True if the administrative metadata exists.

        This is the definition of being a "dataset".
        """
        return _path_exists(self.get_admin_metadata_key())

    def list_overlay_names(self):
        """Return list of overlay names."""
        overlay_names = []
        for fname in _ls(self._overlays_abspath):
            name, ext = os.path.splitext(fname)
            overlay_names.append(name)
        return overlay_names

    def list_annotation_names(self):
        """Return list of annotation names."""
        annotation_names = []
        if not _path_exists(self._annotations_abspath):
            return annotation_names
        for fname in _ls(self._annotations_abspath):
            name, ext = os.path.splitext(fname)
            annotation_names.append(name)
        return annotation_names

    def get_item_abspath(self, identifier):
        """Return absolute path at which item content can be accessed.

        :param identifier: item identifier
        :returns: absolute path from which the item content can be accessed
        """
        if not hasattr(self, "_admin_metadata_cache"):
            self._admin_metadata_cache = self.get_admin_metadata()
        admin_metadata = self._admin_metadata_cache

        uuid = admin_metadata["uuid"]
        # Create directory for the specific dataset.
        dataset_cache_abspath = os.path.join(self._irods_cache_abspath, uuid)
        mkdir_parents(dataset_cache_abspath)

        # Get the file extension from the  relpath from the handle metadata.
        irods_item_path = os.path.join(self._data_abspath, identifier)
        relpath = self._get_metadata_with_cache(irods_item_path, "handle")
        _, ext = os.path.splitext(relpath)

        local_item_abspath = os.path.join(
            dataset_cache_abspath,
            identifier + ext)

        if not os.path.isfile(local_item_abspath):
            tmp_local_item_abspath = local_item_abspath + ".tmp"
            _get_file_forcefully(irods_item_path, tmp_local_item_abspath)
            os.rename(tmp_local_item_abspath, local_item_abspath)

        return local_item_abspath

    def _create_structure(self):
        """Create necessary structure to hold a dataset."""

        # Ensure that the specified path does not exist and create it.
        if _path_exists(self._abspath):
            raise(StorageBrokerOSError(
                "Path already exists: {}".format(self._abspath)
            ))

        # Make sure the parent collection exists.
        parent, _ = os.path.split(self._abspath)
        if not _path_exists(parent):
            raise(StorageBrokerOSError(
                "No such iRODS collection: {}".format(parent)))

        _mkdir(self._abspath)

        # Create more essential subdirectories.
        essential_subdirectories = [
            self._dtool_abspath,
            self._data_abspath,
            self._overlays_abspath,
            self._annotations_abspath
        ]
        for abspath in essential_subdirectories:
            _mkdir_if_missing(abspath)

    def put_item(self, fpath, relpath):
        """Put item with content from fpath at relpath in dataset.

        Missing directories in relpath are created on the fly.

        :param fpath: path to the item on local disk
        :param relpath: relative path name given to the item in the dataset as
                        a handle
        """
        # Put the file into iRODS.
        fname = generate_identifier(relpath)
        dest_path = os.path.join(self._data_abspath, fname)
        _cp(fpath, dest_path)

        # Add the relpath handle as metadata.
        _put_metadata(dest_path, "handle", relpath)

        return relpath

    def iter_item_handles(self):
        """Return iterator over item handles."""
        for abspath in self._ls_abspaths_with_cache(self._data_abspath):
            try:
                relpath = self._get_metadata_with_cache(abspath, "handle")
                yield relpath
            except IrodsNoMetaDataSetError:
                pass

    def get_size_in_bytes(self, handle):
        key = self._get_item_key_from_handle(handle)
        size, timestamp = self._get_size_and_timestamp_with_cache(key)
        return size

    def get_utc_timestamp(self, handle):
        key = self._get_item_key_from_handle(handle)
        size, timestamp = self._get_size_and_timestamp_with_cache(key)
        return timestamp

    def get_hash(self, handle):
        key = self._get_item_key_from_handle(handle)
        checksum = _get_checksum(key)
        return base64_to_hex(checksum)

# According to the tests the below is not needed.
#   def get_relpath(self, handle):
#       key = self._get_item_key_from_handle(handle)
#       return self._get_metadata_with_cache(key, "handle")

    def add_item_metadata(self, handle, key, value):
        """Store the given key:value pair for the item associated with handle.

        :param handle: handle for accessing an item before the dataset is
                       frozen
        :param key: metadata key
        :param value: metadata value
        """
        _mkdir_if_missing(self._metadata_fragments_abspath)

        prefix = self._handle_to_fragment_absprefixpath(handle)
        fpath = prefix + '.{}.json'.format(key)

        _put_obj(fpath, value)

    def get_item_metadata(self, handle):
        """Return dictionary containing all metadata associated with handle.

        In other words all the metadata added using the ``add_item_metadata``
        method.

        :param handle: handle for accessing an item before the dataset is
                       frozen
        :returns: dictionary containing item metadata
        """
        if not self._metadata_dir_exists():
            return {}

        prefix = self._handle_to_fragment_absprefixpath(handle)

        files = [f for f in self._ls_abspaths_with_cache(
                 self._metadata_fragments_abspath)
                 if f.startswith(prefix)]

        metadata = {}
        for f in files:
            key = f.split('.')[-2]  # filename: identifier.key.json
            value = _get_obj(f)
            metadata[key] = value

        return metadata

    def pre_freeze_hook(self):
        """Pre :meth:`dtoolcore.ProtoDataSet.freeze` actions.

        This method is called at the beginning of the
        :meth:`dtoolcore.ProtoDataSet.freeze` method.

        In iRODS it is used to create caches for repetitive and time consuming
        calls to iRODS.
        """
        self._use_cache = True
        self._build_size_and_timestamp_cache()

    def post_freeze_hook(self):
        """Post :meth:`dtoolcore.ProtoDataSet.freeze` cleanup actions.

        This method is called at the end of the
        :meth:`dtoolcore.ProtoDataSet.freeze` method.
        """
        self._use_cache = False
        self._ls_abspath_cache = {}
        self._metadata_cache = {}
        self._size_and_timestamp_cache = {}
        _rm_if_exists(self._metadata_fragments_abspath)

    def _list_historical_readme_keys(self):
        historical_readme_keys = []
        for key in _ls_abspaths(self._abspath):
            if key.find("README.yml-") != -1:
                historical_readme_keys.append(key)
        return historical_readme_keys
