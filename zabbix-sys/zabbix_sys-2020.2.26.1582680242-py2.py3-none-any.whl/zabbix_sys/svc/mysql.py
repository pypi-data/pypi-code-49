
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import sys
import os
import mysql.connector
import mysql.connector.errorcode


# TODO: Refactoring
# TODO: Add debug messages
class MySQL:

    def __init__(self, cfg, logger):
        self.logger = logger
        self.dsn = {
        }

        if cfg and 'mysql' in cfg:
            if 'user' in cfg['mysql']:
                self.dsn.update({"user": cfg['mysql']['user']})
            if 'password' in cfg['mysql']:
                self.dsn.update({"password": cfg['mysql']['password']})
            if 'host' in cfg['mysql']:
                self.dsn.update({"host": cfg['mysql']['host']})
            if 'port' in cfg['mysql']:
                self.dsn.update({"port": cfg['mysql']['port']})
        else:
            if os.path.isfile(os.path.expanduser('~/.my.cnf')):
                self.dsn.update({"read_default_file": os.path.expanduser('~/.my.cnf')})

        self.cnx = None
        self.cur = None

    def __connect__(self, dictionary=False):

        self.cnx = mysql.connector.connect(**self.dsn)
        self.cur = self.cnx.cursor(dictionary=dictionary)

    def __disconnect__(self):
        try:
            if self.cur:
                self.cur.close()
            if self.cnx:
                self.cnx.close()
        except Exception as err:
            self.logger.debug(msg=err.__str__(), exc_info=False)

    def lld(self):
        """
        :return: MySQL version
        """
        try:
            self.__connect__()
            self.cur.execute('SHOW VARIABLES LIKE "version";')

            version = self.cur.fetchone()[1]
            branch = ".".join(str(version).split('.')[:-1])

            self.__disconnect__()

            slave = self.raw_slave()
            master = self.raw_master()

            result = {
                "data": [
                    {
                        "_": "",
                        "mysql_version": str(version),
                        "mysql_branch": str(branch),
                        "mysql_replication_slave": True if slave else False,
                        "mysql_replication_master": True if master else False
                    }
                ]
            }

            return result

        except mysql.connector.errors.Error as err:
            if err.errno == mysql.connector.errorcode.CR_CONN_HOST_ERROR or err.errno == -1:
                return {"data": []}
            else:
                self.logger.error(msg=err.__str__(), exc_info=False)
                sys.exit(1)

    def raw_master(self):
        """
        :return: SHOW MASTER STATUS as dictionary
        """

        result = {}

        try:
            self.__connect__(dictionary=True)
            self.cur.execute("SHOW MASTER STATUS;")
            res = self.cur.fetchone()
            self.__disconnect__()

            if res:
                for key, value in res.items():
                    result.update({str(key).lower(): str(value)})
            return result

        except Exception as err:
            self.logger.error(msg=err.__str__(), exc_info=False)
            sys.exit(1)

    def raw_slave(self):
        """
        :return: SHOW SLAVE STATUS as dictionary
        """
        result = {}

        try:
            self.__connect__(dictionary=True)
            self.cur.execute("SHOW SLAVE STATUS;")
            res = self.cur.fetchone()
            self.__disconnect__()

            if res:
                for key, value in res.items():
                    result.update({str(key).lower(): str(value)})
            return result

        except Exception as err:
            self.logger.error(msg=err.__str__(), exc_info=True)
            sys.exit(1)

    def raw_status(self):
        """
        :return: SHOW GLOBAL STATUS as dictionary
        """
        result = {}

        try:
            self.__connect__()
            self.cur.execute("SHOW GLOBAL STATUS;")
            res = self.cur.fetchall()
            self.__disconnect__()

            for row in res:
                result.update({str(row[0]).lower(): str(row[1])})
            return result

        except Exception as err:
            self.logger.error(msg=err.__str__(), exc_info=False)
            sys.exit(1)

    def raw_config(self):
        """
        :return: SHOW GLOBAL VARIABLES as dictionary
        """
        result = {}

        try:
            self.__connect__()
            self.cur.execute('SHOW GLOBAL VARIABLES;')
            res = self.cur.fetchall()
            self.__disconnect__()

            for row in res:
                result.update({str(row[0]).lower(): str(row[1])})
            return result

        except Exception as err:
            self.logger.error(msg=err.__str__(), exc_info=False)
            sys.exit(1)
