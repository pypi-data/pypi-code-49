# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: Sep 15, 2018
# Modifi: Feb 24, 2020

from siki.pysql import PySQLConnection as pys
from siki.basics import Logger as logger
from siki.basics.Logger import Priority as p
from siki.basics import Exceptions as excepts
from siki.dstruct.Queue import Queue

import threading

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
        self.lock = threading.Lock()

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
            self.lock.acquire()

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
        
        finally:
            self.lock.release()




    def put_connection(self, conn):
        """
        Put a connection back to pool
        Args:
        * [conn] pymysql.connect
        """
        try:
            self.lock.acquire()

            if conn and pys.check_connection(conn):
                return self.pool.enqueue(conn)
            else:
                logger.message(p.ERROR, msg="an empty connection wants to add to queue, skipped")

        finally:
            self.lock.release()




    def refresh(self):
        """
        Refresh the connection pool, this function will fix broken connections.
        """
        try:
            self.lock.acquire()

            backs = []
            for conn in self.pool:
                if conn and not pys.check_connection(conn):
                    backs.append(conn)
            self.pool.merge(backs)

        finally:
            self.lock.release()
    



    def is_empty(self):
        """
        Whether the pool is empty
        Returns:
        * [res] bool
        """
        try:
            self.lock.acquire()

            return self.pool.is_empty()

        finally:
            self.lock.release()




    def close(self):
        """
        Close the connection pool, this function will release all resources
        """
        try:
            self.lock.acquire()

            logger.message(p.INFO, msg = "closing pool...")
            
            while not self.is_empty():
                pys.disconnect(self.pool.dequeue())
            
            logger.message(p.INFO, msg = "PySQLPool colsed")
        
        finally:
            self.lock.release()


    

    def size(self):
        """
        Returning the size of pool
        Returns:
        * [size] int, the size of contained connections
        """
        try:
            self.lock.acquire()
            return self.pool.size()
        finally:
            self.lock.release()
        