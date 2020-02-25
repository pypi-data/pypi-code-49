import json
from urllib.parse import parse_qs

from horno.utiles.IO import IOSistema
from horno.utiles.Singleton import Singleton
import unidecode


#=============================================================================================
class JsonHelper (metaclass=Singleton):

    #------------------------------------------------------------------------------------------
    def __init__(self):
        
        pass

    #------------------------------------------------------------------------------------------
    def find(self, d, path, default=''):
        keys = path.split('.')
        rv = d
        for key in keys:
            if not rv or key not in rv:
                return default
            rv = rv[key]
        return rv

    #------------------------------------------------------------------------------------------
    def set(self, d, path, valor):
        keys = path.split('.')
        rv = d
        for key in keys:
            if not rv or key not in rv:
                rv[key] = {}
            rv = rv[key]
        rv = valor
    
    #------------------------------------------------------------------------------------------
    def to_json(self, d, attr=None):

        try:

            if attr and hasattr(d, attr):
                d = getattr(d, attr)
            if not d:
                return {} 
            if isinstance(d, dict):
                return d
            if isinstance(d, str):
                return json.loads(d)
            if isinstance(d, bytes):
                return json.loads(d.decode('utf-8'))
            
            raise Exception('input invalido: %s' % (d))

        except Exception as exc:
            
            err = str(exc)
            IOSistema().PrintLine('(X) [to_json] ERROR: %s' % (err))
            return {}

    #------------------------------------------------------------------------------------------
    def to_json_from_qs(self, e):
        
        out_json = parse_qs(e)
        for (k, v) in out_json.items():
            out_json[k] = unidecode.unidecode(v[0] if v else '')
            
        return out_json

    #------------------------------------------------------------------------------------------
    def to_string(self, d, attr=None, ret=False):

        try:
            out_json = JsonHelper().to_json(d, attr)
            texto = json.dumps(out_json, indent=4, sort_keys=True)
        except Exception as exc:
            IOSistema().PrintLine('(X) [to_string] ERROR: %s' % (str(exc)))
            texto = str(d)
        finally:
            if ret:
                return texto
            else:
                IOSistema().PrintLine(texto)

    #------------------------------------------------------------------------------------------
    def to_markdown(self, d, ret=False, nivel=0, lista=False):

        try:
            texto = ''
            espacios_gap = 2
            if isinstance(d, str):
                texto += '%s%s\n' % (' ' * (nivel), d)
            elif isinstance(d, list):
                for e in d:
                    texto += JsonHelper().to_markdown(e, ret, nivel+espacios_gap, lista=True)
            elif isinstance(d, dict):
                for (dic_k, dic_v) in d.items():
                    espacios = len(dic_k) - len(dic_k.lstrip())
                    texto += '%s%s: %s' % (' ' * (nivel), dic_k, '' if isinstance(dic_v, str) else '\n')
                    texto += JsonHelper().to_markdown(dic_v, ret, (nivel+espacios)+espacios_gap)
        except Exception as exc:
            IOSistema().PrintLine('(X) [to_markdown] ERROR: %s' % (str(exc)))
        finally:
            if ret:
                return texto
            else:
                IOSistema().PrintLine(texto)
