import requests


class AuthenticationException(Exception):
    def __init__(self):
        pass


class ConfluenceSite(object):
    def __init__(self, confluence_url: str, confluence_username: str, confluence_password: str,
                 confluence_target_space: str,
                 debug_mode: bool = False):
        self.debug_mode = debug_mode
        self.confluence_url = confluence_url.rstrip('/')
        self.confluence_username = confluence_username
        self.confluence_password = confluence_password
        if confluence_target_space is not None:
            self.confluence_target_space = confluence_target_space.lstrip('/')
        else:
            self.confluence_target_space = None
        self.cookies = None
        self.session = requests.session()
        self.login()

    def run(self):
        response = self.session.request(method="GET",
                                        url=f'{self.confluence_url}/display/{self.confluence_target_space}',
                                        cookies=self.session.cookies)
        print(response.text.encode('utf8'))

    def login(self):
        url = f"{self.confluence_url}/dologin.action"

        payload = f'login=Log%20in&os_destination=&os_password={self.confluence_password}&os_username={self.confluence_username}'
        headers = {
            'Origin': f'{self.confluence_url}',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
        response = self.session.request("POST", url, headers=headers, data=payload)
        self.cookies = response.cookies  # save cookies
        if self.debug_mode:
            print(response.text.encode('utf8'))
        # if response.status_code != 302:
        #     raise AuthenticationException()
