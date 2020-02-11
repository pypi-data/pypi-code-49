import os,shutil,glob,json,functools
from wpkit.basic import PowerDirPath,standard_path,get_relative_path

def _copy_dir(src,dst):
    assert os.path.exists(src)
    assert os.path.exists(dst)
    for name in os.listdir(src):
        path=os.path.join(src,name)
        new_path=os.path.join(dst,name)
        if os.path.isdir(path):
            os.mkdir(new_path)
            _copy_dir(path,new_path)
        elif os.path.isfile(path):
            shutil.copy(path,new_path)
def copy_dir(src,dst):
    assert os.path.exists(src)
    src=os.path.abspath(src)
    name=os.path.basename(src)
    if os.path.exists(dst):
        assert os.path.isdir(dst)
        newdir=os.path.join(dst,name)
        os.mkdir(newdir)
        _copy_dir(src,newdir)
    else:
        parent_dir=os.path.dirname(dst)
        assert os.path.exists(parent_dir)
        _copy_dir(src,dst)


class DirDict(object):
    def __init__(self,name=None,realpath=None,*args,**kwargs):
        if realpath and os.path.exists(realpath):
            realpath=os.path.abspath(realpath)
        self.realpath = realpath
        if realpath:
            name=name or os.path.basename(realpath)
        self.name=name
        self.hooked=realpath is not None
    def loadjson(self,fn,encoding='utf-8'):
        path = self.join(fn)
        with open(path,'r',encoding=encoding) as f:
            return json.load(f)
    def dumpjson(self,fn,obj,encoding='utf-8'):
        path=self.join(fn)
        with open(path,'w',encoding=encoding) as f:
            json.dump(obj,f)
    def savetxt(self,fn,string,encoding='utf-8'):
        path=self.join(fn)
        with open(path,'w',encoding=encoding) as f:
            f.write(string)
    def appendTo(self,path):
        if not isinstance(path,DirDict):
            path=DirDict(realpath=path)
        path.append(self)
    def append(self,path):
        if not isinstance(path,DirDict):
            path=DirDict(path)
        if not path.exists():
            self.makedirs(path.name)
        else:
            self.copy(path)
    def copy(self,path):
        assert self.exists()
        if not isinstance(path,DirDict):
            path=DirDict(realpath=path)
        assert path.exists()
        new_path=self.join(path.name)
        assert not os.path.exists(new_path)

        if os.path.isdir(path.realpath):
            copy_dir(path.realpath,new_path)
        else:
            shutil.copy(path.realpath,new_path)
    def makedirs(self,path):
        assert self.hooked
        assert self.exists()
        path = self.join(path)
        os.makedirs(path)
    def mkdir(self,name):
        assert self.hooked
        assert self.exists()
        assert self.secure(name)
        path=self.join(name)
        os.mkdir(path)

    def join(self,path):
        return self.realpath+'/'+path
    def listdir(self):
        return os.listdir(self.realpath)
    def exists(self):
        if not self.realpath:return False
        return os.path.exists(self.realpath)
    def isdir(self):
        return os.path.isdir(self.realpath)
    def isfile(self):
        return os.path.isfile(self.realpath)
    def ismount(self):
        return os.path.ismount(self.realpath)
    def islink(self):
        return os.path.islink(self.realpath)
    def getsize(self):
        return os.path.getsize(self.realpath)
    def getatime(self):
        return os.path.getatime(self.realpath)
    def getmtime(self):
        return os.path.getmtime(self.realpath)
    def getctime(self):
        return os.path.getctime(self.realpath)
    def secure(self,name):
        escapes=['/','\\']
        for ch in escapes:
            if ch in name:
                return False
        return True
    @classmethod
    def from_realpath(cls,path):
        realpath=os.path.abspath(path)
        name=os.path.basename(path)
        return cls(name=name,realpath=realpath)

class FakeOS:
    def __init__(self,path=None):
        if  path and os.path.exists(path):
            path=os.path.abspath(path)
        self.path=standard_path(path) if path else path
    def _relpath(self,root,path):
        return get_relative_path(root,path)
    def _standard_path(self,*args,**kwargs):
        return standard_path(*args,**kwargs)
    def _fakepath(self,path):
        return get_relative_path(self.path,path)
    def _truepath(self,path):
        if not self.path:
            return standard_path(path)
        return self.path+'/'+standard_path(path)
    def glob(self,pathname,recursive=False):
        pathname=self._truepath(pathname)
        fs=glob.glob(pathname=pathname,recursive=recursive)
        fs=[self._fakepath(path) for path in fs]
        return fs

    def tranverse_info(self,path,depth=-1,format=True):
        return self.info(path,depth,format)
    def info(self, path,depth=2,format=True):
        path = self._truepath(path)
        return PowerDirPath(path).tranverse_info(depth=depth,format=format)
    def open(self, file, mode='r'):
        file = self._truepath(file)
        return open(file, mode)

    def read(self, fp, mode='r', encoding='utf-8'):
        with open(fp, mode=mode, encoding=encoding) as f:
            return f.read()

    def write(self, fp, s, mode='w', encoding='utf-8'):
        with open(fp, mode=mode, encoding=encoding) as f:
            f.write(s)
    def newfile(self,path,mode='w',encoding='utf-8'):
        path = self._truepath(path)
        open(path,mode=mode,encoding=encoding).close()
    def writefile(self,path,s,mode='w',encoding='utf-8'):
        path = self._truepath(path)
        open(path,mode=mode,encoding=encoding).write(s)
    def exists(self,path):
        path = self._truepath(path)
        return os.path.exists(path)
    def isdir(self,path):
        path = self._truepath(path)
        return os.path.isdir(path)
    def isfile(self,path):
        path = self._truepath(path)
        return os.path.isfile(path)
    def islink(self,path):
        path = self._truepath(path)
        return os.path.islink(path)
    def ismount(self,path):
        path = self._truepath(path)
        return os.path.ismount(path)
    def dirname(self,path):
        return os.path.dirname(path)
    def basename(self,path):
        return os.path.basename(path)
    def listdir(self,path):
        path=self._truepath(path)
        return os.listdir(path)
    def remove(self,path):
        path=self._truepath(path)
        return os.remove(path)
    def rmtree(self,path):
        path = self._truepath(path)
        return shutil.rmtree(path)
    def mkdir(self,path):
        path = self._truepath(path)
        return os.mkdir(path)
    def makedirs(self,path):
        path = self._truepath(path)
        return os.makedirs(path)
    def copy(self,src,dst):
        src = self._truepath(src)
        dst = self._truepath(dst)
        return shutil.copy(src,dst)
    def copydir(self,src,dst):
        src = self._truepath(src)
        dst = self._truepath(dst)
        return copy_dir(src,dst)
    def rename(self,src,dst):
        src = self._truepath(src)
        dst = self._truepath(dst)
        return os.rename(src,dst)
    def move(self,src,dst):
        src = self._truepath(src)
        dst = self._truepath(dst)
        return shutil.move(src,dst)


