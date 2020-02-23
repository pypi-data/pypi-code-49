import inspect
class InfoDictMetaClass(type):
    def __new__(cls,  name, bases, attrs):
        key='__default_dict__'
        dic={}
        for k,v in attrs.items():
            if not inspect.isfunction(v):
                if not k.startswith('__'):
                    dic[k]=v
        attrs[key]=dic
        return type.__new__(cls,name,bases,attrs)
class InfoDict(dict,metaclass=InfoDictMetaClass):
    def __init__(self,*args,**kwargs):
        dic=dict(*args,**kwargs)
        dic.update(**self.__default_dict__)
        super().__init__(**dic)


def demo():
    class Info(InfoDict):
        name='张三'
        age=21
        gender='男'

    a=Info()
    print(a)
if __name__ == '__main__':
    demo()