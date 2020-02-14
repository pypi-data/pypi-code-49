from Backupy import Backupy

"""
Backup directory is the directory where backups will be saved
By default, it is current working directory
"""

backup = Backupy(backup_directory='/home/backup/')
backup.add_directory('/var/www/html/assets/')
backup.start()
