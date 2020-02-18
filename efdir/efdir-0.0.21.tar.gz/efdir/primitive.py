class _Undefined():
    def __repr__(self):
        return('undefined')

class _Null():
    def __repr__(self):
        return('null')


undefined = _Undefined()
null = _Null()
true = True
false = False
