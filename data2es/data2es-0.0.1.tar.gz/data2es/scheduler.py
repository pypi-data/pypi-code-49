#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#############################################
# File Name: scheduler.py
# Author: stosc
# Mail: stosc@sidaxin.com
# Created Time:  2020-2-8 19:17:34
#############################################
import croniter
import datetime
import time


class SdxScheduler(object):
    def __init__(self):
        super().__init__()
        self.last_run = None

    def add_job(self,cron,func,*args):
        self.cron = cron
        self.job = func
        self.args = args
        self.base = datetime.datetime.now()#+datetime.timedelta(minutes=-1)

    @property
    def next_run(self):
        
        cron = croniter.croniter(self.cron, self.base)    
        return cron.get_next(datetime.datetime)


    @property
    def should_run(self):
        """
        :return: ``True`` if the job should be run now.
        """
        
        return datetime.datetime.now() >= self.next_run and self.next_run != self.last_run

    def run(self):
        if self.should_run:
            self.job(*self.args)
            self.last_run = self.next_run
            self.base = datetime.datetime.now()


if __name__ == "__main__":
    print(datetime.datetime.now()+datetime.timedelta(minutes=-1))
    
    s = SdxScheduler()
    def job():
        print('run')
    s.add_job('* * * * *',job)
    while True:
        s.run()
        time.sleep(1)

    