
import glob,os,re
def count(arr,sort=True):
    items=set(arr)
    counts=[0]*len(items)
    for i,el in enumerate(arr):
        for j,item in enumerate(items):
            if el==item:
                counts[j]+=1
    res=list(zip(items,counts))
    if sort:
        res.sort(key=lambda item:item[1],reverse=True)
    return res
def count_to_dict(arr):
    return {k:v for k,v in count(arr)}
def fill_string_with_list(text,list,replace_char='*'):
    for l in list:
        text=text.replace(replace_char,str(l),1)
    return text
def find_those_who(list,key):
    new=[]
    for i in list:
        if key(i):new.append(i)
    return new

def auto_name(pattern='*.jpg',dir=None):
    if dir:
        ptn=find_path_pattern(dir)
        return auto_name(pattern=ptn)
    else:
        items=glob.glob(pattern)
        indexes=[]
        parts = pattern.split('*')
        def find_all_parts(text):
            myparts=parts.copy()
            reses=[]
            for i in range(len(myparts)-1):
                pre='(?<=%s)'%(myparts[i]) if len(myparts[i]) else ''
                suf='(?=%s)'%(myparts[i+1]) if len(myparts[i+1]) else ''
                reg='%s.*?%s'%(pre,suf)
                res=re.findall(reg,text)
                if not len(res):
                    print("reg not find in text:", reg,text)
                    return None
                res=res[0]
                reses.append(res)
                myparts[i+1]=myparts[i]+res+myparts[i+1]
            if not len(reses)==len(parts)-1:return None
            return reses
        for item in items:
            numbers = find_all_parts(item)
            if  not numbers:
                continue
            # print("numbers:",numbers)
            indexes.append(numbers)
        def get_max_index(indexes):
            # print(indexes)
            for i in range(len(indexes[0])):
                indexes.sort(key=lambda index:index[i])
                tmp=find_those_who(indexes,key=lambda index:index[i]==indexes[-1][i])
                indexes=tmp
            return indexes[0]
        if len(indexes):
            new_index=get_max_index(indexes)
            new_index[-1]=str(int(new_index[-1])+1)
        else:
            new_index=[0]
        path=fill_string_with_list(pattern,new_index,'*')
    return path
def find_path_pattern(dir):
    items = glob.glob(dir + '/*')
    ptns = []
    for item in items:
        nums = re.findall('[0-9]{1,}', item)
        if not len(nums): continue
        ptn = item
        for num in nums:
            ptn = ptn.replace(num, '*', 1)
        ptns.append(ptn)
    if not len(ptns):
        ptns.append('*.jpg')
    counts = count(ptns)
    if not counts:return None
    ptn = counts[0][0]
    return ptn
def get_max_path(pattern='*.jpg',dir=None):
    if dir:
        ptn=find_path_pattern(dir=dir)
        return get_max_path(pattern=ptn)
    else:
        items=glob.glob(pattern)
        indexes=[]
        parts = pattern.split('*')
        def find_all_parts(text):
            myparts=parts.copy()
            reses=[]
            for i in range(len(myparts)-1):
                pre='(?<=%s)'%(myparts[i]) if len(myparts[i]) else ''
                suf='(?=%s)'%(myparts[i+1]) if len(myparts[i+1]) else ''
                reg='%s.*?%s'%(pre,suf)
                res=re.findall(reg,text)
                if not len(res):
                    print("reg not find in text:", reg,text)
                    return None
                res=res[0]
                reses.append(res)
                myparts[i+1]=myparts[i]+res+myparts[i+1]
            if not len(reses)==len(parts)-1:return None
            return reses
        for item in items:
            numbers = find_all_parts(item)
            if  not numbers:
                continue
            # print("numbers:",numbers)
            indexes.append(numbers)
        def get_max_index(indexes):
            # print(indexes)
            for i in range(len(indexes[0])):
                indexes.sort(key=lambda index:index[i])
                tmp=find_those_who(indexes,key=lambda index:index[i]==indexes[-1][i])
                indexes=tmp
            return indexes[0]
        if len(indexes):
            new_index=get_max_index(indexes)
            # print(new_index)
            # new_index[-1]=str(int(new_index[-1])+1)
            path = fill_string_with_list(pattern, new_index, '*')
        else:
            path=None
    return path

# x=auto_name(dir='data/test/result')
# x=auto_name(pattern='data/test/result/*_*_*.jpg')
# x=get_max_path(dir='data/test/result/')
# print(x)
import glob,os,re
def count(arr,sort=True):
    items=set(arr)
    counts=[0]*len(items)
    for i,el in enumerate(arr):
        for j,item in enumerate(items):
            if el==item:
                counts[j]+=1
    res=list(zip(items,counts))
    if sort:
        res.sort(key=lambda item:item[1],reverse=True)
    return res
def count_to_dict(arr):
    return {k:v for k,v in count(arr)}
def fill_string_with_list(text,list,replace_char='*'):
    for l in list:
        text=text.replace(replace_char,str(l),1)
    return text
def find_those_who(list,key):
    new=[]
    for i in list:
        if key(i):new.append(i)
    return new

def auto_name(pattern='*.jpg',dir=None):
    if dir:
        ptn=find_path_pattern(dir)
        return auto_name(pattern=ptn)
    else:
        items=glob.glob(pattern)
        indexes=[]
        parts = pattern.split('*')
        def find_all_parts(text):
            myparts=parts.copy()
            reses=[]
            for i in range(len(myparts)-1):
                pre='(?<=%s)'%(myparts[i]) if len(myparts[i]) else ''
                suf='(?=%s)'%(myparts[i+1]) if len(myparts[i+1]) else ''
                reg='%s[0-9]*?%s'%(pre,suf)
                res=re.findall(reg,text)
                if not len(res):
                    print("reg not find in text:", reg,text)
                    return None
                res=res[0]
                reses.append(res)
                myparts[i+1]=myparts[i]+res+myparts[i+1]
            if not len(reses)==len(parts)-1:return None
            return reses
        for item in items:
            numbers = find_all_parts(item)
            if  not numbers:
                continue
            # print("numbers:",numbers)
            indexes.append(numbers)
        def get_max_index(indexes):
            # print(indexes)
            for i in range(len(indexes[0])):
                indexes.sort(key=lambda index:index[i])
                tmp=find_those_who(indexes,key=lambda index:index[i]==indexes[-1][i])
                indexes=tmp
            return indexes[0]
        if len(indexes):
            new_index=get_max_index(indexes)
            new_index[-1]=str(int(new_index[-1])+1)
        else:
            new_index=[0]
        path=fill_string_with_list(pattern,new_index,'*')
    return path
def find_path_pattern(dir):
    items = glob.glob(dir + '/*')
    ptns = []
    for item in items:
        nums = re.findall('[0-9]{1,}', item)
        if not len(nums): continue
        ptn = item
        for num in nums:
            ptn = ptn.replace(num, '*', 1)
        ptns.append(ptn)
    if not len(ptns):
        ptns.append('*.jpg')
    counts = count(ptns)
    if not counts:return None
    ptn = counts[0][0]
    return ptn
def get_max_path(pattern='*.jpg',dir=None):
    if dir:
        ptn=find_path_pattern(dir=dir)
        return get_max_path(pattern=ptn)
    else:
        items=glob.glob(pattern)
        indexes=[]
        parts = pattern.split('*')
        def find_all_parts(text):
            myparts=parts.copy()
            reses=[]
            for i in range(len(myparts)-1):
                pre='(?<=%s)'%(myparts[i]) if len(myparts[i]) else ''
                suf='(?=%s)'%(myparts[i+1]) if len(myparts[i+1]) else ''
                reg='%s[0-9]*?%s'%(pre,suf)
                res=re.findall(reg,text)
                if not len(res):
                    print("reg not find in text:", reg,text)
                    return None
                res=res[0]
                reses.append(res)
                myparts[i+1]=myparts[i]+res+myparts[i+1]
            if not len(reses)==len(parts)-1:return None
            return reses
        for item in items:
            numbers = find_all_parts(item)
            if  not numbers:
                continue
            # print("numbers:",numbers)
            indexes.append(numbers)
        def get_max_index(indexes):
            # print(indexes)
            for i in range(len(indexes[0])):
                indexes.sort(key=lambda index:index[i])
                tmp=find_those_who(indexes,key=lambda index:index[i]==indexes[-1][i])
                indexes=tmp
            return indexes[0]
        if len(indexes):
            new_index=get_max_index(indexes)
            # print(new_index)
            # new_index[-1]=str(int(new_index[-1])+1)
            path = fill_string_with_list(pattern, new_index, '*')
        else:
            path=None
    return path

# x=auto_name(dir='data/test/result')
# x=auto_name(pattern='data/test/result/*_*_*.jpg')
# x=get_max_path(dir='data/test/result/')
# print(x)