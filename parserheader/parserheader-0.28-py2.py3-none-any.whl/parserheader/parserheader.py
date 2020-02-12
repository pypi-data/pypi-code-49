import re
import click

if __name__ == '__main__':
    try:
        from debug import *
    except:
        def debug(headers_dict=None):
            import os
            if os.getenv('DEBUG'):
                print("headers_dict =", headers_dict)
else:
    def debug(*args, **kwargs):
        return None

class parserheader(object):
    def __init__(self):
        super(parserheader, self)

    def setCookies(self, cookies_str_or_dict, dont_format=False, **kwargs):
        cookie_dict = {}
        cookie_str = ''
        # if not cookies_str_or_dict:
        #     cookies_str_or_dict = "ym_uid=1532996994661863820; _ym_d=1532996994; _ym_isad=2; tr=2 4 6 8 9 10"
        if __name__ == '__main__':
            click.secho("Example Input string cookies:", fg='white', bg='blue')
            print(cookies_str_or_dict)
        if isinstance(cookies_str_or_dict, str):
            cookies_str_or_dict = re.split("; ", cookies_str_or_dict)
            for i in cookies_str_or_dict:
                if i.strip():
                    key,value = str(i).strip().split("=")
                    cookie_dict.update({key:value})
            debug(cookie_dict=cookie_dict)
        elif isinstance(cookies_str_or_dict, dict):
            for i in cookies_str_or_dict:
                cookie_str += str(i) + "=" + cookies_str_or_dict.get(i) + "; "
            cookie_str = cookie_str.strip()
            debug(cookie_str=cookie_str)
            if cookie_str:
                if cookie_str[-1] == ";":
                    cookie_str = cookie_str[:-1]
            cookie_dict = cookies_str_or_dict
        if not cookie_str:
            cookie_str = cookies_str_or_dict
        if __name__ == '__main__':
            click.secho("Example Output Dictionary cookies:", fg='white', bg='green')
            print(cookie_dict)
            print("-" * (click.get_terminal_size()[0] - 1))
            print("\n")
        if kwargs:
            for i in kwargs:
                if not dont_format:
                    key = str(i).replace("_","-")
                else:
                    key = str(i)
                value = kwargs.get(i)
                cookie_dict.update({key:value})
            return self.setCookies(cookie_dict)
        return cookie_dict, cookie_str


    def parserHeader(self, string_headers = None, get_path='/', cookies_dict_str='', **kwargs):
        # cookies_dict_str example: _ym_uid=1532996994661863820; _ym_d=1532996994; _ym_isad=2;
        #
        string_headers_example = """
        GET /L.O.R.D---Legend-Of-Ravaging-Dynasties- HTTP/1.1
        Host: tparser.org
        Connection: keep-alive
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
        Referer: http://tparser.org/
        Accept-Encoding: gzip, deflate
        Accept-Language: en-US,en;q=0.9
        Cookie: _ym_uid=1532996994661863820; _ym_d=1532996994; _ym_isad=2; tr=2 4 6 8 9 10
        """
        headers_dict = {}
        if not string_headers:
            string_headers = string_headers_example
        
        if string_headers:
            data = str(string_headers).replace("       ", "")
            data = re.split("\n", data)
            #print "data 1 =", data
            for i in data:
                if ": " in i:
                    key, value = re.split(": ", i)
                    key = key.strip()
                    value = value.strip()
                    headers_dict.update({key: value,})
            if kwargs:
                for i in kwargs:
                    key = str(i).replace("_","-").title()
                    value = kwargs.get(i)
                    headers_dict.update({key:value})
            debug(headers_dict = headers_dict)
            if cookies_dict_str:
                if isinstance(cookies_dict_str, str):
                    headers_dict.update({'Cookie':cookies_dict_str})
                    debug(headers_dict=headers_dict)
                elif isinstance(cookies_dict_str, dict):
                    cd, cs = self.setCookies(cookies_dict_str)
                    headers_dict.update({'Cookie':cs})
                    debug(headers_dict=headers_dict)
            debug(headers_dict = headers_dict)
        return headers_dict

    def UserAgent(self, user_agent_string):
        '''Get User-Agent
        
        Get user agent string from header (parserHeader Object)
        
        Arguments:
            user_agent_string {string header get 'User-Agent' Object} -- parserHeader Object
        '''
        c = parserheader()
        if isinstance(user_agent_string, dict):
            user_agent = c.parserHeader(headers).get('User-Agent')
        else:
            user_agent = user_agent_string
        user_agent_split = re.split(' ', user_agent, 1)
        if __name__ == '__main__':
            click.secho("Example Output Get User-Agent:", fg='white', bg='yellow')
            print("user_agent =", user_agent)
            print("user_agent_split =", user_agent_split)
            print("-" * (click.get_terminal_size()[0] - 1))
            print("\n")
        return user_agent, user_agent_split

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        click.secho("Example Get Input Data headers string:", fg='white', bg='cyan')
        example_header = """
    GET /L.O.R.D---Legend-Of-Ravaging-Dynasties- HTTP/1.1
    Host: tparser.org
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Referer: http://tparser.org/
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9
    Cookie: _ym_uid=1532996994661863820; _ym_d=1532996994; _ym_isad=2; tr=2 4 6 8 9 10
    """
        click.secho("Example Output Dictionary Headers:", fg='white', bg='magenta')
        print(c.parserHeader())
        c.setCookies(None)
        c.UserAgent(example_header)
        sys.exit(0)
    data = ''
    try:
        import clipboard
        data = clipboard.paste()
    except:
        try:
            data = sys.argv[1]
        except:
            pass
    try:
        data = sys.argv[1]
    except:
        pass
    
    headers = c.parserHeader(data)
    print(headers)
    import traceback
    try:
        clipboard.copy(str(headers))
    except:
        print(traceback.format_exc())