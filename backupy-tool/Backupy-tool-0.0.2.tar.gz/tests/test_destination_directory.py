from Backupy import Backupy
import os


def test_backup_directory():
    backup = Backupy()
    backup2 = Backupy(backup_directory='/var/')

    assert backup.backup_dir == os.getcwd()
    assert backup2.backup_dir == '/var/'
