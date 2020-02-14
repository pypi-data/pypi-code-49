
def makedirs_ifneeded(d):
    import os
    os.makedirs(d) if not os.path.exists(d) else None
def remakedirs_anyway(d):
    import os,shutil
    shutil.rmtree(d) if os.path.exists(d) else None
    os.makedirs(d)
def inrange(n,rg):
    if n>=rg[0] and n<= rg[1]:return True
    return False
def split_list(lis,uint_size):
    num=(len(lis)-1)//uint_size+1
    l_list=[]
    [l_list.append(lis[i*uint_size:(i+1)*uint_size]) if i<num-1 else l_list.append(lis[i*uint_size:]) for i in range(num)]
    return l_list
def render_template(s, *args, **kwargs):
    from jinja2 import Environment
    env = Environment()
    tem = env.from_string(s)
    return tem.render(*args, **kwargs)
def json_load(f,encoding='utf-8',*args,**kwargs):
    import json
    with open(f,'r',encoding=encoding) as fp:
        return json.load(fp,*args,**kwargs)
def json_dump(obj,fp,encoding='utf-8',*args,**kwargs):
    import json
    with open(fp,'w',encoding=encoding) as f:
        json.dump(obj,f,*args,**kwargs)
def load_config(fp,line_split='\n',pair_split='=',encoding="utf-8"):
    with open(fp,'r',encoding=encoding) as f:
        lines=f.read().strip().split(line_split)
        dic={}
        for line in lines:
            if line.strip().startswith('#'):continue
            line=line.strip()
            key,value=line.split(pair_split)
            key=key.strip()
            value=value.strip()
            dic[key]=value
        return dic



