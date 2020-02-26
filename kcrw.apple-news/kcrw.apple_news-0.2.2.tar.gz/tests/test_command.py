#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `kcrw.apple_news` commands module."""

import json
import os
import pytest
import requests
from click.testing import CliRunner
try:
    from unittest import mock
except ImportError:
    import mock

from kcrw.apple_news.command import cli


@pytest.fixture
def command():
    runner = CliRunner(env={
        'APPLE_KEY_ID': 'FAKE_ID',
        'APPLE_KEY_SECRET': 'RkFLRV9TRUNSRVQ=',
        'APPLE_CHANNEL': 'FAKE_CHANNEL'
    })
    with mock.patch('requests.request') as request:
        response_mock = mock.Mock()
        request.side_effect = lambda *args, **kw: response_mock
        response_mock.json.side_effect = lambda: {'result': 'bogus'}
        yield runner


def test_channel(command):
    result = command.invoke(cli, ['channel'], auto_envvar_prefix='APPLE')
    req_call = requests.request
    assert result.exit_code == 0
    assert 'Fetching Channel Info for channel: FAKE_CHANNEL' in result.output
    assert json.dumps({'result': 'bogus'}, indent=True) in result.output
    assert req_call.call_count == 1
    req_args = req_call.call_args[0]
    req_kw = req_call.call_args[1]
    assert req_args[0] == 'GET'
    assert req_args[1] == 'https://news-api.apple.com/channels/FAKE_CHANNEL'
    assert 'Authorization' in req_kw['headers']
    assert 'HHMAC; key=FAKE_ID; signature=' in req_kw['headers']['Authorization']


def test_create(command):
    create_path = os.path.join(os.path.dirname(__file__), 'sample_article')
    result = command.invoke(cli, ['create', create_path],
                            auto_envvar_prefix='APPLE')
    req_call = requests.request
    assert result.exit_code == 0
    assert req_call.call_count == 1
    req_args = req_call.call_args[0]
    req_kw = req_call.call_args[1]
    assert req_args[0] == 'POST'
    assert req_args[1] == 'https://news-api.apple.com/channels/FAKE_CHANNEL/articles'
    assert 'Authorization' in req_kw['headers']
    assert 'HHMAC; key=FAKE_ID; signature=' in req_kw['headers']['Authorization']
    data_lines = req_kw['data'].split(b'\r\n')
    boundaries = [l for l in data_lines if l.startswith(b'--')]
    assert len(boundaries) == 4
    assert data_lines[1] == b'Content-Type: application/json'
    assert data_lines[2] == b'Content-Disposition: form-data; filename=metadata; size=214'
    assert data_lines[6] == b'Content-Type: application/json'
    assert data_lines[7] == b'Content-Disposition: form-data; filename=article.json; size=854'
    assert data_lines[11] == b'Content-Type: image/jpeg'
    assert data_lines[12] == b'Content-Disposition: form-data; filename=image.jpg; size=87555'


def test_update(command):
    create_path = os.path.join(os.path.dirname(__file__), 'update_article')
    result = command.invoke(cli, ['update', 'FAKE_ID', create_path],
                            auto_envvar_prefix='APPLE')
    req_call = requests.request
    assert result.exit_code == 0
    assert req_call.call_count == 1
    req_args = req_call.call_args[0]
    req_kw = req_call.call_args[1]
    assert req_args[0] == 'POST'
    assert req_args[1] == 'https://news-api.apple.com/articles/FAKE_ID'
    assert 'Authorization' in req_kw['headers']
    assert 'HHMAC; key=FAKE_ID; signature=' in req_kw['headers']['Authorization']
    data_lines = req_kw['data'].split(b'\r\n')
    boundaries = [l for l in data_lines if l.startswith(b'--')]
    assert len(boundaries) == 3
    assert data_lines[1] == b'Content-Type: application/json'
    assert data_lines[2] == b'Content-Disposition: form-data; filename=metadata; size=76'
    assert data_lines[6] == b'Content-Type: application/json'
    assert data_lines[7] == b'Content-Disposition: form-data; filename=article.json; size=868'


def test_read(command):
    result = command.invoke(cli, ['read', 'FAKE_ID'],
                            auto_envvar_prefix='APPLE')
    req_call = requests.request
    assert result.exit_code == 0
    assert req_call.call_count == 1
    req_args = req_call.call_args[0]
    req_kw = req_call.call_args[1]
    assert req_args[0] == 'GET'
    assert req_args[1] == 'https://news-api.apple.com/articles/FAKE_ID'
    assert 'Authorization' in req_kw['headers']
    assert 'HHMAC; key=FAKE_ID; signature=' in req_kw['headers']['Authorization']


def test_delete(command):
    result = command.invoke(cli, ['delete', 'FAKE_ID'],
                            auto_envvar_prefix='APPLE')
    req_call = requests.request
    assert result.exit_code == 0
    assert json.dumps(
        {'result': 'Deleted item at url: https://news-api.apple.com/articles/FAKE_ID'},
        indent=True
    ) in result.output
    assert req_call.call_count == 1
    req_args = req_call.call_args[0]
    req_kw = req_call.call_args[1]
    assert req_args[0] == 'DELETE'
    assert req_args[1] == 'https://news-api.apple.com/articles/FAKE_ID'
    assert 'Authorization' in req_kw['headers']
    assert 'HHMAC; key=FAKE_ID; signature=' in req_kw['headers']['Authorization']
