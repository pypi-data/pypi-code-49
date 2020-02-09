import pytest
import betamax
import requests
import flexmock
import os
from labelsync.clients import GithubClient, GitlabClient, GithubMasterClient
from labelsync.logic import SynchronizationService, MasterService
from labelsync.io import LabelCacheManager, FileLoader

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'test/fixtures/cassettes'
    if 'TOKEN' in os.environ:
        TOKEN = os.environ['TOKEN']
        config.default_cassette_options['record_mode'] = 'once'
    else:
        TOKEN = 'false_token'
        config.default_cassette_options['record_mode'] = 'none'
    config.define_cassette_placeholder('<TOKEN>', TOKEN)

def get_token():
    if 'TOKEN' in os.environ:
        return os.environ['TOKEN']
    else:
        return "false_token"

@pytest.fixture
def github_client(betamax_session):
    return GithubClient("novotkry", "mi-pyt-final", get_token(), "https://api.github.com", betamax_session)

def authority_client(betamax_session):
    return GithubMasterClient('novotkry', 'test-repo', get_token(), 'https://api.github.com', "secret", betamax_session)

def test_create_master_invalid_url(betamax_session):
    client = GithubMasterClient('novotkry', 'test-repo', get_token(), 'https://foobar.org', "secret", betamax_session)
    service = MasterService(client)
    result = service.setup_master('http://example.com', 'foobar')
    assert not result[0]

def test_create_master_bad_token(betamax_session):
    client = GithubMasterClient('novotkry', 'foo', 'some nonsense', 'https://api.github.com', "secret", betamax_session)
    service = MasterService(client)
    flexmock(service).should_call('create_master_repo').times(0)
    result = service.setup_master('http://example.com', 'foobar')
    assert not result[0]

def test_create_master_already_there(betamax_session):
    client = GithubMasterClient('novotkry', 'mi-pyt-final', get_token(), 'https://api.github.com', "secret", betamax_session)
    service = MasterService(client)
    flexmock(service).should_call('create_master_repo').times(0)
    result = service.setup_master('http://example.com', 'foobar')
    assert result[0]

def test_create_master_success(betamax_session):
    client = GithubMasterClient('novotkry', 'testoe-test', get_token(), 'https://api.github.com', "secret", betamax_session)
    service = MasterService(client)
    flexmock(service).should_call('create_master_repo').times(1)
    result = service.setup_master('http://example.com', 'foobar')
    assert result[0]


