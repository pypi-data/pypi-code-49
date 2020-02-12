from __future__ import print_function
import requests
import cfscrape
from bs4 import BeautifulSoup as bs
import argparse
import sys
import re
import clipboard
import platform
if platform.uname()[0] == 'Windows':
    import cmdw
    from idm import IDMan
#import vping
import pywget
import os
pid = os.getpid()
import traceback
# import tracert
import termcolor
from make_colors import make_colors
#import random
import time
if sys.version_info.major == 3:
    import urllib.parse
else:
    import urlparse
    class urllib:
        def parse(self):
            pass
    urllib.parse = urlparse
    input = raw_input
from pydebugger.debug import debug
import configset
#import threading
try:
    import __init__
    __version__ = __init__.__version__
    __test__ = __init__.__test__
    __build__ = __init__.__build__
    __platform__ = __init__.__platform__
    __email__ = __init__.__email__
except:
    pass
import cmdw
MAX = cmdw.getWidth()
MAX_TRY = 10
# EXIT=False
# NAME = ""
# url_result = ""
import traceback
from zippyshare_generator import zippyshare

ALL_SITES = ['drive.google', 'siotong', 'zonawibu', 'anonfile', 'isengsub', 'link.safelinkconverter', 'link.safelinkconverter.com']

class autogeneratelink(object):

    def __init__(self, link=None, proxy = None):
        super(autogeneratelink, self)
        self.link = link
        self.url = 'http://www.autogeneratelink.info/link.php'
        self.debug = False
        self.proxy = {}
        self.header = {}
        self.auto = False
        self.try_count = 0
        self.percent = 0
        self.thread = None
        self.MEMCACHED = False
        self.MEMCACHED_HOST = ''
        self.MEMCACHED_PORT = ''
        self.CONFIG = configset.configset()
        self.CONFIG.configname = os.path.join(os.path.dirname(__file__), 'aglink.ini')
        self.cf = cfscrape.create_scraper()
        #if vping.vping(urllib.parse.urlparse(self.url).netloc.split('www.')[1]):
            #pass
        #else:
            #print(make_colors("No Internet Connection !!!", 'yellow', attrs= ['blink']))
            #return
        self.choices = ['red', 'yellow', 'cyan', 'green', 'white', 'blue', 'magenta']
        self.set_memcached({'percent': 0, 'name': '', 'link': '',})
        if self.CONFIG.read_config('PROXY', 'server') and self.CONFIG.read_config('PROXY', 'port'):
            self.proxy.update(
                {
                    'http': 'http://%s:%s'%(self.CONFIG.read_config('PROXY', 'server'), self.CONFIG.read_config('PROXY', 'port')),
                    'https': 'https://%s:%s'%(self.CONFIG.read_config('PROXY', 'server'), self.CONFIG.read_config('PROXY', 'port'))
                })

    def test_proxy(self):
        if self.proxy:
            try:
                a = requests.request('GET', self.url, timeout=5, proxies=self.proxy)
                print("STATUS:", a.status_code)
            except:
                if os.getenv('DEBUG'):
                    traceback.format_exc()
                check_proxy = urllib.parse.urlparse(self.proxy.get('http')).netloc
                print(make_colors('Checking proxy for: ', 'lightyellow') + make_colors("%s"%(check_proxy), 'black', 'lightcyan') + " " + make_colors("ERROR", 'lightwhite', 'lightred'))

    def set_memcached(self, dict_data, host = '127.0.0.1', port = '11211', debug = 0):
        if self.MEMCACHED_HOST:
            host = self.MEMCACHED_HOST
        if self.MEMCACHED_PORT:
            port = self.MEMCACHED_PORT
        try:
            import memcache
            mc = memcache.Client([host + ":" + port], debug = debug)
            for i in dict_data:
                mc.set(i, dict_data.get(i))
        except ImportError:
            print("memcache not installed !")
            return False

    def get_memcached(self, key, host = '127.0.0.1', port = '11211', debug = 0):
        values = []
        if self.MEMCACHED_HOST:
            host = self.MEMCACHED_HOST
        if self.MEMCACHED_PORT:
            port = self.MEMCACHED_PORT
        try:
            import memcache
            mc = memcache.Client([host + ":" + port], debug = debug)
            if isinstance(key, list) or isinstance(key, tuple):
                for i in key:
                    value = mc.get(i)
                    values.append(value)
            else:
                values = mc.get(key)
            return values

        except ImportError:
            print("memcache not installed !")
            return False

    def percent_memcached(self, percent, host = '127.0.0.1', port = '11211', debug = 0):
        if self.MEMCACHED_HOST:
            host = self.MEMCACHED_HOST
        if self.MEMCACHED_PORT:
            port = self.MEMCACHED_PORT
        try:
            import memcache
            mc = memcache.Client([host + ":" + port], debug = debug)
            mc.set('agl_percent', percent)
        except ImportError:
            print("memcache not installed !")
            return False
    def get_percent_memcached(self, host = '127.0.0.1', port = '11211', debug = 0):
        if self.MEMCACHED_HOST:
            host = self.MEMCACHED_HOST
        if self.MEMCACHED_PORT:
            port = self.MEMCACHED_PORT
        try:
            import memcache
            mc = memcache.Client([host + ":" + port], debug = debug)
            percent = mc.get('agl_percent')
            return percent
        except ImportError:
            print("memcache not installed !")
            return False

    def percent_progress(self, percent, memcached = False):
        #print "memcache =", memcached
        #debug(memcached = memcached)
        if not self.percent >= 100:
            self.percent = percent
        if memcached:
            if self.MEMCACHED:
                self.percent_memcached(percent)
        else:
            if self.MEMCACHED:
                self.percent_memcached(percent)
        #print "percent =", percent
        return self.percent

    def getVersion(self, ):
        try:
            return __version__ + "." + __test__
        except:
            pass

    def cek_error(self, c, respon=None):
        try:
            if c == 'Never Give Up ! Generate again and try it up to 10x Generate Link !':
                # print termcolor.colored('Never Give Up ! Generate again and try it up to 10x Generate Link !', 'red', 'on_yellow', attrs= ['bold', 'blink'])
                print(make_colors('Never Give Up ! Generate again and try it up to 10x Generate Link !', 'red', 'on_yellow', attrs= ['bold', 'blink']))
                return True, 'Never Give Up ! Generate again and try it up to 10x Generate Link !'
            elif c == 'Link Dead! or Host is temporarily down! Generate again after 5 minutes!':
                # print termcolor.colored('Link Dead! or Host is temporarily down! Generate again after 5 minutes!', 'white', 'on_red', attrs= ['bold', 'blink'])
                print(make_colors('Link Dead! or Host is temporarily down! Generate again after 5 minutes!', 'white', 'on_red', attrs= ['bold', 'blink']))
                return True, 'Link Dead! or Host is temporarily down! Generate again after 5 minutes!'
            elif c == 'Link Dead!':
                # print termcolor.colored('Link Dead! or Host is temporarily down! Generate again after 5 minutes!', 'white', 'on_red', attrs= ['bold', 'blink'])
                print(make_colors('Link Dead! or Host is temporarily down! Generate again after 5 minutes!', 'white', 'on_red', attrs= ['bold', 'blink']))
                return True, 'Link Dead! or Host is temporarily down! Generate again after 5 minutes!'
            elif c == 'Generate Failed!':
                if respon:
                    if len(respon) == 2:
                        # print termcolor.colored('Generate Failed!', 'white', 'on_red', attrs= ['bold', 'blink']) + termcolor.colored(' ', 'white') + termcolor.colored('~', 'yellow') + termcolor.colored(' ', 'white') + termcolor.colored(respon[0], 'yellow') + termcolor.colored(' ', 'white') + termcolor.colored('~', 'yellow')  + termcolor.colored(' ', 'white') + termcolor.colored(respon[1], 'cyan')
                        print(make_colors('Generate Failed!', 'white', 'on_red', attrs= ['bold', 'blink']) + make_colors(' ', 'white') + make_colors('~', 'yellow') + make_colors(' ', 'white') + make_colors(respon[0], 'yellow') + make_colors(' ', 'white') + make_colors('~', 'yellow')  + make_colors(' ', 'white') + make_colors(respon[1], 'cyan'))
                    elif len(respon) == 1 :
                        # print termcolor.colored('Generate Failed!', 'white', 'on_red', attrs= ['bold', 'blink']) + termcolor.colored(' ', 'white') + termcolor.colored('~', 'yellow') + termcolor.colored(' ', 'white') + termcolor.colored(respon[0], 'yellow')
                        print(make_colors('Generate Failed!', 'white', 'on_red', attrs= ['bold', 'blink']) + make_colors(' ', 'white') + make_colors('~', 'yellow') + make_colors(' ', 'white') + make_colors(respon[0], 'yellow'))
                return True, 'Generate Failed!'
            else:
                return False, ''
        except:
            if debug.DEBUG:
                traceback.format_exc()
            return False, ''
        return False, ''

    def get_req(self, link, headers = {}, proxy = {}):
        '''
            set corrent generate url
            parameter:
                link: (str) url
                proxy: (instance) ~ return of setProxy()
            return: (str) ~ requests.content
        '''
        debug()
        if not proxy:
            proxy = self.proxy
        debug(proxy=proxy)
        # print "proxy 0       =", proxy
        # print "type(proxy 0) =", type(proxy)
        if isinstance(proxy, dict):
            proxy_list = []
            for i in proxy:
                # print "i =",i
                # print "proxy.get(i) =", proxy.get(i)
                proxy_list.append(proxy.get(i))
            proxy = proxy_list

        # print "proxy 1 =", proxy
        # global EXIT
        name = ""
        url_result = ""
        nx = 1
        while 1:
            try:
                proxy_1 = {}
                status_code = requests.request('GET', self.url, timeout=5, proxies=proxy_1).status_code
                # if nx >= 1:
                #     print "\n"
                break
            except:
                time.sleep(1)
                sys.stdout.write(".")
                nx += 1
                proxy_1 = self.setProxy(proxy)
        debug(status_code=status_code)
        if status_code  == 200:
            proxy = {}
        else:
            proxy = self.setProxy(proxy)
        debug(print_function_parameters= True)
        params = {
            'link': link,
            'token': 'agl',
        }

        debug(params = params)

        r = None
        c_connect = 0
        c = None
        error = ''
        while 1:
            try:
                r = requests.get(self.url, params= params, proxies=proxy)
                debug(r_url = r.url)
                # print "\n"
                break
            except:
                if c_connect == 0:
                    print("connecting .")
                    c_connect = 1
                sys.stdout.write("+")
                if os.getenv('DEBUG') == '1':
                    traceback.format_exc()
        if r:
            debug(r_text=r.text)
            b = bs(r.text, 'lxml')
            debug(b = b)
        else:
            print(make_colors("FATAL CONNECTION !", 'white', 'red', ['blink', 'bold']))
            sys.exit(0)

        try:
            respon = re.split(" ", b.text)
            for i in respon:
                if str(i).strip() == '':
                    respon.remove(i)
            if respon[1] == '//':
                name = respon[0]
            debug(respon=respon)
            debug(respon_0=respon[0])
            if len(respon) > 1:
                debug(respon_1=respon[1])
                if len(respon) > 2:
                    debug(respon_2=respon[2])
            respon1 = re.findall(r'(https?://[^\s]+)', respon[2])
            if len(respon1) > 1:
                respon1 = respon1[0]
            if respon1:
                url_result = respon1
            debug(respon1=respon1)
            respon2 = re.split(" ", respon[0])
            debug(respon2=respon2)
            if respon1 in respon2:
                respon2.remove(respon1)
            respon2 = " ".join(respon2)
            debug(respon2=respon2)
            respon_send = [respon2, respon1]
            # respon_send = [respon[0], respon1]

            c =  b.find('b').text
            debug(c = c)
            error = self.cek_error(c, respon=respon_send)
            debug(error = error)
            # if error[0]:
            #     EXIT = True
            #     debug(EXIT=EXIT)
        except:
            if os.getenv('DEBUG_EXTRA'):
                traceback.format_exc()
            else:
                traceback.format_exc(print_msg=False)
        debug(r=r)
        debug(error=error)
        # debug(EXIT=EXIT)
        if r.status_code == 200:
            # if EXIT:
            #     return False, False, error
            if error and len(error) > 1:
                debug(error=error)
                debug(error_0=error[0])
                if error[0] == True:
                    debug("error_0_False")
                    return False, False, error

            debug(url_result=url_result)
            if not url_result:
                try:
                    c = b.find('a', target = re.compile('blank')).get('href')
                    debug(c = c)
                except:
                    c = None
                    traceback.format_exc(print_msg = False)
            else:
                c = url_result
            debug(c=c)
            if not name:
                try:
                    name = b.find('b').text.split('//')[0].strip()
                    self.percent_progress(50, self.MEMCACHED)
                except:
                    if os.getenv('DEBUG_EXTRA'):
                        traceback.format_exc()
                    name = None
            else:
                if error and len(error) > 1:
                    if error[0]:
                        name = None
            debug(name = name)
            self.percent_progress(70, self.MEMCACHED)
            if not name:
                return c, None, error
            else:
                return c, name.encode('utf-8'), error
        else:
            return None, None, error

    def support(self, proxy = None):
        if not proxy:
            proxy = self.proxy
        g = requests.get(self.url, proxies = proxy)
        s = bs(g.text, 'lxml')
        b = s.find('textarea', {'class': 'form-control'})
        return b.get('placeholder')

    def download(self, url, path = ".", output = None, referrer = None, postdata = None, cookies = None, username = None, password = None, confirm = False, wget = False):
        path = os.path.abspath(path)
        if os.path.isfile(path):
            path = os.path.dirname(path)
            output = os.path.basename(path)
        if 'win' in sys.platform:
            try:
                import idm
                IDM = idm.IDMan()
                IDM.download(url, path, output)
            except:
                traceback.format_exc()
                filename = pywget.download(url, path)
                return filename
        elif wget:
            filename = pywget.download(url, path)
            return filename
        else:
            filename = pywget.download(url, path)
            return filename

    def generate(self, link, clip=None, quality=None, verbosity=None, support= False, direct_download=None, download_path=".", pcloud = False, pcloud_username = None, pcloud_password = None, pcloud_folderid = '0', pcloud_rename = None, pcloud_foldername = None, proxy = None, fast = False, bypass_regenerate = False, cliped = False, name = None, wget = False, show_debug = False, no_return=False, use_proxy=False, auto=False):
        global ALL_SITES
        if show_debug:
            os.environ.update({'DEBUG':'1'})
        if not os.path.isdir(download_path):
            os.makedirs(download_path)
        if show_debug:
            debug.DEBUG = 1
        if pcloud_rename and not name:
            name = pcloud_rename
        if name and not pcloud_rename:
            pcloud_rename = name
        debug(link0 = link)
        if cliped:
            link = clipboard.paste()
        debug(link1 = link)
        choices = ['red', 'yellow', 'cyan', 'green', 'white', 'blue', 'magenta']
        if not proxy:
            proxy = self.proxy
        if support:
            print("\n")
            print(self.support())
            print("\n")

        if link == None:
            if self.link == None:
                return False, None
            else:
                pass

        if 'youtu' in link:
            self.youtube(link, direct_download, download_path, True, pcloud, pcloud_username, pcloud_password, pcloud_folderid, pcloud_rename, pcloud_foldername)
        else:
            debug(link2 = link)
            #print "self.get_netloc(link) =", self.get_netloc(link)
            if self.get_netloc(link) == 'siotong' or self.get_netloc(link) == 'coeg' or self.get_netloc(link) == 'telondasmu' or self.get_netloc(link) == 'siherp' or self.get_netloc(link) == 'greget' or self.get_netloc(link) == 'tetew' or self.get_netloc(link) == 'anjay':
                link = self.siotong(link)
                debug(link = link)
            elif self.get_netloc(link) == 'zonawibu':
                link = self.zonawibu(link)
            elif self.get_netloc(link) == 'anonfile':
                debug(netlock = self.get_netloc(link))
                link = self.anonfile(link)
                return True
            elif self.get_netloc(link) == 'isengsub':
                link = self.isengsub(link)
            elif self.get_netloc(link) == 'mediafire':
                link = self.mediafire(link)
            elif 'zippyshare' in link.split(".")[1]:
                try:
                    self.zippyshare(link, name, download_path)
                    return True
                except:
                    traceback.format_exc()
                    return False
            elif 'anonfile' in link.split(".")[1]:
                self.anonfile(url, True, download_path, name, pcloud, pcloud_username, pcloud_password, name, pcloud_folderid, pcloud_foldername, direct_download, use_proxy, self.proxy)
            elif 'googleapis' in link.split(".")[1]:
                try:
                    self.googleapis(link, name, download_path)
                    return True
                except:
                    traceback.format_exc()
                    return False
                
            elif urllib.parse.urlparse(link).netloc == 'link.safelinkconverter.com':
                link = self.safelinkconverter(link)
            elif urllib.parse.urlparse(link).netloc == 'ourabeauty.info':
                link = self.ourabeauty(link)
            else:
                self.percent_progress(30, self.MEMCACHED)
            if self.get_netloc(link) in ALL_SITES:
                print("Re:Generate [ALL_SITES] ...")
                return self.generate(link, clip, quality, verbosity, support, direct_download, download_path, pcloud, pcloud_username, pcloud_password, pcloud_folderid, pcloud_rename, pcloud_foldername, proxy, fast, bypass_regenerate, cliped, name, wget, show_debug, no_return)
            if not self.get_netloc(link) == 'anonfile' and not self.get_netloc(link) == 'isengsub' and not 'mediafire' in link:
                a, out_name, error = self.get_req(link)
            else:
                if clip:
                    clipboard.copy(str(link))
                if direct_download and not pcloud:
                    try:
                        self.percent_progress(99, self.MEMCACHED)
                        idm = IDMan()
                        idm.download(link, download_path)
                        self.percent_progress(100, self.MEMCACHED)
                    except:
                        self.percent_progress(99, self.MEMCACHED)
                        pywget.download(link, out= download_path)
                        self.percent_progress(100, self.MEMCACHED)
                elif direct_download and pcloud:
                    if os.path.isfile(download_path):
                        download_path = os.path.dirname(download_path)
                        name = os.path.basename(download_path)
                    else:
                        name = None
                    print(make_colors('Upload to PCloud and download it...', 'white', 'magenta'))
                    self.pcloud(link, pcloud_username, pcloud_password, name, pcloud_folderid, pcloud_foldername, direct_download, download_path, use_proxy, proxy = self.proxy)
                elif pcloud and not direct_download:
                    print(make_colors('Upload to PCloud and download it...', 'white', 'blue'))
                    self.pcloud(link, pcloud_username, pcloud_password, name, pcloud_folderid, pcloud_foldername, direct_download, download_path, use_proxy)
                print(make_colors('RESULT GENERATED:', 'lightwhite', 'lightmagenta') + " " + make_colors(link, 'lightgreen'))
                return link
            debug(a = a)
            debug(out_name = out_name)
            if out_name and not isinstance(out_name, bool):
                if out_name.strip() == "[Attention] File too big! when allowed only 1.1 Gb on Mega.co.nz ! (Because our server disconnect after 1,1Gb)":
                        error = True, "[Attention] File too big! when allowed only 1.1 Gb on Mega.co.nz ! (Because our server disconnect after 1,1Gb)"
            debug(error=error)
            # print "error =", error
            if isinstance(error, tuple) or isinstance(error, list):
                if error[0]:
                    debug('ERROR 001')
                    if auto:
                        return self.generate(link, clip, quality, verbosity, support, direct_download, download_path, pcloud, pcloud_username, pcloud_password, pcloud_folderid, pcloud_rename, pcloud_foldername, proxy, fast, bypass_regenerate, cliped, name, wget, show_debug, no_return, use_proxy, auto)
                    elif self.auto:
                        return self.generate(link, clip, quality, verbosity, support, direct_download, download_path, pcloud, pcloud_username, pcloud_password, pcloud_folderid, pcloud_rename, pcloud_foldername, proxy, fast, bypass_regenerate, cliped, name, wget, show_debug, no_return, use_proxy, self.auto)
                    q_err = input(make_colors("Re:Generate [y/n/a]: "))
                    if q_err.lower() == 'y':
                        return self.generate(link, clip, quality, verbosity, support, direct_download, download_path, pcloud, pcloud_username, pcloud_password, pcloud_folderid, pcloud_rename, pcloud_foldername, proxy, fast, bypass_regenerate, cliped, name, wget, show_debug, no_return, use_proxy, auto)
                    elif q_err.lower() == 'a':
                        return self.generate(link, clip, quality, verbosity, support, direct_download, download_path, pcloud, pcloud_username, pcloud_password, pcloud_folderid, pcloud_rename, pcloud_foldername, proxy, fast, bypass_regenerate, cliped, name, wget, show_debug, no_return, use_proxy, True)
                    else:
                        try:
                            return error[1]
                        except:
                            return False

            if isinstance(a, list):
                debug(a=a)
                if not len(a[0]) > 5:
                    print(make_colors(name, 'white', 'red', ['blink']))
                    qr = input(make_colors('Re-Generate again', 'white', 'blue') + " " + make_colors('[Y/N]', 'white', 'red') + ': ')
                    if str(qr).lower() == 'n':
                        self.percent_progress(100, self.MEMCACHED)
                        sys.exit(0)
                    elif str(qr).lower() == 'y':
                        self.percent_progress(0, self.MEMCACHED)
                        return self.generate(link, clip, quality, verbosity, support, direct_download, download_path, pcloud, pcloud_username, pcloud_password, pcloud_folderid, pcloud_rename, pcloud_foldername, proxy, fast)
                    else:
                        self.percent_progress(100, self.MEMCACHED)
                        sys.exit('SAVE EXIT')

            if out_name == 'Never Give Up ! Generate again and try it up to 10x Generate Link !' or a == 'Never Give Up ! Generate again and try it up to 10x Generate Link !' or error == 'Never Give Up ! Generate again and try it up to 10x Generate Link !':
                if bypass_regenerate:
                    return a, out_name
                else:
                    qr = input(make_colors('Re-Generate again', 'white', 'blue') + " " + make_colors('[Y/N]', 'white', 'red') + ': ')
                    if str(qr).lower() == 'n':
                        self.percent_progress(100, self.MEMCACHED)
                        sys.exit(0)
                    elif str(qr).lower() == 'y':
                        self.percent_progress(0, self.MEMCACHED)
                        return self.generate(link, clip, quality, verbosity, support, direct_download, download_path, pcloud, pcloud_username, pcloud_password, pcloud_folderid, pcloud_rename, pcloud_foldername, proxy, fast)
                    else:
                        self.percent_progress(100, self.MEMCACHED)
                        sys.exit('SAVE EXIT')
            # print "a =", a
            if a:
                if isinstance(a, list):
                    a = a[0]
                debug(a=a)
                filename = None
                disposition = None
                try:
                    disposition = requests.request('GET', a, stream=True, proxies=proxy, timeout=10).headers.get('Content-Disposition')
                except:
                    pass
                if disposition:
                    filename = disposition.split('attachment; filename=')
                    debug(filename=filename, debug = self.debug)
                    if len(filename) > 1:
                        filename = filename[1]
                    filename = str(filename).replace('AutoGenerateLink_%5', '')
                    filename = str(filename).replace('AutoGenerateLink_', '')
                    filename = str(filename).replace('www.gigapurbalingga.net%5d', '')
                    filename = str(filename).replace('www.gigapurbalingga.net', '')
                    filename = str(filename).replace('-SAMEHADAKU.TV', '')
                    filename = str(filename).replace('-samehadaku.tv', '')
                    filename = str(filename).replace('b_', '')
                    debug(filenamex=filename)
                if filename:
                    name = filename
                    out_name = filename
                self.percent_progress(90, self.MEMCACHED)
                debug(name=name)
                if not name:
                    if out_name:
                        name = out_name
                    else:
                        name = ''
                name = os.path.basename(name)
                if "['attachment;filename=" in name:
                    name = re.sub("\"|\['attachment;filename=|'\]", '', name)
                # if not os.path.isdir(download_path):
                #     download_path, name = os.path.split(download_path)
                #     out_name = name
                # print termcolor.colored('GENERATED         : ', 'white', 'on_red') + termcolor.colored(a, 'white', 'on_red')
                print(make_colors('GENERATED         : ', 'white', 'on_red') + make_colors(a, 'white', 'on_red'))
                # print termcolor.colored('NAME              : ', 'white', 'on_green') + termcolor.colored(out_name, 'white', 'on_blue')
                print(make_colors('NAME              : ', 'white', 'on_green') + make_colors(out_name, 'white', 'on_blue'))
                # print termcolor.colored('DOWNLOAD NAME     : ', 'white', 'on_cyan') + termcolor.colored(name, 'white', 'on_blue')
                print(make_colors('DOWNLOAD NAME     : ', 'white', 'on_cyan') + make_colors(name, 'white', 'on_blue'))
                if out_name == 'Generate Failed!':
                    self.percent_progress(100, self.MEMCACHED)
                    sys.exit('FAILED!')
                # if not name:
                #     name = out_name
                # if name:
                #     name = os.path.basename(name)
                if pcloud and not direct_download:
                    if os.path.isfile(download_path):
                        download_path = os.path.dirname(download_path)
                        name = os.path.basename(download_path)
                    print(make_colors('Upload to PCloud ...', 'white', 'magenta'))
                    if show_debug:
                        try:
                            os.environ.pop('DEBUG')
                        except:
                            pass
                    self.pcloud(a, pcloud_username, pcloud_password, name, pcloud_folderid, pcloud_foldername, False, download_path, use_proxy)
                if pcloud and direct_download:
                    if os.path.isfile(download_path):
                        download_path = os.path.dirname(download_path)
                        name = os.path.basename(download_path)
                    print(make_colors('Upload to PCloud and download it...', 'white', 'magenta'))
                    if show_debug:
                        try:
                            os.environ.pop('DEBUG')
                        except:
                            pass
                    self.pcloud(a, pcloud_username, pcloud_password, name, pcloud_folderid, pcloud_foldername, direct_download, download_path, use_proxy, proxy= self.proxy)
                if clip:
                    self.percent_progress(92, self.MEMCACHED)
                    if name:
                        clipboard.copy(str(name))
                    if a:
                        clipboard.copy(str(a))
                    self.percent_progress(100, self.MEMCACHED)
                if direct_download and not pcloud:
                    self.percent_progress(95, self.MEMCACHED)
                    if os.path.isfile(download_path):
                        download_path = os.path.dirname(download_path)
                        name = os.path.basename(download_path)
                    dict_data = {
                        'name': name,
                        'link': a,
                    }
                    self.set_memcached(dict_data)
                    print(make_colors('Download it...', 'white', 'blue'))
                    #filename = pywget.download(a.get('href'), download_path)
                    #if 'youtu' in link:
                        #name = self.download(str(youtube_list.get(int(q))), download_path, wget = wget)
                    try:
                        self.percent_progress(99, self.MEMCACHED)
                        idm = IDMan()
                        idm.download(a, download_path, name)
                        self.percent_progress(100, self.MEMCACHED)
                    except:
                        self.percent_progress(99, self.MEMCACHED)
                        pywget.download(a, out= os.path.join(download_path, name))
                        self.percent_progress(100, self.MEMCACHED)
                    return a, name
                self.percent_progress(100, self.MEMCACHED)
                dict_data = {
                    'name': name,
                    'link': a,
                }
                self.set_memcached(dict_data)
                if show_debug:
                    try:
                        os.environ.pop('DEBUG')
                    except:
                        pass
                if not no_return:
                    return a, name

    def get_netloc(self, url):
        debug(url = url)
        if "www." in url:
            debug(urlparse0 = urllib.parse.urlparse(url))
            netloc = urllib.parse.urlparse(url).netloc.split(".", 2)[1]
            debug(netloc0 = netloc)
            return netloc
        else:
            debug(urlparse1 = urllib.parse.urlparse(url))
            netloc = urllib.parse.urlparse(url).netloc.split(".", 1)[0]
            debug(netloc1 = netloc)
            return netloc

    def youtube(self, url, direct_download = False, download_path = ".", interactive = True, pcloud = False, pcloud_username = None, pcloud_password = None, pcloud_folderid = '0', pcloud_rename = None, pcloud_foldername = None):
        youtube_list = {}
        self.header.update({
            'Accept' : '*/*',
            'Accept-Encoding' : 'gzip, deflate',
            'Accept-Language' : 'en-US,en;q=0.5',
            'Connection' : 'keep-alive',
            'Host' : 'www.autogeneratelink.us',
            'Referer' : 'http://www.autogeneratelink.us/',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.9) Gecko/20100101 Goanna/3.4 Firefox/52.9 PaleMoon/27.6.2',
            'X-Requested-With' : 'XMLHttpRequest'
        })
        headers = self.header
        debug(headers = headers)
        all_video = {}
        all_audio = {}
        n = 1
        m = 1
        if 'youtu' in url:
            details = {}
            #a0 = self.get_req(url, headers)
            #http://www.autogeneratelink.us/link.php?link=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DUhqwlP_WgF4&token=agl
            params = {
                'link': url,
                'token': 'agl',
            }
            debug(self_url=self.url)
            #URL = self.url + '/link.php?'
            # debug(URL=URL)
            #debug(headers = headers)
            a0 = requests.get(self.url, params = params, headers = headers, proxies=self.proxy)
            a0 = requests.get(self.url, params = params, proxies=self.proxy)
            debug(a0_content=a0.content)
            debug(FULL_URL = a0.url)
            a1 = bs(a0.content, 'lxml')
            debug(a1 = a1)
            #a1 = a11.find("li", {'class': 'list-group-item',})
            #debug(a1 = a1)
            #name = a1.find_next("b")
            try:
                name = a1.find("b").text
            except:
                print(make_colors('SERVER ERROR !', 'white', 'lightred'))
                if os.getenv('debug'):
                    import traceback
                    traceback.format_exc()
                sys.exit(0)
            debug(name = name)
            #c0 = a1.find_next('span', {'class': 'list-group-item',}).find_next('table')
            c0 = a1.find('table')
            debug(c0 = c0)
            if not c0:
                print((make_colors("INVALID URL !", 'lightwhite', 'lightred', attrs=['blink'])))
                sys.exit(1)
            c1 = c0.find_all_next('tr')
            debug(c1 = c1)
            for i in c1:
                c2 = i.find_all_next('b')
                debug(c2 = c2)
                details.update({c2[0].text: c2[1].text,})
                debug(details = details)
            debug(details = details)

            d0 = a1.find_all('a', {'class': 'list-group-item',})
            debug(d0 = d0)
            n = 1
            for i in d0:
                i_quality = []
                a_quality = re.split("Video only|Video| only|Audio only|Audio|:| \| |\(|\)", str(i.text).strip())
                debug(a_quality = a_quality)
                for x in a_quality:
                    if not str(x).strip() == '':
                        i_quality.append(str(x).strip())
                debug(i_quality = i_quality)
                video = False
                audio = False
                video_quality = ''
                audio_quality = ''
                size = ''
                if len(i_quality) == 3:
                    video = True
                    audio = True
                    debug(video = video, audio = audio)
                    video_quality = i_quality[0]
                    audio_quality = i_quality[1]
                    size = i_quality[2]
                    debug(video_quality)
                    debug(audio_quality)
                    debug(size = size)
                else:
                    if 'Video only' in i.text:
                        video = True
                        audio = False
                        debug(video = video, audio = audio)
                        video_quality = i_quality[0]
                        size = i_quality[1]
                        debug(video_quality)
                        debug(size = size)
                    elif 'Audio only' in i.text:
                        video = False
                        audio = True
                        debug(video = video, audio = audio)
                        audio_quality = i_quality[0]
                        size = i_quality[1]
                        debug(audio_quality)
                        debug(size = size)

                youtube_list.update(
                    {
                        n: {
                            'title': i.text.strip(),
                            'url': i.get('href'),
                            'video': video,
                            'audio': audio,
                            'video_quality': video_quality,
                            'audio_quality': audio_quality,
                            'size': size,
                            },
                    }
                )
                n += 1
            debug(youtube_list = youtube_list)
            for i in youtube_list:
                if not youtube_list.get(i).get('video'):
                    i_video = ''
                if not youtube_list.get(i).get('audio'):
                    i_audio = ''
                print(str(i) + ". " + youtube_list.get(i).get('title') + " (" + youtube_list.get(i).get('video_quality') + "~" + youtube_list.get(i).get('audio_quality') + ")")

            if not interactive:
                return youtube_list
            q = input("Select Number: ")
            #if not quality:
                #q = raw_input("Select Number: ")
            #else:
                #q = quality
                #if len(youtube_list) < int(q):
                    #q = raw_input("Select Number: ")
                #else:
                    #q_result = {'audio': [], 'video': [],}
                    #for i in youtube_list:
                        #if str(q) in i.get('video_quality'):
                            #q_result.get('audio').append()
            if q == '' or q == ' ' or q == None:
                sys.stdout.write("  You Not select any number !")
                sys.exit(0)
            debug(URL_SELECTED = str(youtube_list.get(int(q)).get('url')))
            try:
                if isinstance(int(q), int) and int(q) > 0:
                    try:
                        clipboard.copy(str(youtube_list.get(int(q)).get('url')))
                    except:
                        traceback.format_exc()
                    if direct_download:
                        #filename = pywget.download(
                            #str(youtube_list.get(int(q))), download_path)
                        filename = self.download(str(youtube_list.get(int(q)).get('url')), download_path)
                        return str(youtube_list.get(int(q))), filename
                    if pcloud:
                        self.pcloud(str(youtube_list.get(int(q)).get('url')), pcloud_username, pcloud_password, None, pcloud_folderid, pcloud_foldername)
                    return str(youtube_list.get(int(q)).get('url')), None
            except:
                import traceback
                print("ERROR:")
                print(traceback.format_exc())
        return youtube_list
        #sys.exit('still development ............... :)')
        # elif "play.google.com" in url:
        #     a = soup.find('a')
        #     return a.get('href'), None

    def safelinkconverter(self, url):
        a = self.cf.get(url)
        b = bs(a.content, 'lxml')
        URL1 = b.find('div', {'id':'m'}).find('a').get('href')
        debug(URL1=URL1)
        a1 = self.cf.get(URL1)
        b1 = bs(a1.content, 'lxml')
        URL2 = b1.find('div', {'class':"redirect_url"}).find_next('div').get('onclick')
        debug(URL2=URL2)
        URL = re.findall('https.*?\.html',URL2)
        debug(URL=URL)
        return URL[0]

    def anonfile(self, url):
        a = self.cf.get(url)
        b = bs(a.content, 'lxml')
        div_download_wrapper = b.find('div', id='download-wrapper')
        if div_download_wrapper:
            download_url = div_download_wrapper.find('a', id='download-url').get('href')
            debug(download_url=download_url)
        return download_url

    def ourabeauty(self, url):
        # http://ourabeauty.info/?id=R3R3ejRJOWNoQUQ4M2VkVUhRb2hodWNTcVJyQzMwUCt6cDI0V2FDZnhNWmlvNm56c1lzb016Tlh1UFBiemU3Vg==
        a = self.cf.get(url)
        b = bs(a.content, 'lxml')
        form = b.find('div', {'class':'humancheck'}).find('form')
        get_id = form.find('input').get('value')
        action = form.get('action')
        debug(get_id=get_id)
        a1 = self.cf.post(action, data={'get':get_id})
        b1 = bs(a1.content, 'lxml')
        c1 = b1.find('head').find_all('script', {'type':'text/javascript'})[-1]
        debug(c1=c1)
        # print "str(c1) =", str(c1)
        c2 = re.findall('changeLink.*?;', str(c1))
        debug(c2=c2)
        if c2:
            c3 = re.split("//|'|;", c2[0])[-3]
            debug(c3=c3)
            print(make_colors("LINK", 'lw', 'lm') + " : " + make_colors('https://' + c3, 'lw', 'lb'))
            return 'https://' + c3
        return False


    def isengsub(self, url):
        a = self.cf.get(url)
        b = bs(a.content, 'lxml')
        div_download_wrapper = b.find('div', {'class':'pusat'}).find('div', {'align':'center'})
        if div_download_wrapper:
            download_url = div_download_wrapper.find('a').get('href')
            debug(download_url=download_url)
        return download_url

    def mediafire(self, url):
        a = self.cf.get(url)
        b = bs(a.content, 'lxml')
        div_download_link = b.find('div', id='download_link')
        debug(div_download_link=div_download_link)
        if div_download_link:
            download_url = div_download_link.find('a', {'class':'input'}).get('href')
            debug(download_url=download_url)
            clipboard.copy(str(download_url))
        return download_url
    
    def zippyshare(self, url, out_name = '', download_path = os.getcwd(), downloadit = True):
        generator = zippyshare.zippyshare()
        url_download = generator.generate(url)
        
        print(make_colors('GENERATED         : ', 'white', 'on_red') + make_colors(url_download, 'white', 'on_red'))
        # print termcolor.colored('NAME              : ', 'white', 'on_green') + termcolor.colored(out_name, 'white', 'on_blue')
        print(make_colors('NAME              : ', 'white', 'on_green') + make_colors(out_name, 'white', 'on_blue'))
        # print termcolor.colored('DOWNLOAD NAME     : ', 'white', 'on_cyan') + termcolor.colored(name, 'white', 'on_blue')
        print(make_colors('DOWNLOAD NAME     : ', 'white', 'on_cyan') + make_colors(os.path.basename(url_download), 'white', 'on_blue'))
        if downloadit:
            generator.download(url_download, download_path, out_name)
        return url_download
    
    def anonfile(self, url, download = True, download_path = ".", download_name = None, pcloud = False, pcloud_username = None, pcloud_password = None, name = None, pcloud_folderid = None, pcloud_foldername = None, direct_download = None, use_proxy = None, proxy= None):
        if download and not pcloud:
            # download(url, path=".", output=None, referrer=None, postdata=None, cookies=None, username=None, password=None, confirm=False, wget=False)
            self.download(url, download_path, download_name)
        elif download and pcloud:
            self.pcloud(url, pcloud_username, pcloud_password, name, pcloud_folderid, pcloud_foldername, True, download_path, use_proxy, proxy= self.proxy)
        elif not download and pcloud:
            self.pcloud(url, pcloud_username, pcloud_password, name, pcloud_folderid, pcloud_foldername, False, download_path, use_proxy, proxy= self.proxy)
        else:
            print((make_colors("Anonfile url generated:", url, "lw", "lr", attrs = ['blink'])))
            return url
    
    def googleapis(self, url, out_name = '', download_path = os.getcwd(), downloadit = True):
        
        import urllib.request, urllib.error, urllib.parse
        #"https://storage.googleapis.com/degoo-production-large-file-us-east1.degoo.me/QCznsi/ssicCw/mp4/ChR-1ImQ2Ok56UOcvya5KXybuJWpMxAA.mp4?GoogleAccessId=GOOGFMVLH4WIQJU6BJFH&Expires=2204496219&Signature=XHo3gQCx7NaIMZK7aTapt9bO2d4%3D&response-content-disposition=attachment;%20filename=[neonime]_PP3%20-%2004-720p.mp4"
        outname = urllib.parse.unquote(re.split("attachment;|filename=", url)[-1])
        print(make_colors('GENERATED         : ', 'white', 'on_red') + make_colors(url, 'white', 'on_red'))
        # print termcolor.colored('NAME              : ', 'white', 'on_green') + termcolor.colored(out_name, 'white', 'on_blue')
        print(make_colors('NAME              : ', 'white', 'on_green') + make_colors(out_name, 'white', 'on_blue'))
        # print termcolor.colored('DOWNLOAD NAME     : ', 'white', 'on_cyan') + termcolor.colored(name, 'white', 'on_blue')
        print(make_colors('DOWNLOAD NAME     : ', 'white', 'on_cyan') + make_colors(os.path.basename(url), 'white', 'on_blue'))
        self.download(url, download_path, out_name)
        return url

    def youtube1(self, url):
        URL = 'http://api.w3hills.com/youtube/get_video_info'
        params = {
            'video_id': '',
            'token': '',
        }

    def siotong(self, url, verbose = False):
        '''
            generate url containt words "siotong" or "coeg"
            parameter:
                url = (str) ~ first url given
            return:
                str
                format: url
        '''
        while 1:
            try:
                req = requests.get(url)
                break
            except:
                pass
        if verbose:
            os.environ.update({'DEBUG': "1"})
        if self.get_netloc(req.url) == 'siotong' or self.get_netloc(req.url) == 'coeg' or self.get_netloc(req.url) == 'telondasmu' or self.get_netloc(req.url) == 'siherp' or self.get_netloc(req.url) == 'greget' or self.get_netloc(req.url) == 'tetew' or self.get_netloc(req.url) == 'anjay':
            a = bs(req.content, 'lxml')

            b0 = a.find('div', {'class': 'download-link',})
            if b0:
                b = b0.find('a').get('href')  #get siotong
                debug(b_1 = b)
            else:
                b0 = a.find('div', {'class': "col-sm-12",})
                if b0:
                    b = b0.find_next('p', {'style': 'text-align:center;',}).find('a').get('href')
                    debug(b_2 = b)

            debug(b = b)
            if self.get_netloc(b) == 'siotong' or self.get_netloc(b) == 'coeg' or self.get_netloc(b) == 'telondasmu' or self.get_netloc(b) == 'siherp' or self.get_netloc(b) == 'greget' or self.get_netloc(req.url) == 'tetew' or self.get_netloc(req.url) == 'anjay':
                self.percent_progress(10, self.MEMCACHED)
                if verbose or str(os.getenv('DEBUG')) == '1':
                    print(make_colors('re-generate siotong: ', 'white', 'red', ['blink']) + make_colors(str(b), 'blue', 'yellow') + " ...")
                return self.siotong(b)
        else:
            debug(self_get_netloc_req_url = self.get_netloc(req.url))
            debug(return_url = req.url)
            self.percent_progress(50, self.MEMCACHED)
            return req.url

    def zonawibu(self, url, verbose = False):
        '''
            generate url containt words "zonawibu"
            parameter:
                url = (str) ~ first url given
            return:
                str
                format: url
        '''
        req = requests.get(url)
        if verbose:
            os.environ.update({'DEBUG': "1"})
        if self.get_netloc(req.url) == 'zonawibu':
            a = bs(req.content, 'lxml')
            b = a.find('div', {'class': 'notify',}).find('a').get('href')  #get siotong
            debug(b = b)
            if self.get_netloc(b) == 'zonawibu':
                if verbose or str(os.getenv('DEBUG')) == '1':
                    print(make_colors('re-generate siotong: ', 'white', 'red', ['blink']) + make_colors(str(b), 'blue', 'yellow') + " ...")
                self.percent_progress(10, self.MEMCACHED)
                return self.zonawibu(b)
        else:
            debug(self_get_netloc_req_url = self.get_netloc(req.url))
            debug(return_url = req.url)
            self.percent_progress(50, self.MEMCACHED)
            return req.url

    def upload_to_pcloud(self, url, download_path=os.getcwd(), name=None, username=None, password=None, folderid='0', foldername=None, downloadit=False, use_proxy=False, proxy = None):
        debug("upload_to_pcloud")
        from pyPCloud import pcloud
        if use_proxy:
            PCloud = pcloud(proxy=self.proxy)
        else:
            PCloud = pcloud(proxy = proxy)
        datax = PCloud.remoteUpload(url, username=username, password=password,folderid=folderid, renameit=name, foldername=foldername)
        idx = datax.get('metadata')[0].get('id')
        data, cookies = PCloud.getDownloadLink(idx, download_path=download_path)
        download_url = 'https://' + data.get('hosts')[0] + data.get('path')
        if downloadit:
            self.download(download_url, download_path)
        else:
            return download_url

    def pcloud(self, url_download, username = None, password = None, name = None, folderid = '0', foldername = None, downloadit = False, download_path = os.getcwd(), use_proxy=False, proxy = None):
        debug(proxy = proxy)
        debug(self_proxy = self.proxy)
        try:
            import pyPCloud
            return self.upload_to_pcloud(url_download, download_path, name, username, password, folderid, foldername, downloadit, proxy = self.proxy)
        except ImportError:
            PCLOUD_MODULE = ''
            if self.CONFIG.read_config('PCLOUD', 'PATH'):
                PARENT_PATH = self.CONFIG.read_config('PCLOUD', 'PATH')
                sys.path.append(PARENT_PATH)
                PCLOUD_MODULE = os.path.basename(PARENT_PATH)
                PARENT_PATH = os.path.dirname(PARENT_PATH)
                if configset.read_config('PCLOUD', 'NAME', 'aglink.ini'):
                    PCLOUD_MODULE = self.CONFIG.read_config('PCLOUD', 'NAME')
            if os.getenv('PCLOUD_MODULE'):
                PARENT_PATH = os.getenv('PCLOUD_MODULE')
                sys.path.append(PARENT_PATH)
                PCLOUD_MODULE = os.path.basename(PARENT_PATH)
                PARENT_PATH = os.path.dirname(PARENT_PATH)
            #else:
                #PARENT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)),'test')
                #sys.path.append(os.path.join(PARENT_PATH, 'pypcloud'))
            debug(PARENT_PATH = PARENT_PATH)
            debug(PCLOUD_MODULE = PCLOUD_MODULE)
            sys.path.append(PARENT_PATH)
            try:
                import importlib
                pcloud = importlib.import_module(PCLOUD_MODULE)
                if use_proxy:
                    PCloud = pcloud.pcloud(proxy=self.proxy)
                else:
                    PCloud = pcloud.pcloud(proxy = proxy)
                datax = PCloud.remoteUpload(url_download, username = username, password = password, folderid = folderid, renameit = name, foldername = foldername)
                if downloadit:
                    idx = datax.get('metadata')[0].get('id')
                    data, cookies = PCloud.getDownloadLink(idx, download_path = download_path)
                    download_path = os.path.abspath(download_path)
                    if not os.path.isdir(download_path):
                        os.makedirs(download_path)
                    if not os.path.isdir(download_path):
                        download_path = os.path.dirname(__file__)
                    fileid = data.get('fileid')
                    #if name:
                        #PCloud.printlist('usage', renamefile='')
                        #PCloud.renameFile(name, fileid, None, username, password)
                    download_url = 'https://' + data.get('hosts')[0] + data.get('path')
                    if name:
                        return PCloud.download(download_url, download_path, name, cookies)
                    else:
                        return PCloud.download(download_url, download_path, cookies=cookies)
                return datax
            except:
                print(traceback.format_exc())

    def test_proxy(self, proxies, timeout=3):
        if not proxies:
            return False
        try:
            a = requests.request('GET', self.url, proxies=proxies, verify=False, timeout=timeout)
            return True
        except:
            return False

    def setProxy(self, proxies=None, use_proxy=False):
        '''
            format proxies: ['http://ip:port', 'https://ip:port']
        '''
        debug()
        PROXY = {}
        if not self.CONFIG.read_config('PROXY', 'use_proxy'):
            if not use_proxy:
                return PROXY
        else:
            if proxies:  #data must list instance
                for i in proxies:
                    #host, port = str(i).split(":")
                    scheme = urllib.parse.urlparse(i).scheme
                    PROXY.update({scheme: i,})
                if not self.test_proxy(PROXY):
                    PROXY = {}
                    if self.CONFIG.read_config('PROXY', 'server') and self.CONFIG.read_config('PROXY', 'port'):
                        PROXY.update({
                        'http': 'http://%s:%s'%(self.CONFIG.read_config('PROXY', 'server'), self.CONFIG.read_config('PROXY', 'port')),
                        'https': 'https://%s:%s'%(self.CONFIG.read_config('PROXY', 'server'), self.CONFIG.read_config('PROXY', 'port'))
                        })
                # print "PROXY =", PROXY
                # print "self.test_proxy(PROXY) =", self.test_proxy(PROXY)
                if not self.test_proxy(PROXY):
                    from proxy_tester import proxy_tester
                    pt = proxy_tester.proxy_tester()
                    list_proxy_ok = pt.test_proxy_ip(self.url, print_list=True, limit=1)
                    debug(list_proxy_ok=list_proxy_ok)
                    if list_proxy_ok:
                        PROXY.update({
                            'http': 'http://%s'%(list_proxy_ok[0]),
                            'https': 'https://%s'%(list_proxy_ok[0])
                        })
            else:
                if use_proxy:
                    from proxy_tester import proxy_tester
                    pt = proxy_tester.proxy_tester()
                    list_proxy_ok = pt.test_proxy_ip(self.url, print_list=True, limit=1)
                    debug(list_proxy_ok=list_proxy_ok)
                    if list_proxy_ok:
                        PROXY.update({
                            'http': 'http://%s'%(list_proxy_ok[0]),
                            'https': 'https://%s'%(list_proxy_ok[0])
                        })
            if not self.proxy:
                self.proxy = PROXY
            if PROXY:
                for i in PROXY:
                    os.environ.update({i:PROXY.get(i)})
        return PROXY

    def set_percent_progress(self):
        while 1:
            percent = self.percent
            if not percent >= 100:
                if self.percent == percent:
                    if self.percent == 30:
                        self.percent += 30
                        self.percent_progress(self.percent, self.MEMCACHED)
                    else:
                        self.percent += 0.5
                        self.percent_progress(self.percent, self.MEMCACHED)
                    if percent >= 70:
                        time.sleep(0.5)
                    else:
                        time.sleep(1)
                else:
                    percent = self.percent
            else:
                self.percent_progress(percent, self.MEMCACHED)
                debug(percent = percent)
                break

    def daemon_generate(self, link, clip=None, quality=None, verbosity=None, support= False, direct_download=None, download_path=".", pcloud = False, pcloud_username = None, pcloud_password = None, pcloud_folderid = '0', pcloud_rename = None, pcloud_foldername = None, proxy = None, fast = False, bypass_regenerate = False, cliped = False, name = None, wget = False):
        args = (link, clip, quality, verbosity, support, direct_download, download_path, pcloud, pcloud_username, pcloud_password, pcloud_folderid, pcloud_rename, pcloud_foldername, proxy, fast, bypass_regenerate, cliped, name, wget)

        from multiprocessing.pool import ThreadPool
        pool = ThreadPool(processes = 2)
        t1 = pool.apply_async(self.generate, args)
        t2 = pool.apply_async(self.percent_progress, ())
        #t1 = threading.Thread(target = self.generate, args = args)
        #t2 = threading.Thread(target = self.set_percent_progress, args = ())
        #self.thread = t1
        mc_percent = int(self.get_percent_memcached())
        while 1:
            if not mc_percent == 100:
                ##print "mc_percent =", mc_percent
                mc_percent = int(self.get_percent_memcached())
                time.sleep(3)
            else:
                break
        link, name = t1.get()
        debug(link = link)
        debug(name = name)
        return link, name

    def usage(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('LINK', help='Link to be convert', action='store', default = '')
        parser.add_argument(
            '-c', '--clip', help='Copy converted links to Clipboard', action='store_true', default = True)
        #parser.add_argument(
            #'-C', '--cliped', help='Genrate links from Clipboard', action='store_true', default = True)
        parser.add_argument(
            '-N', '--number', help='Number of Quality video download to', action='store')
        parser.add_argument(
            '-n', '--name', help='Name of video download to', action='store')
        parser.add_argument('-d', '--download',
                            help='Direct download', action='store_true')
        parser.add_argument(
            '-s', '--support', help='Show support text', action='store_true')
        parser.add_argument('-f', '--fast', help = 'Fast, no check', action = 'store_true')
        parser.add_argument(
            '-v', '--verbose', help='-v = version | -vv = Verbosity', action='count')
        parser.add_argument('-X', '--proxy', help='Set Proxy, format example http://127.0.0.1:8118 https://127.0.0.1:3128', action='store', nargs = '*')
        parser.add_argument('-x', '--use-proxy', help='Use Auto Proxy', action='store_true')
        parser.add_argument('-Xt', '--test-proxy', help='Test proxy with proxy option given', action='store_true')
        parser.add_argument(
            '-p', '--path', help='Download Path default this', action='store', default='.')
        parser.add_argument('-i', '--wget', action = 'store_true', help = 'Direct use wget (build in) for download manager')
        parser.add_argument('--pcloud', help = 'Remote Upload to Pcloud Storage', action = 'store_true')
        parser.add_argument('--pcloud-username', help = 'Username of Remote Upload to Pcloud Storage', action = 'store')
        parser.add_argument('--pcloud-password', help = 'Password of Remote Upload to Pcloud Storage', action = 'store')
        parser.add_argument('--pcloud-folderid', help = 'Folder ID Remote Upload to Pcloud Storage, default=0', action = 'store', default = '0', type = str)
        parser.add_argument('--pcloud-renameit', help = 'Rename After of Remote Upload to Pcloud Storage', action = 'store')
        parser.add_argument('--pcloud-foldername', help = 'Folder of Remote Upload to Pcloud Storage to', action = 'store')
        parser.add_argument('-z', '--daemon', help = 'Generate with progress monitoring', action = 'store_true')
        parser.add_argument('-m', '--memcached', help = 'Use progress monitoring with memcached ', action = 'store_true')
        parser.add_argument('-ms', '--memcached-host', help = 'Progress monitoring with memcached server address/ip', action = 'store_true')
        parser.add_argument('-mp', '--memcached-port', help = 'Progress monitoring with memcached server port', action = 'store_true')
        parser.add_argument('--debug', help = 'Debug Process', action = 'store_true')

        if len(sys.argv) > 1:
            if '-v' == sys.argv[1]:
                print("version:", self.getVersion())
            else:
                args = parser.parse_args()
                self.debug = args.debug
                if args.memcached:
                    self.MEMCACHED = True
                if args.memcached_host:
                    self.MEMCACHED_HOST = args.memcached_host
                if args.memcached_port:
                    self.MEMCACHED_PORT = args.memcached_port
                if args.proxy:
                    if self.CONFIG.read_config('PROXY', 'server') and self.CONFIG.read_config('PROXY', 'port'):
                        self.proxy.update(
                            {
                                'http': 'http://%s:%s'%(self.CONFIG.read_config('PROXY', 'server'), self.CONFIG.read_config('PROXY', 'port')),
                                'https': 'https://%s:%s'%(self.CONFIG.read_config('PROXY', 'server'), self.CONFIG.read_config('PROXY', 'port'))
                            })
                    else:
                        self.setProxy(args.proxy)
                if args.proxy:
                    self.setProxy()

                if args.test_proxy:
                    return self.test_proxy()
                # print "ARGS - PATH =", args.path
                #print "args =", args
                cliped = False
                if args.LINK == 'c' or args.LINK == 'C':
                    cliped = True
                debug(args_link = args.LINK)
                if args.daemon:
                    self.daemon_generate(args.LINK, True, args.number,
                                         args.verbose, args.support, args.download, args.path, args.pcloud, args.pcloud_username, args.pcloud_password, args.pcloud_folderid, args.pcloud_renameit, args.pcloud_foldername, fast = args.fast, cliped= cliped, name = args.name, wget = args.wget)
                else:
                    self.generate(args.LINK, True, args.number,
                                  args.verbose, args.support, args.download, args.path, args.pcloud, args.pcloud_username, args.pcloud_password, args.pcloud_folderid, args.pcloud_renameit, args.pcloud_foldername, fast = args.fast, cliped= cliped, name = args.name, wget = args.wget, show_debug= args.verbose)
        else:
            parser.print_help()

if __name__ == '__main__':
    print("PID:", pid)
    c = autogeneratelink()
    # c.mediafire('https://www.mediafire.com/file/dq0p6a9uj0sq4bl/')
    c.usage()
    # c.ourabeauty("http://ourabeauty.info/?id=R3R3ejRJOWNoQUQ4M2VkVUhRb2hodWNTcVJyQzMwUCt6cDI0V2FDZnhNWmlvNm56c1lzb016Tlh1UFBiemU3Vg==")
    #while 1:
        #percent = c.percent
        #if not percent == 100:
            #print "percent:", percent
            #if c.percent == percent:
                #if c.percent == 30:
                    #c.percent += 30
                #else:
                    #c.percent += 0.5
                #if percent >= 70:
                    #time.sleep(0.5)
                #else:
                    #time.sleep(1)
                #print "percent:", percent
            #else:
                #print "percent:", percent
                #percent = c.percent
        #else:
            #print "percent:", percent
            #debug(percent = percent)
            #break

    #url = 'https://www.youtube.com/watch?v=_s0nFWar9Co'
    #c.siotong(url, True)
    #print c.get_netloc(url)
    #c.youtube(url)
    #c.get_req(url)
