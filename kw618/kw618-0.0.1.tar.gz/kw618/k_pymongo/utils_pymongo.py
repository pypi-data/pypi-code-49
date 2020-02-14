import re
import json
import collections
import time
import pymongo
import redis



# redis的 pipe管道事务操作:
# 1. pipe为事务管道,必须要execute后才会在服务器端真正执行
# 2.当管道中使用watch开启检测后,到multi语句(或者execute语句)前,会让pipe处于"非事务阶段",
#   可以获取、删除redis服务器中的值.  (意味着此阶段的pipe.set()不需要execute())
# 3. 当pipe.execute()执行时,会把储存在pipe管道中"滞后执行"的事务操作全部一次性完成.
# 4.在"管道事务"阶段,打印出来的都是对象(在后面execute后接受str结果); 而在"非事务"阶段,返回的是字符.

# def lst_to_zset(lst=[4, 1, 88], key_name="queue"):
#     m_ = zip(lst, range(len(lst)))
#     all_z_dict = {i:j for i, j in m_}
#     r.delete(key_name)
#     r.zadd(key_name, all_z_dict)



# 应对业务需求，快速匹配出他们想要的消化数据
def merge_mongo(
    left_table_name="ziru_stock", right_table_name="ziru_name_list", left_join_field="所属业务组",
    right_join_field="ziru_zone", conditions_dict={}, project_dict={"_id":0}, db=None,
    ):
    """
    notes:
        1. project_dict的功能是表示哪些字段需要显示，哪些不要显示。但是只有“_id”可以为0，其他只能标记为1.
        2. 右连接的字段前必须加上matched_field才行
        3. 返回得到的 all_join_docs 中， 右连接得到的所有内容都包含在 matched_field 字段中，以dict形式存在
    """

    if db is None:
        client = pymongo.MongoClient("127.0.0.1")
        db = client["zufang_001"]

    # 输入接口：
    # left_table_name
    # right_table_name

    # 管道筛选：
    pipeline = [
                {
                    "$lookup":
                    {
                        "from":right_table_name,
                        "localField":left_join_field,
                        "foreignField":right_join_field,
                        "as":"matched_field",
                    }
                },
                {
                    "$match": conditions_dict,
                },
                {
                    "$project": project_dict,
                }
                ]

    all_join_docs = db[left_table_name].aggregate(pipeline)
    return all_join_docs



# with r.pipeline() as pipe:
#     while True:
#         try:
#             # 监视我们需要修改的键
#             queue_ = "lll"
#             # pipe.rpush(queue_, *[3, 4, 5])
#             # 进入"非事务"阶段
#             pipe.watch(queue_)
#             pipe.rpush(queue_, *[44, 88])
#
#             # 进入"事务"阶段
#             pipe.multi()
#             x = pipe.lrange(queue_, 0, -1)
#             print(x)
#             # print(pipe.rpop(queue_))
#             ss = pipe.execute()
#             print(ss)
#             break
#
#         except redis.WatchError:
#             # 如果其他客户端在我们 WATCH 和 事务执行期间，则重试
#             # pipe.unwatch()
#             pipe.reset() # unwatch和ureset的作用应该差不多
#             print("error")
#             break
#


def main():
    pass
    # r.sadd("bnm", print(3))
    # r.lpush("aabb", *[1, 2, 3])
    # print(r.lrange("a", 0, -1))
    # print(r.smembers("crawl_cost_price:crawled_queues"))



if __name__ == '__main__':
    print("start test!")
    main()
    print("\n\n\neverything is ok!")
