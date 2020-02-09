from selenium import webdriver


def get_local_ip_by_quick_connect_id(q_id):
    """
    # if nas local ip changed, get ip according to quick_connect
    # see https://quickconnect.to/
    :param q_id: QuickConnect ID
    :return:
    """
    url = f"https://{q_id}.quickconnect.to/"
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get(url)
    driver.implicitly_wait(20)
    cookie = driver.get_cookies()
    dict1 = cookie[2]
    value1 = dict1['value']
    return value1.split('ipv4.')[1].split('.wan')[0]
