import functools
from http import cookiejar

import requests
import simplejson as json
import urllib3

# Used for verify=False in requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class SynologyException(requests.RequestException):

    def __init__(self, code=-1, message=None, *args, **kwargs):
        super(SynologyException, self).__init__(*args, **kwargs)
        self.code = code
        self.message = message

    def __str__(self):
        return self.response.text

    __repr__ = __str__


class BlockAll(cookiejar.CookiePolicy):
    """
    drop cookies from session object
    """
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False


def concat_nas_address(ip_address=None, port=None, nas_domain=None, https=True):
    """
    :param ip_address: 
    :param port: 
    :param nas_domain: 
    :param https: 
    :return: 
    """
    scheme = 'https://' if https else 'http://'
    if port is None:
        # https default port 5001, http default port 5000
        port = '5001' if https else '5000'

    if ip_address is None:
        assert isinstance(nas_domain, str)
        nas_address = ':'.join(filter(None, [nas_domain, port]))
    else:
        assert nas_domain is None
        nas_address = ':'.join(filter(None, [ip_address, port]))

    return f"{scheme}{nas_address}"


def add_sid_token(reqs_data, sid):
    """
    add sid token in requests params
    :param reqs_data: requests kwargs
    :param sid: sid token
    :return:
    """
    if 'params' not in reqs_data:
        reqs_data['params'] = {}

    if 'api' not in reqs_data['params']:
        return reqs_data

    # login logout don't need sid
    if reqs_data['params']['api'] != 'SYNO.API.Auth':
        reqs_data['params']['_sid'] = sid
    return reqs_data


def color_name_to_id(color_name):
    color_id = {
        'gray': '#A0A5AA',
        'red': '#FA8282',
        'orange': '#FA9C3E',
        'yellow': '#F2CA00',
        'green': '#94BF13',
        'blue': '#499DF2',
        'purple': '#A18AE6',
    }
    try:
        return color_id[color_name]
    except KeyError:
        raise KeyError('Color name error! Use gray/red/orange/yellow/green/blue/purple')


def raise_synology_exception(resp):
    """
    :param resp:
    :return:
    """
    # handle 404, 400, ..., and synology server error code
    try:
        resp.raise_for_status()
    except requests.RequestException as reqe:
        code = -1
        message = None
        if reqe.response.text:
            try:
                err_info = json.loads(reqe.response.text)
                code = err_info['code']
                message = err_info['message']
            except (ValueError, KeyError):
                pass
        raise SynologyException(
            code=code,
            message=message,
            request=reqe.request,
            response=reqe.response
        )

    if resp.status_code == 200:
        result = resp.json() if resp.text else {}
        if not result['success']:
            raise SynologyException(
                code=result['error']['code'],
                message=result['error']['errors'],
                request=resp.request,
                response=resp
            )


class SynologySession:
    """
    Synology App base class
    """

    def __init__(self, username, password, ip_address=None, port=None, nas_domain=None, https=True):
        nas_address = concat_nas_address(ip_address, port, nas_domain, https)
        self._username = username
        self._password = password
        self._base_url = f"{nas_address}/webapi/"
        self.req_session = requests.Session()
        self.req_session.cookies.set_policy(BlockAll())
        self._sid = None
        self._session_expire = True

    def _request(self, method, endpoint, **kwargs):
        if not endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url', self._base_url)
            url = f"{api_base_url}{endpoint}"
        else:
            url = endpoint

        if isinstance(kwargs.get('data', ''), dict):
            body = json.dumps(
                kwargs['data'],
                ensure_ascii=False,
            )
            body = body.encode('utf-8')
            kwargs['data'] = body

        kwargs = add_sid_token(kwargs, self._sid)

        if 'https' in url and url.count('.') >= 3:
            # if scheme is https:// and url contains ip,
            # return true indicate adding verify=False to requests.
            kwargs['verify'] = False

        res = self.req_session.request(
            method=method,
            url=url,
            **kwargs
        )
        raise_synology_exception(res)
        result = res.json() if res.text else {}
        return result

    def http_get(self, endpoint, **kwargs):
        return self._request('get', endpoint, **kwargs)

    def http_post(self, endpoint, **kwargs):
        return self._request('post', endpoint, **kwargs)

    def http_put(self, endpoint, **kwargs):
        return self._request('put', endpoint, **kwargs)

    def http_delete(self, endpoint, **kwargs):
        return self._request('delete', endpoint, **kwargs)

    def login(self, application):
        endpoint = 'auth.cgi'
        params = {'api': 'SYNO.API.Auth', 'version': '2', 'method': 'login', 'account': self._username,
                  'passwd': self._password, 'session': application, 'format': 'cookie'}
        if not self._session_expire:
            if self._sid is not None:
                self._session_expire = False
                return 'User already logged'
        else:
            resp = self.http_get(
                endpoint,
                params=params
            )
            self._sid = resp['data']['sid']
            self._session_expire = False
            return 'User logging... New session started!'

    def logout(self, application):
        endpoint = 'auth.cgi'
        params = {'api': 'SYNO.API.Auth', 'version': '2', 'method': 'logout', 'session': application}
        resp = self.http_get(
            endpoint,
            params=params
        )
        if resp['success'] is True:
            self._session_expire = True
            self._sid = None
            return 'Logged out'
        else:
            self._session_expire = True
            self._sid = None
            return 'No valid session is open'

    @functools.lru_cache()
    def get_api_list(self, app=None):
        endpoint = 'query.cgi'
        params = {'api': 'SYNO.API.Info', 'version': '1', 'method': 'query', 'query': 'all'}
        resp = self.http_get(
            endpoint,
            params=params
        )
        if app is not None:
            for key in resp['data']:
                if app.lower() in key.lower():
                    return resp['data'][key]
        else:
            return resp['data']

    @property
    def sid(self):
        return self._sid
