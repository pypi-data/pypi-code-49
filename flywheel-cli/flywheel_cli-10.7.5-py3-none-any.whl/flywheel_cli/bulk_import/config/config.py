"""CLI Bulk Import Config"""

import math
import multiprocessing
import os
import tempfile
import zlib
import zipfile

from ... import util
from .global_config import GlobalConfig
from .verify_config import VerifyBulkImportConfigMixin


class BulkImportConfigError(Exception):
    """Handle Bulk Import Config Errors"""

    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return self.msg


class BulkImportConfigInitError(BulkImportConfigError):
    """Handle Bulk Import Config Init Errors"""


class BulkImportConfig(GlobalConfig):
    """CLI Bulk Import Config"""
    # pylint: disable=too-many-instance-attributes

    def __init__(self, args=None):
        super().__init__(args)

        # Database conntection string
        default_sqlite_db_path = os.path.join(tempfile.gettempdir(), 'flywheel_cli_bulk_import.db')
        self.db_connection_str = self.get("db_connection_str", f'sqlite:{default_sqlite_db_path}')

        self.remote_host = False

        if "postgres" in self.db_connection_str:
            self.remote_host = True

        self.cpu_count = self.get("jobs", -1)
        if self.cpu_count == -1:
            self.cpu_count = max(1, math.floor(multiprocessing.cpu_count() / 2))

        self.buffer_size = 65536
        self.max_tempfile = self.get("max_tempfile", 50)
        self.max_spool = self.max_tempfile * (1024 * 1024)  # Max tempfile size before rolling over to disk

    @staticmethod
    def add_arguments(parser):
        """Add bulk import arguments"""
        super(BulkImportConfig, BulkImportConfig).add_arguments(parser)
        parser.add_argument('--db-connection-str', help='Database connection string (default: sqlite:/tmp/sqlite.db)')
        parser.add_argument('--jobs', '-j', type=int, help='The number of concurrent jobs to run (e.g. scan jobs) (default: <cpu_count> / 2)')
        parser.add_argument('--max-tempfile', type=int, help='The max in-memory tempfile size, in MB, or 0 to always use disk (default: 50)')
        return parser


class BaseImporterConfig(VerifyBulkImportConfigMixin):
    """Base Importer Config"""
    # pylint: disable=too-many-instance-attributes, too-many-arguments

    def __init__(self, folder=None, compression_level=None, max_retries=None, include_dirs=None,
                 exclude_dirs=None, include=None, exclude=None, output_folder=None,
                 skip_existing=None, no_audit_log=None, audit_log_path=None,
                 related_acquisitions=None, de_identify=None, deid_profile=None,
                 deid_profiles=None, ignore_unknown_tags=None, encodings=None,
                 symlinks=None, save_audit_locally=None, importer_type=None):

        # Set the default compression (used by zipfile/ZipFS)
        self.compression_level = compression_level or 1
        if self.compression_level > 0:
            zlib.Z_DEFAULT_COMPRESSION = self.compression_level
        self.importer_type = importer_type
        self.folder = folder
        self.max_retries = max_retries or 3
        self.symlinks = symlinks or False
        self.include_dirs = include_dirs or []
        self.exclude_dirs = exclude_dirs or []
        self.include = include or []
        self.exclude = exclude or []
        self.exclude.extend(['.*', 'ehthumbs.db', 'Thumbs.db', 'Icon\r'])
        self.exclude = set(self.exclude)
        self.output_folder = output_folder or None

        # Skip existing files
        self.skip_existing = skip_existing or False

        # An audit file to track which files are being uploaded to where
        self.no_audit_log = no_audit_log or False
        self.save_audit_locally = save_audit_locally or False
        if not self.no_audit_log:
            self.audit_log_path = audit_log_path or None
        self.related_acquisitions = related_acquisitions or False

        # Get de-identification profile
        self.de_identify = de_identify or False
        self.deid_profile = deid_profile or None
        self.deid_profiles = deid_profiles or []

        # Handle unknown dicom tags
        self.ignore_unknown_tags = ignore_unknown_tags or False

        # Register encoding aliases
        self.encodings = encodings or None
        if self.encodings is not None:
            self.register_encoding_aliases(self.encodings)
        self.verify_config()

    @classmethod
    def from_dict(cls, kwargs):
        """Create an instance from dict"""
        return cls(**kwargs)

    @classmethod
    def from_multi_src(cls, sources):
        """Load attributes from multiple sources and create an instance"""
        kwargs = {}
        for attr in cls.get_public_attrs():
            kwargs[attr] = util.priority_get(sources, attr)
        return cls(**kwargs)

    def to_dict(self):
        """Save the configuration to dict"""
        config = {}
        for attr in self.get_public_attrs():
            config[attr] = getattr(self, attr)
        return config

    def generate_walker_kwargs(self):
        """Create walker"""
        kwargs = {}
        for key in ('follow_symlinks', 'filter', 'exclude', 'filter_dirs', 'exclude_dirs'):
            kwargs.setdefault(key, getattr(self, key, None))
        return kwargs

    def get_compression_type(self):
        """Returns compression type"""
        if self.compression_level == 0:
            return zipfile.ZIP_STORED
        return zipfile.ZIP_DEFLATED

    def verify(self):
        """Verfiy configuration"""

    @staticmethod
    def register_encoding_aliases(encoding_aliases):
        """Register common encoding aliases"""
        import encodings  # pylint: disable=import-outside-toplevel

        for encoding in encoding_aliases:
            key, _, value = encoding.partition("=")
            encodings.aliases.aliases[key.strip().lower()] = value.strip().lower()

    @staticmethod
    def add_arguments(parser):
        """Add bulk import arguments"""
        parser.add_argument('folder', help='The path to the folder to import')
        # parser.add_argument('--max-retries', help='Maximum number of retry attempts, if assume yes')
        parser.add_argument('--compression-level', type=int, choices=range(-1, 9),
                            help='The compression level to use for packfiles. -1 for default, 0 for store')
        parser.add_argument('--symlinks', action='store_true', help='follow symbolic links that resolve to directories')
        parser.add_argument('--include-dirs', action='append', dest='include_dirs', help='Patterns of directories to include')
        parser.add_argument('--exclude-dirs', action='append', dest='exclude_dirs', help='Patterns of directories to exclude')
        parser.add_argument('--include', action='append', dest='filter', help='Patterns of filenames to include')
        parser.add_argument('--exclude', action='append', dest='exclude', help='Patterns of filenames to exclude')
        #parser.add_argument('--output-folder', help='Output to the given folder instead of uploading to flywheel')
        #parser.add_argument('--skip-existing', action='store_true', help='Skip import of existing files')
        #parser.add_argument('--no-audit-log', action='store_true', help='Don\'t generate an audit log.')
        #parser.add_argument('--audit-log-path', help='Location to save audit log')
        #parser.add_argument('--private-dicom-tags', help='Path to a private dicoms csv file')
        parser.add_argument('--ignore-unknown-tags', action='store_true', help='Ignore unknown dicom tags')
        parser.add_argument('--encodings', help='Set character encoding aliases. E.g. win_1251=cp1251')
        parser.add_argument('--de-identify', action='store_true', help='De-identify DICOM files')
        parser.add_argument('--deid-profile', help='Use the De-identify profile by name (default: minimal)')
        return parser

    @staticmethod
    def get_public_attrs():
        """Get attributes to dump"""
        return ["folder", "compression_level", "max_retries", "include_dirs",
                "exclude_dirs", "include", "exclude", "output_folder",
                "skip_existing", "no_audit_log", "audit_log_path", "related_acquisitions",
                "de_identify", "deid_profile", "deid_profiles", "ignore_unknown_tags",
                "encodings", "save_audit_locally", "importer_type"]
