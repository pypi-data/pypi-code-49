from wpkit.basic import DirPath,PowerDirPath
from wpkit.fsutil import FakeOS,copy_dir,copy_file
import os,glob,shutil
class FSItem:
    def __repr__(self):
        return '<%s.%s object:%s>'%(self.__module__,self.__class__.__name__,self.path)

class File(FSItem):
    def __init__(self,path,makefile=False):
        self.path=path
        if makefile:
            if not os.path.exists(path):
                open(self.path,'w').close()

class TextFile(File):
    def __init__(self,path,default=''):
        super().__init__(path,makefile=True)
        if self.read()=='':
            self.write(default)
    def read(self):
        with open(self.path,'r',encoding='utf-8') as f:
            return f.read()
    def write(self,s):
        with open(self.path,'w',encoding='utf-8') as f:
            f.write(s)



class Folder(FakeOS,FSItem):
    def __init__(self,path,writable=False):
        self.writable=writable
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            assert os.path.isdir(path)
        path=os.path.abspath(path)
        self.path=path
        FakeOS.__init__(self,path)
    def clean(self):
        for ch in self.listdir():
            if self.isdir(ch):
                self.rmtree(ch)
            else:
                self.remove(ch)
    def eat(self,path,overwrite=False):
        assert os.path.exists(path)
        if os.path.isdir(path):
            copy_dir(path,self.path)
        else:
            copy_file(path,self.path,overwrite=overwrite)


    def parse_path(self,path):
        items=self._split_path(path)
        return items
    def child(self,name):
        assert not '/' in name
        assert not '\\' in name
        path=self.path+'/'+name
        assert os.path.exists(path)
        if os.path.isdir(path):
            return Folder(path)
        elif os.path.isfile(path):
            return File(path)
        else:
            raise Exception('% should be a file or dir'%(path))
    def route_item(self,items):
        if not items:
            return self
        name=items[0]
        items=items[1:]
        if name=='/':
            return self.route_item(items)
        else:
            if name in self.listdir():
                ch=self.child(name)
                if not len(items):
                    return ch
                else:
                    return ch.route_item(items)
            else:
                raise Exception('%s is not in %s'%(name,self.path))
    def __getitem__(self, item):
        items=self.parse_path(item)
        return self.route_item(items)
    def __setitem__(self, path, value):
        tp=self._truepath(path)
        if os.path.exists(tp):
            if self.writable:
                PowerDirPath(tp).rmself()
            else:
                raise Exception('%s already exists.'%(tp))
        if value is None:
            os.makedirs(tp)
            return
        if isinstance(value,str):
            assert os.path.exists(value)
            if os.path.isfile(value):
                value=File(value)
            else:
                assert os.path.isdir(value)
                value=Folder(value)
        if isinstance(value,Folder):
            value.moveto(tp)
        elif isinstance(value,File):
            shutil.copy(value.path,tp)









