import bs4
import requests
class Stock:
  def __init__(self,symbol):
    self.symbol = symbol
    self.r = requests.get('https://old.nasdaq.com/symbol/{}'.format(symbol.lower()))
    self.html = self.r.text
    self.soup = bs4.BeautifulSoup(self.html,'html.parser')
    self.a = self.soup.find('div',{'id':'qwidget_quote'})
    self.t = self.soup.find('div',{'id':'qwidget_pageheader'})
  def price(self,verbose=False):
    try:
      rt = self.a.find_all('div')[0].text
      if rt.strip() == self.symbol.upper():
        return self.a.find_all('div')[1].text
      else:
        return self.a.find_all('div')[0].text
    except Exception as e:
      if verbose:
        return e
      else:
        return None
  def company(self,verbose=False):
    try:
      return self.t.find_all('h1')[0].text
    except Exception as e:
      if verbose:
        return e
      else:
        return None
