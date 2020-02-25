from __future__ import print_function

import datetime
import getpass
import glob
import os
import platform
import shutil
import subprocess
import sys
from threading import Lock
import traceback

from horno.datos.Encoding import Encoding
from horno.utiles.Singleton import Singleton


#==========================================================================================
class IOSistema (metaclass=Singleton):
    
    #------------------------------------------------------------------------------------------
    def __init__(self):
        self._en_linux = 'linux' in self.GetInfoSO().lower()
        self._en_py3 = sys.version_info > (3, 0)
        self._salida = None
        self._en_docker = False

        cgroup_file = '/proc/self/cgroup'
        if self._en_linux and os.path.exists(cgroup_file):
            with open(cgroup_file, 'r') as ior:
                for line in ior:
                    if 'docker' in line.strip().split('/'):
                        self._en_docker = True
                        break
        
    #------------------------------------------------------------------------------------------
    def Args(self):
        return sys.argv

    #------------------------------------------------------------------------------------------
    def SetearSalida(self, salida):
        self._salida = salida

    #------------------------------------------------------------------------------------------
    def Usuario(self):
        return getpass.getuser()

    #------------------------------------------------------------------------------------------
    def Input(self, msg, ask_once=False):
        while True:
            s = input('%s: ' % (msg))
            if s is not None and len(s.strip()) > 0:
                return s.strip()
            if ask_once:
                return ''

    #------------------------------------------------------------------------------------------
    def PrintLine(self, texto):
        if self._salida is None:
            try:
                print(texto)
            except:
                pass
        else:
            self._salida.PrintLine(texto)

    #------------------------------------------------------------------------------------------
    def Print(self, texto):
        if self._salida is None:
            try:
                print(texto, end='')
                sys.stdout.flush()
            except:
                pass
        else:
            self._salida.Print(texto)

    #------------------------------------------------------------------------------------------
    def Pausar(self):
        msg = 'Presione una tecla..'
        input('%s:' % (msg))

    #------------------------------------------------------------------------------------------
    def MostrarError(self, e):

        self.PrintLine(self.ObtenerError(e))

    #------------------------------------------------------------------------------------------
    def ObtenerError(self, e):
        
        error = '[EXCEPTION] ' + str(e)
        return error 

    #------------------------------------------------------------------------------------------
    def ObtenerUltimoError(self, ret=True):
        
        if ret:
            error = '[EXCEPTION LAST] ' + traceback.format_exc() 
            return error 
        else:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)
            del exc_info
            return None

    #------------------------------------------------------------------------------------------
    def MostrarTitulo(self, txt, sep='-'):
        self.PrintLine(sep * self.CharSep())
        self.PrintLine(txt)
        self.PrintLine(sep * self.CharSep())

    #------------------------------------------------------------------------------------------
    def CharSep(self):
        return 75

    #------------------------------------------------------------------------------------------
    def CheckSOEsLinux(self):
        return self._en_linux 

    #------------------------------------------------------------------------------------------
    def CheckPy3(self):
        return self._en_py3 

    #------------------------------------------------------------------------------------------
    def CheckDocker(self):
        return self._en_docker

    #------------------------------------------------------------------------------------------
    def GetInfoSO(self):
        arch = '64 bits' if platform.machine().endswith('64') else '32 bits'
        return '%s / %s %s [%s]' % (arch, platform.system(), platform.release(), ' '.join(platform.dist()).strip())

    #------------------------------------------------------------------------------------------
    def GetInfoJava(self, path):
        if os.system('"%s/java" -d64 -version > %s 2>&1' % (path, self.DevNull().Ruta())) == 0: return '64 bits'
        if os.system('"%s/java" -version > %s 2>&1' % (path, self.DevNull().Ruta())) == 0: return '32 bits'
        
        return '' 

    #------------------------------------------------------------------------------------------
    def TestMemJava(self, path, mem_min, mem_max):
        if not self.GetInfoJava(path): return False
        
        return os.system('"%s/java" -Xms%s -Xmx%s -version > %s 2>&1' % (path, mem_min, mem_max, self.DevNull().Ruta())) == 0

    #------------------------------------------------------------------------------------------
    def GetEnv(self, clave, default=None):
        return os.environ.get(clave, default)

    #------------------------------------------------------------------------------------------
    def SetEnv(self, clave, valor):
        os.environ[clave] = valor

    #------------------------------------------------------------------------------------------
    def DevNull(self):
        return IOArchivo('/dev/null' if IOSistema().CheckSOEsLinux() else 'nul')

    #------------------------------------------------------------------------------------------
    def NewLine(self):
        return '\n' if self._en_linux else '\r\n'

    #------------------------------------------------------------------------------------------
    def EjecutarEnSO(self, comandos, verbose=False, logueador=None, log_append=True):
        
        res = {'ok':True, 'salida':''}
        comandos_str = ' '.join(comandos)
        salida = ''
        ok = True
        
        try:
            if verbose:
                self.PrintLine('[comando in] %s' % (comandos_str))
            if self.CheckSOEsLinux() or len(comandos) == 1:
                salida = os.system(' '.join(comandos))
            else:
                salida = subprocess.check_output(comandos, shell=True, stderr=subprocess.STDOUT)
                #salida = subprocess.call(comandos)
                
        except subprocess.CalledProcessError as e:
            salida = e.output
            ok = False
        except OSError as e:
            salida = str(e)
            ok = False
            
        finally:
            res['ok'] = res['ok'] and ok
            res['salida'] = salida
            if verbose:
                IOSistema().PrintLine('[comando out] %s\n%s\n' % (ok, salida))            
            if logueador:
                fecha = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S")
                sep = '=' * self.CharSep()
                logueador.EscribirExpress((sep + '\n[FECHA]\n%s\n[COMANDO]\n%s\n' + sep + '\n[SALIDA]\n%s\n' + sep + '\n') % (fecha, comandos_str, salida), log_append, False)
                    
        return res


#==========================================================================================
class IOLector:
    
    #------------------------------------------------------------------------------------------
    def __init__(self, archivo):
        
        self.archivo = archivo
        self.handle = None
        self.lock_o = Lock()
        self.lock_w = Lock()

    #------------------------------------------------------------------------------------------
    @staticmethod
    def DeRuta(ruta):
        
        return IOLector(IOArchivo(ruta))

    #------------------------------------------------------------------------------------------
    def __enter__(self):
        
        return self

    #------------------------------------------------------------------------------------------
    def __exit__(self, tipo, valor, tb):
        
        self.Cerrar()

    #------------------------------------------------------------------------------------------
    def Stream(self):
        
        return self.handle

    #------------------------------------------------------------------------------------------
    def Abrir(self, binario=False, enc='utf-8'):
        
        self.handle = open(self.archivo.Ruta(), 'r' + ('b' if binario else ''), encoding=None if binario else enc)
        return self
        
    #------------------------------------------------------------------------------------------
    def Cerrar(self):
        
        self.handle.close()
        
    #------------------------------------------------------------------------------------------
    def Leer(self):
        
        if self.handle is None:
            IOSistema().PrintLine('(!) Error: el archivo %s no se ha abierto' % (self.ruta))
            return
        
        return self.handle.read()

    #------------------------------------------------------------------------------------------
    def LeerLinea(self):
        
        if self.handle is None:
            IOSistema().PrintLine('(!) Error: el archivo %s no se ha abierto' % (self.ruta))
            return
        
        return self.handle.readline()

#==========================================================================================
class IOEscritor:
    
    #------------------------------------------------------------------------------------------
    def __init__(self, archivo):
        
        self.archivo = archivo
        self.handle = None
        self.lock_o = Lock()
        self.lock_w = Lock()

    #------------------------------------------------------------------------------------------
    @staticmethod
    def DeRuta(ruta):
        
        return IOEscritor(IOArchivo(ruta))

    #------------------------------------------------------------------------------------------
    def __enter__(self):
        
        return self

    #------------------------------------------------------------------------------------------
    def __exit__(self, tipo, valor, tb):
        
        self.Cerrar()

    #------------------------------------------------------------------------------------------
    def Stream(self):
        
        return self.handle

    #------------------------------------------------------------------------------------------
    def EnBinario(self):
    
        return 'b' in self.handle.mode if self.handle else False    
    
    #------------------------------------------------------------------------------------------
    def Abrir(self, append=False, binario=False, enc='utf-8'):
        
        self.handle = open(self.archivo.Ruta(), ('a+' if append else 'w') + ('b' if binario else ''), encoding=None if binario else enc)
        return self
        
    #------------------------------------------------------------------------------------------
    def Cerrar(self):
        
        self.handle.close()
        
    #------------------------------------------------------------------------------------------
    def Escribir(self, msg, stdout=False, newline=False):

        if self.handle is None:
            IOSistema().PrintLine('(!) Error: el archivo %s no se ha abierto' % (self.ruta))
            return

        self.lock_w.acquire()

        msg = Encoding().NormalizarTexto(msg)
        if newline:
            msg = '%s%s' % (msg, IOSistema().NewLine())

        msg = bytes(msg, encoding='utf-8') if self.EnBinario() else msg
        self.handle.write(msg)
        if stdout:
            if newline:
                IOSistema().PrintLine(msg)
            else:               
                IOSistema().Print(msg)
                
        self.lock_w.release()               

    #------------------------------------------------------------------------------------------
    def EscribirLinea(self, msg, stdout=False):
        
        self.Escribir(msg, stdout, True)

    #------------------------------------------------------------------------------------------
    def EscribirExpress(self, msg, append=False, stdout=False):
        
        self.lock_o.acquire()
        
        self.Abrir(append)
        self.EscribirLinea(msg, stdout)
        self.Cerrar()

        self.lock_o.release()
        
#==========================================================================================
class IOArchivo:
    
    #------------------------------------------------------------------------------------------
    def __init__(self, ruta):
        self.ruta = ruta.replace('\\', '/')

    #------------------------------------------------------------------------------------------
    def __str__(self):
        return self.Ruta()

    #------------------------------------------------------------------------------------------
    def Ruta(self):
        return self.ruta

    #------------------------------------------------------------------------------------------
    def RutaEnSO(self):
        return self.ruta if IOSistema().CheckSOEsLinux() else self.ruta.replace('/', '\\')

    #------------------------------------------------------------------------------------------
    def Nombre(self):
        return self.ruta.split('/')[-1]

    #------------------------------------------------------------------------------------------
    def NombreSinExtension(self):
        return self.Nombre().rsplit('.', 1)[0]

    #------------------------------------------------------------------------------------------
    def Extension(self):
        return self.Nombre().split('.')[-1] if '.' in self.Nombre() else ''
    
    #------------------------------------------------------------------------------------------
    def UnirConArchivo(self, ruta_archivo):
        return IOArchivo(os.path.join(self.ruta, ruta_archivo))

    #------------------------------------------------------------------------------------------
    def ConExtension(self, extension):
        return IOArchivo('%s.%s' % (self.ruta.rsplit('.', 1)[0], extension))

    #------------------------------------------------------------------------------------------
    def CarpetaPadre(self):
        return IOCarpeta(self.ruta.rsplit('/', 1)[0])

    #------------------------------------------------------------------------------------------
    def BuscarPorRuta(self):
        return glob.glob(self.ruta)

    #------------------------------------------------------------------------------------------
    def Renombrar(self, ruta_nueva):
        ruta_nueva = ruta_nueva.replace('\\', '/')
        os.rename(self.ruta, ruta_nueva)
        self.ruta = ruta_nueva

    #------------------------------------------------------------------------------------------
    def Existe(self):
        return os.path.exists(self.ruta) and os.path.isfile(self.ruta)

    #------------------------------------------------------------------------------------------
    def CantidadLineas(self):
        if not self.Existe():
            return 0
        
        with IOLector(self).Abrir(binario=True) as io:
            for i, _ in enumerate(io.Stream()): pass
        return i + 1

    #------------------------------------------------------------------------------------------
    def Eliminar(self):
        try:
            if self.Existe():
                os.remove(self.ruta)
        except:
            IOSistema().PrintLine('(!) Error: el archivo %s no se ha borrado' % (self.ruta))
            
    #------------------------------------------------------------------------------------------
    def Copiar(self, ruta_hasta):
        shutil.copyfile(self.ruta, ruta_hasta)

    #------------------------------------------------------------------------------------------
    @staticmethod
    def FormatearANombreValido(texto):
        res = texto
        for s in ['/', '\\', '.']:
            res = res.replace(s, '_')
        return res

    #------------------------------------------------------------------------------------------
    @staticmethod
    def PathFix(path):
        return path.replace('\\', '/') if IOSistema().CheckSOEsLinux() else path.replace('/', '\\')
    
    #------------------------------------------------------------------------------------------
    def RepararEncoding(self, normalizar=False):

        with IOLector(self).Abrir(binario=True) as ior:
            datos = ior.Leer()

        #volar caracteres nulos
        datos = datos.replace('\x00', '')

        #volar prefijos unicode que joden
        boms = [ '\xef\xbb\xbf', '\xfe\xff', '\xff\xfe', '\x00\x00\xff\xfe', '\xff\xfe\x00\x00' ]
        for bom in boms:
            if datos.startswith(bom):
                datos = datos[len(bom):]

        #volar strings unicode que joden
        ustrs = [ '\xef\xbf\xbd' ]
        for ustr in ustrs:
            datos = datos.replace(ustr, '<?>')

        #normalizar caracteres extendidos
        if normalizar:
            datos = Encoding().NormalizarTexto(datos)
        
        with IOEscritor(self).Abrir(False) as iow:
            iow.Escribir(datos)
    
#==========================================================================================
class IOCarpeta(IOArchivo):
    
    #------------------------------------------------------------------------------------------
    def __init__(self, ruta):
        self.ruta = ruta.replace('\\', '/')
    
    #------------------------------------------------------------------------------------------
    def Escritor(self):
        raise Exception('Funcion no implementada')
    
    #------------------------------------------------------------------------------------------
    def GetContenido(self):
        return os.listdir(self.ruta) if self.Existe() else []
  
    #------------------------------------------------------------------------------------------
    def UnirConCarpeta(self, ruta_carpeta):
        return IOCarpeta(os.path.join(self.ruta, ruta_carpeta))

    #------------------------------------------------------------------------------------------
    def Existe(self):
        return os.path.exists(self.ruta) and os.path.isdir(self.ruta)
    
    #------------------------------------------------------------------------------------------
    def Crear(self):
        if not self.Existe():
            os.makedirs(self.ruta)
    
    #------------------------------------------------------------------------------------------
    def Eliminar(self):
        try:
            if self.Existe():
                shutil.rmtree(self.ruta)
        except:
            IOSistema().PrintLine('(!) Error: la carpeta %s no se ha borrado' % (self.ruta))
