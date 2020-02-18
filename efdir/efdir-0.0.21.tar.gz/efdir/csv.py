import pandas as pd
from efdir import fs
import json
import ltdict.ltdict as ltlt
import edict.edict as eded
import elist.elist as elel
import dlist.dlist as dldl
import efuntool.efuntool as efun




def csv_wcols(src_fn,from_file=True):
    df = pd.read_csv(src_fn)
    js = df.to_json()
    dst_fn = fs.repl_suffix(src_fn,"col.json")
    fs.wfile(dst_fn,js)


def csv2cols(src_fn,from_file=True):
    df = pd.read_csv(src_fn)
    columns = df.columns
    js = df.to_json()
    d = json.loads(js)
    cols = eded.mapvV(d,lambda ele:ltlt.json2ltdict(ele))
    return((list(columns),cols))

def csv_wdtb(src_fn,from_file=True):
    df = pd.read_csv(src_fn)
    js = df.T.to_json()
    dst_fn = fs.repl_suffix(src_fn,"dtb.json")
    fs.wfile(dst_fn,js)

def csv2dtb(src_fn,from_file=True):
    df = pd.read_csv(src_fn)
    columns = df.columns
    js = df.T.to_json()
    d = json.loads(js)
    dtb = ltlt.json2ltdict(d)
    dtb = ltlt.to_list(dtb)
    return(dtb)


MIME_ORIG_CL = [".","-","+"]
MIME_REPL_CL = ["$","_","__"]


def js_key_encd(s,**kwargs):
    kl = efun.dflt_kwargs('kl',MIME_ORIG_CL)
    vl = efun.dflt_kwargs('vl',MIME_REPL_CL)
    for i in range(len(kl)):
        s = s.replace(kl[i],vl[i])
    return(s)

def js_key_dcd(s,**kwargs):
    kl = efun.dflt_kwargs('kl',MIME_ORIG_CL)
    vl = efun.dflt_kwargs('vl',MIME_REPL_CL)
    for i in range(len(kl)-1,-1,-1):
        s = s.replace(vl[i],kl[i])
    return(s)

def fmt_mime_key(k):
    arr = k.split(" ")
    return(arr[0])


def csv2jsd(src_fn,colname0,colname1,**kwargs):
    from_file = efun.dflt_kwargs('from_file',True)
    fmt_key = efun.dflt_kwargs('fmt_key',fmt_mime_key)
    dtb = csv2dtb(src_fn,from_file)
    l = elel.mapv(dtb,lambda ele:{js_key_encd(fmt_key(ele[colname0])):ele[colname1]})
    d = dldl.dlist2dict(l)
    return(d)

def csv_wjsd(src_fn,colname0,colname1,**kwargs):
    d = csv2jsd(src_fn,colname0,colname1,**kwargs)
    dst_fn = fs.repl_suffix(src_fn,"json")
    fs.wjson(dst_fn,d)
