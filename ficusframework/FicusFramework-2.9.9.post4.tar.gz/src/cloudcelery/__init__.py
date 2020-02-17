from celery import Celery
from munch import Munch

import config
from config import annotation

yml = Munch.fromDict(annotation.REMOTE_YML_CONFIG)

celery = Celery('tasks')
celery.config_from_object('cloudcelery.celery_config')
celery.conf.timezone = 'Asia/Shanghai'
celery.conf.setdefault('CELERY_DEFAULT_QUEUE', config.actor_name)  # 关心的是actor_name类型的任务

try:
    concurrent_count = yml.celery.concurrency
except:
    concurrent_count = 1
celery.conf.setdefault('CELERYD_CONCURRENCY', concurrent_count)  # 设置任务并发数,默认是1

redis_url: str = yml.redis.url

try:
    redis_password = yml.redis.password
except:
    redis_password = None

# 选择redis类型的缓存时,redis服务器的地址 格式为: ip:port
# 现在支持了redis3-cluster,多个IP使用逗号分割
# 现在支持了redis3-sentinel哨兵模式,使用分号分割. 第一个表示主节点名字. MASTERNAME;哨兵IP1:PORT1;哨兵IP2:PORT2;哨兵IP3:PORT3的方式
if "," in redis_url:
    # 说明是redis-cluster 那么就要初始化集群
    raise NotImplementedError("celery还不支持,see: https://github.com/celery/kombu/pull/1021")
elif ";" in redis_url:
    # 说明是哨兵形式的主从集群
    # app.conf.broker_url = 'sentinel://localhost:26379;sentinel://localhost:26380;sentinel://localhost:26381'
    # app.conf.broker_transport_options = {'master_name': "cluster1"}
    split = redis_url.split(";")
    sentinel = split[0]
    split.remove(sentinel)
    url = ";".join(
        [f'sentinel://{f":{redis_password}@" if (redis_password is not None and redis_password != "") else ""}{url}/0' for
         url in split])
    celery.conf.broker_transport_options = {'master_name': sentinel}
else:
    # 说明是单机
    url = f'redis://{f":{redis_password}@" if (redis_password is not None and redis_password != "") else ""}{redis_url}/0'

celery.conf.broker_url = url  # 中间件
celery.conf.result_backend = url  # 结果存储
