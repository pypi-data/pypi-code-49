import re,inspect
# from collections import deque
import collections
class deque(collections.deque):
    def replacewith(self,x1,x2,key=None):
        if key and '__call__' in dir(key):
            for x in self:
                if key(x,x1):# matched
                    x1=x
                    break
        index=self.index(x1,0,len(self))
        self.remove(x1)
        self.insert(index,x2)

class T:
    NOT_FOUND='NOT_FOUND'
    NO_VALUE='NO_VALUE'
    EMPTY='EMPTY'
    SUCCESS='SUCCESS'
    FAILURE='FAILURE'
    NOT_GIVEN='NOT_GIVEN'
    ARG='ARG'
    KWARG='KWARG'


class NodeMetaClass(type):
    __not_found__='not_found'
    def __new__(cls, name, bases, attrs):
        dic={}
        dic['__attrs__'] = deque([])
        dic['__kwattrs__']={}
        special_keys=['__open_node__','__node_type__']
        if attrs.get('__open_node__',cls.__not_found__)==cls.__not_found__:
            attrs['__open_node__']=bases[0].__dic__['__open_node__']
        if attrs.get('__node_type__',cls.__not_found__)==cls.__not_found__:
            succeed=attrs.get('__secceed_name__', T.NOT_FOUND)
            if succeed!=T.NOT_FOUND and succeed:
                attrs['__node_type__']=bases[0].__dic__['__node_type__']
            else:
                attrs['__node_type__']=name.lower()
        tmp=attrs.copy()
        for k,v in tmp.items():
            if k in special_keys:
                dic[k]=v
                attrs.pop(k)
                continue
            if inspect.isfunction(v):continue
            if (not k.startswith('__')) or (not k.endswith('__')):
                attrs.pop(k)
                if k=='_class':k='class'
                na=NodeAttr(**{k:v})
                dic['__attrs__'].append(na)
                dic['__kwattrs__'][k]=na
        attrs['__dic__']=dic.copy()
        return type.__new__(cls, name, bases, attrs)

def parse_selector(sel):
    s=sel
    # s = '.div.blue[name=big]  #test,div'
    res={}
    pos = 0
    while True:
        if pos >= len(s) - 1:
            break
        reg_el = re.compile("[a-zA-Z0-9]+")
        match = reg_el.match(s, pos=pos)
        if match:
            pos += len(match.group())
            res['__node_type__']=match.group()
            continue

        reg_cls = re.compile('\.[a-zA-Z0-9_\-]+')
        match = reg_cls.match(s, pos=pos)
        if match:
            pos += len(match.group())
            if '_class' in res.keys():res['_class']+=' '+match.group().lstrip('.')
            else:res['_class']=match.group().lstrip('.')
            continue

        reg_id = re.compile('#[a-zA-Z0-9_\-]+')
        match = reg_id.match(s, pos=pos)
        if match:
            pos += len(match.group())
            res['id']=match.group().lstrip('#')
            continue

        reg_attr = re.compile('\[[a-zA-Z0-9_\-]+=[a-zA-Z0-9_\-]+\]')
        match = reg_attr.match(s, pos=pos)
        if match:
            pos += len(match.group())
            k,v=match.group().lstrip('[').rstrip(']').split('=')
            res[k.strip()]=v.strip()
            continue
    return res
def struc(x,**kwargs):
    if 'struc' in dir(x):
        return x.struc(**kwargs)
    return str(x)
def tostr(x,**kwargs):
    if 'to_string' in dir(x):
        return x.to_string(**kwargs)
    return str(x)
import uuid
class NodeAttr(object):
    def __init__(self,*args,**kwargs):
        # assert len(args) or len(kwargs)
        assert not (len(args) and len(kwargs))
        if len(args):
            self.type=T.ARG
            self.value=args[0]
        elif len(kwargs):
            self.type=T.KWARG
            self.name,self.value=list(kwargs.items())[0]
        self.qid=uuid.uuid4().hex
    def deepcopyself(self):
        obj=NodeAttr()
        obj.type=self.type
        obj.value=deepcopy(self.value)
        obj.name=self.name
        obj.qid=self.qid
        return obj
    def __qeq__(self,x1):
        if isinstance(x1,NodeAttr) and x1.qid==self.qid:
            return True
        return False
    def __str__(self):
        if self.type==T.ARG:
            return str(self.value)
        if self.type==T.KWARG:
            name='class' if self.name=='_class' else self.name
            return '%s="%s"'%(name,tostr(self.value,new_line=False))
    def struc(self,*args,**kwargs):
        if self.type==T.ARG:
            return struc(self.value,depth=0)
        if self.type==T.KWARG:
            name='class' if self.name=='_class' else self.name
            return '%s="%s"'%(name,struc(self.value,depth=0,new_line=False))
def escape_style_dic(dic):
    dic2={}
    for k,v in dic.items():
        dic2[k.replace('_','-',-1)]=v
    return dic2
class StyleAttr(dict):
    def __init__(self,*args,**kwargs):
        kwargs=self.escape_style_dic(kwargs)
        args=list(args)
        if len(args) and isinstance(args[0],dict):
            args[0]=self.escape_style_dic(args[0])
        super().__init__(*args,**kwargs)

    def escape_style_dic(self,dic):
        return escape_style_dic(dic)
    def __setattr__(self, key, value):
        key=key.replace('_','-',-1)
        self[key]=value
    def __getattr__(self, key):
        key=key.replace('_','-',-1)
        return self.get(key)
    def __str__(self):
        return ";".join(['%s:%s'%(k,v) for k,v in self.items()])
def deepcopy(x):
    if isinstance(x,list) or isinstance(x,deque):
        cls=x.__class__
        tmp_list=[]
        for item in x:
            tmp_list.append(deepcopy(item))
        return cls(tmp_list)
    elif isinstance(x,dict):
        cls=x.__class__
        tmp_dict={}
        for k,v in x.items():
            tmp_dict[k]=deepcopy(v)
        return cls(tmp_dict)
    elif 'deepcopyself' in dir(x):
        # if isinstance(x, NodeAttr):
        #     print('copying styleattr...')
        return x.deepcopyself()

    return x
class Node(metaclass=NodeMetaClass):
    __indent__=' '*4
    __open_node__=True
    def __init__(self,*args,**kwargs):
        for k,v in self.__dic__.items():
            # self.__dict__[k]=v.copy() if 'copy' in dir(v) else v
            self.__dict__[k]=deepcopy(v)
            # print('v:',v)
            # print(['%s'%i for i in v]) if isinstance(v, deque) else None
            # print('v_copy:',deepcopy(v))
        self.setd(children=deque([]))
        self.update_attr(*args,**kwargs)
        self.setd(parent=None)
    def update_attr(self,*args,**kwargs):

        for a in args:
            self.__dict__['__attrs__'].append(NodeAttr(a))
        for k,v in kwargs.items():
            k='class' if k=='_class' else k
            if isinstance(v,Node):v.setd(parent=self)
            x=NodeAttr(**{k:v})
            kwattrs=self.getd('kwattrs')
            if k in kwattrs.keys():
                x_old=kwattrs[k]

                # if k=='style':
                #     print(k)
                # if isinstance(x_old.value,StyleAttr):
                #     print('x_old:',x_old)
                # else:
                #     print(x_old)
                self.__dict__['__attrs__'].replacewith(x_old,x,key=lambda x1,x2: x1.__qeq__(x2))
                kwattrs[k]=x
            else:
                self.__dict__['__attrs__'].append(x)
                kwattrs[k]=x
    def attr(self,key=None,**kwargs):
        if key:return self.getd('kwattrs').get(key,None)
        if len(kwargs):
            self.update_attr(**kwargs)
            return self
        return self.__dict__['__attrs__']
    def update_class(self,cls):
        old_cls=self.attr('class')
        if old_cls:old_cls=old_cls.value
        def tolist(old_cls):
            if old_cls:
                old_cls = old_cls.split()
            return old_cls or []
        cls=set(tolist(old_cls)).union(tolist(cls))
        cls=' '.join(cls)
        self.update_attr(_class=cls)

    def cls(self,*args):
        if not len(args):
            return self.attr('class').value if self.attr('class') else None
        else:
            self.update_class(*args)
            return self

    def css(self,**kwargs):
        if not self.attr("style"):self.attr(style=StyleAttr())
        if len(kwargs):
            self.attr("style").value.update(escape_style_dic(kwargs))
            style=self.attr('style').value
            self.attr(style=style)
            # if self.__class__.__name__=='QBox':
            #     if 'float' in kwargs.keys():
            #         print('__attrs__:',self.getd('attrs')[0])
            #         print('__kwattrs__:',self.getd('kwattrs')['style'])
            #         print('Qbox style:',self.attr('style'))
            #         print('attr:',[str(i) for i in self.attr()])
            #         print('self:',self)
        return self

    def parent(self):
        return self.getd('parent')
    def children(self,*args):
        if len(args):
            if len(args)==1 and isinstance(args[0],int):return self.getd('children')[args[0]]
            self.setd(children=list(args))
        return self.__dict__['__children__']
    def append(self,x):
        x.setd(parent=self) if isinstance(x,Node) else None
        self.__dict__['__children__'].append(x)
    def appendleft(self,x):
        x.setd(parent=self) if isinstance(x,Node) else None
        return self.__dict__['__children__'].appendleft(x)
    def count(self, x):
        return self.__dict__['__children__'].count(x)
    def extend(self,iterable):
        for x in iterable:x.setd(parent=self) if isinstance(x,Node) else None
        return self.__dict__['__children__'].extend(iterable)
    def extendleft(self,iterable):
        for x in iterable: x.setd(parent=self) if isinstance(x,Node) else None
        return self.__dict__['__children__'].extendleft(iterable)
    def insert(self,i,x):
        x.setd(parent=self) if isinstance(x,Node) else None
        return self.__dict__['__children__'].insert(i,x)
    def index(self,x,start=0,stop=None):
        stop=len(self.children()) if stop is None else stop
        return self.__dict__['__children__'].index(x,start,stop)
    def pop(self,i):
        return self.__dict__['__children__'].pop(i)
    def popleft(self):
        return self.__dict__['__children__'].popleft()
    def remove(self,value):
        return self.__dict__['__children__'].remove(value)
    def reverse(self):
        return self.__dict__['__children__'].reverse()
    def rotate(self, n: int) -> None:
        return self.__dict__['__children__'].rotate(n)
    def replace(self,v1,v2):
        index=self.index(v1)
        self.remove(v1)
        self.insert(index,v2)
        return self
    def replace_var(self,v1,v2):
        for att in self.attr():
            if v1 is att.value:
                if att.type==T.ARG:att.value=v2
                else:self.update_attr(**{att.name:v2})
            return self
        if v1 in self.children():
            self.replace(v1,v2)
            return self
        return self
    def replacewith(self,node):
        if isinstance(node,str):node=Text(node)
        return self.parent().replace(self,node)
    def __getitem__(self, item):
        if isinstance(item,str):
            return self.find(sel=item)[0]
        return self.children()[item]
    def __setitem__(self, key, value):
        value.setd(parent=self)
        return self.__dict__['__children__'].__setitem__(key,value)
    def __call__(self, *args):
        if not len(args):return self
        args=list(args)
        for i in range(len(args)):
            if isinstance(args[i],str):
                s=args[i].strip()
                if s.startswith('<!--') and s.endswith('-->'):
                    args[i]=Comment(s.lstrip('<!--').rstrip('-->'))
                else:
                    args[i]=Text(s)

        self.__dict__['__children__'] = deque(args)
        for i in self.children():
            i.setd(parent=self) if isinstance(i,Node) else None
        return self

    def __getattr__(self, key):
        kw=self.getd('kwattrs').get(key, None)
        if kw:return kw.value
        else:raise AttributeError('No such attribute named %s'%(key))

    def __setattr__(self, key, value):
        return self.update_attr(**{key:value})

    def set_attribute(self, key, value):
        self.__dict__[key] = value

    def get_attribute(self, *args, **kwargs):
        return self.__dict__.get(*args, **kwargs)

    def setd(self, **kwargs):
        for k, v in kwargs.items():
            self.set_attribute('__%s__' % (k), v)

    def getd(self, key, *args, **kwargs):
        return self.get_attribute('__%s__' % (key), *args, **kwargs)
    def render(self,**kwargs):
        for k,v in kwargs.items():
            ns = self.find_var('var[varname=%s]'%(k))
            for n in ns:
                n.replacewith(v)
        return self
    def match(self,**kwargs):
        if '__node_type__' in kwargs.keys():
            if not self.getd('node_type')==kwargs['__node_type__']:return False
            kwargs.pop('__node_type__')
        if '_class' in kwargs.keys():
            if (not self._class) or (not set(kwargs['_class'].split()).issubset(set(self._class.split()))):return False
            kwargs.pop('_class')
        for k,v in kwargs.items():
            if not self.__getattr__(k)==v:return False
        return True
    def find_var(self, sel=None,kws=None, res_list=None):
        # print(kws)
        if sel:kws=parse_selector(sel);
        if not res_list:res_list={'list':FindResult()}
        for att in self.attr():
            if 'match' in dir(att.value) and att.value.match(**kws):
                res_list['list'].append(att.value)
        for ch in self.children():
            if ch.match(**kws):res_list['list'].append(ch)
        for ch in self.children():
            ch.find_var(kws=kws,res_list=res_list)
        return res_list['list']
    def find(self, sel=None,kws=None, res_list=None):
        if sel:kws=parse_selector(sel);
        if not res_list:res_list={'list':FindResult()}
        if self.match(**kws):res_list['list'].append(self)
        for ch in self.children():
            ch.find(kws=kws,res_list=res_list)
        return res_list['list']
    def __str__(self):
        return self.to_string()

    def compile(self):
        return Text(self.to_string())
    def tofile(self,fp):
        from wpkit.basic import PowerDirPath
        PowerDirPath(fp).tofile()(self.to_string())
        return self
    def print(self,depth=0):
        print(self.to_string(depth=depth))
        return self
    def get_children_string(self,depth=0):
        def to_string(ch,depth=0):
           return ch.to_string(depth=depth) if isinstance(ch,Node) else '\n'+self.__indent__*depth+str(ch)

        mid = '\n' + self.__indent__ * depth if len(self.__dict__['__children__']) else ''
        content = ''.join([to_string(ch, depth=depth + 1) for ch in self.__dict__['__children__']])
        return content+mid
    def get_string(self,depth=0):
        def to_string(ch,depth=0):
           return ch.to_string(depth=depth) if isinstance(ch,Node) else '\n'+self.__indent__*depth+str(ch)

        attrs = ' '.join([str(att) for att in self.attr()])
        attrs = ' ' + attrs if len(attrs) else attrs
        if self.getd('open_node'):
            mid='\n'+self.__indent__ * depth if len(self.__dict__['__children__']) else ''
            content=''.join([to_string(ch,depth=depth + 1) for ch in self.__dict__['__children__']])
            return '\n%s<%s%s>%s%s</%s>' % (self.__indent__ * depth,self.__node_type__,attrs,
                                               content,mid,self.__node_type__)
        else:
            return '\n%s<%s %s/>' % (self.__indent__ * depth,self.__node_type__,attrs)
    def to_string(self, depth=0,new_line=True,*args,**kwargs):
        def to_string(ch,depth=0):
           return ch.to_string(depth=depth) if isinstance(ch,Node) else '\n'+self.__indent__*depth+str(ch)
        attrs = ' '.join([str(att) for att in self.attr()])
        attrs = ' ' + attrs if len(attrs) else attrs
        if self.getd('open_node'):
            mid='\n'+self.__indent__ * depth if len(self.__dict__['__children__']) else ''
            content=''.join([to_string(ch,depth=depth + 1) for ch in self.__dict__['__children__']])
            return '\n%s<%s%s>%s%s</%s>' % (self.__indent__ * depth,self.__node_type__,attrs,
                                               content,mid,self.__node_type__)
        else:
            return '\n%s<%s %s/>' % (self.__indent__ * depth,self.__node_type__,attrs)
    def print_structure(self):
        print(self.struc())
    def struc(self,depth=0,new_line=True,*args,**kwargs):
        def to_string(ch,depth=0):
           return ch.struc(depth=depth,new_line=new_line) if isinstance(ch,Node) else '\n'*new_line+self.__indent__*depth+str(ch)
        attrs=' '.join([struc(att,depth=0) for att in self.attr()])
        attrs = ' ' + attrs if len(attrs) else attrs
        pre='\n'*new_line+self.__indent__ * depth
        if self.getd('open_node'):
            mid='\n'*new_line+self.__indent__ * depth if len(self.__dict__['__children__']) else ''
            content=''.join([to_string(ch,depth=depth + 1) for ch in self.__dict__['__children__']])
            return '%s<%s%s>%s%s</%s>' % (pre,self.__node_type__,attrs,
                                               content,mid,self.__node_type__)
        else:
            return '%s<%s %s/>' % (pre,self.__node_type__,attrs)
class FindResult(list):
    pass


class CloseNode(Node):
    __open_node__=False

class Text(Node):
    def __init__(self,content='',**kwargs):
        self.setd(content=content)
        super().__init__(**kwargs)
    def struc(self,depth=0,new_line=True):
        return '\n'*new_line+depth*self.__indent__+'<%s>%s</%s>'%(self.getd('node_type'),self.getd('content'),self.getd('node_type'))
    def to_string(self, depth=0,new_line=True,*args,**kwargs):
        return '\n'*new_line+self.__indent__*depth+str(self.getd('content'))
    def render(self,**kwargs):
        from jinja2 import Environment
        tem = Environment().from_string(self.getd('content'))
        return Text(tem.render(**kwargs))


class Comment(Node):
    def __init__(self, content='', **kwargs):
        self.__dict__['content'] = content
        super().__init__(**kwargs)
    def to_string(self, depth=0,new_line=True,*args,**kwargs):
        return '\n'*new_line+self.__indent__*depth+'<!--'+str(self.__dict__['content'])+'-->'

class NodeList(Node,deque):
    def __init__(self,*args):
        deque.__init__(self,*args)
        Node.__init__(self)
    def struc(self,depth=0,new_line=True,*args,**kwargs):
        mid='\n'*new_line + self.__indent__ * depth
        return mid + '<%s>'%(self.getd('node_type')) + \
        ''.join([struc(item,depth=depth+1,new_line=new_line)  for item in self]) +\
         mid+'</%s>'%(self.getd('node_type'))
    def to_string(self, depth=0,new_line=True,*args,**kwargs):
        return ''.join([item.to_string(depth=depth) if isinstance(item,Node) else str(item) for item in self])

# ------------------------vars------------------------
class Tem(Node):pass
class Var(Node):
    def __init__(self, varname=None, vardefault=T.NOT_GIVEN,**kwargs):
        super().__init__()
        if len(kwargs):
            assert len(kwargs)==1
            varname,vardefault=list(kwargs.items())[0]
        self.varname = varname
        self.vardefault=vardefault
    def replacewith(self,node):
        if not isinstance(node,Node):node=Text(node)
        self.getd('parent').replace_var(self,node)
        return self
    def to_string(self, depth=0,new_line=True,*args,**kwargs):
        d=self.vardefault
        if d==T.NOT_GIVEN:return self.get_string(depth=depth)
        if not d:return ''
        if isinstance(d,Node):return d.to_string(depth=depth)
        return str(d)
class Jvar(Node):
    def __init__(self,name,**kwargs):
        self.setd(name=name)
        super().__init__(**kwargs)
    def __str__(self):
        return self.to_string()
    def to_string(self, depth=0,new_line=True,*args,**kwargs):
        return '{{%s}}' % (self.getd('name'))
class For(Node):
    def __init__(self,forwhat,**kwargs):
        self.setd(forwhat=forwhat)
        super().__init__(**kwargs)
    def to_string(self, depth=0,new_line=True,*args,**kwargs):
        return '\n'+self.__indent__*depth+'{%for '+self.getd('forwhat')+'%}'+self.get_children_string(depth=depth)+'{%endfor%}'

class If(Node):
    def __init__(self, condition, **kwargs):
        self.setd(condition=condition)
        super().__init__(**kwargs)
    def to_string(self, depth=0,new_line=True,*args,**kwargs):
        return '\n'+self.__indent__*depth+'{%if '+self.getd('condition')+'%}'+self.get_children_string(depth=depth)+'{%endif%}'
class Elif(Node):
    def __init__(self, condition, **kwargs):
        self.setd(condition=condition)
        super().__init__(**kwargs)
    def to_string(self, depth=0,new_line=True,*args,**kwargs):
        return '\n'+self.__indent__*depth+'{%elif '+self.getd('condition')+'%}'+self.get_children_string(depth=depth)
class Else(Node):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def to_string(self, depth=0,new_line=True,*args,**kwargs):
        return '\n'+self.__indent__*depth+'{%else%}'+self.get_children_string(depth=depth)



# ------------------------------------------------

class Html(Node):pass
class Head(Node):pass
class Title(Node):pass
class Meta(CloseNode):pass
class Link(CloseNode):pass
class Style(Node):pass
class Script(Node):pass
class Body(Node):pass
class Div(Node):pass
class Span(Node):pass
class P(Node):pass
class A(Node):pass
class Img(CloseNode):pass
class Form(Node):pass
class Input(CloseNode):pass
class Button(Node):pass
# --------------some utils---------------------

# ---------more tags ---------

class Address(Node):pass
class Article(Node):pass
class Aside(Node):pass
class Footer(Node):pass
class Header(Node):pass
class H1(Node):pass
class H2(Node):pass
class H3(Node):pass
class H4(Node):pass
class H5(Node):pass
class H6(Node):pass
class Hgroup(Node):pass
class Main(Node):pass
class Nav(Node):pass
class Section(Node):pass
class Blackquote(Node):pass
class Dd(Node):pass
class Dir(Node):pass
class Dl(Node):pass
class Dt(Node):pass
class Figure(Node):pass
class Hr(Node):pass
class Li(Node):pass
class Ol(Node):pass
class Ul(Node):pass
class Pre(Node):pass
class Abbr(Node):pass
class B(Node):pass
class Br(Node):pass
class Cite(Node):pass
class Code(Node):pass
class Data(Node):pass
class Em(Node):pass
class I(Node):pass
class Kbd(Node):pass
class Mark(Node):pass
class Q(Node):pass
class Small(Node):pass
class Strong(Node):pass
class Sub(Node):pass
class Sup(Node):pass
class Time(Node):pass
class Area(Node):pass
class Audio(Node):pass
class Map(Node):pass
class Video(Node):pass
class Track(Node):pass
class Embed(Node):pass
class Iframe(Node):pass
class Object(Node):pass
class Param(Node):pass
class Picture(Node):pass
class Sourcecanvas(Node):pass
class Noscript(Node):pass
class Del(Node):pass
class Ins(Node):pass
class Caption(Node):pass
class Col(Node):pass
class Table(Node):pass
class Tbody(Node):pass
class Td(Node):pass
class Tfoot(Node):pass
class Th(Node):pass
class Thead(Node):pass
class Tr(Node):pass
class Fieldset(Node):pass
class Datalist(Node):pass
class Label(Node):pass
class Legend(Node):pass
class Meter(Node):pass
class Optgroup(Node):pass
class Option(Node):pass
class Output(Node):pass
class Progress(Node):pass
class Select(Node):pass
class Textarea(Node):pass
class Details(Node):pass
class Dialog(Node):pass
class Menu(Node):pass
class Menuitem(Node):pass
class Summary(Node):pass
class Element(Node):pass
class Shadow(Node):pass
class Slot(Node):pass
class Template(Node):pass
class Big(Node):pass
class Blink(Node):pass
class Center(Node):pass
class Bgsound(Node):pass
class Command(Node):pass

taglist=\
    'address article aside footer header h1 h2 h3 h4 h5 h6 ' \
    'hgroup main nav section ' \
    'blackquote dd dir dl dt figure hr li ol ul pre ' \
    'abbr b br cite code data em i kbd mark q small strong sub sup ' \
    'time var area audio map video track embed iframe object param picture source' \
    'canvas noscript del ins caption col table tbody td tfoot th thead tr ' \
    'button fieldset datalist form input label legend meter optgroup option ' \
    'output progress select textarea details dialog menu menuitem summary ' \
    'comment element shadow slot template ' \
    'big blink center bgsound center command '.split()

class css:
    class color:
        white='#ffffff'
        black='#00000'
# -------------------------Utils---------------------------







