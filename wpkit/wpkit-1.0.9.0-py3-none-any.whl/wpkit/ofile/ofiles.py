import os,shutil,glob,json
from .utils import json_dump,json_load,readtxt,writetxt

class ObjectFile:
    def __init__(self,path):
        self.path=path
        if not os.path.exists(path):
            open(path,'w').close()
    def __call__(self, obj=None):
        if obj is None:
            return self.read()
        return self.write(obj)
    def read(self):
        return json_load(self.path)
    def write(self,obj):
        return json_dump(obj, self.path)
class SimpleListFile(ObjectFile):
    def __init__(self,path,split_char='\n'):
        self.path=path
        self.split_char=split_char
        super().__init__(self.path)
    def write(self,obj):
        obj=self.split_char.join(obj)
        return writetxt(obj,self.path)
    def read(self):
        text=readtxt(self.path).strip()
        return text.split(self.split_char)

