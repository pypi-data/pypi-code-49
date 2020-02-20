# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: Sep 15, 2018
# Modifi: Sep 30, 2018

from siki.pysql import PySQLConnection as pys
from siki.basics import Logger as logger
from siki.basics.Logger import Priority as p
from siki.basics import Exceptions as excepts
from siki.dstruct.Queue import Queue


class PySQLPool(object):

    def __init__(self, size, **params):
        """
        setting up a process pool for sql handling
        Args:
        * [size] the number of sql connections to keep
        * [config] the configuration file in json format to load
        * [params] user, password, host, port, db, bstd, blog, dir, fname
        """
        self.pool = Queue()

        if 'bstd' in params.keys() and 'blog' in params.keys() \
            and 'dir' in params.keys() and 'fname' in params.keys():
            logger.init(bool(params['bstd']), bool(params['blog']), params['dir'], params['fname'])
        else:
            logger.init(True, False)

        try:
            for i in range(size):
                # create a connection to sql server
                conn = pys.connect(user=params['user'], password=params['password'],
                    host=params['host'], port=params['port'])

                # add connection to queue
                self.pool.enqueue(conn)
            
            # print debug message
            logger.message(p.INFO, msg="creating connections pool finished")
        except excepts.SQLConnectionException as e:
            logger.message(p.ERROR, msg="creating connection failed", exception=e)


    def get_connection(self):
        """
        Draw a connection from pool
        Returns:
        * [conn] pymysql.connect, the connection object from pool
        """
        try:
            # returns a conn instance when one is available else 
            # waits until one is
            conn = None
            if len(self.pool) > 0:
                conn = self.pool.dequeue()

            # checks if conn is still connected because conn instance 
            # automatically closes when not in used
            if conn and not pys.check_connection(conn):
                conn.connect()
            
            return conn
        except Exception as e:
            logger.message(p.ERROR, msg="get connection failed", exception=e)


    def put_connection(self, conn):
        """
        Put a connection back to pool
        Args:
        * [conn] pymysql.connect
        """
        if conn and pys.check_connection(conn):
            return self.pool.enqueue(conn)
        else:
            logger.message(p.ERROR, msg="an empty connection wants to add to queue, skipped")


    def refresh(self):
        """
        Refresh the connection pool, this function will fix broken connections.
        """
        backs = []
        for conn in self.pool:
            if conn and not pys.check_connection(conn):
                backs.append(conn)
        self.pool.merge(backs)


    
    def is_empty(self):
        """
        Whether the pool is empty
        Returns:
        * [res] bool
        """
        return self.pool.is_empty()


    def close(self):
        """
        Close the connection pool, this function will release all resources
        """
        logger.message(p.INFO, msg = "closing pool...")
        while not self.is_empty():
            pys.disconnect(self.pool.dequeue())
        logger.message(p.INFO, msg = "PySQLPool colsed")
    

    def size(self):
        """
        Returning the size of pool
        Returns:
        * [size] int, the size of contained connections
        """
        return self.pool.size()

    
    def update_log(self, message):
        """
        Print out a message to console or log file, this depending on your setting of logger 
        Args:
        * [message] str
        """
        logger.message(p.INFO, msg = message)