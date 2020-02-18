"""CLI Global Config"""
import json
import logging
import os
import time

from ruamel.yaml import YAML, YAMLError

from flywheel_cli import util
from .verify_config import VerifyGlobalConfigMixin

DEFAULT_CONFIG_PATH = '~/.config/flywheel/cli.yml'
CLI_LOG_PATH = '~/.cache/flywheel/logs/cli.log'


class GlobalConfigError(Exception):
    """Handle Global Config Errors"""

    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return self.msg


class GlobalConfigInitError(GlobalConfigError):
    """Handle Global Config Init Errors"""


class GlobalConfig(VerifyGlobalConfigMixin):
    """CLI Global Config"""

    def __init__(self, args=None):
        self.raw_config = self.read_config_file(args)
        self._args = args

        # Configure logging
        self.quiet = self.get('quiet', False)
        self.debug = self.get('debug', False)
        self.no_audit_log = self.get('no_audit_log', False)
        self.audit_log_path = self.get('audit_log_path', None)
        self.save_audit_locally = self.get('save_audit_locally', False)

        if os.environ.get('FW_DISABLE_LOGS') != '1':
            self.configure_logging()

        # Assume yes option
        self.assume_yes = self.get('assume_yes', False)

        self.verbose = self.get('verbose', None)

        # Certificates
        self.ca_certs = self.get('ca_certs')
        if self.ca_certs is not None:
            # Monkey patch certifi.where()
            import certifi  # pylint: disable=import-outside-toplevel
            certifi.where = lambda: self.ca_certs

        # Time Zone
        self.timezone = self.get('timezone')

        if self.timezone is not None:
            # Validate the timezone string
            import pytz  # pylint: disable=import-outside-toplevel
            import flywheel_migration  # pylint: disable=import-outside-toplevel

            try:
                tz = pytz.timezone(self.timezone)
            except pytz.exceptions.UnknownTimeZoneError:
                raise GlobalConfigError(f'Unknown timezone: {self.timezone}')

            # Update the default timezone for flywheel_migration and util
            util.DEFAULT_TZ = tz
            flywheel_migration.util.DEFAULT_TZ = tz

            # Also set in the environment
            os.environ['TZ'] = self.timezone

    def configure_logging(self):
        """Logging config"""
        root = logging.getLogger()

        # Propagate all debug logging
        root.setLevel(logging.DEBUG)

        # Always log to cli log file
        log_path = os.path.expanduser(os.environ.get('FW_LOG_FILE_PATH', CLI_LOG_PATH))
        log_dir = os.path.dirname(log_path)
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)

        # Use GMT ISO date for logfile
        file_formatter = logging.Formatter(fmt='%(asctime)s.%(msecs)03d %(levelname)s %(message)s', datefmt='%Y-%m-%dT%H:%M:%S')
        file_formatter.converter = time.gmtime

        # Allow environment overrides for log size and backup count
        log_file_size = int(os.environ.get('FW_LOG_FILE_SIZE', '5242880')) # Default is 5 MB
        log_file_backup_count = int(os.environ.get('FW_LOG_FILE_COUNT', '2')) # Default is 2

        file_handler = logging.handlers.RotatingFileHandler(log_path, maxBytes=log_file_size, backupCount=log_file_backup_count)
        file_handler.setFormatter(file_formatter)
        root.addHandler(file_handler)

        # Control how much (if anything) goes to console
        console_log_level = logging.INFO
        if self.quiet:
            console_log_level = logging.ERROR
        elif self.debug:
            console_log_level = logging.DEBUG

        console_formatter = logging.Formatter(fmt='%(levelname)s: %(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(console_formatter)
        console_handler.setLevel(console_log_level)
        root.addHandler(console_handler)

        # Finally, capture all warnings to the logging framework
        logging.captureWarnings(True)

    def get(self, key, default=None):
        """Get config value by key.
        First checks args, then checks config file if no match returns the default value.

        Args:
            key (str): Key

        Kwargs:
            default (any): Default value

        Returns: Config value relates to the specified key or the default value

        """
        value_from_args = getattr(self._args, key, None)
        if not self.raw_config:
            return value_from_args or default
        raw_config_key = key.replace('_', '-')
        return value_from_args or self.raw_config.get(raw_config_key) or default

    @staticmethod
    def read_config_file(args):
        """Read data from config file"""
        if not getattr(args, 'no_config', False):
            path = getattr(args, "config_file", None)
            if not path:
                path = os.path.expanduser(DEFAULT_CONFIG_PATH)
                if not os.path.exists(path):
                    return None
            if path.endswith('.yml'):
                try:
                    yaml = YAML()
                    with open(path) as config_file:
                        config = yaml.load(config_file)
                except (IOError, YAMLError) as exc:
                    raise GlobalConfigInitError(f'Unable to parse YAML config file: {exc}')
            elif path.endswith('.json'):
                try:
                    with open(path) as json_file:
                        config = json.load(json_file)
                except IOError as exc:
                    raise GlobalConfigInitError(f'Unable to parse JSON file: {exc}')
            else:
                raise GlobalConfigInitError('Only YAML and JSON files are supported')
            return config
        return None

    @staticmethod
    def add_arguments(parser):
        """Add global config arguments"""
        config_group = parser.add_mutually_exclusive_group()
        config_group.add_argument('--config-file', '-C', help='Specify configuration options via config file')
        config_group.add_argument('--no-config', action='store_true', help='Do NOT load the default configuration file')

        parser.add_argument('--no-audit-log', action='store_true', help="Don't generate an audit log")
        parser.add_argument('--audit-log-path', help='Location to save audit log')
        parser.add_argument('--save-audit-locally', action='store_true', help='Save audit log file locally')
        parser.add_argument('-y', '--yes', action='store_true', help='Assume the answer is yes to all prompts', dest='assume_yes')
        parser.add_argument('--ca-certs', help='The file to use for SSL Certificate Validation')
        parser.add_argument('--timezone', help='Set the effective local timezone for imports')
        parser.add_argument('-v', '--verbose', action='store_true', help='Get more information about the import')

        log_group = parser.add_mutually_exclusive_group()
        log_group.add_argument('--debug', action='store_true', help='Turn on debug logging')
        log_group.add_argument('--quiet', action='store_true', help='Squelch log messages to the console')
        return parser
