import sys
import mechanicalsoup

def text(url):
    # Connect to target
    browser = mechanicalsoup.StatefulBrowser()

    try:
        status = browser.open(url)
        if 'text/' in status.headers['Content-Type']:
            pass
        else:
            pass

    except:
        pass

    # All functions for get values
    def all():
        value = ""
        for p in browser.get_current_page().select('p'):
            value = value + p.text + ' '

        for h1 in browser.get_current_page().select('h1'):
            value = value + h1.text + ' '

        for link in browser.get_current_page().select('a'):
            value = value + link.text + ' '

        return value
    # All texts
    try:
        return all()
    except:
        return "Not any texts :("

def listed(url):
    return list(set(text(url).translate(str.maketrans('', '', '\n\t')).replace('—','').replace(',','').replace('|','').split(" ")))
