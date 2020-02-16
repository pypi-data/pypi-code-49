"""Module to create temporal artifacts."""

import pytest
import tempfile


@pytest.fixture()
def temp_dir():
    """Creates a temporal folder on /tmp

    Actually is a wrapper for tempfile.TemporaryDirectory() to be used as a
    pytest fixture.

    This fixture is going to *yield* the object returned by TemporaryDirectory(),
    so you can use it as you would use that object in a context manager.

    As soon as you return from fixtured test the temporal folder will be lost.
    """
    with tempfile.TemporaryDirectory() as temp_folder:
        yield temp_folder