
from wpkit.piu import BackupDB
from flask import Flask,jsonify
from wpkit.web.utils import parse_json,parse_json_and_form
from wpkit.basic import PointDict,Status,StatusSuccess,StatusError
from wpkit.web.base import MyBlueprint,Application
class DBServer(MyBlueprint):
    def __init__(self,import_name,dbpath="./",url_prefix='/db',*args,**kwargs):
        super().__init__(import_name=import_name,url_prefix=url_prefix,enable_CORS=True,*args,**kwargs)
        self.db=BackupDB(path=dbpath)
        self.add_handlers()
    def add_handlers(self):
        @self.route('/cmd',methods=['POST'])
        @parse_json_and_form
        def do_cmd(cmd):
            print("cmd:",cmd)
            try:
                res=self.db.execute(cmd)
                res=StatusSuccess(data=res)
            except:
                res=StatusError()
            return jsonify(res)






