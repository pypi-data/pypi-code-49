class TokenError(ValueError):
    def __init__(self,*args,**kwargs):
        ValueError.__init__(self,*args,**kwargs)

class ServerError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
