import os,re,time
import lxml.html
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(browser, 20)

cbondfile = os.path.join(os.environ['HOME'],'cbond.csv')

def info():
    if os.path.isfile(cbondfile) :
        df = pd.read_csv(cbondfile,sep=',',header=0)
    else : 
        df = update()
    return df


def update():
    if os.path.isfile(cbondfile) : df_bak = pd.read_csv(cbondfile,sep=',',header=0)
    try:
        fields = []
        url = "https://www.jisilu.cn/data/cbnew/#cb"
        browser.get(url)
        wait.until(lambda e: e.execute_script('return document.readyState') != "loading")
        range = browser.find_element_by_id('flex_cb')
        content = range.get_attribute('innerHTML')
        with open('/tmp/bond.html', "w", encoding='utf-8') as fh:
            fh.write(content)
        root = lxml.html.document_fromstring(open('/tmp/bond.html','r').read())
        header = root.xpath('.//thead/tr')[1].xpath('//th')
        for item in header:
             fields.append(''.join(item.text_content().split()))
        tmp_fields = []
        for idx,item in enumerate(fields):
            if idx not in [7,9,10,11,12,13,16,17,20,21,22,23,24,25,26]:
               tmp_fields.append(fields[idx])
        tmp_fields.extend(['正股名称','正股代码','转股起始日','发行规模','剩余规模'])    
        fields = tmp_fields
        data_row = root.xpath('.//tr')[2:]
        df = pd.DataFrame(columns = fields)
        for bond_info in data_row:
            every_bond = []
            for idx,item in enumerate(bond_info.xpath('.//td')):
                if idx == 0 :
                    other_info = get_element(item.text_content())
                if idx not in [7,9,10,11,12,13,16,17,20,21,22,23,24,25,26]:        
                    every_bond.append(''.join(item.text_content().split()))
            every_bond.extend([other_info['正股名称'],other_info['正股代码'],other_info['转股起始日'],other_info['发行规模'],other_info['剩余规模']])
            df.loc[len(df)] = every_bond
        df[['现价','正股价','剩余年限' ]] = pd.DataFrame(df[['现价','正股价','剩余年限']],dtype=np.float)
        df['转股价'] = df['转股价'].apply(lambda x: float(x.replace('*','')))
        df['回售触发价'] = df['回售触发价'].apply(lambda x: 0 if x == '-' else x)
        df['强赎触发价'] = df['强赎触发价'].apply(lambda x: 0 if x == '-' else x)
        df['正股涨跌'] = df['正股涨跌'].apply(lambda x:  round(float(x.replace('%',''))/100,4))
        df['涨跌幅'] = df['涨跌幅'].apply(lambda x:  round(float(x.replace('%',''))/100,4))
        curprice = df['现价']
        stockprice = df['正股价']
        conprice = df['转股价']
        premium =  (100/conprice)*stockprice/curprice - 1
        premium = premium.apply(lambda x: round(x,4))
        df['转股溢价率'] = premium
        os.remove(cbondfile)
        df.to_csv(cbondfile,index=False)
    except:
        print("update failure,please use the old data")
        df = df_bak
        del df_bak
    return df


def get_element(code):
    import lxml.html
    import urllib.request
    url="https://www.jisilu.cn/data/convert_bond_detail/{}".format(code)
    page = urllib.request.urlopen(url).read().decode("utf-8")
    root = lxml.html.document_fromstring(page)
    content = root.xpath('.//table[@class="jisilu_tcdata"]')[0]
    name_string = content.xpath('.//tr/td')[0].text_content()
    parsed = re.search("\(正股：(\S+).+?(\d+)",name_string)
    stock_name = parsed.group(1)
    stock_code = parsed.group(2)
    date = content.xpath('.//td[text()="转股起始日"]/following-sibling::td')[0].text
    scale_issue = content.xpath('.//td[text()="发行规模(亿)"]/following-sibling::td')[0].text
    scale_remain = content.xpath('.//td[text()="剩余规模(亿)"]/following-sibling::td')[0].text
    time.sleep(1)
    return  {'正股名称':stock_name ,'正股代码':stock_code,'转股起始日':date,'发行规模':scale_issue,'剩余规模':scale_remain}


