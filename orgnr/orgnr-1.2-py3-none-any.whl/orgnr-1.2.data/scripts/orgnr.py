import requests
import re
from bs4 import BeautifulSoup

base = 'https://allabolag.se/'

def create_json(orgnr, title):
    json = {
        "result": {
            "title": title,
            "orgnr": orgnr
        }
    }
    return(json)

def get_orgnr(orgnr):
    orgnr = re.sub('\D', '', orgnr)
    url = base + orgnr
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    try:
        data = soup.find("div", {"class": "informationcontainer"})
        title = data.find_next('h1')
        json = create_json(orgnr, title.text)
        print(json)
    except:
        json = {
            "result": {
                "error": "404",
                "msg": "Orgnr {} not found".format(orgnr)
            }
        }
        print(json)