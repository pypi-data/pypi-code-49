from wpkit.piu import FileDict,PointDict
from wpkit.basic import DirPath,T
import os,glob,shutil
class ConfigFileDict(FileDict):
    def __init__(self,path):
        super().__init__(path)
        if not len(self):
            self.children=[]
            self.length=0
            self.path=DirPath(self.geta('path'))
            self.dir=self.path.dirname()
    def add_child(self,name,type):
        child={
            'name':name,
            'type':type
        }
        self.children.append(child)
        self.length+=1
    def load_children(self):
        children={}
        for item in self.children:
            p = self.dir +'/'+ item['name']
            if item['type']==T.DIR:
                ch=DirDict(p)
            else:
                ch=FileDict(p)
            children[item['name']]=ch
        return children


class DirDict(dict):
    def __init__(self,path):
        super().__init__()
        self.path=DirPath(path).abspath().todir()
        self.config_path=self.path/'.dirdict.config'
        self.configfile=ConfigFileDict(self.config_path)
        self.load()
    def load(self):
        dic=self.configfile.load_children()
        self.update(dic)
    def createFiledict(self,name):
        path=self.path/name
        dic=FileDict(path)
        self.configfile.add_child(name,T.FILE)
        self[name]=dic
        return dic
    def createDirdict(self,name):
        path = self.path / name
        dic = DirDict(path)
        self.configfile.add_child(name, T.DIR)
        self[name] = dic
        return dic

def demo():
    dic=DirDict('dict')
    a=dic.createFiledict('a')
    a['name']='wangpei'
    dic.createDirdict('b')
    b=dic['b']

    print(b)


if __name__ == '__main__':
    demo()
