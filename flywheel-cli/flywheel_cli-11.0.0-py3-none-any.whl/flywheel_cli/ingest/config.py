"""Provides config classes."""

import copy
import json
import logging
import math
import multiprocessing
import os
import re
import socket
import zipfile
import zlib
from typing import Any, List

from pydantic import BaseModel, BaseSettings, Field, validator  # pylint: disable=no-name-in-module
from ruamel.yaml import YAML, YAMLError

from ..sdk_impl import load_config
from .. import util, walker, config as root_config

DEFAULT_CONFIG_PATH = os.path.join(root_config.CONFIG_DIRPATH, "cli.yml")
INGEST_CONFIG_PATH = os.path.join(root_config.CONFIG_DIRPATH, "ingest.yaml")
UUID_REGEX = "[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"
INGEST_OPERATION_REF_REGEX = re.compile(f"(?P<host>.*)/ingests/(?P<ingest_id>{UUID_REGEX})")

FIELD_TEMPLATES = {
    "db_url": {
        "default": None,
        "argparse_opts": {
            "positional": True,
            "nargs": "?",
            "metavar": "DB",
            "help": "Database connection string",
        }
    },
    "db_check_fn": {
        "default": None,
        "argparse_opts": {
            "help": "Optional database schema check function"
        }
    },
    "jobs": {
        "default": 1,
        "argparse_opts": {
            "help": "The number of concurrent jobs to run (e.g. scan jobs), ignored when using cluster"
        }
    },
    "sleep_time": {
        "default": 1,
        "argparse_opts": {
            "metavar": "SECONDS",
            "help": "Number of seconds to wait before trying to get a task",
        }
    },
    "max_tempfile": {
        "default": 50,
        "argparse_opts": {
            "help": "The max in-memory tempfile size, in MB, or 0 to always use disk"
        }
    },
    "buffer_size": {
        "default": 65536,
        "argparse_opts": {
            "skip": True,
        }
    },
    "worker_name": {
        "default": socket.gethostname(),
        "argparse_opts": {
            "metavar": "NAME",
            "help": "Unique name of the worker",
        }
    },
    "save_audit_log": {
        "argparse_opts": {
            "metavar": "PATH",
            "help": "Save audit log to the specified path on the current machine",
        }
    },
    "save_deid_log": {
        "argparse_opts": {
            "metavar": "PATH",
            "help": "Save deid log to the specified path on the current machine",
        }
    },
    "save_subjects": {
        "argparse_opts": {
            "metavar": "PATH",
            "help": "Save subjects to the specified file",
        }
    },
    "load_subjects": {
        "argparse_opts": {
            "metavar": "PATH",
            "help": "Load subjects from the specified file",
        }
    }
}


log = logging.getLogger(__name__)


def create_field(template_name, override_default=None, override_argparse_opts=None):
    """Create pydantic field from a template"""
    template = FIELD_TEMPLATES[template_name]
    default_value = override_default or template.get("default")
    argparse_opts = copy.deepcopy(template.get("argparse_opts", {}))
    if override_argparse_opts:
        argparse_opts.update(override_argparse_opts)
    return Field(default_value, argparse_opts=argparse_opts)


class BaseConfig(BaseSettings):
    """Base config module that reads """

    config_file: str = Field(DEFAULT_CONFIG_PATH, argparse_opts={
        "flags": ["-C", "--config-file"],
        "metavar": "PATH",
        "mutually_exclusive_group": "config",
        "help": "Specify configuration options via config file",
    })
    no_config: bool = Field(False, argparse_opts={
        "mutually_exclusive_group": "config",
        "help": "Do NOT load the default configuration file",
    })

    @classmethod
    def parse_arguments(cls, args):
        """Load values from namespace and config file"""
        config_filepath = getattr(args, "config_file", None) or cls.__fields__["config_file"].default
        config_filepath = os.path.expanduser(config_filepath)
        config_from_file = {}
        if not getattr(args, "no_config", None):
            config_from_file = cls.read_config_file(config_filepath) or {}

        values = {}

        for field in cls.__fields__.values():
            snake_name = field.name
            dash_name = field.name.replace("_", "-")
            # try get the value from arguments first
            # then from the loaded config file
            value = (getattr(args, snake_name, None) or
                     config_from_file.get(snake_name) or
                     config_from_file.get(dash_name))
            # only add values which are not None to let BaseSettings load them
            # from environment variables
            if value is not None:
                values[snake_name] = value
        return cls(**values)

    @classmethod
    def add_arguments(cls, parser):
        """Add arguments to a given parser"""
        groups = {}

        for field in cls.__fields__.values():
            # by default add all fields to the parser, except it is marked
            # not to add
            opts = copy.deepcopy(field.field_info.extra.get("argparse_opts", {}))
            skip = opts.pop("skip", False)

            if skip:
                # Skip fields that we don't want to expose on cli
                continue

            parser_group = parser
            # Build parser groups
            for grp_type in ("mutually_exclusive_group", "argument_group"):
                grp_name = opts.pop(grp_type, None)
                if not grp_name:
                    continue
                if not groups.get(grp_name):
                    grp_opts = opts.pop("group_opts", {})
                    groups[grp_name] = getattr(parser, f"add_{grp_type}")(**grp_opts)
                parser_group = groups[grp_name]

            kwargs = {}
            # prepare flags
            # handle positional arguments
            if opts.pop("positional", False):
                # can't set dest for positional argument
                flags = field.name
            else:
                flags = opts.pop("flags", f"--{field.name.replace('_', '-')}")
                kwargs["dest"] = field.name
            if not isinstance(flags, list):
                flags = [flags]
            # add the remainder opts as is to the kwargs
            kwargs.update(opts)
            # automatically add default value to the help text
            if not field.required:
                kwargs.setdefault("help", "")
                kwargs["help"] = f"{kwargs['help']} (default: {field.default})"
            # set action if necessary
            if field.type_ == bool:
                kwargs["action"] = "store_true"
            parser_group.add_argument(*flags, **kwargs)

    @staticmethod
    def read_config_file(filepath):
        """Read data from config file"""
        if not os.path.exists(filepath):
            return None
        file_extension = filepath.rsplit(".", maxsplit=1)[-1]
        if file_extension in ("yml", "yaml"):
            try:
                yaml = YAML()
                with open(filepath) as config_file:
                    config = yaml.load(config_file)
            except (IOError, YAMLError) as exc:
                raise ConfigError(f"Unable to parse YAML config file: {exc}")
        elif file_extension == "json":
            try:
                with open(filepath) as json_file:
                    config = json.load(json_file)
            except IOError as exc:
                raise ConfigError(f"Unable to parse JSON file: {exc}")
        else:
            raise ConfigError("Only YAML and JSON files are supported")
        return config

    @validator("config_file")
    def expand_user_config_file_path(cls, v):  # pylint: disable=no-self-argument, no-self-use
        """Expand user in the provided config file path"""
        return os.path.expanduser(v)

    @staticmethod
    def get_api_key():
        """Load api-key from config"""
        config = load_config()
        if not config and config.get("key"):
            raise Exception("Not logged in, please login using `fw login`")
        return config["key"]

    class Config:  # pylint: disable=too-few-public-methods
        """Set config for BaseSettings"""
        env_prefix = "FLYWHEEL_CLI_"


class GlobalConfig(BaseConfig):
    """Base configuration model"""

    assume_yes = Field(False, argparse_opts={
        "flags": ["-y", "--yes"],
        "help": "Assume the answer is yes to all prompts",
    })
    ca_certs: str = Field(None, argparse_opts={
        "help": "The file to use for SSL Certificate Validation"
    })
    timezone: str = Field(None, argparse_opts={
        "help": "Set the effective local timezone for imports"
    })
    quiet: bool = Field(False, argparse_opts={
        "mutually_exclusive_group": "logging",
        "help": "Squelch log messages to the console",
    })
    debug: bool = Field(False, argparse_opts={
        "mutually_exclusive_group": "logging",
        "help": "Turn on debug logging",
    })
    verbose: bool = Field(False, argparse_opts={
        "flags": ["-v", "--verbose"],
        "help": "Get more detailed output",
    })

    def configure_ca_certs(self):
        """Configure ca-certs"""
        if self.ca_certs is not None:
            # Monkey patch certifi.where()
            import certifi  # pylint: disable=import-outside-toplevel
            certifi.where = lambda: self.ca_certs

    def configure_timezone(self):
        """Configure timezone"""
        if self.timezone is not None:
            # Validate the timezone string
            import pytz  # pylint: disable=import-outside-toplevel
            import flywheel_migration  # pylint: disable=import-outside-toplevel

            try:
                tz = pytz.timezone(self.timezone)
            except pytz.exceptions.UnknownTimeZoneError:
                raise ConfigError(f'Unknown timezone: {self.timezone}')

            # Update the default timezone for flywheel_migration and util
            util.DEFAULT_TZ = tz
            flywheel_migration.util.DEFAULT_TZ = tz

            # Also set in the environment
            os.environ['TZ'] = self.timezone

    def startup_initialize(self):
        """Execute configure methods, this should be only called once, when cli starts."""
        if os.environ.get('FW_DISABLE_LOGS') != '1':
            root_config.Config.configure_logging(self)
        self.configure_ca_certs()
        self.configure_timezone()


    @validator("debug")
    def exclusive_logging_flags(cls, val, values):  # pylint: disable=no-self-argument, no-self-use
        """Validate logging mutually exclusive group"""
        if val and values["quiet"]:
            raise ValueError("quiet not allowed with debug")
        return val


class WorkerIngestConfig(GlobalConfig):
    """Worker ingest configuration"""
    db_url: str = create_field("db_url")
    jobs: int = create_field("jobs", override_argparse_opts={"skip": True})
    sleep_time: int = create_field("sleep_time")
    max_tempfile: int = create_field("max_tempfile")
    buffer_size: int = create_field("buffer_size")
    worker_name: str = create_field("worker_name")
    db_check_fn: str = create_field("db_check_fn")

    @validator("db_url")
    def db_required(cls, val):  # pylint: disable=no-self-argument, no-self-use
        """Validate that database connection string is not None"""
        if not val:
            raise ValueError("Database connection string is required, provide one in cli arguments or in config file.")
        return val


class ManageIngestConfig(GlobalConfig):
    """Used to manage ingest operation, currently to follow or abort"""
    ingest_url: dict = Field(None, argparse_opts={
        "positional": True,
        "metavar": "INGEST_URL",
        "nargs": "?",
        "help": "The url of the ingest to manage (<cluster_host>/ingests/<ingest_id>)",
    })
    cluster: str = Field(None, argparse_opts={
        "skip": True,
    })
    ingest_id: str = Field(None, argparse_opts={
        "skip": True,
    })
    save_audit_log: str = create_field("save_audit_log")
    save_deid_log: str = create_field("save_deid_log")
    save_subjects: str = create_field("save_subjects")

    @validator("ingest_url", pre=True)
    def validate_ingest_url(cls, val):  # pylint: disable=no-self-argument, no-self-use
        """Get the ingest operation url from the config file if not provided."""
        ingest_url = val
        if not ingest_url:
            try:
                config = cls.read_config_file(os.path.expanduser(INGEST_CONFIG_PATH)) or {}
            except ConfigError:
                ingest_url = None
            else:
                ingest_url = config.get("ingest_operation_url")
        if not ingest_url:
            raise ValueError(
                "Couldn't determine the ingest URL, "
                "probably it was started on a different machine or by a different user. "
                "Please specify the ingest URL as a positional argument."
            )
        match = INGEST_OPERATION_REF_REGEX.match(ingest_url)
        if not match:
            raise ValueError("The provided url should have the following format: <cluster_url>/ingests/<ingest_id>")
        return {
            "cluster": match.group("host"),
            "ingest_id": match.group("ingest_id"),
        }

    @validator("cluster")
    def validate_cluster(cls, val, *, values, **kwargs):  # pylint: disable=no-self-argument, no-self-use, unused-argument
        """Validate cluster, get from ingest url if not defined explicitly"""
        return val or values.get("ingest_url", {}).get("cluster")

    @validator("ingest_id")
    def validate_ingest_id(cls, val, *, values, **kwargs):  # pylint: disable=no-self-argument, no-self-use, unused-argument
        """Validate ingest id, get from ingest url if not defined explicitly"""
        return val or values.get("ingest_url", {}).get("ingest_id")


class SubjectConfig(BaseModel):  # pylint: disable=too-few-public-methods
    """Subject config"""
    code_serial: int = 0
    code_format: str
    map_keys: List[str]


class BaseIngestConfig(GlobalConfig):
    """Base ingest configuration.
    The different ingest startegies should extend this class.
    """
    src_fs_url: str = Field(..., argparse_opts={
        "positional": True,
        "metavar": "SRC",
        "help": "The path to the folder to import",
    })
    no_subjects: bool = Field(False, argparse_opts={
        "mutually_exclusive_group": "no_level",
        "help": "no subject level (create a subject for every session)",
    })
    no_sessions: bool = Field(False, argparse_opts={
        "mutually_exclusive_group": "no_level",
        "help": "no session level (create a session for every subject)",
    })
    symlinks: bool = Field(False, argparse_opts={
        "help": "Follow symbolic links that resolve to directories",
    })
    include_dirs: List[str] = Field([], argparse_opts={
        "metavar": "PATTERN",
        "nargs": "+",
        "help": "Patterns of directories to include",
    })
    exclude_dirs: List[str] = Field([], argparse_opts={
        "metavar": "PATTERN",
        "nargs": "+",
        "help": "Patterns of directories to exclude",
    })
    include: List[str] = Field([], argparse_opts={
        "metavar": "PATTERN",
        "nargs": "+",
        "help": "Patterns of filenames to include",
    })
    exclude: List[str] = Field([], argparse_opts={
        "metavar": "PATTERN",
        "nargs": "+",
        "help": "Patterns of filenames to exclude",
    })
    compression_level: int = Field(zlib.Z_DEFAULT_COMPRESSION, argparse_opts={
        "help": (
            "The compression level to use for packfiles -1 by default. "
            "0 for store. "
            "A higher compression level number means more compression."
        )
    })
    ignore_unknown_tags: bool = Field(False, argparse_opts={
        "help": "Ignore unknown dicom tags when parsing dicom files"
    })
    encodings: List[str] = Field([], argparse_opts={
        "nargs": "+",
        "help": "Set character encoding aliases. E.g. win_1251=cp1251",
    })
    de_identify: bool = Field(False, argparse_opts={
        "help": "De-identify DICOM files",
    })
    deid_profile: str = Field("minimal", argparse_opts={
        "metavar": "NAME",
        "help": "Use the De-identify profile by name",
    })
    deid_profiles: List[Any] = Field([], argparse_opts={"skip": True})
    skip_existing: bool = Field(False, argparse_opts={
        "help": "Skip import of existing files",
    })
    no_audit_log: bool = Field(False, argparse_opts={
        "help": "Skip uploading audit log to the target projects",
    })
    subject_config: SubjectConfig = Field(None, argparse_opts={"skip": True})
    load_subjects: str = create_field("load_subjects")
    max_retries: int = Field(3, argparse_opts={"skip": True})
    # attached mode config
    save_audit_log: str = create_field(
        "save_audit_log",
        override_argparse_opts={
            "argument_group": "attached",
            "group_opts": {
                "title": "Attached mode config",
                "description": (
                    "These config options are only available when using "
                    "cluster mode with the --follow argument "
                    "or when using local worker."
                ),
            },
        }
    )
    save_deid_log: str = create_field("save_deid_log", override_argparse_opts={"argument_group": "attached"})
    save_subjects: str = create_field("save_subjects", override_argparse_opts={"argument_group": "attached"})
    # worker config
    db_url: str = create_field("db_url", override_argparse_opts={"skip": True})
    db_check_fn: str = create_field("db_check_fn")
    jobs: int = create_field(
        "jobs",
        override_default=max(1, math.floor(multiprocessing.cpu_count() / 2)),
        override_argparse_opts={
            "argument_group": "worker",
            "group_opts": {
                "title": "Worker config",
                "description": "These config options are only available when using local worker (--cluster is not defined)",
            },
        }
    )
    sleep_time: int = create_field("sleep_time", override_argparse_opts={"argument_group": "worker"})
    max_tempfile: int = create_field("max_tempfile", override_argparse_opts={"argument_group": "worker"})
    buffer_size: int = create_field("buffer_size", override_argparse_opts={"argument_group": "worker"})
    worker_name: str = create_field("worker_name", override_argparse_opts={"skip": True})
    # cluster config
    cluster: str = Field(None, argparse_opts={
        "argument_group": "cluster",
        "group_opts": {
            "title": "Cluster config",
            "description": "These config options apply when using a cluster to ingest data.",
        },
        "help": "Ingest cluster url",
    })
    follow: bool = Field(False, argparse_opts={
        "flags": ["-f", "--follow"],
        "argument_group": "cluster",
        "help": "Follow the progress of the ingest",
    })

    @validator("compression_level")
    def validate_compression_level(cls, val):  # pylint: disable=no-self-argument, no-self-use
        """Validate compression level."""
        if val not in range(-1, 9):
            raise ValueError("Compression level needs to be between 0-9")
        return val

    def create_walker(self, fs_url, **kwargs):
        """Create walker"""
        for key in ("include", "exclude", "include_dirs", "exclude_dirs"):
            kwargs[key] = util.merge_lists(kwargs.get(key, []), getattr(self, key, []))
        kwargs.setdefault("follow_symlinks", self.symlinks)

        return walker.create_walker(fs_url, **kwargs)

    def register_encoding_aliases(self):
        """Register common encoding aliases"""
        import encodings  # pylint: disable=import-outside-toplevel
        for encoding_spec in self.encodings:
            key, _, value = encoding_spec.partition('=')
            encodings.aliases.aliases[key.strip().lower()] = value.strip().lower()

    def get_compression_type(self):
        """Returns compression type"""
        if self.compression_level == 0:
            return zipfile.ZIP_STORED
        return zipfile.ZIP_DEFLATED

    def save_ingest_operation_url(self, ingest_id):
        """Save ingest operation url to the ingest config file.
        It makes possible to use the ingest manager subcommand like `ingest follow` without parameters.
        """
        if not self.cluster:
            raise ConfigError("Saving ingest operation url only supported when using ingest cluster")
        # Ensure directory exists
        config_dir = os.path.dirname(INGEST_CONFIG_PATH)
        os.makedirs(config_dir, exist_ok=True)
        ingest_operation_url = f"{self.cluster}/ingests/{ingest_id}"
        with open(INGEST_CONFIG_PATH, "w") as f:
            yaml = YAML()
            yaml.dump({"ingest_operation_url": ingest_operation_url}, f)
        return ingest_operation_url


class ConfigError(ValueError):
    """ConfigError"""
