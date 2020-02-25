from horno.datos.Encoding import Encoding
from horno.utiles.IO import IOSistema
from horno.utiles.Singleton import Singleton
import html
import re


#==============================================================================================
class HtmlHelper (metaclass=Singleton):
    
    #------------------------------------------------------------------------------------------
    def UnescapearTexto(self, texto):
                        
        return html.unescape(texto)
        
    #------------------------------------------------------------------------------------------
    def CargarUrl(self, url):

        from lxml import etree, html
        from urllib import request

        url_partes = url.split('://', 2)
        url = '%s://%s' % (url_partes[0], url_partes[-1].replace('//', '/'))

        req = request.Request(url, headers={'User-Agent' : "Magic Browser"})
        page_content = request.urlopen(req).read()
        page_content = re.sub(b'\<\!\[CDATA\[(.+)\]\]\>', br'\1', page_content)
        page_elem = html.fromstring(page_content)
        
        #parser = etree.XMLParser(strip_cdata=False)
        #page_elem = etree.XML(page_content, parser)
        
        return page_elem

    #------------------------------------------------------------------------------------------
    def ElemToString(self, elem):
        
        from lxml import etree
        
        inner_html = etree.tostring(elem)
        return inner_html        

    #------------------------------------------------------------------------------------------
    def XPathSafeText(self, elem, paths, default=''):
        
        try:
            if type(elem) in [str, bytes] or any([t in str(type(elem)) for t in ['_ElementStringResult', '_ElementUnicodeResult']]): 
                return Encoding().NormalizarTexto(elem)
            if not type(paths) == list: 
                paths = [paths]
            for path in paths:
                res = elem.xpath(path)
                if not res: continue
                txt = Encoding().NormalizarTexto(res[0]).strip()
                if not txt: continue
                return txt
            return default
        except Exception as e:
            IOSistema().PrintLine(e)
            return '[ERROR-xpathtext]'

    #------------------------------------------------------------------------------------------
    def XPathSafeProp(self, elem, path, prop, default=''):

        try:
            res = elem.xpath(path)
            if not res: return default
            txt = Encoding().NormalizarTexto(res[0].get(prop))
            return txt
        except Exception as e:
            IOSistema().PrintLine(e)
            return '[ERROR-xpathprop]'
        


#==============================================================================================
class UrlHelper ():
    
    #------------------------------------------------------------------------------------------
    def __init__(self, url, url_rel=''):
        
        from urllib.parse import urlparse
        
        self.url_data = urlparse(url)
        self.esquema = self.url_data.scheme or 'http'
        self.hostpuerto = self.url_data.netloc or '.'
        self.host = self.url_data.hostname or '.'
        self.ruta = self.url_data.path
        self.puerto = self.url_data.port
        self.params = self.url_data.params
        self.query = self.url_data.query
        
        if url_rel and self.host == '.':
            url_data_rel = urlparse(url_rel)
            self.esquema = url_data_rel.scheme or 'http'
            self.hostpuerto = url_data_rel.netloc or '.'
            self.host = url_data_rel.hostname or '.'
            self.puerto = url_data_rel.port
            if not self.ruta.startswith('/'):
                self.ruta = '%s/%s' % (url_data_rel.path, self.url_data.path)
        
        self.ruta = self.ruta.replace('//', '/') 

    #------------------------------------------------------------------------------------------
    def __str__(self):
        
        return self.full_path()

    #------------------------------------------------------------------------------------------
    def full_path(self):

        url_link_ok = '%s://%s/%s%s' % (
            self.esquema, 
            self.hostpuerto,
            self.ruta,
            '?%s' % (self.query) if self.query else ''
        )
        return url_link_ok

    #------------------------------------------------------------------------------------------
    def prev_path(self):
        
        path = self.full_path()
        path_partes = path.rsplit('/', 1)
        return path_partes[0] if '.' in path_partes[-1] else path
