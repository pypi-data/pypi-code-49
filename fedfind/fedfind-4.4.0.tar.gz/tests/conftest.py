# Copyright (C) 2016 Red Hat
#
# This file is part of fedfind.
#
# fedfind is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Adam Williamson <awilliam@redhat.com>

# these are all kinda inappropriate for pytest patterns
# pylint: disable=old-style-class, no-init, protected-access, no-self-use, unused-argument

"""Test configuration and fixtures."""

from __future__ import unicode_literals
from __future__ import print_function

import json
import os
import re
import shutil
import subprocess
import time

import mock
import pytest
# pylint:disable=import-error
from six.moves.urllib.error import URLError, HTTPError
from six.moves.urllib.request import urlopen

import fedfind.const
import fedfind.helpers

# Fake data for the releases fixtures. This is pruned real data as of
# 2020-02-21, but with F33 (Rawhide) removed, to act as if we had no
# Branched, only stable F31 and Rawhide F32. We include samples of
# all the other release types the functions should basically ignore.
RELEASES_NOBRANCHED_JSON = [
    {
        "branch": "el6",
        "candidate_tag": "dist-6E-epel-testing-candidate",
        "composed_by_bodhi": True,
        "composes": [],
        "create_automatic_updates": None,
        "dist_tag": "dist-6E-epel",
        "id_prefix": "FEDORA-EPEL",
        "long_name": "Fedora EPEL 6",
        "mail_template": "fedora_epel_legacy_errata_template",
        "name": "EL-6",
        "override_tag": "dist-6E-epel-override",
        "package_manager": "unspecified",
        "pending_signing_tag": "",
        "pending_stable_tag": "",
        "pending_testing_tag": "",
        "stable_tag": "dist-6E-epel",
        "state": "current",
        "testing_repository": None,
        "testing_tag": "dist-6E-epel-testing",
        "version": "6"
    },
    {
        "branch": "f30m",
        "candidate_tag": "f30-modular-updates-candidate",
        "composed_by_bodhi": True,
        "composes": [],
        "create_automatic_updates": None,
        "dist_tag": "f30-modular",
        "id_prefix": "FEDORA-MODULAR",
        "long_name": "Fedora 30 Modular",
        "mail_template": "fedora_errata_template",
        "name": "F30M",
        "override_tag": "f30-modular-override",
        "package_manager": "unspecified",
        "pending_signing_tag": "f30-modular-signing-pending",
        "pending_stable_tag": "f30-modular-updates-pending",
        "pending_testing_tag": "f30-modular-updates-testing-pending",
        "stable_tag": "f30-modular-updates",
        "state": "current",
        "testing_repository": None,
        "testing_tag": "f30-modular-updates-testing",
        "version": "30"
    },
    {
        "branch": "f32",
        "candidate_tag": "f32-container-updates-candidate",
        "composed_by_bodhi": True,
        "composes": [],
        "create_automatic_updates": False,
        "dist_tag": "f32-container",
        "id_prefix": "FEDORA-CONTAINER",
        "long_name": "Fedora 32 Containers",
        "mail_template": "fedora_errata_template",
        "name": "F32C",
        "override_tag": "f32-container-override",
        "package_manager": "unspecified",
        "pending_signing_tag": "",
        "pending_stable_tag": "f32-container-updates-pending",
        "pending_testing_tag": "f32-container-updates-testing-pending",
        "stable_tag": "f32-container-updates",
        "state": "pending",
        "testing_repository": None,
        "testing_tag": "f32-container-updates-testing",
        "version": "32"
    },
    {
        "branch": "f31",
        "candidate_tag": "f31-flatpak-updates-candidate",
        "composed_by_bodhi": True,
        "composes": [],
        "create_automatic_updates": False,
        "dist_tag": "f31-flatpak",
        "id_prefix": "FEDORA-FLATPAK",
        "long_name": "Fedora 31 Flatpaks",
        "mail_template": "fedora_errata_template",
        "name": "F31F",
        "override_tag": "f31-flatpak-override",
        "package_manager": "unspecified",
        "pending_signing_tag": "",
        "pending_stable_tag": "f31-flatpak-updates-pending",
        "pending_testing_tag": "f31-flatpak-updates-testing-pending",
        "stable_tag": "f31-flatpak-updates",
        "state": "current",
        "testing_repository": None,
        "testing_tag": "f31-flatpak-updates-testing",
        "version": "31"
    },
    {
        "branch": "f21",
        "candidate_tag": "f21-updates-candidate",
        "composed_by_bodhi": True,
        "composes": [],
        "create_automatic_updates": None,
        "dist_tag": "f21",
        "id_prefix": "FEDORA",
        "long_name": "Fedora 21",
        "mail_template": "fedora_errata_template",
        "name": "F21",
        "override_tag": "f21-override",
        "package_manager": "dnf",
        "pending_signing_tag": "",
        "pending_stable_tag": "f21-updates-pending",
        "pending_testing_tag": "f21-updates-testing-pending",
        "stable_tag": "f21-updates",
        "state": "archived",
        "testing_repository": "updates-testing",
        "testing_tag": "f21-updates-testing",
        "version": "21"
    },
    {
        "branch": "f30",
        "candidate_tag": "f30-updates-candidate",
        "composed_by_bodhi": True,
        "composes": [],
        "create_automatic_updates": None,
        "dist_tag": "f30",
        "id_prefix": "FEDORA",
        "long_name": "Fedora 30",
        "mail_template": "fedora_errata_template",
        "name": "F30",
        "override_tag": "f30-override",
        "package_manager": "dnf",
        "pending_signing_tag": "f30-signing-pending",
        "pending_stable_tag": "f30-updates-pending",
        "pending_testing_tag": "f30-updates-testing-pending",
        "stable_tag": "f30-updates",
        "state": "current",
        "testing_repository": "updates-testing",
        "testing_tag": "f30-updates-testing",
        "version": "30"
    },
    {
        "branch": "f31",
        "candidate_tag": "f31-updates-candidate",
        "composed_by_bodhi": True,
        "composes": [],
        "create_automatic_updates": False,
        "dist_tag": "f31",
        "id_prefix": "FEDORA",
        "long_name": "Fedora 31",
        "mail_template": "fedora_errata_template",
        "name": "F31",
        "override_tag": "f31-override",
        "package_manager": "dnf",
        "pending_signing_tag": "f31-signing-pending",
        "pending_stable_tag": "f31-updates-pending",
        "pending_testing_tag": "f31-updates-testing-pending",
        "stable_tag": "f31-updates",
        "state": "current",
        "testing_repository": "updates-testing",
        "testing_tag": "f31-updates-testing",
        "version": "31"
    },
    {
        "branch": "f32",
        "candidate_tag": "f32-updates-candidate",
        "composed_by_bodhi": False,
        "composes": [],
        "create_automatic_updates": True,
        "dist_tag": "f32",
        "id_prefix": "FEDORA",
        "long_name": "Fedora 32",
        "mail_template": "fedora_errata_template",
        "name": "F32",
        "override_tag": "f32-override",
        "package_manager": "dnf",
        "pending_signing_tag": "f32-signing-pending",
        "pending_stable_tag": "f32-updates-pending",
        "pending_testing_tag": "f32-updates-testing-pending",
        "stable_tag": "f32",
        "state": "pending",
        "testing_repository": "updates-testing",
        "testing_tag": "f32-updates-testing",
        "version": "32"
    }
]

# Now we copy it and add F33 back in, to give us data with a Branched
# and a Rawhide.
RELEASES_BRANCHED_JSON = list(RELEASES_NOBRANCHED_JSON)
RELEASES_BRANCHED_JSON.append({
    "branch": "f33",
    "candidate_tag": "f33-updates-candidate",
    "composed_by_bodhi": False,
    "composes": [],
    "create_automatic_updates": True,
    "dist_tag": "f33",
    "id_prefix": "FEDORA",
    "long_name": "Fedora 33",
    "mail_template": "fedora_errata_template",
    "name": "F33",
    "override_tag": "f33-override",
    "package_manager": "unspecified",
    "pending_signing_tag": "f33-signing-pending",
    "pending_stable_tag": "f33-updates-pending",
    "pending_testing_tag": "f33-updates-testing-pending",
    "stable_tag": "f33",
    "state": "pending",
    "testing_repository": None,
    "testing_tag": "f33-updates-testing",
    "version": "33"
})

@pytest.fixture(scope="session")
def http(request):
    """Run a SimpleHTTPServer that we can use as a fake dl.fp.o. Serve
    the contents of tests/data/http, for the entire test session. We
    just do this with subprocess as we need it to run parallel to the
    tests and this is really the easiest way.
    """
    root = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        'data', 'http')
    args = ("python3", "-m", "http.server", "5001")
    proc = subprocess.Popen(args, cwd=root)
    # block until the server is actually running
    resp = None
    while not resp:
        try:
            resp = urlopen('http://localhost:5001/pub')
        except (ValueError, URLError, HTTPError):
            time.sleep(0.1)
    # Redefine the HTTPS_DL and HTTPS constants to point to the fake
    fedfind.const.HTTPS_DL = 'http://localhost:5001/pub'
    fedfind.const.HTTPS = 'http://localhost:5001/pub'
    yield

    # teardown
    proc.kill()

@pytest.fixture(scope="function")
def clean_home(request):
    """Provides a fake user home directory, at data/home/ under the
    tests directory. Before the test, re-create it, change the cache
    dir global to use it, and patch os.path.expanduser to return it.
    After the test, delete it and clean up the other bits. Yields
    the full path.
    """
    home = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'home')
    if os.path.exists(home):
        shutil.rmtree(home)
    cachedir = os.path.join(home, '.cache', 'fedfind')
    os.makedirs(cachedir)
    with mock.patch('os.path.expanduser', return_value=home, autospec=True):
        origcache = fedfind.helpers.CACHEDIR
        fedfind.helpers.CACHEDIR = cachedir
        yield home

    # teardown stuff
    fedfind.helpers.CACHEDIR = origcache
    if os.path.exists(home):
        shutil.rmtree(home)

def fake_pdc_query(path, params=None):
    """A fake pdc_query that doesn't really hit PDC, it just returns
    canned information (some inline, some loaded from tests/data) for
    queries the tests are known to make.
    """
    # match how pdc_query sanitizes the path
    path = path.strip('/') + '/'
    # composes query. This is hit for cid_from_label.
    if path == 'composes/':
        # Knowns in (release, label, composeid) form:
        composes = (
            ('fedora-24', 'RC-1.2', 'Fedora-24-20160614.0'),
            ('fedora-25', 'RC-1.3', 'Fedora-25-20161115.0'),
            ('fedora-26', 'RC-1.5', 'Fedora-26-20170705.0'),
            ('fedora-27', 'RC-1.6', 'Fedora-27-20171105.0'),
            ('fedora-28', 'RC-1.1', 'Fedora-28-20180425.0'),
            ('fedora-29', 'RC-1.2', 'Fedora-29-20181024.1'),
            # these two were apparently never actually imported to the
            # real PDC, so our fake PDC shouldn't 'find' them either
            #('fedora-30', 'RC-1.2', 'Fedora-30-20190425.0'),
            #('fedora-31', 'RC-1.9', 'Fedora-31-20191023.0'),
        )
        for (rel, label, cid) in composes:
            # We can make this matching smarter if needed, for now
            # it's specific to cid_from_label:
            if params.get('release') == rel and params.get('compose_label') == label:
                return [{'compose_id': cid, 'release': rel, 'compose_label': label}]
            # ...or label_from_cid:
            if params.get('compose_id') == cid:
                return [{'compose_id': cid, 'release': rel, 'compose_label': label}]
        # fallthrough
        return []

    # compose-images query. Just grab the compose ID and look for a
    # backing file to return.
    compimgs = re.compile(r'compose-images/(.*)/')
    match = compimgs.match(path)
    if match:
        fname = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             'data', 'pdc-compimages-{}.json'.format(match.group(1)))
        with open(fname, 'r') as datafh:
            return json.loads(datafh.read())

@pytest.fixture(scope="function")
def pdc(request):
    """Mock fedfind.helpers.pdc_query with fake_pdc_query."""
    with mock.patch('fedfind.helpers.pdc_query', fake_pdc_query):
        yield

@pytest.fixture(scope="function")
def releases_branched(request):
    """Mock fedfind.helpers._get_releases to return test data (with a
    Branched release)."""
    with mock.patch('fedfind.helpers._get_releases', return_value=RELEASES_BRANCHED_JSON,
                    autospec=True):
        yield

@pytest.fixture(scope="function")
def releases_nobranched(request):
    """Mock fedfind.helpers._get_releases to return test data."""
    with mock.patch('fedfind.helpers._get_releases', return_value=RELEASES_NOBRANCHED_JSON,
                   autospec=True):
        yield

@pytest.fixture(scope="function")
def json_releases(request):
    """Mock fedfind.helpers.download_json to return releases test
    data (wrapped appropriately). Returns the mock so tests can check
    its call count, and the test data so they can verify it.
    """
    with mock.patch('fedfind.helpers.download_json',
                    return_value={'releases': RELEASES_BRANCHED_JSON}, autospec=True) as mocked:
        yield (mocked, RELEASES_BRANCHED_JSON)

# vim: set textwidth=100 ts=8 et sw=4:
