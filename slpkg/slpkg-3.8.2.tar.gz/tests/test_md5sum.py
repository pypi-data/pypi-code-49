from slpkg.md5sum import md5


def test_md5_superuser():
    result = md5('slpkg/superuser.py')
    assert result == "c6a3576c247bda199c75b43540bfc3d7"


def test_md5_security():
    result = md5('slpkg/security.py')
    assert result == "36c3a9213a27ab0b49e9c1bdd5bd2db6"
