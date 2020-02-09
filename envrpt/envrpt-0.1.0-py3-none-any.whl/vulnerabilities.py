
import json
import os
import time

from pathlib import Path

from pip._vendor import requests
from pip._vendor.packaging.specifiers import SpecifierSet


SAFETYDB_URL = 'https://raw.githubusercontent.com/pyupio/safety-db/master/data/insecure_full.json'  # noqa
SAFETYDB_RECHECK_THRESHOLD = 60 * 60 * 24  # a day


def get_cache_dir():
    cache = Path(os.getenv('XDG_CACHE_HOME', os.path.expanduser('~/.cache')))
    cache = cache / 'envrpt'
    cache.mkdir(parents=True, exist_ok=True)
    return cache


def retrieve_db(etag=None):
    headers = {}
    if etag:
        headers['If-None-Match'] = etag

    resp = requests.get(SAFETYDB_URL, headers=headers)

    if resp.status_code == requests.codes.not_modified:  # noqa: no-member
        return None, etag

    if resp.ok:
        return resp.json(), resp.headers.get('etag')

    raise Exception(
        'Could not retrieve vulnerability database: %s %s' % (
            resp.status_code,
            resp.reason,
        )
    )


def get_vulnerability_db():
    vuln_file = get_cache_dir() / 'vulnerabilities'

    last_modified = last_etag = last_db = None

    if vuln_file.exists():
        last_modified = vuln_file.stat().st_mtime
        with vuln_file.open() as cfp:
            cache = json.load(cfp)
            last_etag = cache['etag']
            last_db = cache['db']

    if not last_modified \
            or last_modified < (time.time() - SAFETYDB_RECHECK_THRESHOLD):
        new_db, new_etag = retrieve_db(last_etag)

        if new_db:
            cache = {
                'etag': new_etag,
                'db': new_db,
            }
        else:
            cache = {
                'etag': last_etag,
                'db': last_db,
            }

        with vuln_file.open('w') as cfp:
            json.dump(cache, cfp)

    return cache['db']


def identify_vulnerable_packages(environment):
    vulns = get_vulnerability_db()
    for pkg in environment['packages'].values():
        if pkg['key'] in vulns:
            for advisory in vulns[pkg['key']]:
                for spec in advisory['specs']:
                    if pkg['version'] in SpecifierSet(spec):
                        pkg['issues'].append({
                            'type': 'VULNERABLE',
                            'id': advisory['cve'] or advisory['id'],
                            'description': advisory['advisory'],
                            'affected_versions': advisory['v'],
                        })

