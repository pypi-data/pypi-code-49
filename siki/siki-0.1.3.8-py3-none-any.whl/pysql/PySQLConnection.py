# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: May 08, 2018
# Modifi: Oct 02, 2018

import pymysql
from siki.basics.Exceptions import *
from siki.basics import ParametersCheck as paramc



def connect(password, user="root", host="127.0.0.1", port=3306):
    """
    Create a connection to server
    Args:
    * [host] host ip address, default is localhost
    * [user] user name for sql authorization, default is root
    * [password] user password for sql authorization
    * [port] connection port, default is 3306, not requried
    Returns:
    a connection to the database
    """
    res, nullkeys = paramc.check_null_params(user=user, password=password, host=host, port=port)
    
    if res is True:
        raise InvalidParamException("parameters cannot be null!")

    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        charset="UTF8",
        cursorclass=pymysql.cursors.DictCursor)
    return connection


def disconnect(connection):
    """
    Disconnect to MySQL server
    Args:
    connection (connector)
    """
    connection.close()


def reconnect(connection):
    """
    Reconnect to server
    """
    connection.connect()


def check_connection(connection):
    """
    Check a connection is available
    Args:
    connection (connector)
    """
    with connection.cursor() as cursor:
        cursor.execute("SELECT version()")
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False


def execute(connection, statement):
    """
    execute sql command
    Args:
    connection (connector)
    statement (str)
    """
    with connection.cursor() as cursor:
        rows = cursor.execute(statement)
        connection.commit()
        return rows


def query(connection, statement):
    """
    query sql command
    Args:
    connection (connector)
    statement (str)
    """
    with connection.cursor() as cursor:
        rows = cursor.execute(statement)
        res = None
        if rows > 1:
            res = cursor.fetchall()
        if rows == 1:
            res = cursor.fetchone()
        return res


def multi_execute(connection, statement, varbs):
    """
    execute multi-commands
    Args:
    * [connection] pymysql.connection
    * [statement] str, template
    * [varbs] list
    Usage:
    multi_execute(conn, "insert into table (key1, key2, key3, ...) values (% % % %)"), varbs
    is list of [[val1, val2, val3, ...], [val1, val2, val3, ...]]
    """
    with connection.cursor() as cursor:
        rows = 0
        for var in varbs:
            rows += cursor.execute(statement, var)
        connection.commit()
        return rows