import os
import random
import threading
import time
import uuid
import random
from whatap import logging
from whatap.conf.configure import Configure as conf
from whatap.io.data_inputx import DataInputX
from whatap.io.data_outputx import DataOutputX
from whatap.util.linked_map import LinkedMap
import whatap.util.date_util as date_util


class TraceContextManager(object):
    entry = LinkedMap()
    local = threading.local()
    node = uuid.getnode()
    clock_seq = random.randrange(1 << 14)
    
    @classmethod
    def keys(cls):
        return cls.entry.keys()
    
    @classmethod
    def getActiveCount(cls):
        act = [0 for _ in range(3)]
        try:
            en = cls.entry.values()
            while en.hasMoreElements():
                ctx = en.nextElement()
                elapsed = ctx.getElapsedTime()
                if elapsed < conf.trace_active_transaction_yellow_time:
                    act[0] += 1
                elif elapsed < conf.trace_active_transaction_red_time:
                    act[1] += 1
                else:
                    act[2] += 1
        
        except Exception as e:
            logging.debug(e, extra={'id': 'WA310'}, exc_info=True)
        
        return act

    @classmethod
    def getActiveStats(cls):
        act = [0 for _ in range(5)]
        try:
            en = cls.entry.values()
            while en.hasMoreElements():
                ctx = en.nextElement()
                if ctx.active_sqlhash:
                    act[1] += 1 # sql
                elif ctx.active_httpc_hash:
                    act[2] += 1 # httpc
                elif ctx.db_opening:
                    act[3] += 1 # dbc
                elif ctx.socket_connecting:
                    act[4] += 1  # socket
                else:
                    act[0] += 1 # method
        except Exception as e:
            logging.debug(e, extra={'id': 'WA311'}, exc_info=True)
        return act

    @classmethod
    def getContextEnumeration(cls):
        return cls.entry.values()
    
    @classmethod
    def getContext(cls, key):
        return cls.entry.get(key)
    
    @classmethod
    def getLocalContext(cls):
        if not bool(cls.local.__dict__):
            cls.local.context = None
        
        return cls.local.context
    
    @classmethod
    def getId(cls):
        uuid1 = uuid.uuid1(TraceContextManager.node, TraceContextManager.clock_seq)
        key = (uuid1.int >> 64 & 0xffffffffffffffff) ^ (uuid1.int << 64 & 0xffffffffffffffff)
        return key
    
    @classmethod
    def start(cls, o, thread_id):
        pid = os.getpid()
        dout = DataOutputX()
        dout.writeInt(pid)
        dout.writeInt(0)
        din = DataInputX(dout.buffer.getvalue())
        key = din.readLong() + thread_id
        cls.local.context = o
        cls.entry.put(key, o)

        return key
    
    @classmethod
    def parseThreadId(cls, key):
        pid = os.getpid()
        dout = DataOutputX()
        dout.writeInt(pid)
        dout.writeInt(0)
        din = DataInputX(dout.buffer.getvalue())
        thread_id = key - din.readLong()
        return thread_id, pid
    
    @classmethod
    def end(cls, key):
        cls.local.context = None
        cls.entry.remove(key)

    @classmethod
    def getTxProfile(cls, n):
        ctx = cls.getLocalContext()
        if not ctx:
            return None
        return ctx.profile.getLastSteps(n)
