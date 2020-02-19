import inspect
import logging

logger = logging.getLogger('pinspector')

class URIInvoker():

    def __init__(self, targets):
        self.targets = targets

    def convert(self, val:str, ref):
        obj = val
        if type(ref) is bool:
            obj = bool(val)
        elif type(ref) is int:
            obj = int(val)
        elif type(ref) is float:
            obj = float(val)
        return obj

    def getval(self, obj, key:str):
        try:
            if isinstance(obj, dict):
                return obj[key]
            elif isinstance(obj, (list, tuple)):
                return obj[int(key)]
        except:
            pass
        return getattr(obj, key, None)

    def setval(self, obj, key:str, val):
        if isinstance(obj, dict):
            obj[key] = val
        elif isinstance(obj, (list, tuple)):
            obj[int(key)] = val
        else:
            return setattr(obj, key, val)

    def isfield(self, obj):
        return not inspect.isroutine(obj)

    def invoke(self, target, spec:str, prev_target=None):
        if isinstance(target, str) and not prev_target:
            target = self.targets[target]
        if spec == '_length':
            return len(target)
        elif spec == '_type':
            return type(target).__name__
        elif spec == '_islist':
            return 'true' if isinstance(target, list) else 'false'
        elif spec == '_methods':
            return [f[0] + '() ' + type(f[1]).__name__ for f in inspect.getmembers(target, inspect.isroutine)]
        elif spec == '_fields':
            fields = [f[0] + ' ' + type(f[1]).__name__ for f in inspect.getmembers(target, self.isfield)]
            if hasattr(target, '__dict__'):
                fields += [k + ' ' + type(v).__name__ for k, v in vars(target).items()]
            return fields
        elif spec == '_keys':
            if isinstance(target, dict):
                return target.keys()
            else:
                return ''
        elif spec == '_protocols':
            protos = []
            if isinstance(target, dict):
                protos.append('dict')
            if isinstance(target, list):
                protos.append('list')
            return protos
        elif '..' in spec:
            spec_info = spec.split('..', 1)
            return self.invoke(self.invoke(target, spec_info[0], prev_target=prev_target), spec_info[1], prev_target=target)
        else:
            if spec.startswith('$'):
                spec = spec[1:]
            elif spec.startswith('~'):
                spec = spec[1:]
            if '~~' in spec:
                spec_info = spec.split('~~', 1)
                attr = self.getval(target, spec_info[0])
                if callable(attr):
                    args = spec_info[1].split('::')
                    try:
                        val = attr(args)
                        if callable(val):
                            return val()
                        else:
                            return val
                    except:
                        try:
                            return attr([int(arg) for arg in args])
                        except:
                            return attr
                else:
                    val = self.convert(spec_info[1], attr)
                    self.setval(target, spec_info[0], val)
                    return self.getval(target, spec_info[0])
            else:
                attr = self.getval(target, spec)
                if isinstance(attr, (dict, list, int, str, float, bool)):
                    return attr
                elif callable(attr):
                    try:
                        val = attr()
                        if callable(val):
                            return val()
                        else:
                            return val
                    except:
                        return attr
                else:
                    return attr

    def print(self, obj):
        if isinstance(obj, str):
            return obj
        try:
            val = ''
            for el in obj:
                val += str(el)
                val += '\n'
            return val
        except:
            return str(obj)

    def run(self, target, spec:str):
        return self.print(self.invoke(target, spec))


