from k_functions import *

"""
input: [楼盘坐标.csv]
output: [附近1公里楼盘.csv]
function:
    自己搭建的一个异步爬虫框架，很完美的应用！！（可作为模板，之后重复利用）
api:
    [in_file_name,
    out_file_name
    DISTANCE (自定义周边距离)]

tips: []
warning: []
"""
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

db = client["zufang_001"]
req = myRequest().req


# @decorate_error_log
def req_and_parse_detail_page(url):
    # 打印正在运行的函数名
    print(sys._getframe().f_code.co_name)
    # 请求url，获得response对象
    response = req(url, selector=True)
    try:
        item = {}
        house_id = re.findall(r".*?/(\w+).html", url)[0]
        # 针对每个房源的个性标签
        room_title = response.xpath("/html/body/div[3]/div[1]/div[2]/div[2]/div[2]//text()").extract()
        room_title = "".join(room_title)

        room_list_box = response.xpath("/html/body/div[3]/div[1]/div[2]/div[2]/div[4]")
        print(room_list_box)
        for e in room_list_box:
            housing_area = e.xpath("./div[1]/div[1]/label/text()").re(r"约(\d+)")[0]
            house_numbering = e.xpath("./div[1]/div[2]/label/text()").re(r"编号：(\d+.*?\w)")[0]
            shi = e.xpath("./div[1]/div[3]/label/text()").re(r"户型：(\d+)室(\d+)卫")[0]
            wei = e.xpath("./div[1]/div[3]/label/text()").re(r"户型：(\d+)室(\d+)卫")[1]


        # 把所有字段映射放入item字典中
        item["house_id"] = house_id

        item["housing_area"] = housing_area
        item["house_numbering"] = house_numbering
        item["shi"] = shi
        item["wei"] = wei

        print(item, "\n\n")
        return item

    except Exception as e:
        tb_txt = traceback.format_exc(limit=1)
        print("detail_url 页面解析出错啦：\n", tb_txt)
        with open("detail_url_error.txt", "a", encoding="utf8") as f:
            f.write("{0}\ndetail_url 页面解析出错啦:\n{1}\n{2}\n\n\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), url, tb_txt))

# req_and_parse_detail_page(url="https://www.danke.com/room/2086319156.html")




def get_data_to_produce():
    docs = db["danke_stock"].find({"estate":None})
    url_lst = []
    for doc in docs:
        url = doc.get("detail_url")
        # print(url)
        url_lst.append(url)
    print(url_lst)
    print(len(url_lst))
    return url_lst


def consume(e):
    # 这里的e 使用的是url
    url = e
    # 获取danke详情页中的所有字段信息，得到item
    item = req_and_parse_detail_page(url)
    # 更新danke_stock表
    house_id = item["house_id"]
    db["danke_stock"].update_one({"house_id":house_id}, {"$set":item})
    # 手动延迟0.2秒， 防止被反爬
    time.sleep(0.8)


def main():
    """
    in: get_data_to_produce函数；  queue_name;   consume函数(核心是还是 req_and_parse_detail_page函数--用来‘请求’和’解析’)
    function: 获取所有待爬元素e，使用consume进行消费

    【自己搭建的异步爬虫的整体框架】

    """
    # 1. 获取所有待爬元素 (包含所有的 'e' )
    url_lst = get_data_to_produce()
    # 2. 定义队列名
    queue_name = "get_detail_page"
    # 3. 生产待爬队列：生产者将所有元素放入redis的待爬队列中。
    k_produce(lst=url_lst, queue_name=queue_name)
    # 4. 消费待爬队列：建立多线程池，循环消费redis待爬队列中的所有元素 (consume_func函数循环获取所有的‘e’)
    ### 其中，已经建立了防漏爬的安全机制！
    ### consume_func 才是真正执行任务的消费函数
    k_consume_pool(consume_func=consume, queue_name=queue_name, thread_num=5, time_sleep=1)
    ## tips: 上面生产者传入reids的e， 与后面消费者消费的e， 必须要保证"e"一致！
    ##        (可以都是id，也可以都是url)  (本脚本使用url)



if __name__ == '__main__':
    print("start test!")
    main()
    print("\n\n\neverything is ok!")
