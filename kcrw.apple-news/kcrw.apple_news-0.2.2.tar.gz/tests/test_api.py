#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `kcrw.apple_news` api module."""

import json
import pytest
import requests
import six
try:
    from unittest import mock
except ImportError:
    import mock

from kcrw.apple_news.api import API, AppleNewsError


@pytest.fixture
def api():
    api = API('FAKE_ID', 'RkFLRV9TRUNSRVQ=', 'FAKE_CHANNEL')
    with mock.patch('requests.request'):
        yield api


@pytest.fixture
def patched_logger():
    with mock.patch('kcrw.apple_news.api.logger') as logger:
        yield logger


def test_api_read_channel(api):
    """Test Apple Read Channel API"""
    response = api.read_channel()
    assert "name='request().json()'" in repr(response)
    req_call = requests.request
    assert req_call.call_count == 1
    req_args = req_call.call_args[0]
    req_kw = req_call.call_args[1]
    assert req_args[0] == 'GET'
    assert req_args[1] == 'https://news-api.apple.com/channels/FAKE_CHANNEL'
    assert 'Authorization' in req_kw['headers']
    assert 'HHMAC; key=FAKE_ID; signature=' in req_kw['headers']['Authorization']
    assert req_kw['data'] is None


def test_api_create_article(api):
    """Test Apple Create Article API"""
    response = api.create_article(
         {"title": "A Title"},
         {"key1": "value1"},
         {'image1.jpg': 'FFFDASFAFADADFA',
          'image2.jpg': 'AFFDASFAFADADFA'},
    )
    assert "name='request().json()'" in repr(response)
    req_call = requests.request
    assert req_call.call_count == 1
    req_args = req_call.call_args[0]
    req_kw = req_call.call_args[1]
    assert req_args[0] == 'POST'
    assert req_args[1] == 'https://news-api.apple.com/channels/FAKE_CHANNEL/articles'
    assert 'Authorization' in req_kw['headers']
    assert 'HHMAC; key=FAKE_ID; signature=' in req_kw['headers']['Authorization']
    data_lines = req_kw['data'].split(b'\r\n')
    # Each file has 5 parts:
    #   boundary, Content-Type, Content-Disposition, blank, body data
    # Three items => 15 lines + 1 final boundary
    assert len(data_lines) == 21
    assert data_lines[1] == b'Content-Type: application/json'
    assert data_lines[2] == b'Content-Disposition: form-data; filename=metadata; size=18'
    assert data_lines[4] == six.ensure_binary(json.dumps({"key1": "value1"}), 'utf8')
    assert data_lines[6] == b'Content-Type: application/json'
    assert data_lines[7] == b'Content-Disposition: form-data; filename=article.json; size=20'
    assert data_lines[9] == six.ensure_binary(json.dumps({"title": "A Title"}), 'utf8')
    assert data_lines[11] == b'Content-Type: image/jpeg'
    assert data_lines[12] == b'Content-Disposition: form-data; filename=image1.jpg; size=15'
    assert data_lines[14] == b'FFFDASFAFADADFA'
    assert data_lines[16] == b'Content-Type: image/jpeg'
    assert data_lines[17] == b'Content-Disposition: form-data; filename=image2.jpg; size=15'
    assert data_lines[19] == b'AFFDASFAFADADFA'


def test_api_create_missing_article(api):
    with pytest.raises(AppleNewsError) as excinfo:
        api.create_article(None, None)
    assert str(excinfo.value) == 'No article body found for article'


def test_api_create_no_assets(api):
    """Test Apple Create Article API"""
    api.create_article(
        {"title": "A Title"},
        {"key1": "value1"},
    )
    req_call = requests.request
    req_kw = req_call.call_args[1]
    data_lines = req_kw['data'].split(b'\r\n')
    # Unknown file type is skipped
    assert len(data_lines) == 11


def test_api_create_unknown_file(api):
    """Test Apple Create Article API"""
    api.create_article(
        {"title": "A Title"},
        {"key1": "value1"},
        {'test.zip': 'FFFDASFAFADADFA'},
    )
    req_call = requests.request
    req_kw = req_call.call_args[1]
    data_lines = req_kw['data'].split(b'\r\n')
    # Unknown file type is skipped
    assert len(data_lines) == 11


def test_api_update_article(api):
    response = api.update_article(
        'IDENTIFIER',
        {'data': {'metadata': 'a', 'revision': "12233323"}}
    )
    assert "name='request().json()'" in repr(response)
    req_call = requests.request
    assert req_call.call_count == 1
    req_args = req_call.call_args[0]
    req_kw = req_call.call_args[1]
    assert req_args[0] == 'POST'
    assert req_args[1] == 'https://news-api.apple.com/articles/IDENTIFIER'
    assert 'Authorization' in req_kw['headers']
    assert 'HHMAC; key=FAKE_ID; signature=' in req_kw['headers']['Authorization']
    data_lines = req_kw['data'].split(b'\r\n')
    assert len(data_lines) == 6
    assert data_lines[1] == b'Content-Type: application/json'
    assert data_lines[2] == b'Content-Disposition: form-data; filename=metadata; size=51'
    assert data_lines[4] == six.ensure_binary(
        json.dumps({'data': {'metadata': 'a', 'revision': "12233323"}}), 'utf8'
    )


def test_api_update_with_article(api):
    response = api.update_article(
        'IDENTIFIER',
        {'data': {'metadata': 'a', 'revision': "12233323"}},
        {"title": "A Title"},
        {'image1.jpg': 'FFFDASFAFADADFA'},
    )
    assert "name='request().json()'" in repr(response)
    req_call = requests.request
    assert req_call.call_count == 1
    req_args = req_call.call_args[0]
    req_kw = req_call.call_args[1]
    assert req_args[0] == 'POST'
    assert req_args[1] == 'https://news-api.apple.com/articles/IDENTIFIER'
    assert 'Authorization' in req_kw['headers']
    assert 'HHMAC; key=FAKE_ID; signature=' in req_kw['headers']['Authorization']
    data_lines = req_kw['data'].split(b'\r\n')
    assert len(data_lines) == 16
    assert data_lines[1] == b'Content-Type: application/json'
    assert data_lines[2] == b'Content-Disposition: form-data; filename=metadata; size=51'
    assert data_lines[4] == six.ensure_binary(
        json.dumps({'data': {'metadata': 'a', 'revision': "12233323"}}), 'utf8'
    )
    assert data_lines[6] == b'Content-Type: application/json'
    assert data_lines[7] == b'Content-Disposition: form-data; filename=article.json; size=20'
    assert data_lines[9] == six.ensure_binary(json.dumps({"title": "A Title"}), 'utf8')
    assert data_lines[11] == b'Content-Type: image/jpeg'
    assert data_lines[12] == b'Content-Disposition: form-data; filename=image1.jpg; size=15'
    assert data_lines[14] == b'FFFDASFAFADADFA'


def test_api_update_missing_metadata(api):
    with pytest.raises(AppleNewsError) as excinfo:
        api.update_article('IDENTIFIER', None)
    assert str(excinfo.value) == 'No valid metadata data found for article update'


def test_api_update_invalid_metadata(api):
    with pytest.raises(AppleNewsError) as excinfo:
        api.update_article('IDENTIFIER', {'identifier': 'IDENTIFIER'})
    assert str(excinfo.value) == 'No valid metadata data found for article update'


def test_api_read(api):
    response = api.read_article('IDENTIFIER')
    assert "name='request().json()'" in repr(response)
    req_call = requests.request
    assert req_call.call_count == 1
    req_args = req_call.call_args[0]
    req_kw = req_call.call_args[1]
    assert req_args[0] == 'GET'
    assert req_args[1] == 'https://news-api.apple.com/articles/IDENTIFIER'
    assert 'Authorization' in req_kw['headers']
    assert 'HHMAC; key=FAKE_ID; signature=' in req_kw['headers']['Authorization']


def test_api_delete(api):
    response = api.delete_article('IDENTIFIER')
    assert isinstance(response, dict)
    assert 'result' in response
    req_call = requests.request
    assert req_call.call_count == 1
    req_args = req_call.call_args[0]
    req_kw = req_call.call_args[1]
    assert req_args[0] == 'DELETE'
    assert req_args[1] == 'https://news-api.apple.com/articles/IDENTIFIER'
    assert 'Authorization' in req_kw['headers']
    assert 'HHMAC; key=FAKE_ID; signature=' in req_kw['headers']['Authorization']


def test_api_raises_applenewserror_on_request(api, patched_logger):
    def raiseReqError(*args, **kw):
        raise requests.exceptions.RequestException('Error')
    requests.request.side_effect = raiseReqError

    with pytest.raises(AppleNewsError) as excinfo:
        api.read_channel()

    assert (
        'Error during Apple News request to https://news-api.apple.com/channels/FAKE_CHANNEL'
        in str(excinfo.value)
    )
    assert patched_logger.exception.call_count == 1
    assert patched_logger.exception.call_args[0][0] == 'Requests error'


def test_api_raises_applenewserror_after_request(api, patched_logger):
    def resp_mock(*args, **kw):
        def raiseReqError(*args, **kw):
            raise requests.exceptions.RequestException('Error')
        resp_mock = mock.Mock()
        resp_mock.raise_for_status.side_effect = raiseReqError
        return resp_mock
    requests.request.side_effect = resp_mock

    with pytest.raises(AppleNewsError) as excinfo:
        api.read_channel()

    exception = excinfo.value
    assert (
        'Error during Apple News request to https://news-api.apple.com/channels/FAKE_CHANNEL'
        in str(exception)
    )
    assert 'mock.status_code' in str(exception.code)
    assert 'mock.json' in str(exception.data)

    assert patched_logger.exception.call_count == 1
    assert patched_logger.exception.call_args[0][0] == 'Requests error'


def test_api_handles_unicode(api):
    """Test Apple Create Article API"""
    api.create_article(
         {"title": "A Title"},
         {"key1": "value1"},
         {u'imagé1.jpg': u'F\u2665FFDASFAFADADFA',
          'imåge2.jpg': u'A\u2665FFDASFAFADADFA'},
    )
    req_call = requests.request
    assert req_call.call_count == 1
    req_kw = req_call.call_args[1]
    assert isinstance(req_kw['data'], six.binary_type)
