import os
from Backupy import Backupy


def test_backup():
    backup = Backupy()
    backup.add_directory('./')
    backup.start()

    assert os.path.exists(backup.filename)
    os.remove(backup.filename)
