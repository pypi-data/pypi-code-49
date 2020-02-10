# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: May 08, 2018
# Modifi: Oct 02, 2018

import re

from siki.pysql import PySQLConnection as pys
from siki.basics import Exceptions as excepts

STR_SQL = ""

def _has_keywords(arg):
    pattern = r"(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|MERGE|SELECT|UPDATE|UNION( +ALL){0,1})"
    return re.search(pattern, arg) is not None


def _sql_args_check(*args):
    for arg in args:
        if _has_keywords(str(arg).upper()):
            return False
    return True


def get_last_cmd():
    global STR_SQL
    return STR_SQL


def safe_insert(conn, db, table, item_id, **args):
    """
    safely inserting database, and avoid sql injection attack
    Returns:
    * [sql] str, command of sql
    """
    res = _sql_args_check(db, table, item_id, args.keys(), args.values())
    if res is False:
        raise excepts.SQLInjectionException(
            "SQL injection detected, params: table[{}], id[{}], args[{}]"
            .format(table, item_id, args)
        )

    if conn is None:
        raise excepts.InvalidParamException("Conn cannot be null")

    # append item it 
    args['id'] = item_id

    # generate a insert sql command
    keys = "`" + "`, `".join(args.keys()) + "`"
    values = "'" + "', '".join(args.values()) + "'"

    # generate insert sentence
    global STR_SQL
    STR_SQL = "INSERT INTO `{}`.`{}` ({}) VALUES ({})".format(db, table, keys, values)

    # executing sql command
    return pys.execute(conn, STR_SQL)



def safe_query_id(conn, db, table, item_id):
    """
    safely querying database, and avoid sql injection attack
    Returns:
    * [rows] dict, the execution results
    * [sql] str, the command of sql
    """
    res = _sql_args_check(db, table, item_id)
    if res is False:
        raise excepts.SQLInjectionException(
            "SQL injection detected, params: table[{}], id[{}]"
            .format(table, item_id)
        )

    if conn is None:
        raise excepts.InvalidParamException("Conn cannot be null")
    
    # generate query sentence
    global STR_SQL
    STR_SQL = "SELECT * FROM `{}`.`{}` WHERE `id`='{}'".format(db, table, item_id)

    # executing sql
    return pys.query(conn, STR_SQL)



def safe_simple_query(conn, db, table, select_conn, where_conn = None, order_by = None):
    """
    safely simple querying, not allow nested querying to avoid sql injection.
    Returns:
    * [rows] dict, the execution results
    * [sql] str, the command of sql    
    """
    res = _sql_args_check(db, table, select_conn, where_conn, order_by)
    if res is False:
        raise excepts.SQLInjectionException(
                "SQL injection detected, params: table[{}] select[{}] where[{}] order[{}]"
                .format(table, select_conn, where_conn, order_by)
        )
    
    if conn is None:
        raise excepts.InvalidParamException("Conn cannot be null")

    # generate simple querying
    global STR_SQL
    STR_SQL = "SELECT {} FROM `{}`.`{}`".format(select_conn, db, table)
    if where_conn is not None:
        STR_SQL += " WHERE {}".format(where_conn)
    if order_by is not None:
        STR_SQL += " ORDER BY {}".format(order_by)

    # executing sql
    return pys.query(conn, STR_SQL)



def safe_update(conn, db, table, item_id, **args):
    """
    safely updating database, and avoid sql injection attack
    Returns:
    * [sql] str, the command of sql
    """
    res = _sql_args_check(db, table, item_id, args.keys(), args.values())
    if res is False:
        raise excepts.SQLInjectionException(
                "SQL injection detected, params: table[{}] item_id[{}] vals[{}]"
                .format(table, item_id, args)
        )

    if conn is None:
        raise excepts.InvalidParamException("Conn cannot be null")

    # generate sql querying
    setvals = []
    for key, val in args.items():
        if val:
            setvals.append("`" + str(key) + "`='" + str(val) + "'")
        else:
            setvals.append("`" + str(key) + "`=NULL")
    pvals = ", ".join(setvals)

    # generate sql
    global STR_SQL
    STR_SQL = "UPDATE `{}`.`{}` SET {} WHERE `id`='{}'".format(db, table, pvals, item_id)

    # executing sql
    return pys.execute(conn, STR_SQL)



def safe_delete(conn, db, table, item_id):
    """
    safely deleting row in table
    Returns:
    * [sql] str, the command of sql    
    """
    res = _sql_args_check(table, item_id)
    if res is False:
        raise excepts.SQLInjectionException(
                "SQL injection detected, params: table[{}] item_id[{}]"
                .format(table, item_id)
        )

    if conn is None:
        raise excepts.InvalidParamException("Conn cannot be null")

    # generate sql
    global STR_SQL
    STR_SQL = "DELETE FROM `{}`.`{}` WHERE `id` = '{}'".format(db, table, item_id)
    
    # executing sql
    return pys.execute(conn, STR_SQL)



def safe_query_tables(conn, db):
    """
    safely show tables in schema
    Returns:
    * [rows] dict, the execution results
    * [sql] str, the command of sql    
    """
    res = _sql_args_check(db)
    if res is False:
        raise excepts.SQLInjectionException(
                "SQL injection detected, params: db[{}]".format(db))

    if conn is None:
        raise excepts.InvalidParamException("Conn cannot be null")

    # generating sql
    global STR_SQL
    STR_SQL = "SHOW TABLES IN `{}`".format(db)
    
    # executing sql
    rets = []
    for i in pys.query(conn, STR_SQL): # obtaining a list
        for k, v in i.items():
            rets.append(v)
    return rets



def safe_query_columns(conn, db, table):
    """
    safely show columns in table
    Returns:
    * [rows] dict, the execution results
    * [sql] str, the command of sql    
    """
    res = _sql_args_check(db, table)
    if res is False:
        raise excepts.SQLInjectionException(
                "SQL injection detected, params: db[{}] table[{}]".format(db, table))

    if conn is None:
        raise excepts.InvalidParamException("Conn cannot be null")
    
    # generating sql
    global STR_SQL
    STR_SQL = "SHOW COLUMNS IN `{}`.`{}`".format(db, table)
    
    # executing sql
    return pys.query(conn, STR_SQL) # obtaining a list
