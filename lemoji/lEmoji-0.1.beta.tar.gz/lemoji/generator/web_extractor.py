import requests

from bs4 import BeautifulSoup as Souper, Tag

proxies = {
  "http": "http://localhost:1087",
  "https": "http://localhost:1087",
}


class WebExtractor:
    base_url = 'https://www.unicode.org/Public/emoji/'

    @staticmethod
    def emoji_fetcher(url):
        print('Retrieving', url, '...')
        r = requests.get(url, proxies=proxies)
        data = r.content.decode()
        r.close()

        lines = list(filter(lambda line_: not line_.startswith('#'), data.split('\n')))
        lines = list(filter(lambda line_: line_.find(';') >= 0, lines))
        lines = list(map(lambda line_: line_[:line_.find(';') - 1].strip(), lines))

        emoji_list = []
        for line in lines:
            seq_mark = line.find('..')
            if seq_mark > 0:
                left = int(line[:seq_mark], 16)
                right = int(line[seq_mark+2:], 16)
                emoji_list.extend(map(chr, range(left, right + 1)))
            else:
                emoji_list.append(''.join(map(lambda s: chr(int(s, 16)), line.split(' '))))

        return emoji_list

    @classmethod
    def analyse(cls, url):
        r = requests.get(url, proxies=proxies)
        soup = Souper(r.content.decode(), 'html.parser')
        r.close()

        img_list = soup.find_all('img')
        node_list = []
        for img in img_list:  # type: Tag
            if img.get('src') == '/icons/folder.gif':
                type_ = 'folder'
            elif img.get('src') == '/icons/text.gif':
                type_ = 'file'
            else:
                continue
            a_tag = img.next_element.next_element  # type: Tag
            node = dict(
                type=type_,
                link=url + a_tag.get('href'),
                name=a_tag.text,
            )
            if node['name'].endswith('/'):
                node['name'] = node['name'][:-1]

            time = a_tag.next_sibling  # type: str
            time = time.strip()
            time = time[:time.rfind(' ')].strip()
            node['time'] = time
            node_list.append(node)

        return node_list

    @classmethod
    def build(cls, url=None):
        url = url or cls.base_url
        print('Retrieving', url, '...')
        node_list = cls.analyse(url)
        for node in node_list:
            if node['type'] == 'folder':
                node['children'] = cls.build(node['link'])
        return node_list
