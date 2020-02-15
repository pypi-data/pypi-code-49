from .scraper import Stock
if __name__ == '__main__':
  symbol = input('Enter Symbol:')
  r = requests.get('https://old.nasdaq.com/symbol/{}'.format(symbol.lower()))
  html = r.text
  soup = bs4.BeautifulSoup(html,'html.parser')
  a = soup.find('div',{'id':'qwidget_quote'})
  t = soup.find('div',{'id':'qwidget_pageheader'})
  print('Scraping {}'.format(r.url))
  try:
    rt = a.find_all('div')[0].text
    if rt.strip() == symbol.upper():
      print('Company: {}'.format(t.find_all('h1')[0].text))
      print('Price: {}'.format(a.find_all('div')[1].text))
    else:
      print('Company: {}'.format(t.find_all('h1')[0].text))
      print('Price: {}'.format(rt))
  except Exception as e:
    print('Symbol not found')
    print('Error {}'.format(e))
