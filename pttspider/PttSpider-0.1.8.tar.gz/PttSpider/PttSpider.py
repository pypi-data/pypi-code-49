import requests
from fake_useragent import UserAgent
from pyquery import PyQuery as pq
import re


url = 'https://www.ptt.cc/bbs/index.html'
board = {}
title = {}
content = {}

def Get(url, headers="", cookies="", SLL_verify=True):
    ua = UserAgent().random
    if headers == "":
        headers = {'User-Agent': ua}
    res = requests.get(url, headers=headers, cookies=cookies, verify=SLL_verify)
    return res

def Get_Board():
    res = Get(url)
    data = pq(res.text)
    board_pack = data("div.b-ent")
    for item in board_pack:
        board_name = pq(item)("div.board-name").text()
        board[board_name] = {}
        board[board_name]["class"] = pq(item)("div.board-class").text()
        board[board_name]["title"] = pq(item)("div.board-title").text()
        board[board_name]["user"] = pq(item)("div.board-nuser").text()
        board[board_name]["url"] = "https://www.ptt.cc" + pq(item)("a.board").attr("href")
    print(board)
    return board


def Get_res(url):
    if re.findall(r"gossiping", url, re.IGNORECASE):
        cookies = {"over18": "1"}
        res = Get(url=url, cookies=cookies)
    else:
        res = Get(url=url)
    return res


def Get_Title(url="", board="", page=""):  # 爬取看板裡的標題
    if url == "":
        board_data = Get_Board()
        url = board_data[board]["url"]
        url = url[0:len(url) - len(".html")] + str(page) + ".html"
    res = Get_res(url=url)
    data = pq(res.text)
    rent = data('div.r-ent')
    titles = rent('div.title')
    dates = rent('div.date')
    for i in range(len(titles)):
        title = pq(titles[i])
        title[title.text()] = {}
        temp = title
        try:
            url = 'https://www.ptt.cc' + pq(title)('a').attr('href')
        except:  # 本文章已刪除
            url = '本文章已刪除'
        title[title.text()]["url"] = url
        title[title.text()]["date"] = (pq(dates[i]).text())
    print(title)
    return title


def Get_Content(url="", title=""):
    if url == "":
        url = title[title]["url"]
    res = Get_res(url=url)
    data = pq(res.text)("div#main-content.bbs-screen.bbs-content")
    article_pack = data("div.article-metaline")
    content['author'] = article_pack("span")[1].text
    content['title'] = article_pack("span")[3].text
    content['date'] = article_pack("span")[5].text
    article = data
    article('span').remove()
    article('div').remove()
    content['article'] = article.text()
    print(content)
    return (content)


if __name__ == '__main__':

    Get_Board()
    # Get_Title(board="Gossiping", page=4565)
    url = "https://www.ptt.cc/bbs/car/M.1567591551.A.F53.html"
    Get_Content(url=url)









