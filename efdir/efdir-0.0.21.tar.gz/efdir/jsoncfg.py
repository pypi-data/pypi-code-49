
#FILE_LEAF_SIGN = "$"
#DIR_LEAF_SIGN  = {}
#LINE_SP = '\n'  
#DIR_PATH_SP = '/'   
# 整个机构是一个嵌套的字典
# {} 表示空 directory
# "$" 表示FILE 

from xdict.hdict_object import obj_to_hdict as d2h
import elist.elist as elel
from efdir import fs

def get_dirs(cfgdict):
    rslt  = d2h(cfgdict)
    prdict = rslt['prdict']
    dirs = list(prdict['h:o'].values())
    dirs.remove([])
    dirs = elel.mapv(dirs,fs.pl2path)
    return(dirs)
