
import requests
from lxml import etree


headers = {
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}

base_url = 'https://www.allacronyms.com/'


def get_abbr(query: str):
    """
    :param query: the query string, example: "China Eastern Airlines"
    :return:
    """
    # query = 'China Eastern Airlines'
    url = base_url + '_'.join(query.lower().split(' ')) + '/abbreviated'
    abbr_sets = []

    try:
        html = requests.get(url=url, headers=headers).text
    except Exception as e:
        print(e)
        return abbr_sets

    elements = etree.HTML(html)

    try:
        for element in elements.xpath(
                "//div[@class='terms']/div[@class='terms_items']//div[@class='item_container']"):
            abbr_sets.append(element.xpath('string()').replace('\n', '').strip())
    except Exception as e:
        print(e)
    return abbr_sets


#
# # input query
# query = 'China Eastern Airlines'
#
# base_url = 'https://www.allacronyms.com/'
#
# forward_url = base_url + '_'.join(query.lower().split(' ')) + '/abbreviated'
# backward_url = base_url + query.capitalize()
#
# r = requests.get(url=forward_url, headers=headers)
#
# element = etree.HTML(r.text)
#
# table = element.xpath("//div[@class='terms']/div[@class='terms_items']/table")[0]
# table.xpath('string()').split('\n')


# 需求
# 给定一个字符串，拿到其缩写

# def get_abbr(query: str, from_web=True, ):
#     """
#     :param query: the query string, example: "China Eastern Airlines"
#     :param from_web: get abbreviation from local or internet
#     :return:
#     """
#     conn = sqlite3.connect("abbr.db")
#     cursor = conn.cursor()
#     # sql = 'create table abbr (string1 VARCHAR , string2 VARCHAR )'
#     sql = "insert into abbr (string1, string2) values ('china', 'ca')"
#     cursor.execute(sql)
#     cursor.close()
#     conn.close()
#
#     conn = sqlite3.connect("abbr.db")
#     cursor = conn.cursor()
#     # sql = 'create table abbr (string1 VARCHAR , string2 VARCHAR )'
#     sql = "select string1,string2  from abbr"
#     cursor.execute(sql)
#     cursor.close()
#     conn.close()


