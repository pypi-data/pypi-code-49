# Copyright 2019 Okera Inc. All Rights Reserved.
#
# Some integration tests for Presto in PyOkera
#
# pylint: disable=global-statement
# pylint: disable=no-self-use

import unittest
import pytest

import prestodb
import requests
import urllib3

from okera import context

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEFAULT_PRESTO_HOST = 'localhost'
DEFAULT_PRESTO_PORT = 8049
BAD_PRESTO_PORT = 1234

@pytest.mark.filterwarnings('ignore::urllib3.exceptions.InsecureRequestWarning')
@pytest.mark.filterwarnings('ignore:numpy.dtype size changed')
class PrestoTest(unittest.TestCase):
    def test_basic(self):
        ctx = context()
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT) as conn:
            results = conn.scan_as_json('select * from okera_sample.whoami',
                                        dialect='presto')
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['user'], 'root')

    def test_explicit_presto_host(self):
        ctx = context()
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_host='127.0.0.1',
                         presto_port=DEFAULT_PRESTO_PORT) as conn:
            results = conn.scan_as_json('select * from okera_sample.whoami',
                                        dialect='presto')
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['user'], 'root')

    def test_auto_choose_dialect(self):
        ctx = context()
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT) as conn:
            results = conn.scan_as_json('select * from okera_sample.whoami')
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['user'], 'root')

    def test_presto_disabled_auto_choose_dialect(self):
        ctx = context()
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050) as conn:
            results = conn.scan_as_json('select * from okera_sample.whoami')
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['user'], 'root')

    def test_presto_disabled_presto_dialect(self):
        ctx = context()
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050) as conn:
            with pytest.raises(ValueError):
                conn.scan_as_json('select * from okera_sample.whoami',
                                  dialect='presto')

    def test_presto_enabled_okera_dialect(self):
        ctx = context()
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT) as conn:
            results = conn.scan_as_json('select * from okera_sample.whoami',
                                        dialect='okera')
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['user'], 'root')

    def test_bad_presto_connection(self):
        ctx = context()
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_host='127.0.0.1',
                         presto_port=BAD_PRESTO_PORT) as conn:
            with pytest.raises(requests.exceptions.ConnectionError):
                conn.scan_as_json('select * from okera_sample.whoami',
                                  dialect='presto')

    def test_presto_ctx_namespace(self):
        ctx = context(namespace='okera')
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT) as conn:
            results = conn.scan_as_json('select * from okera_sample.whoami',
                                        dialect='presto')
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['user'], 'root')

    def test_presto_ctx_bad_namespace(self):
        ctx = context(namespace='okera2')
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT) as conn:
            with pytest.raises(prestodb.exceptions.PrestoUserError):
                conn.scan_as_json('select * from okera_sample.whoami',
                                  dialect='presto')

    def test_presto_conn_namespace(self):
        ctx = context(namespace='okera_bad')
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT, namespace='okera') as conn:
            results = conn.scan_as_json('select * from okera_sample.whoami',
                                        dialect='presto')
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['user'], 'root')

    def test_presto_conn_bad_namespace(self):
        ctx = context(namespace='okera_bad')
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT, namespace='okera2') as conn:
            with pytest.raises(prestodb.exceptions.PrestoUserError):
                conn.scan_as_json('select * from okera_sample.whoami',
                                  dialect='presto')

    def test_max_records(self):
        ctx = context()
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT) as conn:
            results = conn.scan_as_json(
                'select * from okera_sample.users', dialect='presto', max_records=100)
            self.assertEqual(len(results), 100)
            results = conn.scan_as_pandas(
                'select * from okera_sample.users', dialect='presto', max_records=100)
            self.assertEqual(len(results), 100)

    def test_max_records_with_less_records(self):
        ctx = context()
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT) as conn:
            results = conn.scan_as_json('select * from okera_sample.users limit 50',
                                        dialect='presto', max_records=100)
            self.assertEqual(len(results), 50)
            results = conn.scan_as_pandas('select * from okera_sample.users limit 50',
                                          dialect='presto', max_records=100)
            self.assertEqual(len(results), 50)

    def test_json_pandas_equality(self):
        ctx = context()
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT) as conn:
            json_results = conn.scan_as_json('select * from okera_sample.users limit 50',
                                             dialect='presto', max_records=100)
            pandas_results = conn.scan_as_pandas(
                'select * from okera_sample.users limit 50',
                dialect='presto', max_records=100)
            self.assertEqual(json_results, pandas_results.to_dict('records'))

    def test_no_auth(self):
        ctx = context()
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT) as conn:
            with pytest.raises(RuntimeError):
                conn.scan_as_json('select * from okera_sample.whoami',
                                  dialect='presto')

    def test_ctx_dialect(self):
        ctx = context(dialect='okera')
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT) as conn:
            results = conn.scan_as_json('okera_sample.whoami')
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['user'], 'root')

    def test_ctx_dialect_override(self):
        ctx = context(dialect='presto')
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT) as conn:
            results = conn.scan_as_json('okera_sample.whoami', dialect='okera')
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['user'], 'root')

    def test_complex_types(self):
        datasets = [
            'rs_complex.struct_t',
            'rs_complex.multiple_structs_nested',
            'rs_complex.map_t',
            'rs_complex.struct_nested',
            'rs_complex_parquet.map_struct_t',
            'rs_complex_parquet.map_struct_array_t',
        ]
        ctx = context()
        ctx.enable_token_auth(token_str='root')
        with ctx.connect(host='localhost', port=12050,
                         presto_port=DEFAULT_PRESTO_PORT) as conn:
            for dataset in datasets:
                presto_results = conn.scan_as_json(
                    'select * from %s' % dataset, dialect='presto')
                okera_results = conn.scan_as_json(
                    'select * from %s' % dataset, dialect='okera', strings_as_utf8=True)
                self.assertEqual(okera_results, presto_results)
