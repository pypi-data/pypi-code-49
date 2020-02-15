"""
Class to query the Public Suffix List.

See https://publicsuffix.org/ for details.
"""

import datetime
import os
import threading
import time
import urllib.error
import urllib.request
from typing import Any, Dict, Optional, Tuple

from typing_extensions import Protocol


class Logger(Protocol):
    """Logging protocol to get debug information from the list."""

    def detail(self, *args) -> None:
        """Print detailed debug information."""
        ...

    def warning(self, *args) -> None:
        """Print a non-fatal error."""
        ...

    def error(self, *args) -> None:
        """Print a fatal error."""
        ...


ListMap = Dict[str, Any]

URL = 'https://publicsuffix.org/list/public_suffix_list.dat'


class FetchPSL(threading.Thread):
    """Thread class to refresh the cache and reload the list when out of date."""

    def __init__(self, psl: 'PublicSuffixList') -> None:
        super().__init__()
        self.psl = psl

    def run(self) -> None:
        """Check for newer version of the list, download, save, and load if available."""
        if (self.psl._populate_cache()):
            self.psl._load_cache()
        with self.psl._lock:
            self.psl._fetch_thread = None


class PublicSuffixList:
    """The Public Suffix List."""

    list_url: str
    cache_path: str
    cache_time: Optional[datetime.datetime]
    interval: datetime.timedelta
    log: Optional[Logger]
    _lock: threading.RLock
    _fetch_thread: Optional[threading.Thread]
    _suffixes: ListMap
    _exceptions: ListMap

    def __init__(self, url: str = None,
                 cache_dir: str = None, refresh_interval: datetime.timedelta = None,
                 log: Logger = None) -> None:
        self.list_url = url if (url) else URL
        self.cache_path = os.path.realpath(os.path.join(os.path.expanduser(cache_dir) if (cache_dir) else '.', 'public_suffix_list.dat'))
        self.cache_time = self._file_time(self.cache_path)
        self.refresh_interval = refresh_interval if (refresh_interval) else datetime.timedelta(days=1)
        self.log = log
        self._lock = threading.RLock()
        self._fetch_thread = None
        self._suffixes = {}
        self._exceptions = {}
        self._load_cache()

    def _file_time(self, file_path: str) -> Optional[datetime.datetime]:
        if (os.path.isfile(file_path)):
            return datetime.datetime.fromtimestamp(os.path.getmtime(file_path), tz=datetime.timezone.utc)
        return None

    def _make_dirs(self, dir_path: str) -> None:
        if (not os.path.isdir(dir_path)):
            try:
                os.makedirs(dir_path)
            except Exception as error:
                if (self.log):
                    self.log.error('Unable to create directory:', dir_path, '-', error)
                else:
                    raise

    def _populate_cache(self) -> bool:
        request = urllib.request.Request(url=self.list_url)
        if (self.cache_time):
            request.add_header('If-Modified-Since', self.cache_time.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            pass
        try:
            if (self.log):
                self.log.detail('Fetching public suffix list from:', self.list_url)
            with urllib.request.urlopen(request) as response:
                list_bytes = response.read()
                try:
                    cache_dir = os.path.dirname(self.cache_path)
                    self._make_dirs(cache_dir)
                    temp_path = os.path.join(cache_dir, 'public_suffix_list.part')
                    with open(temp_path, 'wb') as public_suffix_list_file:
                        public_suffix_list_file.write(list_bytes)
                    os.replace(temp_path, self.cache_path)
                    if (self.log):
                        self.log.detail('Downloaded', len(list_bytes), 'bytes')
                    self.cache_time = self._file_time(self.cache_path)
                    return True
                except Exception as error:
                    if (self.log):
                        self.log.error('Unable to write public suffix list to:', self.cache_path, '-', error)
                    else:
                        raise
        except urllib.error.HTTPError as error:
            if ((400 <= error.code) and (error.code < 500)):
                if (self.log):
                    self.log.warning('Unable to retrieve public suffix list from:', self.list_url,
                                     'HTTP error:', error.code, error.reason, error.read())
            elif (304 == error.code):
                now_timestamp = time.time()
                os.utime(self.cache_path, (now_timestamp, now_timestamp))
                self.cache_time = self._file_time(self.cache_path)
                if (self.log):
                    self.log.detail('Public suffix list not modified')
            elif (self.log):
                self.log.warning('Unable to retrieve public suffix list from:', self.list_url,
                                 'HTTP error:', error.code, error.reason)
        except Exception as error:
            if (self.log):
                self.log.warning('Unable to retrieve public suffix list from:', self.list_url, '-', error)
        return False

    def _add_entry(self, entry: str) -> None:
        if (entry.startswith('!')):
            entry = entry[1:]
            list = self._exceptions
        else:
            list = self._suffixes
        entry_parts = entry.split('.')
        for part in reversed(entry_parts):
            if part not in list:
                list[part] = {}
            list = list[part]

    def _load_cache(self) -> None:
        if (not os.path.isfile(self.cache_path)):
            if (not self._populate_cache()):
                if (self.log):
                    self.log.error('Public suffix list not available')
                    return
                else:
                    raise Exception('Public suffix list is not available')

        with self._lock:
            self._suffixes = {}
            self._exceptions = {}

            with open(self.cache_path, encoding='utf-8') as public_suffix_list_file:
                lines = public_suffix_list_file.read().splitlines()
                for line in lines:
                    line = line.strip()
                    if ((not line) or line.startswith('//')):
                        continue
                    entry = line.split()[:1][0]
                    for char in entry:
                        if (127 < ord(char)):   # add punycode equivalent
                            self._add_entry(entry.encode('idna').decode('ascii'))
                            break
                    self._add_entry(entry)

    def _refresh_cache(self) -> None:
        with self._lock:
            now = datetime.datetime.now(datetime.timezone.utc)
            if (self.cache_time and ((now - self.refresh_interval) < self.cache_time)):
                return
            if (not self._fetch_thread):
                self._fetch_thread = FetchPSL(self)
                self._fetch_thread.start()

    def split_domain(self, domain_name: str) -> Tuple[str, str, str]:
        """
        Split a domain name into subdomain, registered name, and publix suffix.

        Returns a Tuple of (subdomain, registered name, public suffix).
        e.g. www.example.com -> (www, example, com)
        """
        self._refresh_cache()

        domain_name = domain_name.strip('.').lower()
        public_parts = []
        registered_part = ''
        parts = domain_name.split('.')

        with self._lock:
            list = self._suffixes
            exceptions: Optional[ListMap] = self._exceptions
            part = parts.pop() if (parts) else ''
            while part:
                if ((exceptions is not None) and (part in exceptions)):
                    exceptions = exceptions[part]
                else:
                    exceptions = None
                if ((exceptions is not None) and (not exceptions)):
                    registered_part = part
                    break
                if ('*' in list):
                    list = list['*']
                elif (part in list):
                    list = list[part]
                else:
                    registered_part = part
                    break
                public_parts.append(part)
                part = parts.pop() if (parts) else ''

        public_name = '.'.join(reversed(public_parts))
        if ('' == public_name):  # not listed in PSL
            public_name = registered_part
            registered_part = parts.pop() if (parts) else ''

        if (public_name == domain_name):
            return ('', '', public_name)
        registered_name = registered_part + '.' + public_name
        return (domain_name[:-(len(registered_name) + 1)], registered_part, public_name)

    def public_suffix(self, domain_name: str) -> str:
        """
        Return public suffix of domain name.

        e.g. www.example.com -> com
        """
        _, _, public = self.split_domain(domain_name)
        return public

    def registered_name(self, domain_name: str) -> str:
        """
        Return registered name of domain name only.

        e.g. www.example.com -> example
        """
        _, registered, _ = self.split_domain(domain_name)
        return registered

    def registered_domain_name(self, domain_name: str) -> str:
        """
        Return registered domain name.

        e.g. www.example.com -> example.com
        """
        _, registered, public = self.split_domain(domain_name)
        return (registered + '.' + public) if (registered) else public

    def split_registered_domain_name(self, domain_name: str) -> Tuple[str, str]:
        """
        Split a domain name into subdomain and registered domain.

        e.g. www.example.com -> (www, example.com)
        """
        subdomain, registered, public = self.split_domain(domain_name)
        return (subdomain, (registered + '.' + public) if (registered) else public)
