#!/usr/bin/python
#coding=utf-8
import logging
import simplified_scrapy.core.logex
import threading,traceback,time,importlib,imp,os,json,io
from imp import reload
from simplified_scrapy.dictex import Dict
from concurrent.futures import ThreadPoolExecutor
from simplified_scrapy.core.utils import printInfo,getFileModifyTime,isExistsFile,getTimeNow,appendFile
from simplified_scrapy.downloader import execDownload
from simplified_scrapy.extracter import Extracter
from queue import Queue
import sys
if sys.version_info.major == 2:
  reload(sys)
  sys.setdefaultencoding('utf-8')
try:
  from setting import SETTINGFILE
except ImportError:
  SETTINGFILE = 'setting.json'
try:
  from extension_method import dealRequestTm
except ImportError:
  dealRequestTm = None
class _SimplifiedMain():
  def __init__(self):
    try:
      self.downloadCount=0
      self._runflag = True
      self._settingObj = Dict()
      self.singleSSP = None
      self._extracter = None
      self._pool = None
      self._requestTmq = {} #Queue(maxsize=0)
    except Exception as err:
      self.log(err,logging.ERROR)
  
  def _init(self,ssp=None):
    try:
      self.singleSSP = ssp
      self.refrashSSP()
      self._extracter = Extracter()
      self._pool = ThreadPoolExecutor(max_workers=self._settingObj["max_workers"])
    except Exception as err:
      self.log(err,logging.ERROR)

  def refrashSSP(self):
    try:
      if(os.path.exists(SETTINGFILE)):
        settingJson = io.open(SETTINGFILE, "r",encoding="utf-8").read()
        settingObj = json.loads(settingJson)
        dicTmp = []
        if(not self.singleSSP and settingObj.get('spiders')):
          for spider in settingObj['spiders']:
            try:
              if not spider.get('stop'):
                dicTmp.append(spider['file'])
                self.getSpider(spider['file'],spider["class"],settingObj.get('request_tm'))
            except Exception as err:
              self.log(err,logging.ERROR)

          keys = self._spiderDic.keys()
          for key in keys:
            if(key not in dicTmp):
              del self._spiderDic[key]
              if self._requestTmq.get(key):
                del self._requestTmq[key]
      else:
        settingObj = Dict()
      if(self.singleSSP): 
        if not self.singleSSP.logged_in: 
          self.singleSSP.logged_in = self.singleSSP.login()
        self._spiderDic[self.singleSSP.name] = self.singleSSP
        if settingObj.get("request_tm") or self.singleSSP.request_tm:
          if not self._requestTmq.get(self.singleSSP.name):
            self._requestTmq[self.singleSSP.name] = Queue(maxsize=0)
        elif self._requestTmq.get(self.singleSSP.name):
          del self._requestTmq[self.singleSSP.name]

      if(not settingObj.get("concurrency")):
        settingObj["concurrency"] = 5
      if(not settingObj.get("concurrencyPer1S")):
        settingObj["concurrencyPer1S"] = 10
      if(not settingObj.get("intervalTime")):
        settingObj["intervalTime"] = 0.3
      if(not settingObj.get("max_workers")):
        settingObj["max_workers"] = 10
      if(not settingObj.get("refresh_tm")):
        settingObj["refresh_tm"] = 60
      if(not settingObj.get("disable_extract")):
        settingObj["disable_extract"] = False
      if(not settingObj.get("request_tm")):
        settingObj["request_tm"] = False
      if(not settingObj.get("request_tm_file")):
        settingObj["request_tm_file"] = "request_tm{}.txt"
      
      self._settingObj = settingObj
    except Exception as err:
      self.log(err,logging.ERROR)
    
  def log(self, msg, level=logging.DEBUG):
    if (isinstance(msg,UnicodeEncodeError)):
      printInfo('UnicodeEncodeError', msg)
      return
    printInfo(msg)
    if(level==logging.ERROR):
      logger = logging.getLogger()
      logging.LoggerAdapter(logger, None).log(level, msg)

  def setRunFlag(self, flag):
    self._runflag = flag

  _started=False
  _spiderDic = Dict()
  def startThread(self,ssp=None):
    if(self._started): return
    self._started = True

    self._init(ssp)
    if(not self._settingObj["disable_extract"]):
      threadExtract = threading.Thread(target=self.extractThread)
      threadExtract.start()
    else:
      self.log('extract disabled......')
    if not dealRequestTm: # and self.__class__.__name__ != '_SimplifiedMain':
      threadRequestTm = threading.Thread(target=self._dealRequestTmThread)
      threadRequestTm.start()
    startTime = time.time()
    self.log('simplified-scrapy is running......')
    lastUrl=None
    while self._runflag:
      if((time.time()-startTime) > self._settingObj["refresh_tm"]):
        startTime = time.time()
        self.refrashSSP()
      try:
        if(os.path.exists('stop.txt')):
          self._runflag = False
          os.rename('stop.txt','stoped.txt')
          break
        for ssp in self._spiderDic.values():
          if(not ssp or ssp.stop): continue
          urlCount = ssp.urlCount()
          if(urlCount and self.checkConcurrency(ssp.name,urlCount)):
            url = ssp.popUrl()
            if(url):
              lastUrl = url
              link = url.get('url')
              if(not link):
                link = url.get('href')
              if(not link):
                link = url.get('src')
              if(not link): raise Exception('no url parameter')
              url['url']=link

              self.downloadCount+=1
              if(isinstance(url,dict) and (url.get("requestMethod")=="render" or url.get('method')=='render')):
                url['_startTm'] = time.time()
                self.downloadRender(url,ssp)
              else:
                self._pool.submit(self.downloadThread2,url,ssp)
            else:
              self._concurrency-=1
          if(urlCount==0):
            plan = ssp.plan()
            ssp.resetUrls(plan)
            if lastUrl:
              lastUrl = None
              print ('waiting for new urls...')
      except Exception as err:
        self.log(err,logging.ERROR)
        time.sleep(10)
      time.sleep(self._settingObj["intervalTime"])
    self._runflag=False
    self._pool.shutdown()
    self.log('simplified-scrapy stopped......')

  _concurrency=0
  _downloadPageNum=0
  _startCountTs=time.time()
  def checkConcurrency(self,name,count):
    tmSpan = time.time()-self._startCountTs
    showFlag = False
    if(tmSpan>5):
      showFlag = True
      if(self._downloadPageNum>(self._settingObj["concurrencyPer1S"]*tmSpan)):
        self.log('name={}, count={}, concurrency={}, downloadPageNum={}, tmSpan={}, reason={}'.format(name,count,self._concurrency,self._downloadPageNum,tmSpan,'exceed the config number CONCURRENCYPER1S'))
        return False
      self._startCountTs=time.time()
      self._downloadPageNum=0
    if self._concurrency >= self._settingObj["concurrency"]:
      if showFlag:
        self.log('name={}, count={}, concurrency={}, downloadPageNum={}, tmSpan={}, reason={}'.format(name,count,self._concurrency,self._downloadPageNum,tmSpan,'exceed the config number CONCURRENCY'))
      return False
    self._concurrency+=1
    if showFlag:
      self.log('name={}, count={}, concurrency={}, downloadPageNum={}, tmSpan={}'.format(name,count,self._concurrency,self._downloadPageNum,tmSpan))
    return True
  def _getTm(self, fileName):
    name = fileName.replace('.','/')+'.py'
    if isExistsFile(name):
      tm = getFileModifyTime(name)
      return tm
    return False
  def getSpider(self, fileName, className, requestTm):
    try:
      logged_in = False
      if(fileName in self._spiderDic):
        oldSsp = self._spiderDic[fileName]
        logged_in = oldSsp.logged_in
        tm = self._getTm(fileName)
        if(not tm or oldSsp.tm == tm):
          return self._spiderDic[fileName]

        m = importlib.import_module(fileName)
        reload(m)
        cls = getattr(m, className)
        ssp = cls()
        ssp.logged_in = logged_in
        ssp.tm = tm
      else:
        m = importlib.import_module(fileName)
        cls = getattr(m, className)
        ssp = cls()
        ssp.tm = self._getTm(fileName)
      if not ssp.logged_in:
        ssp.logged_in = ssp.login()
      self._spiderDic[fileName]=ssp
      if (requestTm or ssp.request_tm):
        if not self._requestTmq.get(ssp.name):
          self._requestTmq[ssp.name] = Queue(maxsize=0)
      elif self._requestTmq.get(ssp.name):
        del self._requestTmq[ssp.name]
      return ssp
    except Exception as err:
      self.log(err,logging.ERROR)

  def extractThread(self):
    while(self._runflag):
      flag=False
      for ssp in self._spiderDic.values():
        try:
          data = ssp.popHtml()
          if(not data):
            data = ssp.popHtml(2)

          if(data):
            flag = True
            obj = self._extracter.extract(data["url"],data["html"],ssp)
            if obj==True:
              ssp.updateHtmlState(data["id"],1)
            elif obj: 
              ssp.saveData(obj)
              ssp.updateHtmlState(data["id"],1)
            else:
              ssp.updateHtmlState(data["id"],2)
            if(ssp.models and len(ssp.models)>0):
              time.sleep(0.5)
            else:
              time.sleep(0.01)
        except Exception as err:
          self.log(err,logging.ERROR)
          time.sleep(10)
      if(not flag):
        time.sleep(3)
      time.sleep(1)
      
  def down_callback(self,html,url,ssp):
    self._concurrency-=1
    if(not isinstance(url,dict)):
      url={'url':url}
    try:
      url['_endTm'] = time.time()
      if url.get('_startTm'):
        tmSpan = url['_endTm']-url['_startTm']
      state = 1
      if(html=="_error_"):
        state = 0
        ssp.downloadError(url)
      elif html:
        ssp.saveHtml(url,html)
      if url.get('_startTm'):
        if dealRequestTm:
          dealRequestTm(ssp,url,tmSpan,state)
        else:
          self._dealRequestTm(ssp,url,tmSpan,state)
    except Exception as err:
      self.log(err)
  def downloadRender(self,url,ssp):
    printInfo(url['url'])
    self._downloadPageNum+=1
    ssp.renderUrl(url,self.down_callback)
  def _dealRequestTm(self, ssp, url, tmSpan, state):
    q = self._requestTmq.get(ssp.name)
    if not q: return
    method = url.get('method') if url.get('method') else url.get('requestMethod')
    if not method: method = 'GET'
    q.put("{},{},{},{},{},{}".format(method.upper(),url.get('url'),tmSpan,state,self._concurrency,getTimeNow()))

  def _dealRequestTmThread(self):
    while(self._runflag):
      try:
        for kv in self._requestTmq:
          name = "data/{}_request_tm_{}".format(kv,int(time.time()/86400))
          q = self._requestTmq[kv]
          while(True):
            data = q.get()
            if not data: break
            appendFile(name,data)

      except Exception as err:
        self.log(err,logging.ERROR)
      time.sleep(1)
  def downloadThread2(self,*args):
    url=args[0]
    ssp=args[1]
    try:
      self._concurrency-=1
      if(not isinstance(url,dict)):
        url={'url':url}
      printInfo(url['url'])
      self._downloadPageNum+=1
      startTm=time.time()
      html = execDownload(url,ssp)
      url['_endTm'] = time.time()
      tmSpan = url['_endTm']-startTm
      state = 1
      if(html=="_error_"):
        state = 0
        ssp.downloadError(url)
      else:
        ssp.saveHtml(url,html)
      if dealRequestTm:
        dealRequestTm(ssp,url,tmSpan,state)
      else:
        self._dealRequestTm(ssp,url,tmSpan,state)
    except Exception as err:
      self.log(err,logging.ERROR)

SimplifiedMain = _SimplifiedMain()