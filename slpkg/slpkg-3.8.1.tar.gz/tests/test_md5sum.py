from slpkg.md5sum import md5


def test_md5_superuser():
    result = md5('slpkg/superuser.py')
    assert result == "25ec85aa9c2803ece6397e4147449ea6"


def test_md5_security():
    result = md5('slpkg/security.py')
    assert result == "3f10bf99b21f66af879dc0882bcd92b3"
