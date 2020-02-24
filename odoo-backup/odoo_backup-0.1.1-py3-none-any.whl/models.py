import os
from config import CONFIGURATION_DIR, DATA_DIR
import configparser
import requests
from datetime import datetime
from humanize import naturalsize
from datetime import datetime
from utils import backup_name_from_datetime, backup_datetime_from_name


class Server():
    name: str
    ip: str
    master_pwd: str
    port: int = 8069
    bases = list()

    def __init__(self, config_path):
        try:
            if not os.path.isfile(config_path):
                raise FileNotFoundError(config_path + " does not exist")
            config = configparser.ConfigParser()
            config.read(config_path)
            self.name = os.path.split(config_path)[-1].split('.')[0]
            self.ip = config.get('DEFAULT', 'ip')
            self.master_pwd = config.get('DEFAULT', 'master_pwd')
            self.port = config.getint('DEFAULT', 'port', fallback=8069)
            self.bases = config.sections()
        except (configparser.NoOptionError, FileNotFoundError) as err:
            print(config_path)
            print(err)
            exit(1)

    @staticmethod
    def all():
        servers = list()
        for server_file in os.listdir(CONFIGURATION_DIR):
            server = Server(os.path.join(CONFIGURATION_DIR, server_file))
            servers.append(server)
        return servers

    @staticmethod
    def get(name: str):
        server = Server(os.path.join(CONFIGURATION_DIR, name + '.conf'))
        return server

    def list_backups(self, database: str):
        """Returns [(datetime, size)] in chronological order"""
        if not database in self.bases:
            print("Database {}:{} doesn't exist in config file.".format(self.name, database))
            exit(0)
        if not os.path.isdir(os.path.join(DATA_DIR, self.name)):
            os.mkdir(os.path.join(DATA_DIR, self.name))
        if not os.path.isdir(os.path.join(DATA_DIR, self.name, database)):
            os.mkdir(os.path.join(DATA_DIR, self.name, database))
        backups = os.listdir(os.path.join(DATA_DIR, self.name, database))
        backups_datetimes = [backup_datetime_from_name(backup) for backup in backups]
        backups_sizes = [os.path.getsize(os.path.join(DATA_DIR, self.name, database, backup)) for backup in backups]
        return zip(backups_datetimes, backups_sizes)

    def get_backup_name(self, database: str, date: str):
        backups = self.list_backups(database)
        backups_datetimes, backups_sizes = list(zip(*backups))
        if date == 'latest':
            return backup_name_from_datetime(max(backups_datetimes))
        elif date == 'oldest':
            return backup_name_from_datetime(min(backups_datetimes))
        else:
            try:
                date = datetime.fromisoformat(date)
                dates = [d.date() for d in backups_datetimes]
                index = max(idx for idx, d in enumerate(backups_datetimes) if d.date() == date.date()) 
                return backup_name_from_datetime(backups_datetimes[index])
            except Exception as err:
                print(err)

    def check(self):
        print("Server {}:".format(self.name))
        res = requests.get(f'http://{self.ip}:{self.port}')
        print("\tHTTP: " + "OK" if res.ok else "FAILED")
        print("\tBASES:")
        for base in self.bases:
            backups = self.list_backups(base)
            if not backups:
                print("\t\t{} (no backup available)".format(base))
                break
            backups_datetimes, backups_sizes = list(zip(*backups))
            total_size = sum(backups_sizes)
            print("\t\t{} (total size: {})".format(base, naturalsize(total_size)))
            latest_id = backups_datetimes.index(max(backups_datetimes))
            print("\t\t\tLatest backup: {} ({})".format(backups_datetimes[latest_id], naturalsize(backups_sizes[latest_id])))
            oldest_id = backups_datetimes.index(min(backups_datetimes))
            print("\t\t\tOldest backup: {} ({})".format(backups_datetimes[oldest_id], naturalsize(backups_sizes[oldest_id])))

    def backup(self, name: str):
        if not name in self.bases:
            print("Database {}:{} doesn't exist in config file.".format(self.name, name))
            exit(0)
        print("Backup of {}:{} started".format(self.name, name))
        if not os.path.isdir(os.path.join(DATA_DIR, self.name)):
            os.mkdir(os.path.join(DATA_DIR, self.name))
        if not os.path.isdir(os.path.join(DATA_DIR, self.name, name)):
            os.mkdir(os.path.join(DATA_DIR, self.name, name))
        res = requests.post(
            'http://{}:{}/web/database/backup'.format(self.ip, self.port),
            data=dict(
                master_pwd=self.master_pwd,
                name=name,
                backup_format="zip"
            )
        )
        if not res.ok:
            print("Failed to download backup:", res.status_code)
        now = datetime.now()
        with open(os.path.join(DATA_DIR, self.name, name, backup_name_from_datetime(now)), 'wb') as file:
            file.write(res.content)
        print("Backup succesfull at {} (size: {})".format(now, naturalsize(len(res.content))))


    def backup_all(self):
        for base in self.bases:
            self.backup(base)
