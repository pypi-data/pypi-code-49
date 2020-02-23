#!/usr/bin/python
#coding=utf-8

from simplified_scrapy.core.utils import printInfo,getTime,appendFile,removeFile
from simplified_scrapy.core.requesttm_base import RequestTmBase
import threading, time
from queue import Queue

class TxtRequestTm(RequestTmBase):
  def __init__(self,name=None,setting={}):
    self.fileName = name
    
  _threadRequestTm=None
  _requestTmq = {}
  
  _lock = threading.Lock()
  def addRecode(self, ssp, url, tmSpan, state, concurrency,countPer10s,size):
    if ssp.request_tm==False: return
    q = self._requestTmq.get(ssp.name)
    if not q: 
      self._lock.acquire()
      q = self._requestTmq.get(ssp.name)
      if not q:
        self._requestTmq[ssp.name]=Queue(maxsize=0)
      return
    method = url.get('method') if url.get('method') else url.get('requestMethod')
    if not method: method = 'GET'
    else: method = method.upper()
    if method=='POST':
      url['url'] = url.get('url').split('#')[0]
    q.put("{},{},{},{},{},{},{},{}".format(method,url.get('url'),tmSpan,state,concurrency,countPer10s,size,getTime(url.get('_startTm'))))

  def startRecode(self):
    self._runflag = True
    if not self._threadRequestTm:
      self._threadRequestTm = threading.Thread(target=self._dealRequestTmThread)
      self._threadRequestTm.start()
  def endRecode(self):
    self._runflag=False
  def clearRecode(self,name):
    removeFile(name)

  def _dealRequestTmThread(self):
    while(self._runflag):
      try:
        for kv in self._requestTmq:
          if self.fileName: 
            name = self.fileName
          else:
            name = "data/{}_request_tm_{}.csv".format(kv,int(time.time()/86400))
          q = self._requestTmq[kv]
          while(True):
            if q.empty(): break
            data = q.get_nowait()
            if not data: break
            appendFile(name,data)

      except Exception as err:
        printInfo('error', err)
      time.sleep(1)

if __name__=='__main__':
  pass
  