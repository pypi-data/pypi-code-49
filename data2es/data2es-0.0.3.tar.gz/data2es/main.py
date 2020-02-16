#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#############################################
# File Name: main.py
# Author: stosc
# Mail: stosc@sidaxin.com
# Created Time:  2020-2-8 19:17:34
#############################################
import sys
import os
import time
import argparse

import argparse
import atexit  
import signal 
import traceback

from pyhocon import ConfigFactory


try:
    from webhook import WebhookClient,WebhookServer
    from mysqlProvider import MysqlProvider
    from providerBase import ProviderBase
    from esHelper import EsHelper
    from scheduler import SdxScheduler
    from __init__ import __serverName__
except ModuleNotFoundError:
    from data2es.webhook import WebhookClient,WebhookServer
    from data2es.mysqlProvider import MysqlProvider
    from data2es.providerBase import ProviderBase
    from data2es.esHelper import EsHelper
    from data2es.scheduler import SdxScheduler
    from data2es.__init__ import __serverName__



import _thread

import logging

logger = logging.getLogger('data2es_main')
logger.setLevel(level=logging.INFO)




class Data2es(object):

    def __init__(self,filename):
        super().__init__()
        
        self.loadConfig(filename)
        
    def loadConfig(self,filename):
        try:
            conf = ConfigFactory.parse_file(filename)
            inputs = conf.get_config('input')
            outputs = conf.get_config('output')
            webhook = conf.get_config('webhook')
            self.start_urls = webhook.get_list('start')
            self.finished_urls=webhook.get_list('finished')
            self.error_urls=webhook.get_list('error')
            for i in inputs:
                c = inputs[i]
                provider = c['provider']            
                host = c['db_host']
                port = c['db_port']
                user=c['db_user']
                password=c['db_password']
                db=c['db_name']
                self.record_last_run=bool(c['record_last_run'])
                if self.record_last_run:
                    self.tracking_column=c['tracking_column']
                    self.last_run_metadata_path=c['last_run_metadata_path']
                    self.tracking_column=c['tracking_column']
                sql = c['statement']
                output_name=c['output_name']
                self.trigger = c['trigger']
                self.cron = c['schedule']
                self.webhook_token = c['webhook_token']
                self.webhook_port = c['webhook_port'] 
                if provider == 'mysql':
                    self.data_provider = MysqlProvider(host=host,port=port,user=user,password=password,db=db,sql=sql,canSaveId=self.record_last_run,idFile=self.last_run_metadata_path,idName=self.tracking_column)
                o = outputs[output_name]
                o_hosts = o['hosts']
                self.index_name=o['index']
                self.document_id = ""
                try:
                   o_user = o['username']
                   o_pwd=o['password']
                   self.document_id = o['document_id']
                   self.es= EsHelper(o_hosts,o_user,o_pwd)
                except:
                    self.es= EsHelper(o_hosts)
        except Exception as e:
            print(e)
            sys.exit()

    def transmit_data(self):
        try:
            logger.info('start data transmission.')
            start_id = self.data_provider.lastId
            for url in self.start_urls:
                WebhookClient.sendStart(url,start_id)
            while(True):            
                datas,sql = self.data_provider.getData()  
                if len(datas) > 0:          
                    self.es.saveData(self.index_name,datas,self.document_id)
                    self.data_provider.saveId()
                    logger.info(sql)
                else:
                    logger.info('data transmission finished.')
                    for url in self.finished_urls:
                        WebhookClient.sendFinished(url,start_id,self.data_provider.lastId)
                    return
        except Exception as e:
            for url in self.error_urls:
                WebhookClient.sendFinished(url, e, self.data_provider.lastId)
        
    
    def run(self):
        if self.trigger == 'schedule':
            self.schedule = SdxScheduler()
            self.schedule.add_job(self.cron,self.transmit_data)
            logger.info('waite the schedule.')
            while True:
                self.schedule.run()
                time.sleep(1)
            pass
        elif self.trigger == 'webhook':
            
            server = WebhookServer(self.transmit_data,self.webhook_token,int(self.webhook_port))
            server.run()
            pass
        else:
            print('Error value for configuration item trigger.')
            sys.exit()

def initLogger(isDaemon,logPath=''):
    formatter = logging.Formatter('[%(asctime)s %(levelname)s %(lineno)d:%(filename)s(%(process)d)] - %(message)s')     
    if isDaemon:
        log_file = os.path.join(logPath,'data2es.log')
        print(log_file)
        handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=20*1024*1024, backupCount=10)
    else:
        handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)    
    

def term_sig_handler(signum, frame):  
    print('\n catched singal: %d' % signum  )
    sys.exit()


def runData2es(configfileName,callBack):
    if os.path.exists(configfileName):
        log_path = os.path.abspath(os.path.dirname(configfileName))
        
        initLogger(isDaemon = True,logPath = log_path)
        d2e = Data2es(configfileName)             
        d2e.run()
    else:
        logger.error('The configfile " %s " is not exists.'%(configfileName))


def run(isDaemon = False):
    signal.signal(signal.SIGTERM, term_sig_handler)  
    signal.signal(signal.SIGINT, term_sig_handler) 
    configfileName=""
    parser = argparse.ArgumentParser(prog='%s' % __serverName__, usage='%s [-c]' % __serverName__)
    parser.add_argument("-c", "--config", help="Specify configuration file path.", metavar='CONFIGFILE_PATH',
                        required=True)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0')    
    args = parser.parse_args()
    initLogger(False)
    runData2es(args.config)
    

if __name__ == "__main__":
    
    run()
    