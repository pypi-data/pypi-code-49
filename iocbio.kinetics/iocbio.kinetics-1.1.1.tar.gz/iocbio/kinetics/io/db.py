# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2019-2020
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  This file is part of project: IOCBIO Kinetics
#
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QGridLayout, QMessageBox, QLabel, QCheckBox, QFileDialog
from PyQt5.QtCore import QSettings
from collections import OrderedDict
import os, keyring, sys, traceback

from ..thirdparty.records import Database

def mkdir_p(path):
    import errno
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


class Login(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("PostgreSQL login")
        self.textName = QLineEdit(self)
        self.textPass = QLineEdit(self)
        self.textPass.setEchoMode(QLineEdit.Password)
        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.rememberPassword = QCheckBox("Store password in keyring")
        self.rememberPassword.setCheckState(False)
        layout = QGridLayout(self)
        layout.addWidget(QLabel("User:"), 0, 0)
        layout.addWidget(self.textName, 0, 1)
        layout.addWidget(QLabel("Password:"), 1, 0)
        layout.addWidget(self.textPass, 1, 1)
        layout.addWidget(self.buttonLogin,2,1)
        layout.addWidget(self.rememberPassword,3,1)

    def handleLogin(self):
        self.username = self.textName.text()
        self.password = self.textPass.text()
        self.accept()


class DatabaseInterface:
    """Database interface and helper functions"""

    schema_version = "2"
    database_table = "iocbio"
    keyring_key = "iocbio-kinetics"

    settings_compname = "iocbio"
    settings_appname = "kinetics"
    settings_dbtype = "database/type"

    settings_pg_hostname = "database/postgresql/hostname"
    settings_pg_database = "database/postgresql/database"
    settings_pg_schema = "database/postgresql/schema"
    settings_pg_username = "database/postgresql/username"

    username = None
    password = None

    def __init__(self):
        settings = self.settings()

        self.database = None
        self.dbtype = str(settings.value(DatabaseInterface.settings_dbtype, "sqlite3"))
        self.read_only = False
        self.disable_read_only = False # not needed here, but keeping for completeness
        self.pg_schema = str(settings.value(DatabaseInterface.settings_pg_schema, ""))

        self.debug_sql = (int(settings.value("database/debug", 0)) > 0)

        if self.dbtype == "sqlite3":
            self.database, self.connection_parameters = self.open_sqlite3()
        elif self.dbtype == "postgresql":
            self.database, self.connection_parameters = self.open_postgresql()
        else:
            raise NotImplementedError("Not implemented: " + self.dbtype)

        if self.database is not None:
            self.schema()

    def __del__(self):
        self.close()

    def set_read_only(self, state):
        if self.disable_read_only:
            self.read_only = False
        else:
            self.read_only = state

    @staticmethod
    def open_sqlite3():
        from PyQt5.QtCore import QStandardPaths

        path = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        mkdir_p(path)
        fname = os.path.join(path,"kinetics.sqlite")

        database = Database("sqlite:///" + fname)

        # require foreign key constraints to be followed
        database.query("PRAGMA foreign_keys=ON")

        # save parameters
        connection_parameters = OrderedDict()
        connection_parameters['Database connection type'] = 'SQLite3'
        connection_parameters['File name'] = fname
        return database, connection_parameters

    @staticmethod
    def open_postgresql():
        save = False

        settings = DatabaseInterface.settings()

        pg_hostname = str(settings.value(DatabaseInterface.settings_pg_hostname, ""))
        pg_database = str(settings.value(DatabaseInterface.settings_pg_database, ""))
        pg_schema = str(settings.value(DatabaseInterface.settings_pg_schema, ""))

        if len(pg_hostname)<1 or len(pg_database)<1 or len(pg_schema)<1:
            QMessageBox.warning(None, 'Error',
                                "Failed to open PostgreSQL database connection\nEither hostname, database, or schema not specified")
            return None,None

        if DatabaseInterface.username is None:
            username = str(settings.value(DatabaseInterface.settings_pg_username, defaultValue = ""))
            try:
                password = keyring.get_password(DatabaseInterface.keyring_key, username)
            except:
                print('Failed to get password from keyring, assuming that it is not available')
                password = None

            if len(username) < 1 or password is None:
                login = Login()
                if login.exec_() == QDialog.Accepted:
                    username = login.username
                    password = login.password
                    save = login.rememberPassword.checkState()
                else:
                    return None,None
        else:
            username = DatabaseInterface.username
            password = DatabaseInterface.password

        try:
            database = Database("postgresql://" + username + ":" + password +
                                "@" + pg_hostname + "/" + pg_database)
            DatabaseInterface.username = username
            DatabaseInterface.password = password
        except Exception as expt:
            if not save:
                DatabaseInterface.remove_login(username = username)
            print('Exception', expt)
            QMessageBox.warning(None, 'Error',
                                "Failed to open PostgreSQL database connection\n\nException: " + str(expt))
            database = None

        if save:
            # let's save the settings
            settings.setValue(DatabaseInterface.settings_pg_username, username)
            try:
                keyring.set_password(DatabaseInterface.keyring_key, username, password)
            except Exception as e:
                errtxt = '\nError occurred while saving password to the keyring:\n\n' + str(e) + "\n\n" + str(type(e))
                print(errtxt + '\n\n')
                print(traceback.format_exc())
                QMessageBox.warning(None, 'Warning',
                                    "Failed to save password in a keyring")

        # store connection parameters
        connection_parameters = OrderedDict()
        connection_parameters['Database connection type'] = 'PostgreSQL'
        connection_parameters['Host name'] = pg_hostname
        connection_parameters['Database'] = pg_database
        connection_parameters['Schema'] = pg_schema
        connection_parameters['User'] = username
        return database, connection_parameters

    def close(self):
        if self.database is not None:
            self.database.close()
            self.database = None

    def query(self, command, **kwargs):
        if self.read_only:
            for k in ['insert ', 'create ', 'update ', 'set ', 'delete ']:
                if k in command.lower():
                    print('Read only mode, no data changes allowed. Skipped:', command)
                    return None

        if self.debug_sql:
            print(command, kwargs)

        # the rest goes via records
        return self.database.query(command, **kwargs)

    def schema(self):
        """Check the present schema version, create if missing and return the version of current schema"""

        tname = self.table(DatabaseInterface.database_table)
        self.query("CREATE TABLE IF NOT EXISTS " + tname + "(name text NOT NULL PRIMARY KEY, value text NOT NULL)")

        version = None
        for row in self.query("SELECT value FROM " + tname + " WHERE name=:name", name = "kinetics_version"):
            version = row[0]

        if version is None:
            self.query("INSERT INTO " + tname + "(name, value) VALUES(:name,:val)",
                       name = "kinetics_version", val = DatabaseInterface.schema_version)
            version = DatabaseInterface.schema_version

        if version == DatabaseInterface.schema_version:
            pass
        else:
            raise RuntimeError("This version (%s) of database schema is not supported" % version)

    def table(self, name, with_schema=True):
        # IF CHANGED HERE, CHECK OUT also the following methods
        #   has_view
        if self.dbtype == "sqlite3": return name
        elif self.dbtype == "postgresql":
            if with_schema: return self.pg_schema + ".kinetics_" + name
            else: return "kinetics_" + name
        else:
            raise NotImplementedError("Not implemented table name mangling: " + self.dbtype)

    def get_table_column_names(self, name):
        for c in self.query("SELECT * FROM %s LIMIT 1" % self.table(name)):
            return c.keys()
        return None

    def has_record(self, table, **kwargs):
        a = []
        sql = "SELECT 1 FROM " + self.table(table) + " WHERE "
        for key in kwargs.keys():
            sql += key + "=:" + key + " AND "
        sql = sql[:-5] # dropping excessive " AND "
        sql += " LIMIT 1"
        for row in self.query(sql, **kwargs):
            return True
        return False

    def has_view(self, view):
        if self.dbtype == "sqlite3":
            for row in self.query("SELECT 1 AS reply FROM sqlite_master WHERE type='view' AND " +
                                  "name=:view", view=self.table(view)):
                return True
        elif self.dbtype == "postgresql":
            for row in self.query("SELECT 1 AS reply FROM information_schema.views WHERE " +
                                  "table_schema=:schema AND table_name=lower(:view)",
                                  schema=self.pg_schema, view=self.table(view, with_schema=False)):
                return True
        else:
            raise NotImplementedError("Not implemented table name mangling: " + self.dbtype)

        return False

    @property
    def is_ok(self):
        return self.database is not None

    @staticmethod
    def get_database():
        settings = DatabaseInterface.settings()
        dbtype = str(settings.value(DatabaseInterface.settings_dbtype, "sqlite3"))
        if dbtype == "sqlite3":
            database, connection_parameters = DatabaseInterface.open_sqlite3()
        elif dbtype == "postgresql":
            database, connection_parameters = DatabaseInterface.open_postgresql()
        else:
            raise NotImplementedError("Not implemented: " + dbtype)
        return database

    @staticmethod
    def remove_login(username = None):
        """Remove all saved login information"""
        settings = DatabaseInterface.settings()
        if not username:
            username = str(settings.value(DatabaseInterface.settings_pg_username, defaultValue = ""))
        settings.setValue(DatabaseInterface.settings_pg_username, "")
        DatabaseInterface.username = None
        DatabaseInterface.password = None
        try:
            if username:
                keyring.delete_password(DatabaseInterface.keyring_key, username)
                print('User %s deleted from keyring %s' % (username, DatabaseInterface.keyring_key))
        except:
            print('Failed to delete password from keyring')

    @staticmethod
    def settings():
        return QSettings(DatabaseInterface.settings_compname, DatabaseInterface.settings_appname)



#####################################################################################
### Authentication function used by legacy scripts

def authenticate_sysbio_database(username, server='sysbio-db.kybi/experiments_v2'):
    print('WARNING TO SYSBIO DEVELOPERS: Please adjust the scripts to call DatabaseInterface.get_database()')
    py3 = version_info[0] > 2 # If true python3 is used
    if py3: cli_input = input
    else: cli_input = raw_input

    try:
        password = keyring.get_password(server, username)
    except:
        pwd_file = '/home/martinl/crypt/auth/sysbio-db/pwd'
        if os.path.isfile(pwd_file):
            with open(pwd_file, 'r') as f:
                password = f.read()
        else:
            print('No such file:', pwd_file)
            print('Create password file in crypted folder.')
            exit()

    print('Connecting to {}'.format(server))

    if password is None:
        username = cli_input('  Enter your username: ')
        password = getpass.getpass(prompt='  Enter your password: ')
        save_inp = cli_input('  Save username and password [n/y]: ')

        save = False
        if save_inp == 'y':
            save = True
            keyring.set_password(server, username, password)
            print('Username and password saved.')

        else:
            keyring.delete_password(server, username)
            print('Username and password not saved.')

    return username, password, server
