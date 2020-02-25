from spheres import *
import qutip as qt
import copy

########################################################################################

class OperatorExpression:
    def __init__(self, ops):
        self.ops = ops        

    def __mul__(self, other):
        if type(other) == OperatorExpression:
            return OperatorExpression(self.ops+other.ops)
        elif other.__class__ == qt.Qobj and other.type == "oper":
            return OperatorExpression(self.ops+[other])
        else:
            return self.reduced()*other

    def __rmul__(self, other):
        if type(other) == OperatorExpression:
            return OperatorExpression(other.ops+self.ops)
        elif other.__class__ == qt.Qobj and other.type == "oper":
            return OperatorExpression([other]+self.ops)
        else:
            return other*self.reduced()

    def __getattr__(self, name):
        return getattr(self.reduced(), name)

    def reduced(self, i=None):
        if i == None:
            return self.prod(self.ops)
        else:
            return self.prod(self.ops[:i]),\
                   self.prod(self.ops[i+1:]),\

    def prod(self, l):
        p = l[0]
        for el in l[1:]:
            p = View(p.__old_mul__(el), local=True)
        return p

    def __implement_set__(self, view, silent=False):
        object.__setattr__(view, "_obj", self.reduced())
        if not silent:
            for i, op in enumerate(self.ops):
                if "View" in type(op).__name__ and op.uuid == view.uuid:
                    before, after = self.reduced(i=i)
                    for uuid, listener_data in view.listeners.items():
                        with_func = listener_data["with_func"]
                        if uuid in View.views:
                            View.views[uuid].set(\
                                    with_func(view,\
                                    View.views[uuid],\
                                    {"before": before, "after": after}),\
                                    exclude=[view.uuid])

    def __repr__(self):
        return str(self.ops)

########################################################################################

_qview_type = type(View(qt.basis(2,0)))
setattr(_qview_type, "__old_mul__", copy.copy(_qview_type.__mul__))
setattr(_qview_type, "__old_rmul__", copy.copy(_qview_type.__rmul__))
def __new_mul__(self, other):
    if self.type == "bra":
        if type(other) == OperatorExpression:
            return self.__old_mul__(other.reduced())
    elif self.type == "oper":
        if type(other) == OperatorExpression:
            return OperatorExpression([self]+other.ops)
        elif other.__class__ == qt.Qobj and other.type == "oper":
            return OperatorExpression([self, other])
    return self.__old_mul__(other)
setattr(_qview_type, "__mul__", __new_mul__)
def __new_rmul__(self, other):
    if self.type == "ket":
        if type(other) == OperatorExpression:
            return other.reduced().__old_mul__(self)
    elif self.type == "oper":
        if type(other) == OperatorExpression:
            return OperatorExpression(other.ops+[self])
        elif other.__class__ == qt.Qobj and other.type == "oper":
            return OperatorExpression([other, self])
    return other.__old_mul__(self)
setattr(_qview_type, "__rmul__", __new_rmul__)
setattr(_qview_type, "__old_repr__", copy.copy(_qview_type.__repr__))
def __new_repr__(self):
    if self.name == "":
        return self.__old_repr__()
    self.__old_repr__()
    return self.name
setattr(_qview_type, "__repr__", __new_repr__)
setattr(_qview_type, "name", "")

_special_names = [
    '__abs__', '__add__', '__and__', '__call__', '__cmp__', '__coerce__', 
    '__contains__', '__delitem__', '__delslice__', '__div__', '__divmod__', 
    '__eq__', '__float__', '__floordiv__', '__ge__', '__getitem__', 
    '__getslice__', '__gt__', '__hash__', '__hex__', '__iadd__', '__iand__',
    '__idiv__', '__idivmod__', '__ifloordiv__', '__ilshift__', '__imod__', 
    '__imul__', '__int__', '__invert__', '__ior__', '__ipow__', '__irshift__', 
    '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', 
    '__long__', '__lshift__', '__lt__', '__mod__',  '__ne__', #'__mul__',
    '__neg__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', 
    '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', #'__repr__', 
    '__reversed__', '__rfloorfiv__', '__rlshift__', '__rmod__',
    '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', #'__rmul__',
    '__rtruediv__', '__rxor__', '__setitem__', '__setslice__', '__sub__', 
    '__truediv__', '__xor__', 'next',
]
setattr(_qview_type, "__old_dag__", copy.copy(qt.Qobj.dag))
def __new_dag__(self):
    return View(self.__old_dag__(), local=True)
setattr(_qview_type, "dag", __new_dag__)

for name in _special_names:
    if name in dir(qt.Qobj):
        def wrap(name):
            def __wrapper__(self, *args, **kwargs):
                args = [arg.reduced() if type(arg) == OperatorExpression else arg for arg in args]
                kwargs = dict([(k, v.reduced() if type(v) == OperatorExpression else v) for k, v in kwargs.items()])
                return getattr(self.reduced(), name)(*args, **kwargs)
            return __wrapper__
        setattr(OperatorExpression, name, wrap(name))

########################################################################################

View.register_expression_type(OperatorExpression)