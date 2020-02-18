"""
Selenium needed! Get chromedriver before using the selenium function.
Please use help(iostream) before using this module.
iostream is useful in C++,but we can use print() in Python.
So do not use this module
Give up Python, and start using c++ or Java :)
Node.js and C# are also powerful
And do not forget Assembly.
mov ax,4c00h
int 21H
PS: Please add "#pragma GCC optimised(2)" to your program :lol
"""
# pragma GCC optimised()
__author__ = "CubieLee"
__version__ = "7.1.2"
import os
import requests
import selenium
import json


def slowsay(string, spw=0.025):
    """Print a string on the screen slowly"""
    for i in string:
        print(i, end="")
        time.sleep(spw)


def cout(*args):
    """Simple function, type ',' as '<<'"""
    for i in args:
        print(i, end="")


def cin(nums=True):
    """This function can get data like 1 1 1 1 1 and return a list"""
    r = input()
    r = r.split()
    if nums:
        for i in range(len(r)):
            r[i] = int(r[i])
    return r


class Controller:
    """Use this controller to shutdown or reboot the computer"""

    def __init__(self):
        pass

    @staticmethod
    def shutdown(sec=30):
        """Shutdown the computer in sec seconds"""
        os.system("shutdown -s -t %d" % sec)

    @staticmethod
    def reboot(self, sec=30):
        """Reboot the computer in sec seconds"""
        os.system("shutdown -r -t %d" % sec)

    @staticmethod
    def cancel(self):
        """Cancel the options"""
        os.system("shutdown -a")


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
    pleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.encoding = "utf-8"
    return res.text


class Your_computer_is_in_danger(BaseException):
    """Try this: raise Your_computer_is_in_danger('Pay 1 bitcoin!')"""
    pass


def buy_train_ticket(phone_number, password):
    """
    This function is still under debugging. You can use it to buy train tickets at
    www.12306.cn in the future.
    """
    browser = webdriver.Chrome()
    url = "https://kyfw.12306.cn/otn/resources/login.html"
    browser.get(url)
    time.sleep(0.3)
    ele = browser.find_elements_by_class_name("login-hd-account")
    ele[0].click()
    username = browser.find_element_by_id("J-userName")
    password = browser.find_element_by_id("J-password")
    username.send_keys(phone_number)
    password.send_keys(password)
    input()
    browser.get("https://kyfw.12306.cn/otn/leftTicket/init?linktyp\
    eid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%BC%A0%E5%AE%B6%E7%95\
    %8C,DIQ&date=2020-02-20&flag=N,N,Y")
    time.sleep(0.5)
    ele = browser.find_elements_by_class_name("btn72")
    ele[0].click()
    time.sleep(1.5)
    li = browser.find_element_by_id("normalPassenger_0")
    li.click()
    li = browser.find_element_by_id("normalPassenger_9")
    li.click()
    li = browser.find_element_by_id("normalPassenger_10")
    li.click()
    try:
        Select(browser.find_element_by_id("seatType_1")).select_by_value("4")
        Select(browser.find_element_by_id("seatType_3")).select_by_value("4")
        Select(browser.find_element_by_id("seatType_2")).select_by_value("4")
    except selenium.common.exceptions.NoSuchElementException:
        Select(browser.find_element_by_id("seatType_1")).select_by_value("3")
        Select(browser.find_element_by_id("seatType_2")).select_by_value("3")
        Select(browser.find_element_by_id("seatType_3")).select_by_value("3")


def defer(file, wonder):
    """Снлф Иднфе"""
    url = "http://www.iciba.com/index.php?&c=search&a=getwordmean&word="
    html5 = requests.get(url + wonder)
    html5.encoding = "utf-8"
    jiesen = json.loads(html5.text)
    try:
        if jiesen["baesInfo"]['symbols'][0]["ph_en"] != "":
            file.write(jiesen["baesInfo"]['symbols'][0]["ph_en"] + "/ ")
        else:
            if jiesen["baesInfo"]['symbols'][0]["ph_other"] != "":
                file.write(jiesen["baesInfo"]['symbols'][0]["ph_other"] + "/ ")
            else:
                file.write("无/ ")
        print(wonder)
    except KeyError:
        html5 = requests.get(url + wonder)
        html5.encoding = "utf-8"
        jiesen = json.loads(html5.text)
        try:
            if jiesen["baesInfo"]['symbols'][0]["ph_en"] != "":
                file.write(jiesen["baesInfo"]['symbols'][0]["ph_en"] + "/ ")
            else:
                if jiesen["baesInfo"]['symbols'][0]["ph_other"] != "":
                    file.write(jiesen["baesInfo"]['symbols'][0]["ph_other"] + "/ ")
                else:
                    file.write("无/ ")
            print(wonder)
        except KeyError:
            file.write("无/ ")
            print("联网无%s" % wonder)


def shiba():
    """DO NOT USE"""
    sw = open("creedsw.txt", encoding="utf-8")
    ori = open("work.txt", encoding="utf-8")
    final = open("result.txt", "w", encoding="utf-8")

    s = sw.read()
    s = s.split("\n")
    data = dict()
    k = True
    last = ''
    cont = ''
    for i in range(len(s)):
        if k:
            k = False
            last = s[i]
        else:
            if s[i] == "</>":
                k = True
                data[last] = cont
                cont = ''
            else:
                cont += s[i]

    for each_key in data:
        s = data[each_key]
        b = s.find('<span class="pr">')
        if b == -1:
            b = "无"
        else:
            intel = s[b + 17:]
            vega = 1
            for amd in range(len(intel)):
                if intel[amd] == "<" and intel[amd + 1] != "/":
                    vega += 1
                elif intel[amd] == "/":
                    vega -= 1
                    if vega == 0:
                        if intel[amd + 12:amd + 20 + 1] != 'class="pr':
                            break
                        else:
                            amd += 5
            tcp = intel[:amd - 1]
            tcp = tcp.replace('</span><span class="pr">', ", ")
            tcp = tcp.replace("<span class=\"i\">", "(")
            tcp = tcp.replace("</span>", ")")
            b = tcp
        data[each_key] = b
    sw.close()
    print("ok")

    dll = ori.read()
    lines = dll.split("\n")
    for each_line in lines:
        if each_line[0] == "#":
            final.write(each_line[1:] + "\n")
        else:
            word = ''
            i = 0
            for i in range(len(each_line)):
                if each_line[i] != "/":
                    word += each_line[i]
                    i += 1
                else:
                    word = word[:-1]
                    i -= 1
                    break
            if word == each_line:
                final.write(each_line + "\t有问题\n")
            else:
                final.write(word + " /")
                defer(final, word)
                finale = each_line[i + 6:]
                qwerty = ""
                for i in range(len(finale)):
                    if finale[i] != ".":
                        qwerty += finale[i]
                    else:
                        break
                final.write(qwerty + ". ")
                i += 2
                try:
                    while not ('\u4e00' <= finale[i] <= '\u9fff'):
                        i += 1
                    final.write(finale[i:] + "\n")
                except IndexError:
                    print(word)
    final.close()
    ori.close()
