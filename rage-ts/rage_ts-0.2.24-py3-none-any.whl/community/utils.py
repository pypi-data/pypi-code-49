import argparse
import asyncio  # pytype: disable=pyi-error
import datetime
import decimal
import json
import logging
import os
import random
import re
import string
import tempfile
import typing
from hashlib import md5
from pathlib import Path
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Set,
    Text,
    TextIO,
    Tuple,
    Union,
    Callable,
    NamedTuple,
    Sequence,
    Collection,
    Awaitable,
)

import dateutil.parser
import isodate
import requests
import ruamel.yaml as yaml
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rasa.utils.io import DEFAULT_ENCODING
from packaging import version
from ruamel.yaml.comments import CommentedMap
from sanic import response, Sanic
from sanic.request import File, Request
from sanic.response import HTTPResponse
from sanic.views import CompositionView
from sqlalchemy.ext.declarative import DeclarativeMeta

import rasa.cli.utils as rasa_cli_utils
import rasa.utils.common as rasa_utils
import rasa.utils.io as rasa_io_utils
import ragex.community
from ragex.community.api import json_schema
from ragex.community.constants import CONFIG_FILE_TERMS_KEY, DEFAULT_RASA_ENVIRONMENT

if typing.TYPE_CHECKING:
    from rasa.utils.endpoints import EndpointConfig

logger = logging.getLogger(__name__)


# SQL query result containing the result and the count
class QueryResult(NamedTuple):
    result: Union[Dict, List[Dict[Text, Any]]]
    count: int

    def __len__(self) -> int:
        """Return query count.

        Implemented here to override tuple's default __len__ which would return
        the amount of elements in the tuple (which could be misleading).
        """
        return self.count


def get_columns_from_fields(fields: Optional[List[Tuple[Text, bool]]]) -> List[Text]:
    """Get column names from field query which are explicitly included."""
    if fields:
        return [k.rsplit(".", 1)[-1] for k, v in fields if v]
    else:
        return []


def get_query_selectors(
    table: DeclarativeMeta, fields: List[Text]
) -> List[DeclarativeMeta]:
    """Create select statement based on fields list."""
    if fields:
        return [table.__table__.c[f] for f in fields]
    else:
        return [table]


def query_result_to_dict(
    query_result: List[Optional[Text]], fields: List[Tuple[Text, bool]]
) -> Dict[Text, Text]:
    """Convert row to dictionary matching the structure of the field queries.

    A result `["John Doe", 42] and a field query
    `[("username", True), ("user.age", True)]` would be converted to
    `{"username": "John Doe", "user": {"age": 42}}`.

    """
    fields = [k for k, v in fields if v]
    result = {}

    for i, f in enumerate(fields):
        _dot_notation_to_dict(result, f, query_result[i])

    return result


def _dot_notation_to_dict(dictionary: Dict, keys: Text, item: Any) -> None:
    """Creates a dictionary structure matching the given field query."""
    if "." in keys:
        key, rest = keys.split(".", 1)
        if key not in dictionary:
            dictionary[key] = {}
        _dot_notation_to_dict(dictionary[key], rest, item)
    else:
        dictionary[keys] = item


def filter_fields_from_dict(dictionary: Dict, fields: List[Tuple[Text, bool]]):
    """Gets only the specified fields from a dictionary."""

    # Create a dictionary which resembles our desired structure
    selector_dict = query_result_to_dict([None] * len(fields), fields)

    return common_items(dictionary, selector_dict)


def common_items(d1: Dict, d2: Dict):
    """Recursively get common parts of the dictionaries."""

    return {
        k: common_items(d1[k], d2[k]) if isinstance(d1[k], dict) else d1[k]
        for k in d1.keys() & d2.keys()
    }


def _get_json_hash(hashable):
    """Get hash of the dictionary's json representation.

    `hashable` must be json-serializable."""
    try:
        return hash(json.dumps(hashable))
    except TypeError:
        logger.exception(
            "Could not json-serialise object {} of type {}.".format(
                hashable, type(hashable)
            )
        )
        return None


def float_arg(
    request: Request, key: Text, default: Optional[float] = None
) -> Optional[float]:
    arg = default_arg(request, key, default)

    if arg is default:
        return arg

    try:
        return float(arg)
    except (ValueError, TypeError):
        logger.warning(f"Failed to convert '{arg}' to `float`.")
        return default


def int_arg(
    request: Request, key: Text, default: Optional[int] = None
) -> Optional[int]:
    arg = default_arg(request, key, default)

    if arg is default:
        return arg

    try:
        return int(arg)
    except (ValueError, TypeError):
        logger.warning(f"Failed to convert '{arg}' to `int`.")
        return default


def time_arg(
    request: Request, key: Text, default: Optional[float] = None
) -> Optional[float]:
    """Return the value of a time query parameter.

    Returns `None` if no valid query parameter was found.
    Supports Unix format or ISO 8601."""
    arg = default_arg(request, key, default)

    # Unix format, e.g. 1541189171.389349
    try:
        return float(arg)
    except (ValueError, TypeError):
        pass

    # ISO 8601 format
    try:
        dt = dateutil.parser.parse(arg)
        return dt.timestamp()
    except (ValueError, TypeError):
        return None


def duration_to_seconds(duration_string: Optional[Text]) -> Optional[float]:
    """Return the value of a duration query parameter.

    Returns `None` if no valid query parameter was found.
    Supports durations in ISO 8601 format"""
    try:
        t_delta = isodate.parse_duration(duration_string)
        if isinstance(t_delta, isodate.Duration):
            t_delta = t_delta.totimedelta(start=datetime.datetime.now())
        return t_delta.total_seconds()
    except (isodate.ISO8601Error, TypeError):
        return None


def bool_arg(request: Request, name: Text, default: bool = True) -> bool:
    d = str(default)

    return request.args.get(name, d).lower() == "true"


def default_arg(
    request: Request, key: Text, default: Optional[Any] = None
) -> Optional[Any]:
    """Return an argument of the request or a default.

    Checks the `name` parameter of the request if it contains a value.
    If not, `default` is returned."""

    found = request.args.get(key, None)
    if found is not None:
        return found
    else:
        return default


def deployment_environment_from_request(
    request: Request, default: Text = DEFAULT_RASA_ENVIRONMENT
) -> Text:
    """Get deployment environment from environment query parameter."""

    return default_arg(
        request, "environment", default  # pytype: disable=bad-return-type
    )


def extract_numeric_value_from_header(
    request: Request, header: Text, key: Text
) -> Optional[float]:
    """Extract numeric value from request header `header: key=value`."""

    request_header = request.headers.get(header)

    if not request_header:
        return None

    try:
        return float(request_header.split(f"{key}=")[-1])
    except (ValueError, TypeError):
        return None


def fields_arg(request: Request, possible_fields: Set[Text]) -> List[Tuple[str, bool]]:
    """Looks for the `fields` parameter in the request, which contains

    the fields for filtering. Returns the set
    of fields that are part of `possible_fields` and are also in the
    query. `possible_fields` is a set of strings, each of the form `a.b.c`.
    Ex: a query of `?fields[a][b][c]=false` yields
    `[('a.b.c', False)]`."""

    # create a list of keys, e.g. for `?fields[a][b]=true`
    # we have an element `fields[a][b]`
    keys = [k for k in request.args.keys() if "fields" in k]

    # get the bool values for these fields, store in list of 2-tuples
    # [(key, True/False), (...)]
    data = []
    for k in keys:
        # get the bool value
        b = bool_arg(request, k)

        # translate the key to a tuple representing the nested structure
        # fields[a][b]=true becomes ("a.b", True)
        # get the content between brackets, [<CONTENT>], as a list
        d = re.findall(r"\[(.*?)\]", k)

        if d and d[0]:
            data.append((".".join(d), b))

    # finally, return only those entries in data whose key is in
    # the set of possible keys
    out = []
    for d in data:
        if d[0] in possible_fields:
            out.append(d)
        else:
            logger.warning(
                "Cannot add field {}, as it is not part of `possible_fields` {}".format(
                    d[0], possible_fields
                )
            )
    return out


def list_arg(request, key, delimiter=","):
    """Return an argument of the request separated into a list or None."""

    found = request.raw_args.get(key)
    if found is not None:
        return found.split(delimiter)
    else:
        return None


def list_routes(app):
    """List all the routes of a sanic application.

    Mainly used for debugging.
    """

    from urllib.parse import unquote

    output = []
    for endpoint, route in app.router.routes_all.items():
        if endpoint[:-1] in app.router.routes_all and endpoint[-1] == "/":
            continue

        options = {}
        for arg in route.parameters:
            options[arg] = f"[{arg}]"

        methods = ",".join(route.methods)
        if not isinstance(route.handler, CompositionView):
            handlers = [route.name]
        else:
            handlers = {v.__name__ for v in route.handler.handlers.values()}
        name = ", ".join(handlers)
        line = unquote(f"{endpoint:40s} {methods:20s} {name}")
        output.append(line)

    for line in sorted(output):
        print(line)


def check_schema(schema_identifier: Text, data: Dict) -> bool:
    try:
        validate(data, json_schema[schema_identifier])
        return True
    except ValidationError:
        return False


def write_bytes_to_file(filename: str, data: bytes) -> None:
    """Write the data (byte array) to the filename."""

    with open(filename, "wb") as f:
        f.write(data)


def dump_yaml(content: Any) -> Optional[str]:
    """Dump content to yaml."""

    _content = CommentedMap(content)
    return yaml.round_trip_dump(_content, default_flow_style=False)


def dump_as_yaml_to_temporary_file(data: Dict) -> Optional[Text]:
    """Dump `data` as yaml to a temporary file."""

    content = dump_yaml(data)
    return rasa_io_utils.create_temporary_file(content)


def extract_partial_endpoint_config(
    endpoint_config_path: Text, key: Text
) -> Optional["EndpointConfig"]:
    """Extracts partial endpoint config at `key`.

    Args:
        endpoint_config_path: Path to endpoint config file to read.
        key: Endpoint config key (section) to extract.

    Returns:
        Endpoint config initialised only from `key`.

    """
    from rasa.utils import endpoints

    # read endpoint config file and create dictionary containing only one
    # key-value pair
    content = rasa_io_utils.read_file(endpoint_config_path)
    endpoint_dict = {key: load_yaml(content)[key]}

    # dump this sub-dictionary to a temporary file and load endpoint config from it
    temp_path = dump_as_yaml_to_temporary_file(endpoint_dict)

    return endpoints.read_endpoint_config(temp_path, key)


# unlike rasa.utils.io's yaml writing method, this one
# uses round_trip_dump() which preserves key order and doesn't print yaml markers
def dump_yaml_to_file(filename: Union[Text, Path], content: Any) -> None:
    """Dump content to yaml."""
    write_text_to_file(filename, dump_yaml(content))


def write_text_to_file(filename: Union[Text, Path], content: Text) -> None:
    """Writes text to a file."""

    from rasa.utils import io as io_utils

    # Create parent directories
    io_utils.create_path(filename)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


def load_yaml(content: Union[str, TextIO]) -> Any:
    """Load content from yaml."""
    return yaml.round_trip_load(content)


def file_as_bytes(path: str) -> bytes:
    """Read in a file as a byte array."""
    with open(path, "rb") as f:
        return f.read()


def get_file_hash(path: str) -> str:
    """Calculate the md5 hash of a file."""
    return get_text_hash(file_as_bytes(path))


def get_text_hash(text: Optional[Union[str, bytes]]) -> str:
    """Calculate the md5 hash of a string."""
    if text is None:
        text = b""
    elif not isinstance(text, bytes):
        text = text.encode()
    return md5(text).hexdigest()


def secure_filename(filename: str) -> str:
    """Pass it a filename and it will return a secure version of it.

    This filename can then safely be stored on a regular file system
    and passed to :func:`os.path.join`.

    Function is adapted from
    https://github.com/pallets/werkzeug/blob/master/werkzeug/utils.py#L253

    :copyright: (c) 2014 by the Werkzeug Team, see
        https://github.com/pallets/werkzeug/blob/master/AUTHORS
        for more details.
    :license: BSD, see NOTICE for more details.
    """

    _filename_ascii_strip_re = re.compile(r"[^A-Za-z0-9_.-]")
    _windows_device_files = (
        "CON",
        "AUX",
        "COM1",
        "COM2",
        "COM3",
        "COM4",
        "LPT1",
        "LPT2",
        "LPT3",
        "PRN",
        "NUL",
    )

    if isinstance(filename, str):
        from unicodedata import normalize

        filename = normalize("NFKD", filename).encode("ascii", "ignore")
        filename = filename.decode("ascii")
    for sep in os.path.sep, os.path.altsep:
        if sep:
            filename = filename.replace(sep, " ")
    filename = str(_filename_ascii_strip_re.sub("", "_".join(filename.split()))).strip(
        "._"
    )

    # on nt a couple of special files are present in each folder.  We
    # have to ensure that the target file is not such a filename.  In
    # this case we prepend an underline
    if (
        os.name == "nt"
        and filename
        and filename.split(".")[0].upper() in _windows_device_files
    ):
        filename = "_" + filename

    return filename


def write_request_file_to_disk(_file: File, filename: Text) -> Text:
    """Write the request file to a temporary file and return the path."""

    tdir = tempfile.mkdtemp()
    tpath = os.path.join(tdir, filename)
    write_bytes_to_file(tpath, _file.body)
    return tpath


def slice_array(arr: List, offset: int, limit: int) -> List:
    """Returns array from arr with arr[offset:offset + limit]"""

    if offset:
        arr = arr[offset:]
    if limit:
        arr = arr[:limit]

    return arr


def error(
    status: int,
    reason: Text,
    message: Optional[Text] = None,
    details: Any = None,
    help_url: Optional[Text] = None,
) -> HTTPResponse:
    return response.json(
        {
            "version": ragex.community.__version__,
            "status": "failure",
            "message": message,
            "reason": reason,
            "details": details or {},
            "help": help_url,
            "code": status,
        },
        status=status,
        content_type="application/json",
    )


def random_password(password_length=12):
    """Generate a random password of length `password_length`.

    Implementation adapted from
    https://pynative.com/python-generate-random-string/.
    """

    random_source = string.ascii_letters + string.digits
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)

    for _ in range(password_length - 3):
        password += random.choice(random_source)

    password_list = list(password)

    random.SystemRandom().shuffle(password_list)

    return "".join(password_list)


class DecimalEncoder(json.JSONEncoder):
    """Json encoder that properly dumps python decimals as floats."""

    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super().default(o)


def is_enterprise_installed() -> bool:
    """Check if Rasa Enterprise is installed."""

    try:
        import ragex.enterprise

        return True
    except ImportError:
        return False


def update_log_level():
    """Set the log level to log level defined in config."""

    from ragex.community.config import log_level

    logging.basicConfig(level=log_level)
    logging.getLogger("ragex").setLevel(log_level)

    packages = ["rasa", "apscheduler"]
    for p in packages:
        # update log level of package
        logging.getLogger(p).setLevel(log_level)
        # set propagate to 'False' so that logging messages are not
        # passed to the handlers of ancestor loggers.
        logging.getLogger(p).propagate = False

    from sanic.log import logger, error_logger, access_logger

    logger.setLevel(log_level)
    error_logger.setLevel(log_level)
    access_logger.setLevel(log_level)

    logger.propagate = False
    error_logger.propagate = False
    access_logger.propagate = False


def _get_newer_stable_version(all_versions, current_version):
    most_recent_version = version.parse(current_version)
    for v in all_versions:
        parsed = version.parse(v)
        if not parsed.is_prerelease and parsed > most_recent_version:
            most_recent_version = parsed
    return str(most_recent_version)


def check_for_updates(timeout: Union[int, float] = 1) -> None:
    """Check whether there is a newer version of Rage X."""
    try:
        current_version = ragex.community.__version__
        rasa_cli_utils.print_info(f"current Rage X version:{current_version}")
        # resp = requests.get("http://pypi.rasa.com/api/package/rasa-x", timeout=timeout)
        # resp.raise_for_status()
        # all_versions = [package["version"] for package in resp.json()["packages"]]
        # # Check if there's a stable version newer than the current version
        # newest_stable_version = _get_newer_stable_version(all_versions, current_version)
        # if newest_stable_version != current_version:
        #     rasa_cli_utils.print_info(
        #         f"You are using an outdated version of Rasa X ({current_version}).\n"
        #         f"You should consider upgrading via the command:\npip3 install "
        #         f"--upgrade rasa-x --extra-index-url https://pypi.rasa.com/simple"
        #     )
    except Exception as e:
        logger.debug(
            f"Could not fetch updates from PyPI about newer versions of Rasa X: {e}"
        )


def are_terms_accepted() -> Optional[bool]:
    """Check whether the user already accepted the term."""

    return rasa_utils.read_global_config_value(CONFIG_FILE_TERMS_KEY)


def accept_terms_or_quit(args: argparse.Namespace) -> None:
    """Prompt the user to accept the Rasa terms."""

    import webbrowser
    import questionary
    from ragex.community.constants import RASA_TERMS_URL

    show_prompt = not hasattr(args, "no_prompt") or not args.no_prompt

    if not show_prompt:
        print(
            f"By adding the '--no_prompt' parameter you agreed to the Rasa "
            f"X license agreement ({RASA_TERMS_URL})"
        )
        return

    rasa_cli_utils.print_success(
        "Before you can use Rasa X, you have to agree to its "
        "license agreement (you will only have to do this "
        "once)."
    )

    should_open_in_browser = questionary.confirm(
        "Would you like to view the license agreement in your web browser?"
    ).ask()

    if should_open_in_browser:
        webbrowser.open(RASA_TERMS_URL)

    accepted_terms = questionary.confirm(
        "\nRasa X CE License Agreement\n"
        "===========================\n\n"
        "Do you agree to the Rasa X CE license agreement ({})?\n"
        "By typing 'y', you agree to the terms. "
        "If you are using this software for a company, by confirming, "
        "you acknowledge you have the authority to do so.\n"
        "If you do not agree, type 'n' to stop Rasa X."
        "".format(RASA_TERMS_URL),
        default=False,
        qmark="",
    ).ask()

    if accepted_terms:
        rasa_utils.write_global_config_value(CONFIG_FILE_TERMS_KEY, True)
    else:
        rasa_cli_utils.print_error_and_exit(
            "Sorry, without accepting the terms, you cannot use Rasa X. "
            "You can of course still use the (Apache 2 licensed) Rasa framework: "
            "https://github.com/RasaHQ/rasa",
            exit_code=0,
        )


def run_operation_in_single_sanic_worker(
    app: Sanic, f: Union[Callable[[], Union[None, Awaitable]]]
) -> None:
    """Run operation `f` in a single Sanic worker."""

    from multiprocessing.sharedctypes import Value
    from ctypes import c_bool

    lock = Value(c_bool, False)

    async def execute():
        if lock.value:
            return

        with lock.get_lock():
            lock.value = True

        if asyncio.iscoroutinefunction(f):
            await f()
        else:
            f()

    app.add_task(execute)


def truncate_float(_float: float, decimal_places: int = 4) -> float:
    """Truncate float to `decimal_places` after the decimal separator."""

    return float(f"%.{decimal_places}f" % _float)


def add_plural_suffix(s: Text, obj: Union[Sequence, Collection]) -> Text:
    """Add plural suffix to replacement field in string `s`.

    The plural suffix is based on `obj` having a length greater than 1.
    """

    is_plural = len(obj) > 1
    return s.format("s" if is_plural else "")


def decode_base64(encoded: Text, encoding: Text = "utf-8") -> Text:
    """Decodes a base64-encoded string."""

    import base64

    return base64.b64decode(encoded).decode(encoding)


def encode_base64(original: Text, encoding: Text = "utf-8") -> Text:
    """Encodes a string to base64."""

    import base64

    return base64.b64encode(original.encode(encoding)).decode(encoding)


def in_continuous_integration() -> bool:
    """Returns `True` if currently running inside a continuous integration context (e.g.
    Travis CI)."""
    return "CI" in os.environ or "TRAVIS" in os.environ


def set_project_directory(directory: Union[Path, Text]) -> None:
    """Sets the path to the current project directory."""

    from ragex.community import config

    with config.PROJECT_DIRECTORY.get_lock():
        config.PROJECT_DIRECTORY.value = str(directory).encode(DEFAULT_ENCODING)


def get_project_directory() -> Path:
    """Returns the path to the current project directory."""

    from ragex.community import config

    if not config.PROJECT_DIRECTORY.value:
        return Path()
    else:
        return Path(config.PROJECT_DIRECTORY.value.decode(DEFAULT_ENCODING))


def should_dump() -> bool:
    """Whether data should be dumped to disk."""

    from ragex.community import config

    return bool(config.PROJECT_DIRECTORY.value)


def is_git_available() -> bool:
    """Checks if `git` is available in the current environment.

    Returns:
        `True` in case `git` is available, otherwise `False`.
    """

    try:
        import git

        return True
    except ImportError as e:
        logger.error(
            f"An error happened when trying to import the Git library. "
            f"Possible reasons are that Git is not installed or the "
            f"`git` executable cannot be found. 'Integrated Version Control' "
            f"won't be available until this is fixed. Details: {str(e)}"
        )
    return False


def get_uptime() -> float:
    """Return the process uptime in seconds.

    Returns:
        Number of seconds elapsed since this process has started. More
        specifically, get the number of seconds elapsed since the `config`
        module was imported for the first time.
    """
    from ragex.community import config
    import time

    return time.time() - config.PROCESS_START
