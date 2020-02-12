# Copyright 2019 Okera Inc. All Rights Reserved.
#
# Some integration tests for auth in PyOkera
#
# pylint: disable=global-statement
# pylint: disable=no-self-use

import unittest
import pytest

import thriftpy
from okera import context

#
# NOTE: this test suite uses the fact that enable_token_auth will treat
# a string that has a period in it as a JWT/OkeraToken, and any other string
# as if it was the username (for an unauthed server). Since the test runs
# against an unauthed server, a JWT/OkeraToken will always fail, causing
# us to go through the retry logic.
#

# Global variable for attempts
attempts = 0

def bad_then_good_func():
    global attempts
    token = None
    if attempts == 0:
        token = "foo.bar"
    else:
        token = "foo"
    attempts += 1
    return token

def bad_twice_then_good_func():
    global attempts
    token = None
    if attempts < 2:
        token = "foo.bar"
    else:
        # should never be called
        raise Exception()
    attempts += 1
    return token

def good_then_bad_func():
    global attempts
    token = None
    if attempts == 0:
        token = "foo"
    else:
        # this should never be called
        raise Exception()
    attempts += 1
    return token

def always_bad():
    return "foo.bar"

class AuthTest(unittest.TestCase):
    @staticmethod
    def _reset_attempts():
        global attempts
        attempts = 0

    def setUp(self):
        AuthTest._reset_attempts()

    def test_token_func_basic(self):
        ctx = context()
        ctx.enable_token_auth(token_func=bad_then_good_func)
        with ctx.connect(host='localhost', port=12050) as conn:
            results = conn.scan_as_json('okera_sample.whoami')
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['user'], 'foo')

    def test_token_func_no_failure(self):
        ctx = context()
        ctx.enable_token_auth(token_func=good_then_bad_func)
        with ctx.connect(host='localhost', port=12050) as conn:
            results = conn.scan_as_json('okera_sample.whoami')
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['user'], 'foo')

    def test_token_func_and_token_str(self):
        ctx = context()
        ctx.enable_token_auth(token_func=always_bad, token_str='foo')
        with ctx.connect(host='localhost', port=12050) as conn:
            results = conn.scan_as_json('okera_sample.whoami')
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['user'], 'foo')

    def test_token_func_never_succeed(self):
        ctx = context()
        ctx.enable_token_auth(token_func=always_bad)
        with pytest.raises(thriftpy.transport.TTransportException):
            with ctx.connect(host='localhost', port=12050):
                # we should never get here
                raise Exception()

    def test_token_func_retry_once_still_fail(self):
        ctx = context()
        ctx.enable_token_auth(token_func=bad_twice_then_good_func)
        with pytest.raises(thriftpy.transport.TTransportException):
            with ctx.connect(host='localhost', port=12050):
                # we should never get here
                raise Exception()

    def test_token_func_non_picklable(self):
        def fn():
            return "foo"

        ctx = context()
        with pytest.raises(ValueError):
            ctx.enable_token_auth(token_func=fn)
