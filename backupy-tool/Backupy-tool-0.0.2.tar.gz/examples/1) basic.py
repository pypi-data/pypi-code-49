from Backupy import Backupy

backup = Backupy(backup_directory='/home/backup/')
backup.add_directory('/var/www/html/assets/')
backup.add_directory('/etc/apache2/')
backup.add_database_credentials(host='DB_HOST', user='DB_USER', password='DB_PASS')
backup.start()
