## -*- coding: utf-8 -*-
# Founder138 v1.2.5
import requests, re
__all__ = ['ip', 'mobile', {"zip_zone": ["area2zip", "zip2area", "area2zone", "zone2area"]}]
__version__  = "1.2.5"
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 Edg/80.0.361.48"
get = lambda text, mode: requests.get("https://m.ip138.com/{}.asp".format(mode), params = {mode: text}, headers = {"User-Agent": ua}).text

class AreaError(Exception):
    def __init__(self, error):
        super().__init__(self)
        self.info = error

    def __str__(self):
        return self.info

class ZipCodeError(Exception):
    def __init__(self, error):
        super().__init__(self)
        self.info = error

    def __str__(self):
        return self.info

class ZoneCodeError(Exception):
    def __init__(self, error):
        super().__init__(self)
        self.info = error

    def __str__(self):
        return self.info

class ModeError(Exception):
    def __init__(self, error):
        super().__init__(self)
        self.info = error

    def __str__(self):
        return self.info

class IDNumberError(Exception):
    def __init__(self, error):
        super().__init__(self)
        self.info = error

    def __str__(self):
        return self.info

class ProvinceError(Exception):
    def __init__(self, error):
        super().__init__(self)
        self.info = error

    def __str__(self):
        return self.info

def get_list_indexes(text, aims):
    """
    从列表中找出目标文本的所有索引值。
    """
    if type(text) != list: raise TypeError("This must be list type. ")
    info  = []
    a = 0
    for i in text:
        if i == aims: info.append(a)
        a += 1
    return info

def ip(text):
    if type(text) != str: raise TypeError('"text" must be a string. ')
    ip_text = get(text=text, mode="ip")
    info = {}
    try:
        info["您查询的IP"] = (re.findall('<h1 class="query">您查询的IP：(.*?)</h1>', ip_text)[0])
        info["主数据"] = (re.findall('<p class="result">本站主数据：(.*?)</p>', ip_text)[0])
        info["参考数据"] = (re.findall('<p class="result">参考数据一：(.*?)</p>', ip_text)[0])
    except: raise ValueError("Can't found infomations. The IP address can be wrong. ")
    return info

def mobile(text):
    if type(text) != str: raise TypeError('"text" must be a string. ')
    mobile_text = get(text=text, mode="mobile")
    info = {}
    try:
        info["卡号归属地"] = (re.findall('<tr><td>卡号归属地</td><td><span>(.*?)</span></td></tr>', mobile_text)[0])
        info["卡类型"] = (re.findall('<tr><td>卡 类 型</td><td><span>(.*?)</span></td></tr>', mobile_text)[0])
        info["电话区号"] = (re.findall('<tr><td>区 号</td><td><span>(.*?)</span></td></tr>', mobile_text)[0])
        info["邮编"] = (re.findall('<tr><td>邮 编</td><td><span>(.*?)</span></td></tr>', mobile_text)[0])
    except: raise ValueError("Can't found infomations. The Phone Number can be wrong. ")
    return info

class zip_zone:
    def __init__(self, text):
        self.text = text
    
    def area2zip(self):
        a2z_text = requests.get("https://m.ip138.com/youbian/youbian.asp", params={"area": self.text, "action": "area2zip"}, headers={"User-Agent": ua})
        a2z_text.encoding = "utf-8"
        a2z_text = a2z_text.text
        r = re.findall('''<p class="query-hd"><ul id='dantiao'><li>(.*?)邮政编码</li><li>(.*?)</li></ul></p>''', a2z_text)
        if r == []: 
            r = re.findall("""<li><span>(.*?)</span><span>(.*?)</span></li>""", a2z_text)
        info = {}
        for i in range(len(r)): info[r[i][1]] = []
        for i in range(len(r)):
            try: info[r[i][1]].append(r[i][0])
            except: raise AreaError("Can't found this area. ")
        return info
    
    def zip2area(self):
        z2a_text = requests.get("https://m.ip138.com/youbian/youbian.asp", params={"zip": self.text, "action": "zip2area"}, headers={"User-Agent": ua})
        z2a_text.encoding = "utf-8"
        z2a_text = z2a_text.text
        try:
            r = re.findall("""<li><span>(.*?)</span><span>(.*?)</span></li>""", z2a_text)
            r.pop(0)
        except: raise ZipCodeError("Can't found this zip code. ")
        info = {}
        for i in r:
            if i[0] in info.keys(): info[i[0]].append(i[1])
            else: info[i[0]] = [i[1]]                
        return info
    
    def area2zone(self):
        a2z_text = requests.get("https://m.ip138.com/youbian/youbian.asp", params={"area": self.text, "action": "area2zone"}, headers={"User-Agent": ua})
        a2z_text.encoding = "utf-8"
        a2z_text = a2z_text.text
        r = re.findall("""<p class="query-hd"><ul id='dantiao'><li>(.*?)区号</li><li>(.*?)</li></ul></p>""", a2z_text)
        if r == []: r = re.findall("<li><span>(.*?)</span><span>(.*?)</span></li>", a2z_text)
        info = {}
        for i in range(len(r)):
            try: info[r[i][0]] = r[i][1]
            except: raise AreaError("Can't found this area. ")
        return info
    
    def zone2area(self):
        z2a_text = requests.get("https://m.ip138.com/youbian/youbian.asp", params={"zone": self.text, "action": "zone2area"}, headers={"User-Agent": ua})
        z2a_text.encoding = "utf-8"
        z2a_text = z2a_text.text
        try:
            r = re.findall("""<li><span>(.*?)</span><span>(.*?)</span></li>""", z2a_text)
            r.pop(0)
        except: raise ZoneCodeError("Can't found this zip code. ")
        info = {}
        for i in r:
            if i[0] in info.keys(): info[i[0]].append(i[1])
            else: info[i[0]] = [i[1]]                
        return info

class idcard:
    def __init__(self, text):
        if type(text) != str: raise TypeError('"text" must be a string. ')
        self.text = text
    def id_info(self):
        if len(self.text) == 15: self.t = idcard(self.text).upto18()["升位后号码"]
        elif len(self.text) == 18: self.t = self.text
        else: raise TypeError('"text" must be a string of 15 or 18.')
        id_text = requests.get("http://qq.ip138.com/idsearch/index.asp", params = {"userid": self.t, "action": "idcard"}, headers = {"User-Agent": ua})
        id_text.encoding = "utf-8"
        id_text = id_text.text
        r = re.findall("""<td><p>(.*?)</p></td><td><p>(.*?)</p></td>""", id_text)
        for i in range(len(r)): r[i] = list(r[i])
        try:  r[3][1] = r[3][1].replace(" <br/>", "")
        except: raise IDNumberError("ID Number format error. ")
        if '<font color="red">提示：该18位身份证号校验位不正确，您可以使用我们的15位升18位的小工具来验证</font>' in r[3][1]: raise IDNumberError("ID Number format error. ")
        for i in range(len(r)): r[i] = tuple(r[i])
        info = {}
        for i in r: info[i[0]] = i[1]
        info['您查询的身份证号码'] =self.text
        return info
    
    def upto18(self):
        if len(self.text) != 15: raise TypeError('"text" must be a string of 15.')
        id_text = requests.get("http://qq.ip138.com/idsearch/index.asp", params = {"userid": self.text, "action": "upto18"}, headers = {"User-Agent": ua})
        id_text.encoding = "utf-8"
        id_text = id_text.text
        r = re.findall("<tr><td><p>(.*?)</p></td><td><p>(.*?)</p></td></tr>", id_text)
        info = {"升位前号码": self.text}
        try: info[r[0][0]] = r[0][1]
        except: raise IDNumberError("ID Number type error. ")
        return info


def carlist(all, *province):
    """
    如果all为False，必须提供省份信息！若all为True，不得提供省份信息！
    """
    provinces = [
        ["北京市", "京", "beijing"],
        ["上海市", "沪", "shanghai"],
        ["天津市", "津", "tianjin"],
        ["重庆市", "渝", "chongqing"],
        ["河北省", "冀", "hebei"],
        ["河南省", "豫", "henan"],
        ["云南省", "云", "yunnan"],
        ["辽宁省", "辽", "liaoning"],
        ["黑龙江省", "黑", "heilongjiang"],
        ["湖南省", "湘", "hunan"],
        ["安徽省", "皖", "anhui"],
        ["山东省", "鲁", "shandong"],
        ["新疆维吾尔自治区", "新", "xinjiang"],
        ["江苏省", "苏", "jiangsu"],
        ["浙江省", "浙", "zhejiang"],
        ["江西省", "赣", "jiangxi"],
        ["湖北省", "鄂", "hubei"],
        ["广西壮族自治区", "桂", "guangxi"],
        ["甘肃省", "甘", "gansu"],
        ["山西省", "晋", "shanx"],
        ["内蒙古自治区", "蒙", "neimenggu"],
        ["陕西省", "陕", "shanxi"],
        ["吉林省", "吉", "jilin"],
        ["福建省", "闽", "fujian"],
        ["贵州省", "贵", "guizhou"],
        ["广东省", "粤", "guangdong"],
        ["四川省", "川", "sichuan"],
        ["青海省", "青", "qinghai"],
        ["西藏自治区", "藏", "xizang"],
        ["海南省", "琼", "hainan"],
        ["宁夏回族自治区", "宁", "ningxia"]
    ]
    if province != ():
        province = province[0]
    if not type(all) == bool:
        raise TypeError('Variable "all" the wrong type of text, this value should be of type bool. ')
    if all == True and type(province) != tuple:
        raise ValueError('Variable "all" has been selected, "province" must not be selected. ')
    if all == False and type(province) == tuple:
        raise ValueError('Variable "all" is not selected, "province" must provide the information. ')
    provinces_1 = []
    for i in range(31):
        provinces_1.append(provinces[i][0])
        provinces_1.append(provinces[i][1])
    if not province in provinces_1 and province != (): raise ProvinceError("This province not found. ")
    if province != ():
        if provinces_1.index(province) % 2 == 1: propy1 = int(provinces_1.index(province) / 2 - 0.5)
        if provinces_1.index(province) % 2 == 0: propy1 = int(provinces_1.index(province) / 2)
        propy = provinces[propy1][2]
    cl_text = requests.get("http://www.ip138.com/carlist.htm", headers = {"User-Agent": ua})
    cl_text.encoding = "utf-8"
    cl_text = cl_text.text
    r = re.findall("<td>(.*?)</td><td>(.*?)</td>", cl_text)
    r = str(r)
    r = r.replace(", ('&nbsp;', '&nbsp;')", "")
    r = eval(r)
    prodict = {}
    for i in provinces: prodict[i[1]] = {}
    for i in r: prodict[i[0][0]][i[0]] = i[1]
    if all: return prodict
    else: return prodict[provinces[propy1][1]]

def carNo(text):
    """
    提供车牌区号或地区名text查询另一项
    """
    if text == "云AV": return "东川区"
    if type(text) not in [str, list]: raise TypeError('"text" must be string or list.')
    cl_text = requests.get("http://www.ip138.com/carlist.htm", headers = {"User-Agent": ua})
    cl_text.encoding = "utf-8"
    cl_text = cl_text.text
    r = re.findall("<td>(.*?)</td><td>(.*?)</td>", cl_text)
    r = str(r)
    r = r.replace(", ('&nbsp;', '&nbsp;')", "")
    r = eval(r)
    dic = {}
    for i in r: dic[i[0]] = i[1]
    keys, values = list(dic.keys()), list(dic.values())
    if type(text) == str:
        if text in keys: return {text: values[keys.index(text)]}
        elif text in values:
            indexes = get_list_indexes(text=values, aims=text)
            city = []
            for i in indexes: city.append(keys[i])
            return {text: city}
        else: raise ValueError("Can't found this text online. ")
    if type(text) == list:
        info = {}
        for i in text:
            if i in keys: info[i] = values[keys.index(i)]
            elif i in values:
                indexes = get_list_indexes(text=values, aims=i)
                city = []
                for n in indexes: city.append(keys[n])
                info[i] = city
            else:
                info[i] = None
                print('''Error: Can't found text "{}" online. '''.format(i))
        return info
