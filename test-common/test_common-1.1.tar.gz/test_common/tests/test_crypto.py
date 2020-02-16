"""
Tests for crypto module.
"""
import tempfile
import pytest

import test_common.fs.crypto as crypto


@pytest.mark.crypto
def test_hash_file():
    EXPECTED_HASH = "c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2"
    with tempfile.NamedTemporaryFile() as file:
        file.write(b"foobar")
        file.flush()
        file_hash = crypto.hash_file(file.name)
        assert EXPECTED_HASH == file_hash

