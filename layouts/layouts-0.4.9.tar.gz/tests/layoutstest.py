'''
Common test functions used across a variety of tests
'''

### Imports ###

import os
import tempfile

import layouts
import pytest


### Functions ###

@pytest.fixture
def cache_dir():
    '''
    Return a unique cache directory
    Directory is created when calling this function.

    @returns: Full path to directory
    '''
    # Find the temporary directory
    tmp_dir = os.path.join(tempfile.gettempdir(), "layouts-python-test")
    os.makedirs(tmp_dir, exist_ok=True)

    # Create unique directory
    unique_dir = tempfile.mkdtemp(dir=tmp_dir)

    return unique_dir

@pytest.fixture(scope="session")
def common_cache_dir():
    '''
    Returns a pre-populated cache directory
    Used to speed-up tests so the cache does not have to be re-downloaded each time
    '''
    # Get unique cache directory
    unique_dir = cache_dir()

    # Force cache to generate
    layouts.Layouts(cache_dir=unique_dir)

    return unique_dir

@pytest.fixture(scope="session")
def layout_mgr():
    '''
    Layout manager setup

    Uses the default cache location, but the retrieval is cached so tests can run faster and not
    have to re-initialize Layouts()
    '''
    return layouts.Layouts()

