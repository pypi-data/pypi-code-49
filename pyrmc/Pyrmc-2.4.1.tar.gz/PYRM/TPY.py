import os
import sys
import sqlite3
import getpass
import time
import threading
from datetime import datetime
import PYRM.PYRM


class pyTS:
    def __init__(self, dump_path="cache", precision_update=1):
        try:
            os.mkdir(dump_path)
        except:
            pass
        self.updating_time=precision_update
        self.sqldb=f'{dump_path}/infot.db3'
        try:
            conn = sqlite3.connect(self.sqldb)
            c = conn.cursor()
            c.execute('CREATE TABLE info (pseudo text, time text)')
            conn.commit()
            conn.close()
        except:
            os.remove(self.sqldb)
            conn = sqlite3.connect(self.sqldb)
            c = conn.cursor()
            c.execute('CREATE TABLE info (pseudo text, time text)')
            conn.commit()
            conn.close()
        self.commands={}
        self.stop=False

    def add_time_func(self, path_call, pseudo, time):
        self.commands[pseudo]= path_call
        conn = sqlite3.connect(self.sqldb)
        c = conn.cursor()
        c.execute(f"INSERT INTO info VALUES ('{pseudo}','{time}')")
        conn.commit()
        conn.close()
    def __updating_thread(self):

        while True:
            if self.stop==True:
                break    
            now = datetime.now()
            self.dcurrent_time = now.strftime("%H:%M:%S")
            self.mcurrent_time = now.strftime("%M:%S")
            self.scurrent_time = now.strftime("%S")
            time.sleep(self.updating_time)
    def __dverif_thread(self):
        while True:
            if self.stop==True:
                break
            conn = sqlite3.connect(self.sqldb)
            c = conn.cursor()
            c.execute(f'SELECT pseudo FROM info WHERE time="{self.dcurrent_time}"')
            for i in c.fetchall():
                func2exe=self.commands[i[0]]
                func2exe()
            
            conn.commit()
            conn.close()
            time.sleep(self.updating_time)
    def __mverif_thread(self):
        while True:
            if self.stop==True:
                break
            conn = sqlite3.connect(self.sqldb)
            c = conn.cursor()
            c.execute(f'SELECT pseudo FROM info WHERE time="{self.mcurrent_time}"')
            for i in c.fetchall():
                func2exe=self.commands[i[0]]
                func2exe()
            conn.commit()
            conn.close()
            time.sleep(self.updating_time)
    def __sverif_thread(self):
        while True:
            if self.stop==True:
                break
            conn = sqlite3.connect(self.sqldb)
            c = conn.cursor()
            c.execute(f'SELECT pseudo FROM info WHERE time="{self.scurrent_time}"')
            for i in c.fetchall():
                func2exe=self.commands[i[0]]
                func2exe()
            
            conn.commit()
            conn.close()
            time.sleep(self.updating_time)
    def quit(self):
        self.stop=True

    def post(self):
        self.u = threading.Thread(target=self.__updating_thread, args=())
        self.u.start()
        self.d = threading.Thread(target=self.__dverif_thread, args=())
        self.d.start()
        self.m = threading.Thread(target=self.__mverif_thread, args=())
        self.m.start()
        self.s = threading.Thread(target=self.__sverif_thread, args=())
        self.s.start()
        