from wpkit.node import *
from . import Q

class script:
    class jquery(Script):__node_type__='script';src = '/pkg-resource/js/jquery-3.4.1.js'
    class propper(Script):__node_type__='script';src='/pkg-resource/js/popper.min.js'
    class boostrap(Script):__node_type__='script';src='/pkg-resource/js/bootstrap.min.js'
    class vue(Script):__node_type__='script';src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"
    class myjs(Script):__node_type__='script';src="/pkg-resource/js/my.js"
class link:
    class csslink(Link): rel = "stylesheet";__node_type__='link'
    class bootstrap(csslink):__node_type__='link'; href="/pkg-resource/css/bootstrap.min.css";rel = "stylesheet"
class meta:
    boostrap=lambda :Text('<meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">')
class Htmlbase(Html):
    __node_type__='html'
    def __init__(self):
        super().__init__()
        self(
            Head()(Meta(charset=Var(charset='utf-8')),Title()(Var(title='Home')),Var(head_items=None)),
            Body()(Var(body=None))
        )
class Loginform(Form):
    __node_type__='form'
    def __init__(self):
        super().__init__(method=Var(method='get'), action=Var(action='/login'))
        self(Input(name='email', type='email'),
        Input(name='password', type='password'),
        Button(name='submit', type='submit')('Submit'))
class Loginpage(Htmlbase):
    __node_type__='html'
    def __init__(self):
        super().__init__()
        self.render(body=Loginform())
class Sitebase(Htmlbase):
    __node_type__ = 'html'
    def __init__(self):
        super().__init__()
        self.render(head_items=NodeList([
            meta.boostrap(),
            link.bootstrap(),
            script.jquery(),
            script.propper(),
            script.boostrap(),
            script.vue(),
            script.myjs()
        ]))
def stylestr(**kwargs):
    return ';'.join(["%s:%s"%(k.replace('_','-',-1),v) for k,v in kwargs.items()])
class PlaceHolder(Div):
    __node_type__ = 'div'
    def __init__(self,**kwargs):
        default=dict(width="100%",background_color="#fcfcfc",padding=0,margin=0)
        default.update(kwargs)
        super().__init__(style=stylestr(**default))





