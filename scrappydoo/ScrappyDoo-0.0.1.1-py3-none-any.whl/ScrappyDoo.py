import requests
from lxml import html
from bs4 import BeautifulSoup

class ScrappyDoo():
    def __init__(self,url):
        self.url = url

    def login_page(self,login_url,username,password):
        with requests.Session() as s:
            site = s.get(login_url)
            bs_content = BeautifulSoup(site.content, "html.parser")
            token = bs_content.find("input", {"name":"csrf_token"})["value"]
            login_data = {"username":username,"password":password, "csrf_token":token}
            s.post("http://quotes.toscrape.com/login",login_data)
            self.load_page()
    
    def load_page(self):
        page = requests.get(self.url)
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def find_element(self,element_type):
        results = self.soup.find_all(element_type)
        return results

    def find_table(self,match_headers=None):
        results = self.find_element("table")
        if (match_headers is not None):
            for result in results:
                print("Next Result...")
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
                    return result
        else: #if headers are not specified then return all tables from the page
            return results

    def find_table_headers(self,table):
        table_headers = []
        for tx in table.find_all('th'):
            tx_t = tx.get_text()
            if tx_t != "":
                table_headers.append(tx_t)
        return table_headers