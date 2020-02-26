import requests
from fake_useragent import UserAgent
from pyquery import PyQuery as pq
import re

class ptt(object):

    def __init__(self):
        self.url = 'https://www.ptt.cc/bbs/index.html'
        self.board = {}
        self.title = {}
        self.content = {}

    def Get(self, url, headers="", cookies="", SLL_verify=True):
        ua = UserAgent().random
        if headers == "":
            headers = {'User-Agent': ua}
        res = requests.get(url, headers=headers, cookies=cookies, verify=SLL_verify)
        return res

    def Get_Board(self):
        res = self.Get(self.url)
        data = pq(res.text)
        board_pack = data("div.b-ent")
        for item in board_pack:
            board_name = pq(item)("div.board-name").text()
            self.board[board_name] = {}
            self.board[board_name]["class"] = pq(item)("div.board-class").text()
            self.board[board_name]["title"] = pq(item)("div.board-title").text()
            self.board[board_name]["user"] = pq(item)("div.board-nuser").text()
            self.board[board_name]["url"] = "https://www.ptt.cc"+ pq(item)("a.board").attr("href")
        print(self.board)
        return self.board

    def Get_res(self, url):
        if re.findall(r"gossiping", url, re.IGNORECASE):
            cookies = {"over18": "1"}
            res = self.Get(url=url, cookies=cookies)
        else:
            res = self.Get(url=url)
        return res

    def Get_Title(self, url="", board="", page=""):  # 爬取看板裡的標題
        if url == "":
            board_data = self.Get_Board()
            url = board_data[board]["url"]
            url = url[0:len(url) - len(".html")] + str(page) + ".html"
        res = self.Get_res(url=url)
        data = pq(res.text)
        rent = data('div.r-ent')
        titles = rent('div.title')
        dates = rent('div.date')
        for i in range(len(titles)):
            title = pq(titles[i])
            self.title[title.text()] = {}
            temp = self.title
            try:
                url = 'https://www.ptt.cc' + pq(title)('a').attr('href')
            except:  # 本文章已刪除
                url = '本文章已刪除'
            self.title[title.text()]["url"] = url
            self.title[title.text()]["date"] = (pq(dates[i]).text())
        print(self.title)
        return self.title

    def Get_Content(self, url="", title=""):
        if url == "":
            url = self.title[title]["url"]
        res = self.Get_res(url=url)
        data = pq(res.text)("div#main-content.bbs-screen.bbs-content")
        article_pack = data("div.article-metaline")
        self.content['author'] = article_pack("span")[1].text
        self.content['title'] = article_pack("span")[3].text
        self.content['date'] = article_pack("span")[5].text
        article = data
        article('span').remove()
        article('div').remove()
        self.content['article'] = article.text()
        print(self.content)
        return(self.content)


if __name__ == '__main__':
    obj = ptt()
    # obj.Get_Board()
    # obj.Get_Title(board="Gossiping", page=4565)
    url = "https://www.ptt.cc/bbs/car/M.1567591551.A.F53.html"
    obj.Get_Content(url=url)









