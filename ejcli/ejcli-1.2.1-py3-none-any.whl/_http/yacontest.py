import urllib.request, urllib.parse, html, json, random
from .base import Backend
from ..error import EJError
from .openerwr import OpenerWrapper

class YaContest(Backend):
    @staticmethod
    def detect(url):
        if url.endswith('/'): url = url[:-1]
        if url.endswith('/enter'): url = url[:-6]
        return url.startswith('https://contest.yandex.ru/contest/') and url[34:].isnumeric()
    @staticmethod
    def _get_bem(data, sp):
        return json.loads(html.unescape(data.split(sp, 1)[1].split('"', 1)[0]))
    @classmethod
    def _get_sk(self, data):
        try: return data.split('<input type="hidden" name="sk" value="', 1)[1].split('"', 1)[0]
        except IndexError: return self._get_bem(data, '<div class="aside i-bem" data-bem="')['aside']['sk']
    def __init__(self, url, login, passwd):
        if url.endswith('/'): url = url[:-1]
        if url.endswith('/enter'): url = url[:-6]
        if not self.detect(url):
            raise EJError("Not a contest.yandex.ru URL")
        self.opener = OpenerWrapper(urllib.request.build_opener(urllib.request.HTTPCookieProcessor))
        data = self.opener.open('https://passport.yandex.ru/auth?'+urllib.parse.urlencode({'origin': 'consent', 'retpath': 'https://passport.yandex.ru/profile'}), urllib.parse.urlencode({'login': login, 'passwd': passwd}).encode('ascii'))
        if data.geturl() != 'https://passport.yandex.ru/profile':
            print(data.geturl())
            raise EJError('Login failed.')
        self.url = url
        self.short_url = '/'+url.split('/', 3)[3]
    def task_list(self):
        data = self.opener.open(self.url+'/problems/').read().decode('utf-8', 'replace')
        return [html.unescape(i) for i in (i.split('/', 1)[0] for i in data.split('<a class="link" href="'+self.short_url+'/problems/')[1:]) if '"' not in i]
    def task_ids(self):
        return list(range(len(self.task_list())))
    def submit(self, task, lang, code):
        if isinstance(code, str): code = code.encode('utf-8')
        t = self.task_list()[task]
        data = self.opener.open(self.url+'/problems/'+t+'/').read().decode('utf-8', 'replace')
        prob_id = self._get_bem(data, '<div class="solution solution_type_compiler-list i-bem" data-bem="')['solution']['problemId']
        cmplrs = self._compiler_list(data)
        sk = self._get_sk(data)
        data = []
        data.append(b'')
        data.append(prob_id.encode('ascii')+b'@compilerId"\r\n\r\n'+cmplrs[lang][1].encode('ascii')+b'\r\n')
        data.append(prob_id.encode('ascii')+b'@solution"\r\n\r\ntext\r\n')
        data.append(prob_id.encode('ascii')+b'@text"\r\n\r\n'+code+b'\r\n')
        data.append(b'sk"\r\n\r\n'+sk.encode('ascii')+b'\r\n')
        data.append(b'retpath"\r\n\r\nhttps://ya.ru/\r\n')
        rand = b''
        while any(rand in i for i in data):
            rand = ('%020d'%random.randrange(10**20)).encode('ascii')
        data = (b'--'+rand+b'\r\nContent-Disposition: form-data; name="').join(data)+b'--'+rand+b'--\r\n'
        data2 = self.opener.open(urllib.request.Request(self.url+'/submit/', data, {'Content-Type': 'multipart/form-data; boundary='+rand.decode('ascii')}))
        if '?error=' in data2:
            raise EJError('Error: '+data2.split('?error=', 1)[1])
    @staticmethod
    def _compiler_list(data):
        ans = []
        for i in data.split('<select class="select__control" name="')[1:]:
            if i.split('"', 1)[0].endswith('@compilerId'):
                for idx, j in enumerate(i.split('</select>', 1)[0].split('<option class="select__option" value="')[1:]):
                    short_name = html.unescape(j.split('"', 1)[0])
                    long_name = html.unescape(j.split('</option>', 1)[0].rsplit('>', 1)[1])
                    ans.append((idx, short_name, long_name))
        return ans
    def compiler_list(self, task):
        t = self.task_list()[task]
        data = self.opener.open(self.url+'/problems/'+t+'/').read().decode('utf-8', 'replace')
        return self._compiler_list(data)
    def do_action(self, action, *args):
        try: url = self.url + {'stop_virtual': '/finish/?return=false', 'restart_virtual': '/finish/?return=true'}[action]
        except KeyError: pass
        else:
            #WIP, doesn't work yet
            try: return self.opener.open(url, urllib.parse.urlencode({'sk': self._get_sk(self.opener.open(self.url).read().decode('utf-8', 'replace'))}).encode('ascii')).read() == b'OK'
            except urllib.request.URLError: return False
        action = {'register': 'register', 'start_virtual': 'startVirtual'}[action]
        try: data = self.opener.open(self.url+'/enter/', urllib.parse.urlencode({'sk': self._get_sk(self.opener.open(self.url).read().decode('utf-8', 'replace')), 'action': action, 'retpath': self.url}).encode('ascii'))
        except urllib.request.URLError: return False
        url = data.geturl()
        return url.startswith(self.url+'/') and '?error=' not in url
