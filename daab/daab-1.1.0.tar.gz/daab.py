#!/usr/bin/env python

import fnmatch
import re
import digitalocean


class Error(Exception):
    pass


class KeyNotFoundError(Error):
    pass


class Store(object):

    def __init__(self, record):
        self._record = record

        v = record.data.split('=')
        self.key = v[0]
        self.value = ''.join(v[1:])

    def _set(self, value):
        self.value = value
        data = f'{self.key}={self.value}'

        self._record.data = data
        self._record.save()

    def to_dict(self):
        return {self.key: self.value}


class DAAB(object):

    def __init__(self, token, domain_name, hostname='@'):
        self._domain = digitalocean.Domain(token=token, name=domain_name)
        self.hostname = hostname

    def _get_rows(self):
        return [Store(r) for r in self._domain.get_records() if r.type == 'TXT']

    def scan(self, pattern):
        rows = self._get_rows()
        # Translate glob into regex
        pattern = re.compile(fnmatch.translate(pattern))

        return [row for row in rows if pattern.search(row.key)]

    def get(self, key):
        # Gets an exact match - no globs
        rows = self._get_rows()

        for row in rows:
            if row.key == key:
                return row

        return None

    def set(self, key, value):
        store = self.get(key)

        if store:
            store._set(value)
        else:
            record = digitalocean.Record(
                **self._domain.create_new_domain_record(
                    type='TXT',
                    name=self.hostname,
                    data=f'{key}={value}'
                )['domain_record']
            )

            store = Store(record)

        return store

    def delete(self, key):
        store = self.get(key)

        if store is None:
            raise KeyNotFoundError(f'Key: {key} does not exist')

        store._record.destroy()

        return
