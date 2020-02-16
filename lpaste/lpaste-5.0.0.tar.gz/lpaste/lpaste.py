import os
import sys
import re
import getpass
import argparse
import logging
import socket
import functools
import http.client

import pkg_resources
import webbrowser
import requests
import keyring

from .source import CodeSource, FileSource
from . import clipboard

version = pkg_resources.require('lpaste')[0].version
session = requests.Session()
log = logging.getLogger(__name__)

py_version = re.sub(r'\s*\n\s*', '; ', sys.version, re.M)
agent = 'lpaste ({version}) Python ({py_version})'.format(**locals())
session.headers['User-Agent'] = agent


def log_level(level_str):
    return getattr(logging, level_str.upper())


def _resolve_url():
    return os.environ.get('LIBRARYPASTE_URL') or _default_url()


def _default_url():
    """
    If 'paste' resolves, use the hostname to which it resolves.
    """
    name, aliaslist, addresslist = socket.gethostbyname_ex('paste')
    name = _patch_heroku(name, aliaslist)
    return 'https://{name}/'.format(name=name)


def _patch_heroku(name, aliases):
    """
    Heroku will resolve its host to a name which fails SSL validation. Find a
    preferable name from the aliases.
    """
    if name.endswith('.route.herokuapp.com'):
        matches = filter(re.compile(r'[^.]*\.herokuapp\.com').match, aliases)
        name = next(matches, name)
    return name


def get_options():
    default_url = _resolve_url()
    default_user = os.environ.get('LIBRARYPASTE_USER', getpass.getuser())

    description = "version {version}".format(**globals())

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        '-s',
        '--site',
        dest='site',
        default=default_url,
        help="URL for the library paste site to use. By default: %s" % default_url,
    )
    parser.add_argument(
        '-t',
        '--format',
        dest='format',
        default='_',
        help="Which syntax code highlighter would you like to use? "
        "Defaults to plain text.",
    )
    parser.add_argument(
        '-u',
        '--username',
        dest='username',
        default=default_user,
        help="Username to paste as, attempts to "
        "use system account name if none specified.",
    )
    parser.add_argument(
        '-l',
        '--longurl',
        dest='longurl',
        action="store_true",
        default=False,
        help="Use a long url instead of the default short",
    )
    parser.add_argument(
        '-a',
        '--attach',
        dest='attach',
        action="store_true",
        default=False,
        help="Upload the file as an attachment instead of as code/text",
    )
    parser.add_argument(
        '-b',
        '--browser',
        dest='browser',
        action="store_true",
        default=False,
        help="Open your paste in a new browser window after it's " "uploaded",
    )
    parser.add_argument(
        '-c',
        '--clipboard',
        action="store_true",
        default=False,
        help="Get the input from the clipboard",
    )
    parser.add_argument(
        '--auth-username',
        default=default_user,
        help="The username to use when HTTP auth is required",
    )
    parser.add_argument('--log-level', default=logging.WARNING, type=log_level)
    parser.add_argument(
        'file', nargs='?', help="If file is not supplied, stdin will be used."
    )
    parser.add_argument(
        '--auth-password', help="The password to use when HTTP auth is required",
    )
    options = parser.parse_args()
    if options.file and options.clipboard:
        parser.error("Either supply a file or --clipboard, but not both")
    if options.clipboard:
        source = clipboard.get_source()
    else:
        use_stdin = options.file in (None, '-')
        stream = open(options.file, 'rb') if not use_stdin else sys.stdin
        filename = os.path.basename(options.file) if not use_stdin else None
        if options.attach:
            source = FileSource(stream, filename=filename)
        else:
            source = CodeSource(stream.read())

    options.source = source
    if hasattr(source, 'format'):
        options.format = source.format
    return options


def parse_auth_realm(resp):
    """
    From a 401 response, parse out the realm for basic auth.
    """
    header = resp.headers['www-authenticate']
    mode, _sep, dict = header.partition(' ')
    assert mode.lower() == 'basic'
    return requests.utils.parse_dict_header(dict)['realm']


def get_auth(options, realm):
    username = options.auth_username
    password = (
        keyring.get_password(realm, username)
        or options.auth_password
        or getpass.getpass()
    )
    return username, password


def configure_logging(level):
    logging.basicConfig(level=level)

    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(level)
    requests_log.propagate = True

    # enable debugging at http.client level (requests->urllib3->http.client)
    http.client.HTTPConnection.debuglevel = level <= logging.DEBUG


def detect_auth(url, resolver):
    """
    Load the root URL to determine if auth is required. `resolver` should
    resolve a realm to an auth parameter.

    Return an auth parameter suitable for a request parameter.
    """
    resp = session.get(url)
    if resp.status_code != 401:
        return None
    realm = parse_auth_realm(resp)
    return resolver(realm)


def main():

    options = get_options()
    configure_logging(options.log_level)

    log.info("Using {site}".format(**vars(options)))

    paste_url = options.site
    data = {
        'nick': options.username,
        'fmt': options.format,
    }
    if not options.longurl:
        data['makeshort'] = 'True'
    files = options.source.apply(data)

    resolver = functools.partial(get_auth, options)
    auth = detect_auth(paste_url, resolver)
    resp = session.post(paste_url, data=data, files=files, auth=auth)
    resp.raise_for_status()
    url = resp.url
    clipboard.set_text(url)
    print('Paste URL:', url)
    if options.browser:
        print("Now opening browser...")
        webbrowser.open(url)


def get_realm(authenticate_header):
    pattern = re.compile(r'\w+ realm="(?P<realm>.*)"')
    res = pattern.match(authenticate_header)
    return res.groupdict()['realm']


if __name__ == '__main__':
    main()
