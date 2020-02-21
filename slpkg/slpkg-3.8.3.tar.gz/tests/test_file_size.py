from slpkg.file_size import FileSize


def test_FileSize():
    """Testing the remote and local servers
    """
    url = "https://mirrors.slackware.com/slackware/slackware64-14.2/ChangeLog.txt"
    lc = "tests/test_units.py"
    fs1 = FileSize(url)
    fs2 = FileSize(lc)
    assert fs1.server() is not None
    assert fs2.local() is not None
