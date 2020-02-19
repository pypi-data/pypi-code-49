#! python3
'''
calculate stock's pe at hk ipo
example:
    import analyse.data.pehkipo.getpe as getpeipo
    code = "00788"
    print(getpeipo(code))
'''
import re
import lxml.html
import urllib.request
import pandas as pd

def  getpe(code):
    currency_list = ['人民币','港元','美元','新加坡元','英镑']
    unit_list = ['千','百万']
    market_value_url = "http://www.aastocks.com/sc/stocks/market/ipo/\
                        upcomingipo/company-summary?symbol={}#info".format(code)
    income_url = "http://www.aastocks.com/sc/stocks/market/ipo/upcomingipo/\
                        profit-loss?symbol={}&s=3&o=1#info".format(code)
    market_value_page = urllib.request.urlopen(market_value_url).read().decode("utf-8")
    market_value_root = lxml.html.document_fromstring(market_value_page)
    market_value_str = market_value_root.xpath(".//table[@id='IPOInfo']//tr")[2].\
                                               text_content().replace(",","")
    market_value_base = re.findall("\d+",market_value_str)
    market_value_low = float(market_value_base[0])
    market_value_high = float(market_value_base[1])
    ipo_price = market_value_root.xpath(".//table[@id='IPOInfo']//tr")[1].\
                                         text_content().replace("招股价","").strip()
    income_page = urllib.request.urlopen(income_url).read().decode("utf-8")
    income_root = lxml.html.document_fromstring(income_page)
    currency = income_root.xpath(".//tr[.//td[text() = '货币']]//td")[1].text_content()
    unit = income_root.xpath(".//tr[.//td[text() = '单位']]//td")[1].text_content()
    if currency not in currency_list :
        print("add a new currency_list for {}".format(currency))
        return
    if currency == "港元":
        ex = 1
    elif currency == "人民币":
        ex = getex("rmb_hkd")
    elif currency == "美元":
        ex = getex("usd_hkd")
    elif currency == "新加坡元":
        ex = getex("xsd_hkd")
    if unit not in unit_list:
        print("add a new unit {} to calculate".format(unit))
        return
    if unit == '千':
        unit_value = 1000
    elif unit == '百万':
        unit_value = 1000000
    income_str = income_root.xpath(".//tr[.//td[text() = '股东应占溢利']]//td")[1].\
                                   text_content().replace(",","")
    income = ex*float(income_str)*unit_value
    code = code
    data = [code,ipo_price,income,market_value_low,market_value_high,\
            round(market_value_low/income,2),round(market_value_high/income,2)]
    col = ["代码","招股价","最近一年收益","市值_low","市值_high","pe_low","pe_high"]
    pe_df =pd.DataFrame([data],columns=col)
    return  pe_df


def getex(ex):
    ex_url = "https://www.bochk.com/whk/rates/exchangeRatesHKD/\
              exchangeRatesHKD-input.action?lang=en"
    ex_page = urllib.request.urlopen(ex_url).read().decode("utf-8")
    ex_root = lxml.html.document_fromstring(ex_page)
    if ex == "rmb_hkd":
        exrate = ex_root.xpath(".//tr[.//td[text() = 'CNY']]/td")[1].\
                                text_content().strip()
        exrate =  round(float(exrate),4)
    elif ex == "usd_hkd":
        exrate = ex_root.xpath(".//tr[.//td[text() = 'USD']]/td")[1].\
                                text_content().strip()
        exrate =  round(float(exrate),4)
    elif ex == "sgd_hkd":
        exrate = ex_root.xpath(".//tr[.//td[text() = 'SGD']]/td")[1].\
                                text_content().strip()
        exrate =  round(float(exrate),4)
    return exrate
