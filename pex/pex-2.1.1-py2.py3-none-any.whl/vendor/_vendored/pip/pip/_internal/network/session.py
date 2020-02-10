"""PipSession and supporting code, containing all pip-specific
network request configuration and behavior.
"""

# The following comment should be removed at some point in the future.
# mypy: disallow-untyped-defs=False

import email.utils
import json
import logging
import mimetypes
import os
import platform
import sys
import warnings

from pip._vendor import requests, six, urllib3
from pip._vendor.cachecontrol import CacheControlAdapter
from pip._vendor.requests.adapters import BaseAdapter, HTTPAdapter
from pip._vendor.requests.models import Response
from pip._vendor.requests.structures import CaseInsensitiveDict
from pip._vendor.six.moves.urllib import parse as urllib_parse
from pip._vendor.urllib3.exceptions import InsecureRequestWarning

from pip import __version__
from pip._internal.network.auth import MultiDomainBasicAuth
from pip._internal.network.cache import SafeFileCache
# Import ssl from compat so the initial import occurs in only one place.
from pip._internal.utils.compat import has_tls, ipaddress
from pip._internal.utils.filesystem import check_path_owner
from pip._internal.utils.glibc import libc_ver
from pip._internal.utils.misc import (
    build_url_from_netloc,
    get_installed_version,
    parse_netloc,
)
from pip._internal.utils.typing import MYPY_CHECK_RUNNING
from pip._internal.utils.urls import url_to_path

if MYPY_CHECK_RUNNING:
    from typing import (
        Iterator, List, Optional, Tuple, Union,
    )

    from pip._internal.models.link import Link

    SecureOrigin = Tuple[str, str, Optional[Union[int, str]]]


logger = logging.getLogger(__name__)


# Ignore warning raised when using --trusted-host.
warnings.filterwarnings("ignore", category=InsecureRequestWarning)


SECURE_ORIGINS = [
    # protocol, hostname, port
    # Taken from Chrome's list of secure origins (See: http://bit.ly/1qrySKC)
    ("https", "*", "*"),
    ("*", "localhost", "*"),
    ("*", "127.0.0.0/8", "*"),
    ("*", "::1/128", "*"),
    ("file", "*", None),
    # ssh is always secure.
    ("ssh", "*", "*"),
]  # type: List[SecureOrigin]


# These are environment variables present when running under various
# CI systems.  For each variable, some CI systems that use the variable
# are indicated.  The collection was chosen so that for each of a number
# of popular systems, at least one of the environment variables is used.
# This list is used to provide some indication of and lower bound for
# CI traffic to PyPI.  Thus, it is okay if the list is not comprehensive.
# For more background, see: https://github.com/pypa/pip/issues/5499
CI_ENVIRONMENT_VARIABLES = (
    # Azure Pipelines
    'BUILD_BUILDID',
    # Jenkins
    'BUILD_ID',
    # AppVeyor, CircleCI, Codeship, Gitlab CI, Shippable, Travis CI
    'CI',
    # Explicit environment variable.
    'PIP_IS_CI',
)


def looks_like_ci():
    # type: () -> bool
    """
    Return whether it looks like pip is running under CI.
    """
    # We don't use the method of checking for a tty (e.g. using isatty())
    # because some CI systems mimic a tty (e.g. Travis CI).  Thus that
    # method doesn't provide definitive information in either direction.
    return any(name in os.environ for name in CI_ENVIRONMENT_VARIABLES)


def user_agent():
    """
    Return a string representing the user agent.
    """
    data = {
        "installer": {"name": "pip", "version": __version__},
        "python": platform.python_version(),
        "implementation": {
            "name": platform.python_implementation(),
        },
    }

    if data["implementation"]["name"] == 'CPython':
        data["implementation"]["version"] = platform.python_version()
    elif data["implementation"]["name"] == 'PyPy':
        if sys.pypy_version_info.releaselevel == 'final':
            pypy_version_info = sys.pypy_version_info[:3]
        else:
            pypy_version_info = sys.pypy_version_info
        data["implementation"]["version"] = ".".join(
            [str(x) for x in pypy_version_info]
        )
    elif data["implementation"]["name"] == 'Jython':
        # Complete Guess
        data["implementation"]["version"] = platform.python_version()
    elif data["implementation"]["name"] == 'IronPython':
        # Complete Guess
        data["implementation"]["version"] = platform.python_version()

    if sys.platform.startswith("linux"):
        from pip._vendor import distro
        distro_infos = dict(filter(
            lambda x: x[1],
            zip(["name", "version", "id"], distro.linux_distribution()),
        ))
        libc = dict(filter(
            lambda x: x[1],
            zip(["lib", "version"], libc_ver()),
        ))
        if libc:
            distro_infos["libc"] = libc
        if distro_infos:
            data["distro"] = distro_infos

    if sys.platform.startswith("darwin") and platform.mac_ver()[0]:
        data["distro"] = {"name": "macOS", "version": platform.mac_ver()[0]}

    if platform.system():
        data.setdefault("system", {})["name"] = platform.system()

    if platform.release():
        data.setdefault("system", {})["release"] = platform.release()

    if platform.machine():
        data["cpu"] = platform.machine()

    if has_tls():
        import _ssl as ssl
        data["openssl_version"] = ssl.OPENSSL_VERSION

    setuptools_version = get_installed_version("setuptools")
    if setuptools_version is not None:
        data["setuptools_version"] = setuptools_version

    # Use None rather than False so as not to give the impression that
    # pip knows it is not being run under CI.  Rather, it is a null or
    # inconclusive result.  Also, we include some value rather than no
    # value to make it easier to know that the check has been run.
    data["ci"] = True if looks_like_ci() else None

    user_data = os.environ.get("PIP_USER_AGENT_USER_DATA")
    if user_data is not None:
        data["user_data"] = user_data

    return "{data[installer][name]}/{data[installer][version]} {json}".format(
        data=data,
        json=json.dumps(data, separators=(",", ":"), sort_keys=True),
    )


class LocalFSAdapter(BaseAdapter):

    def send(self, request, stream=None, timeout=None, verify=None, cert=None,
             proxies=None):
        pathname = url_to_path(request.url)

        resp = Response()
        resp.status_code = 200
        resp.url = request.url

        try:
            stats = os.stat(pathname)
        except OSError as exc:
            resp.status_code = 404
            resp.raw = exc
        else:
            modified = email.utils.formatdate(stats.st_mtime, usegmt=True)
            content_type = mimetypes.guess_type(pathname)[0] or "text/plain"
            resp.headers = CaseInsensitiveDict({
                "Content-Type": content_type,
                "Content-Length": stats.st_size,
                "Last-Modified": modified,
            })

            resp.raw = open(pathname, "rb")
            resp.close = resp.raw.close

        return resp

    def close(self):
        pass


class InsecureHTTPAdapter(HTTPAdapter):

    def cert_verify(self, conn, url, verify, cert):
        super(InsecureHTTPAdapter, self).cert_verify(
            conn=conn, url=url, verify=False, cert=cert
        )


class PipSession(requests.Session):

    timeout = None  # type: Optional[int]

    def __init__(self, *args, **kwargs):
        """
        :param trusted_hosts: Domains not to emit warnings for when not using
            HTTPS.
        """
        retries = kwargs.pop("retries", 0)
        cache = kwargs.pop("cache", None)
        trusted_hosts = kwargs.pop("trusted_hosts", [])  # type: List[str]
        index_urls = kwargs.pop("index_urls", None)

        super(PipSession, self).__init__(*args, **kwargs)

        # Namespace the attribute with "pip_" just in case to prevent
        # possible conflicts with the base class.
        self.pip_trusted_origins = []  # type: List[Tuple[str, Optional[int]]]

        # Attach our User Agent to the request
        self.headers["User-Agent"] = user_agent()

        # Attach our Authentication handler to the session
        self.auth = MultiDomainBasicAuth(index_urls=index_urls)

        # Create our urllib3.Retry instance which will allow us to customize
        # how we handle retries.
        retries = urllib3.Retry(
            # Set the total number of retries that a particular request can
            # have.
            total=retries,

            # A 503 error from PyPI typically means that the Fastly -> Origin
            # connection got interrupted in some way. A 503 error in general
            # is typically considered a transient error so we'll go ahead and
            # retry it.
            # A 500 may indicate transient error in Amazon S3
            # A 520 or 527 - may indicate transient error in CloudFlare
            status_forcelist=[500, 503, 520, 527],

            # Add a small amount of back off between failed requests in
            # order to prevent hammering the service.
            backoff_factor=0.25,
        )

        # Check to ensure that the directory containing our cache directory
        # is owned by the user current executing pip. If it does not exist
        # we will check the parent directory until we find one that does exist.
        if cache and not check_path_owner(cache):
            logger.warning(
                "The directory '%s' or its parent directory is not owned by "
                "the current user and the cache has been disabled. Please "
                "check the permissions and owner of that directory. If "
                "executing pip with sudo, you may want sudo's -H flag.",
                cache,
            )
            cache = None

        # We want to _only_ cache responses on securely fetched origins. We do
        # this because we can't validate the response of an insecurely fetched
        # origin, and we don't want someone to be able to poison the cache and
        # require manual eviction from the cache to fix it.
        if cache:
            secure_adapter = CacheControlAdapter(
                cache=SafeFileCache(cache),
                max_retries=retries,
            )
        else:
            secure_adapter = HTTPAdapter(max_retries=retries)

        # Our Insecure HTTPAdapter disables HTTPS validation. It does not
        # support caching (see above) so we'll use it for all http:// URLs as
        # well as any https:// host that we've marked as ignoring TLS errors
        # for.
        insecure_adapter = InsecureHTTPAdapter(max_retries=retries)
        # Save this for later use in add_insecure_host().
        self._insecure_adapter = insecure_adapter

        self.mount("https://", secure_adapter)
        self.mount("http://", insecure_adapter)

        # Enable file:// urls
        self.mount("file://", LocalFSAdapter())

        for host in trusted_hosts:
            self.add_trusted_host(host, suppress_logging=True)

    def add_trusted_host(self, host, source=None, suppress_logging=False):
        # type: (str, Optional[str], bool) -> None
        """
        :param host: It is okay to provide a host that has previously been
            added.
        :param source: An optional source string, for logging where the host
            string came from.
        """
        if not suppress_logging:
            msg = 'adding trusted host: {!r}'.format(host)
            if source is not None:
                msg += ' (from {})'.format(source)
            logger.info(msg)

        host_port = parse_netloc(host)
        if host_port not in self.pip_trusted_origins:
            self.pip_trusted_origins.append(host_port)

        self.mount(build_url_from_netloc(host) + '/', self._insecure_adapter)
        if not host_port[1]:
            # Mount wildcard ports for the same host.
            self.mount(
                build_url_from_netloc(host) + ':',
                self._insecure_adapter
            )

    def iter_secure_origins(self):
        # type: () -> Iterator[SecureOrigin]
        for secure_origin in SECURE_ORIGINS:
            yield secure_origin
        for host, port in self.pip_trusted_origins:
            yield ('*', host, '*' if port is None else port)

    def is_secure_origin(self, location):
        # type: (Link) -> bool
        # Determine if this url used a secure transport mechanism
        parsed = urllib_parse.urlparse(str(location))
        origin_protocol, origin_host, origin_port = (
            parsed.scheme, parsed.hostname, parsed.port,
        )

        # The protocol to use to see if the protocol matches.
        # Don't count the repository type as part of the protocol: in
        # cases such as "git+ssh", only use "ssh". (I.e., Only verify against
        # the last scheme.)
        origin_protocol = origin_protocol.rsplit('+', 1)[-1]

        # Determine if our origin is a secure origin by looking through our
        # hardcoded list of secure origins, as well as any additional ones
        # configured on this PackageFinder instance.
        for secure_origin in self.iter_secure_origins():
            secure_protocol, secure_host, secure_port = secure_origin
            if origin_protocol != secure_protocol and secure_protocol != "*":
                continue

            try:
                addr = ipaddress.ip_address(
                    None
                    if origin_host is None
                    else six.ensure_text(origin_host)
                )
                network = ipaddress.ip_network(
                    six.ensure_text(secure_host)
                )
            except ValueError:
                # We don't have both a valid address or a valid network, so
                # we'll check this origin against hostnames.
                if (
                    origin_host and
                    origin_host.lower() != secure_host.lower() and
                    secure_host != "*"
                ):
                    continue
            else:
                # We have a valid address and network, so see if the address
                # is contained within the network.
                if addr not in network:
                    continue

            # Check to see if the port matches.
            if (
                origin_port != secure_port and
                secure_port != "*" and
                secure_port is not None
            ):
                continue

            # If we've gotten here, then this origin matches the current
            # secure origin and we should return True
            return True

        # If we've gotten to this point, then the origin isn't secure and we
        # will not accept it as a valid location to search. We will however
        # log a warning that we are ignoring it.
        logger.warning(
            "The repository located at %s is not a trusted or secure host and "
            "is being ignored. If this repository is available via HTTPS we "
            "recommend you use HTTPS instead, otherwise you may silence "
            "this warning and allow it anyway with '--trusted-host %s'.",
            origin_host,
            origin_host,
        )

        return False

    def request(self, method, url, *args, **kwargs):
        # Allow setting a default timeout on a session
        kwargs.setdefault("timeout", self.timeout)

        # Dispatch the actual request
        return super(PipSession, self).request(method, url, *args, **kwargs)
