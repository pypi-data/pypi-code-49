from spheres import *

def Sphere(obj, *args, **kwargs):
    kwargs = {**kwargs, \
              **{"to_client": lambda view:\
                    {"stars": spin_XYZ(view),\
                     "phase": [1,0]},\
                "from_client": lambda data: XYZ_spin(data["stars"]),\
                "js_class": "Sphere"}}
    return View(obj, *args, **kwargs)

def partials(pure):
    _partials = []
    n = len(pure.dims[0])
    for i in range(n):
        partial = View(pure.ptrace(i))
        def __pure_to_partial__(index, dims):
            def __pure_to_partial__inner__(_pure):
                val = _pure.get()
                val.dims = dims
                return val.ptrace(index)
            return __pure_to_partial__inner__
        partial.listen(pure, __pure_to_partial__(i, pure.dims))
        def __partial_to_pure__(index, dims):
            def __partial_to_pure__iner__(_partial, _pure, data):
                return qt.tensor(*[qt.identity(d)\
                    if j!=index else data["after"]\
                        for j, d in enumerate(dims[0])])*_pure.get()
            return __partial_to_pure__iner__
        pure.listen(partial, __partial_to_pure__(i, pure.dims),\
            expression_type=OperatorExpression)
        _partials.append(partial)
    return _partials