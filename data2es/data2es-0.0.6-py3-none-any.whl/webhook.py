import requests
import json
import datetime
import tornado.web
import tornado.ioloop
from tornado import gen
import asyncio
import threading


hook_token = 'amituofo@xfjl'
call=None
thread_main = None

def _sendStart(url,content):
    headers={'Content-Type': 'application/json'}
    f=requests.post(url,data=json.dumps(content),headers=headers)

#定义处理类型
class IndexHandler(tornado.web.RequestHandler):
    #添加一个处理get请求方式的方法
    
    @gen.coroutine
    def get(self,path):
        global thread_main
        global call,hook_token,thread_main
        #向响应中，添加数据        
        token = self.get_argument('token')               
        if token == hook_token and call != None and hasattr(call, '__call__'): 
            if thread_main != None :
                if thread_main.is_alive() :
                    self.write('is running on :%s'%thread_main.get_ident()) 
                else:
                    thread_main.start()
                    self.write('is started on :%s'%thread_main.get_ident())             
        self.finish()


class WebhookServer(object): #threading.Thread
    def __init__(self,callhandler,token=None,port=9899):
        super().__init__()
        global call,hook_token,thread_main              
        self.port = port if port > 0 else 9899
        call = callhandler 
        thread_main = threading.Thread(target=call)       
        if token != None and token != "":
            hook_token = token
        
    def run(self):
        # tornado 5 中引入asyncio.set_event_loop即可
        asyncio.set_event_loop(asyncio.new_event_loop())
        #创建一个应用对象
        app = tornado.web.Application(handlers=[(r"/hook(.*)", IndexHandler)])
        #绑定一个监听端口
        app.listen(self.port)
        print('webhook server is running on port %s,the access token is %s.'%(self.port,hook_token))
        #启动web程序，开始监听端口的连接
        tornado.ioloop.IOLoop.current().start()

class WebhookClient(object):

    @staticmethod
    def sendFinished(url,start,end):
        program={
            "msgtype": "text",
            "text": {"content": "[%s] 完成数据从 [ %s ] 到 [ %s ] 的同步。" %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),start,end)},
        }
        _sendStart(url,program)

    @staticmethod
    def sendStart(url,start):
        program={
            "msgtype": "text",
            "text": {"content": "[%s] 从第 [ %s ] 开始同步数据。" %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),start)},
        }
        _sendStart(url,program)

    @staticmethod
    def sendError(url,errMas,id):
        program={
            "msgtype": "text",
            "text": {"content": "[%s] 同步到 [%s] 发生 [错误] %s。" %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),id,errMas)},
        }
        _sendStart(url,program)


   
    


    


if __name__ == "__main__":
    
    url = 'https://oapi.dingtalk.com/robot/send?access_token=413657725cd9b92c4e06f17696df0afacff6feb450d007f1328810def0ee968a'
    url1 = 'https://oapi.dingtalk.com/robot/send?access_token=0ead35e2f76ecfff379979a7e751c2edee127bfef4c7ac663c8c867c027ea94a'
    WebhookClient.sendFinished(url,0,100)
    WebhookClient.sendStart(url1,100)