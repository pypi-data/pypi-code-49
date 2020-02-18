from efdir import fs
from efdir import rstcfg
from efdir import jsoncfg
import os
#dlmktree  mktree-from-dirs
#fmktree   mktree-from-filecfg

def _cfgfile2pl(cfgfile):
    suffix = os.path.splitext(cfgfile)[1]
    if(suffix == ".rst"):
        rst_str = fs.rfile(cfgfile)
        dirs = rstcfg.get_dirs(rst_str)
    elif(suffix == ".json"):
        d = fs.rjson(cfgfile)
        dirs = jsoncfg.get_dirs(d)
    else:
        print("error,must be .rst or .json")
    return(dirs)


def _cfg2pl(cfg):
    if(isinstance(cfg,str)):
        dirs = rstcfg.get_dirs(cfg)
    elif(isinstance(cfg,dict)):
        dirs = jsoncfg.get_dirs(cfg)
    else:
        print("error,must be .rst or .json")
    return(dirs)


def _creat_dir(dir,parent_dir,**kwargs):
    if(os.path.exists(parent_dir)):
        if(os.path.isdir(parent_dir)):
            pass
        else:
            print(parent_dir+"exists,but is not a dir!!!")
    else:
        fs.mkdirs(parent_dir,**kwargs)
    dirname = os.path.dirname(dir)
    basename = os.path.basename(dir)
    tail = basename[-1]
    if(tail == "$"):
        full = os.path.join(parent_dir,dirname,basename[:-1])
        fs.mkdirs(os.path.join(parent_dir,dirname),**kwargs)
        fs.touch(full)
    else:
        fs.mkdirs(os.path.join(parent_dir,dir),**kwargs)

def _dlmktree(dirs,parent_dir="./",**kwargs):
    for i in range(dirs.__len__()):
        _creat_dir(dirs[i],parent_dir,**kwargs)

def mktree(cfg,parent_dir="./",**kwargs):
    dirs = _cfg2pl(cfg)
    _dlmktree(dirs,parent_dir,**kwargs)


def fmktree(cfgfile,parent_dir="./",**kwargs):
    dirs = _cfgfile2pl(cfgfile)
    _dlmktree(dirs,parent_dir,**kwargs)


