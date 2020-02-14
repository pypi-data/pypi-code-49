from Backupy import Backupy

"""
:param databases is optional:
1) You can specify the databases for backup by listing them with a space
2) Or leave it blank to backup all databases
"""

backup = Backupy()
backup.add_database_credentials(host='DB_HOST', user='DB_USER', password='DB_PASS', databases='database1 database2 database3')
backup.add_database_credentials(host='DB_HOST', user='DB_USER', password='DB_PASS')
backup.start()
