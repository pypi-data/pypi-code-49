from wpkit.pan import LocalFSHandle,Pan
from flask import Blueprint,Flask,jsonify
from wpkit.web.utils import parse_json,parse_json_and_form,request
from wpkit.web.bps import BlueStatic
from wpkit.basic import Status,StatusError,StatusSuccess,PointDict
from flask_cors import CORS
import json
class LocalFSServer(LocalFSHandle,Flask):
    def __init__(self,import_name,path="./",url_prefix="/fs",debug=False,*args,**kwargs):
        LocalFSHandle.__init__(self,path)
        Flask.__init__(self,import_name=import_name,*args,**kwargs)
        self.url_prefix = url_prefix
        self.add_handlers()
        CORS(self,resources=r'/*')
    def run(self, host='127.0.0.1', port=80, debug=None, load_dotenv=True, **options):
        self.host=host
        self.port=port
        Flask.run(self,host=host,port=port,debug=debug,load_dotenv=load_dotenv,**options)
    def add_handlers(self):
        @self.route(self.url_prefix+'/cmd',methods=['POST'])
        @parse_json_and_form
        def do_cmd(cmd):
            print("cmd:", cmd)
            try:
                res = self.execute(cmd)
                res = StatusSuccess(data=res)
            except:
                res = StatusError()
                raise
            return jsonify(res)
        @self.route(self.url_prefix+'/upload',methods=['POST','GET'])
        @parse_json_and_form
        def do_upload(info):
            file=request.files['file']
            if isinstance(info,str):
                info=json.loads(info)
            info=PointDict.from_dict(info)
            path=self.local_path(info.location)
            path=self.local_path(path+'/'+info.filename)
            file.save(path)
            print('path:',path)
            print('file:',file)
            return StatusSuccess(msg="Uploading succeeded.")
        self.register_blueprint(BlueStatic(self.import_name,url_prefix=self.url_prefix+'/files',static_dir=self.lpath))
        def getUrl(location,name):
            return 'http://%s:%s'%(self.host,self.port)+ self.url_prefix+'/files/'+self.local_path(location+'/'+name)
        self.add_cmd('getUrl',getUrl)








