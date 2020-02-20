import os
import yaml
import pymysql
from termcolor import colored

def get_config(path):
    return yaml.load(open(path).read())

def create_connection(config):
    try:
        connection = pymysql.connect(host=config['host'],
                                     user=config['user'],
                                     password=config['password'],
                                     db=config['db'])
    except pymysql.err.InternalError:
        connection = pymysql.connect(host=config['host'],
                                     user=config['user'],
                                     password=config['password'])
        print(colored('[!] warning, database not exists, please create database "{}"'.format(config['db']), 'yellow'))
    return connection

def check_column_exist(conn, db, table, column):
    cur = conn.cursor()
    cur.execute('''SELECT COUNT(*) FROM information_schema.columns WHERE
                        table_name='%s' AND
                        table_schema='%s' AND
                        column_name='%s' ''' % (table, db, column))
    return cur.fetchone()[0]

def add_column(conn, table, column, datatype):
    cur = conn.cursor()
    cur.execute('''ALTER TABLE %s ADD %s %s''' % (table, column, datatype))
    conn.commit()
