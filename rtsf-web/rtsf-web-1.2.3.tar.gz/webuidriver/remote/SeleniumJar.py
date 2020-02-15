# -*- encoding: utf-8 -*-
'''
Current module: rock4.softtest.web.SeleniumJar

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      rock4.softtest.web.SeleniumJar,v 1.0 2017年2月27日
    FROM:   2017年2月27日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

import requests
import time,subprocess

class SeleniumJar(object):    
    def __init__(self, server_jar_full_path, java_exe_full_path = "java"):
        self._conf = {
            "java_path": java_exe_full_path,
            "jar_path": server_jar_full_path,
            }
                        
    def hub(self, port):
        ''' java -jar selenium-server.jar -role hub -port 4444
        @param port:  listen port of selenium hub 
        '''
        self._ip = "localhost"
        self._port = port 
        self.command = [self._conf["java_path"], "-jar", self._conf["jar_path"], "-port", str(port), "-role", "hub"]        
        return self
        
    def node(self,port, hub_address=("localhost", 4444)):
        ''' java -jar selenium-server.jar -role node -port 5555 -hub http://127.0.0.1:4444/grid/register/
        @param port:  listen port of selenium node
        @param hub_address: hub address which node will connect to 
        '''
        self._ip, self._port = hub_address
        self.command = [self._conf["java_path"], "-jar", self._conf["jar_path"], "-port", str(port), "-role", "node", "-hub", "http://%s:%s/grid/register/" %(self._ip, self._port)]        
        return self
    
    def start_server(self):
        """start the selenium Remote Server."""        
        self.__subp = subprocess.Popen(self.command)        
        #print("\tselenium jar pid[%s] is running." %self.__subp.pid)        
        time.sleep(2)
        
    def stop_server(self):
        """stop the selenium Remote Server
        :return:
        """
        self.__subp.kill()
        #print("\tselenium jar pid[%s] is stopped." %self.__subp.pid)
        
    def re_start_server(self):
        """reStart the selenium Remote server"""
        self.stop_server()
        self.start_server()
    
    def is_runnnig(self):
        """Determine whether hub server is running
        :return:True or False
        """
        resp = None
        try:
            resp = requests.get("http://%s:%s" %(self._ip, self._port))

            if resp.status_code == 200:
                return True
            else:
                return False
        except:
            return False
    