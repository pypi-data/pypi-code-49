import pytest
import flexmock
from labelsync.io import LabelCacheManager, FileLoader, JsonFileLoader

@pytest.fixture
def file_loader():
    return FileLoader()

def test_cache_attach(file_loader):

    cache_manager = LabelCacheManager(file_loader, 'test', 'test_cache', 'name')
    label1 = {"name": "foo", "color": "1af351", "description": "bar"}
    label2 = {"name": "another", "color": "ab32cd", "description": "another desc"}
    cache_manager.attach(label1)
    cache_manager.attach(label2)
    cache_manager.persist()
    content = ''
    with open('test/test_cache') as f:
        content = f.read()
    assert content == '[{"name": "foo", "color": "1af351", "description": "bar"}, {"name": "another", "color": "ab32cd", "description": "another desc"}]\n'



def test_cache_detach(file_loader):

    flexmock(file_loader, load='[{"name": "foo", "color": "1af351", "description": "bar"}, {"name": "another", "color": "ab32cd", "description": "another desc"}]\n')
    mock = flexmock(file_loader).should_call('load').times(1)
    cache_manager = LabelCacheManager(file_loader, 'test', 'test_cache', 'name')
    cache_manager.detach("another")
    cache_manager.persist()

    content = ''
    with open('test/test_cache') as f:
        content = f.read()
    assert content == '[{"name": "foo", "color": "1af351", "description": "bar"}]\n'

def test_cache_nonexistent(file_loader):

    cache_manager = LabelCacheManager(file_loader, 'test', 'nonexistent_cache', 'name')
    content = cache_manager.read()

    assert content != None
    assert len(content) == 0

    with open('test/nonexistent_cache') as f:
        content = f.read()
    assert content == '[]\n'

def file_content(name):
    with open(name) as f:
        content = f.read()
    return content
