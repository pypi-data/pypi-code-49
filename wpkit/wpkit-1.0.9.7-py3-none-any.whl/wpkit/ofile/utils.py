
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
def write_config(config,path,splitchar='='):
    open(path,'w').close()
    f=open(path,'a')
    for k,v in config.items():
        if isinstance(v,str):
            f.write('%s %s %s\n' % (key,splitchar,value))
        else:
            f.write('[%s]\n'%(k))
            assert isinstance(v,dict)
            for key,value in v.items():
                f.write('%s %s %s\n' % (key,splitchar,value))


def read_config(path,splitchar='=',comment_tag='#'):
    f=open(path,'r')
    config={}
    section_open=False
    current_section=None
    while True:
        s=f.readline()
        if not s:
            break
        if s.strip()=='':
            continue
        s=s.strip()
        if s.startswith('#'):
            continue
        if s.startswith('[') and s.endswith(']'):
            s=s[1:-1]
            assert '[' not in s and ']' not in s
            current_section=s
            config[current_section]={}
            section_open=True
            continue
        key,value=s.split(splitchar)
        key=key.strip()
        value=value.strip()
        if section_open:
            config[current_section][key]=value
        else:
            config[key]=value
    f.close()
    return config