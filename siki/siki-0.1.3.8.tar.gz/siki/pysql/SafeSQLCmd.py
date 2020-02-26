# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Created: May 08, 2018
# LastChg: Feb 18, 2020

import re

from siki.pysql import PySQLConnection as pys
from siki.basics import Exceptions as excepts

def _has_keywords(arg):
    pattern = r"(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|MERGE|SELECT|UPDATE|UNION( +ALL){0,1})"
    return re.search(pattern, arg) is not None


def _sql_args_check(*args):
    for arg in args:
        if _has_keywords(str(arg).upper()):
            return False
    return True


def safe_insert(conn, db, table, args, debug=False):
    """
    safely inserting database, and avoid sql injection attack
    
    Args:
    * [conn] connection of sql
    * [db] database name
    * [table] table name
    * [args(dict)] the data to insert, something like: {id:1, key1:val1, key2:val2, ...}
    * [debug] default to False, if you wannar to see the output sql statement, make it to True
    
    Returns:
    * [sql] str, command of sql
    """
    
    res = _sql_args_check(db, table, args.keys(), args.values())
    
    if res is False:
        raise excepts.SQLInjectionException(
            "SQL injection detected, params: table[{}], args[{}]".format(table, args))

    if conn is None:
        raise excepts.InvalidParamException("conn cannot be null")

    if type(args) is not dict:
        raise excepts.InvalidParamException("args must be dict type")

    # generate a insert sql command
    keys = "`" + "`, `".join(args.keys()) + "`"
    values = "'" + "', '".join(args.values()) + "'"

    # generate insert sentence
    STR_SQL = "INSERT INTO `{}`.`{}` ({}) VALUES ({})".format(db, table, keys, values)

    if debug: # for debug only
        print(STR_SQL)

    # executing sql command
    return pys.execute(conn, STR_SQL)



def safe_query_id(conn, db, table, item_id, debug=False):
    """
    safely querying database, and avoid sql injection attack

    Args:
    * [conn] connection of sql
    * [db] database name
    * [table] table name
    * [item_id] the item id want to search
    * [debug] default to False, if you wannar to see the output sql statement, make it to True

    Returns:
    * [rows(dict)] the execution results
    """
    res = _sql_args_check(db, table, item_id)
    if res is False:
        raise excepts.SQLInjectionException(
            "SQL injection detected, params: table[{}], id[{}]".format(table, item_id))

    if conn is None:
        raise excepts.InvalidParamException("Conn cannot be null")
    
    # generate query sentence
    STR_SQL = "SELECT * FROM `{}`.`{}` WHERE `id`='{}'".format(db, table, item_id)
    
    if debug: # for debug only
        print(STR_SQL)

    # executing sql
    return pys.query(conn, STR_SQL)



def safe_simple_query(conn, db, table, select_con, where_con=None, order_by=None, debug=False):
    """
    safely simple querying, not allow nested querying to avoid sql injection.

    Args:
    * [conn] connection of sql
    * [db] database name
    * [table] table name
    * [select_con] selection condition
    * [where_con] where condition
    * [order_by] order by command, default sequency is asc, if you want a desc results, append "DESC" to your command
    * [debug] default to False, if you wannar to see the output sql statement, make it to True

    Returns:
    * [rows(dict/list)] dict, the execution results
    """
    res = _sql_args_check(db, table, select_con, where_con, order_by)
    if res is False:
        raise excepts.SQLInjectionException(
                "SQL injection detected, params: table[{}] select[{}] where[{}] order[{}]"
                .format(table, select_con, where_con, order_by)
        )
    
    if conn is None:
        raise excepts.InvalidParamException("Conn cannot be null")

    # generate simple querying
    STR_SQL = "SELECT {} FROM `{}`.`{}`".format(select_con, db, table)
    if where_con is not None:
        STR_SQL += " WHERE {}".format(where_con)
    if order_by is not None:
        STR_SQL += " ORDER BY {}".format(order_by)

    if debug: # for debug only
        print(STR_SQL)    

    # executing sql
    return pys.query(conn, STR_SQL)



def safe_update(conn, db, table, item_id, args, debug=False):
    """
    safely updating database, and avoid sql injection attack

    Args:
    * [conn] connection of sql
    * [db] database name
    * [table] table name
    * [item_id] the item id want to update
    * [args(dict)] the data to update, something like: {id:1, key1:val1, key2:val2, ...}
    * [debug] default to False, if you wannar to see the output sql statement, make it to True

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
    STR_SQL = "UPDATE `{}`.`{}` SET {} WHERE `id`='{}'".format(db, table, pvals, item_id)
    
    if debug: # for debug only
        print(STR_SQL)  

    # executing sql
    return pys.execute(conn, STR_SQL)



def safe_delete(conn, db, table, item_id, debug=False):
    """
    safely deleting row in table

    Args:
    * [conn] connection of sql
    * [db] database name
    * [table] table name
    * [item_id] the item id want to delete

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
    STR_SQL = "DELETE FROM `{}`.`{}` WHERE `id` = '{}'".format(db, table, item_id)

    if debug: # for deubg
        print(STR_SQL)
    
    # executing sql
    return pys.execute(conn, STR_SQL)



def safe_query_tables(conn, db):
    """
    safely show tables in schema

    Args:
    * [conn] connection of sql
    * [db] database name

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

    Args:
    * [conn] connection of sql
    * [db] database name
    * [table] table name

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
    STR_SQL = "SHOW COLUMNS IN `{}`.`{}`".format(db, table)
    
    # executing sql
    return pys.query(conn, STR_SQL) # obtaining a list
