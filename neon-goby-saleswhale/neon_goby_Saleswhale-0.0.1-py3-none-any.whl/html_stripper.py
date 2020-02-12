from html.parser import HTMLParser
import re

# ref: https://stackoverflow.com/a/925630
class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []

    def handle_data(self, data):
        self.fed.append(data)

    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = HTMLStripper()
    s.feed(html)
    stripped_data = s.get_data()
    return re.sub("(<!--.*?-->)", "", stripped_data, flags=re.DOTALL)
