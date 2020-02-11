import requests
from lxml import html
from bs4 import BeautifulSoup

class ScrappyDoo():
    def __init__(self,url):
        self.url = url
        self.session = requests.Session()

    def login_page(self,login_url,username,password,username_element="email",password_element="password",enable_csrf=False):
        site = self.session.get(login_url)
        bs_content = BeautifulSoup(site.content, "html.parser")
        if enable_csrf:
            csrf_wrapper = bs_content.find("input", {"name":"csrf_token"})
            token = csrf_wrapper["value"]
            login_data = {username_element:username,password_element:password, "csrf_token":token}
        else:
            login_data = {username_element:username,password_element:password}
        self.session.post(login_url,login_data)
        self.load_page()
    
    def load_page(self):
        page = self.session.get(self.url)
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def find_tables(self,match_headers=None):
        results = self.soup.find_all("table")
        tables = []
        for result in results:
            if (match_headers is not None):
                headers = self.find_table_headers(result)
                headers_matched = True
                if len(headers) == len(match_headers):
                    for h,m_h in zip(match_headers,headers):
                        if h != m_h:
                            headers_matched = False
                            break
                else:
                    headers_matched = False
                if (headers_matched):
                    print("Headers matched in table")
                    tables.append(result)
            else:
                tables.append(result) #if headers are not specified then return all tables from the page

    def find_table_headers(self,table):
        table_headers = []
        for tx in table.find_all('th'):
            tx_t = tx.get_text()
            if tx_t != "":
                table_headers.append(tx_t)
        return table_headers