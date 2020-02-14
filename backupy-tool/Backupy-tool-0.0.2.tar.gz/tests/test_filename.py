from Backupy import Backupy
from datetime import datetime


def test_backup_directory():
    backup = Backupy(filename_prefix='-backup', filename_format='{date}{prefix}', date_format='%Y.%m.%a')
    current_date = datetime.today().strftime(backup.date_format)

    assert backup.filename == current_date + '-backup'
