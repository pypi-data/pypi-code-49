from Backupy import Backupy

"""
By default filename format is backup_13-02-2020
prefix: backup_
filename format: {prefix}{date}
date format: %d-%m-%Y
"""

backup = Backupy(
    filename_prefix='-backup',  # change filename prefix
    filename_format='{date}{prefix}',  # change filename format
    date_format='%Y-%m-%a'  # change date format
)
backup.add_directory('/var/www/html/assets/')
backup.start()  # Output file will be: 2020-02-Thu-backup
