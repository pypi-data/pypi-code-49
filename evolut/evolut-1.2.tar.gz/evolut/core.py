#The Content has been made available for informational and educational purposes only
import cfscrape,urllib3
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context, DEFAULT_CIPHERS
from fake_headers import Headers
# urllib3.util.ssl_.DEFAULT_CIPHERS = DEFAULT_CIPHERS
DEFAULT_CIPHERS += ':!SHA1'

def evolut(account):
    class CustomAdapter(HTTPAdapter):
        def init_poolmanager(self, *args, **kwargs):
            ctx = create_urllib3_context(ciphers=DEFAULT_CIPHERS)
            super(CustomAdapter, self).init_poolmanager(*args, ssl_context=ctx, **kwargs)

    header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
    )
    scraper = cfscrape.create_scraper()
    scraper.mount('https://', CustomAdapter())
    url = "https://twitter.com/account/begin_password_reset"
    #print(url)
    req = scraper.get(url,headers=header.generate())
    soup = BeautifulSoup(req.text, 'html.parser')
    authenticity_token = soup.input.get('value')
    data = {
      'authenticity_token': authenticity_token,
      'account_identifier': account
    }
    cookies = req.cookies
    response = scraper.post(url, cookies=cookies, data=data,headers=header.generate())
    soup2 = BeautifulSoup(response.text, 'html.parser')
    try:
        if(soup2.find('div', attrs = {'class' : 'is-errored'}).text=="Please try again later."):
            return("Rate limit change your ip")
    except:
        pass
    try:
        info = soup2.find('ul', attrs = {'class' : 'Form-radioList'}).findAll("strong")
    except:
        return("Not email or phone")
    try:
        phone = int(info[0].text)
        phone = str("XX XX XX XX" +phone)
        email = str(info[1].text)
    except:
        email = str(info[0].text)
    if(len(info)==2):
        return({"phone":phone,"email":email})
    else:
        return({"email":email})
