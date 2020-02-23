#!/usr/bin/python
#coding=utf-8
import json,random,sqlite3,logging,os
from simplified_scrapy.core.utils import printInfo,getTime,md5
from simplified_scrapy.core.requesttm_base import RequestTmBase
import threading, time,sys
from queue import Queue

class SqliteRequestTm(RequestTmBase):
  _dbPath = 'db/statistics_{}.db'
  _tbName = 'request_tm'
  _name = None
  def __init__(self,name,setting={}):
    if(not os.path.exists('db/')):
      os.mkdir('db/')
    self._name = name
    self._dbPath = self._dbPath.format(name)
    conn = None
    try:
      conn = sqlite3.connect(self._dbPath)
      c = conn.cursor()
      c.execute('''CREATE TABLE IF NOT EXISTS {}
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            method VARCHAR(10) NOT NULL,
            url TEXT NOT NULL,
            tmSpan REAL NOT NULL,
            concurrency INT NOT NULL DEFAULT 0,
            countPer10s INT NOT NULL DEFAULT 0,
            state INT NOT NULL DEFAULT 0,
            size INT NOT NULL DEFAULT 0,
            tm CHAR(20));'''.format(self._tbName))
      conn.commit()
    except Exception as err:
      printInfo('error',err)
    if (conn): conn.close()
  
  _threadRequestTm=None
  _requestTmq = Queue(maxsize=0)
  def addRecode(self, ssp, url, tmSpan, state, concurrency,countPer10s,size):
    if ssp.request_tm==False: return
    method = url.get('method') if url.get('method') else url.get('requestMethod')
    if not method: method = 'GET'
    else: method = method.upper()
    if method=='POST':
      url['url'] = url.get('url').split('#')[0]
    self._requestTmq.put((ssp.name,method,url.get('url'),tmSpan,concurrency,countPer10s,state,size,getTime(url.get('_startTm'))))

  def startRecode(self):
    self._runflag = True
    if not self._threadRequestTm:
      self._threadRequestTm = threading.Thread(target=self._dealRequestTmThread)
      self._threadRequestTm.start()
  def endRecode(self):
    self._runflag=False

  def clearRecode(self):
    conn = sqlite3.connect(self._dbPath)
    try:
      cursor = conn.cursor()
      cursor.execute("delete from request_tm")
      conn.commit()
    except Exception as err:
      printInfo('error',err)
    conn.close()
  def _dealRequestTmThread(self):
    while(self._runflag):
      try:
        datas = []
        i=0
        while(True):
          i+=1
          if self._requestTmq.empty():
            break
          data = self._requestTmq.get_nowait()
          datas.append(data)
          if i>1000: break
        if datas: self._insertRT(datas)
      except Exception as err:
        printInfo('error', err)
      time.sleep(1)
  def _insertRT(self,datas):
    conn = sqlite3.connect(self._dbPath)
    try:
      cursor = conn.cursor()
      cursor.executemany("insert into request_tm(name,method,url,tmSpan,concurrency,countPer10s,state,size,tm) values(?,?,?,?,?,?,?,?,?)",tuple(datas))
      conn.commit()
    except Exception as err:
      printInfo('error',err)
    conn.close()
  def __del__(self):
    self._runflag=False
  def getstatistics(self):
    sql = '''
    select method,url,state,sum(tmSpan)/count(id) as avg_tm,max(tmSpan) as max_tm,min(tmSpan) as min_tm,
    count(id) as count from request_tm where name='{}' group by method,url,state
    '''.format(self._name)
    conn = sqlite3.connect(self._dbPath)
    rows=[]
    header=[]
    try:
      cursor = conn.cursor().execute(sql)
      for i in cursor.description:
        header.append(i[0])
      for row in cursor:
        rows.append(row)
    except Exception as err:
      printInfo('error', err)
    conn.close()
    return (rows,header)
  