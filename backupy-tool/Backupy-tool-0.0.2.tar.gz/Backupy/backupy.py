import os
import zipfile
from datetime import datetime
from fnmatch import fnmatch


class Backupy:
    dirs = tuple()
    exclude = dict()
    backup_dir = None

    archive = None
    filename = None
    filename_prefix = None
    filename_format = None
    date_format = None

    db_host = None
    db_user = None
    db_pass = None
    db_name = None

    def __init__(self, backup_directory=os.getcwd(), filename_prefix='backup_', filename_format='{prefix}{date}', date_format='%d-%m-%Y'):
        self.filename_prefix = filename_prefix
        self.filename_format = filename_format
        self.date_format = date_format
        self.__set_backup_dir(backup_directory)
        self.__set_filename()

    def add_directory(self, directory, exclude=None):
        self.exclude[directory] = list()

        if exclude:
            for d in exclude:
                self.exclude[directory].append(d)

        self.dirs = self.dirs + (directory, )
        return self.dirs

    def add_database_credentials(self, host, user, password, databases=None):
        self.db_host = host
        self.db_name = databases
        self.db_user = user
        self.db_pass = password

    def start(self):
        self.archive = zipfile.ZipFile(os.path.join(self.backup_dir, self.filename), 'w', zipfile.ZIP_DEFLATED)
        self.backup_files()
        self.backup_database()
        self.archive.close()

    def backup_files(self):
        if not self.dirs:
            print("Notice: to backup files use add_directory()")
            return False
        for d in self.dirs:
            self.__zip(d)
        return True

    def backup_database(self):
        if not self.db_host and not self.db_user and not self.db_pass:
            print("Notice: to backup database use add_database_credentials()")
            return False
        db = '--databases {}'.format(self.db_name)
        if not self.db_name:
            db = '--all-databases'
        filename = 'mysqldump.sql'
        output = os.path.join(self.backup_dir, filename)
        sql = 'mysqldump -h {host} -u {user} --password={password} {db} > {out}'
        sql = sql.format(host=self.db_host, user=self.db_user, password=self.db_pass, db=db, out=output)
        os.popen(sql).read()
        self.archive.write(output, filename)
        os.remove(output)
        return True

    def __set_backup_dir(self, path):
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except PermissionError:
                raise
            except OSError:
                if not os.path.isdir(path):
                    raise
        self.backup_dir = path
        return self.backup_dir

    def __set_filename(self):
        date = datetime.today().strftime(self.date_format)
        self.filename = self.filename_format.format(prefix=self.filename_prefix, date=date)
        return self.filename

    def __zip(self, path):
        for root, dirs, files in os.walk(path):
            parent = os.path.relpath(root, path)
            if path in self.exclude and len(self.exclude[path]) != 0:
                for d in dirs:
                    for ex in self.exclude[path]:
                        if ex.startswith('/'):
                            ex = ex[1:]
                        if os.path.normpath(os.path.join(parent, d)) == ex:
                            dirs.remove(d)
            for file in files:
                skip = False
                complete = os.path.join(root, file)
                if path in self.exclude and len(self.exclude[path]) != 0:
                    for ex in self.exclude[path]:
                        if ex.startswith('/'):
                            ex = ex[1:]
                        if fnmatch(complete, os.path.join(path, ex)):
                            files.remove(file)
                            skip = True
                if complete not in self.exclude and not skip:
                    self.archive.write(complete)
        return True
