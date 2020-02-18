from efdir.primitive import *
import os
from efdir.etree import *
from efdir.fs import mkdir,mkdirs,rmdir


class F(object):
    def __init__(self,*args):
        ele = os.getcwd() if(len(args) == 0) else args[0]
        if(isinstance(ele,str)):
            abspath = os.path.abspath(ele)
            ele = abspath2etree(abspath)
            self.__dict__['__parent'] = null
            mkdirs(abspath)
        else:
            self.__dict__['__parent'] = undefined
        self.__dict__['__#ele'] = ele
    def __repr__(self):
        ele = self.__dict__['__#ele']
        abspath = etree2abspath(ele)
        return(abspath)
    def __getattribute__(self,an):
        #*args 在这个函数里 无法 使用 会随结果一起返回
        if(an[0]=="_"):
            pass
        else:
            if(an in self.__dict__):
                pass
            else:
                ele = self.__dict__['__#ele']
                self.__dict__[an] = F(append_child(an,ele))
                child = self.__dict__[an]
                child.__dict__['__parent'] = self 
                chele = child.__dict__['__#ele']
                abspath = etree2abspath(chele)
                mkdirs(abspath)
        return(object.__getattribute__(self,an))
    def __setattr__(self,an,value):
        if(an[0]=="_"):
            object.__setattr__(self,an,value)
        else:
            if(an in self.__dict__):
                #rename
                child = self.__dict__[an]
                chele = child.__dict__['__#ele']
                old_abspath = etree2abspath(chele)
                chele.tag = value
                self.__dict__[value] = child
                del self.__dict__[an]
                new_abspath = etree2abspath(chele)
                os.rename(old_abspath,new_abspath)
            else:
                raise(TypeError('just xxx.yyy is ok,no need to explicitly set'))
    def __delattr__(self,an):
        if(an[0:2]=="__"):
            raise(TypeError('cant delete '+an))
        elif(an[0] == "_"):
            object.__delattr__(self,an)
        else:
            child = self.__dict__[an]
            chele = child.__dict__['__#ele']
            abspath = etree2abspath(chele)
            disconn(chele)
            object.__delattr__(self,an)
            rmdir(abspath,force=true)


