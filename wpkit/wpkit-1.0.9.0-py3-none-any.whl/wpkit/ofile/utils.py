
def json_load(f,encoding='utf-8',*args,**kwargs):
    import json
    with open(f,'r',encoding=encoding) as fp:
        return json.load(fp,*args,**kwargs)
def json_dump(obj,fp,encoding='utf-8',*args,**kwargs):
    import json
    with open(fp,'w',encoding=encoding) as f:
        json.dump(obj,f,*args,**kwargs)
def readtxt(path,encoding='utf-8'):
    with open(path,'r',encoding=encoding) as f:
        return f.read()
def writetxt(txt,path,encoding='utf-8'):
    with open(path,'w',encoding=encoding) as f:
        f.write(txt)