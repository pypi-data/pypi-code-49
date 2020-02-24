# from scrapy.exceptions import DropItem
# from pyreBloom import pyreBloom

# class RedisDuplicatesPipeline(object):
#     def __init__(self, redis_host, redis_port, redis_password, redis_db):
#         self.redis_host = redis_host
#         self.redis_port = redis_port
#         self.redis_password = redis_password
#         self.redis_db = redis_db

#     def process_item(self, item, spider):
#         unique_key = item.unique_key()
#         if self.bloom.contains(unique_key):
#             raise DropItem("Duplicate item found: %s" % item)
#         else:
#             self.bloom.add(unique_key)
#             return item

#     def open_spider(self, spider):

#         redis_conf = {
#             'host': self.redis_host,
#             'password': self.redis_password,
#             'port': self.redis_port,
#             'db': self.redis_db
#         }

#         self.bloom = pyreBloom('bloom' + spider.name,
#                                spider.settings.MAX_COUNT, 0.0001, **redis_conf)

#     def close_spider(self, spider):
#         self.bloom.close()
#         spider.logger.info(f'close connection success')

#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             crawler.spider.settings['REDIS_HOST'],
#             crawler.spider.settings['REDIS_PORT'],
#             crawler.spider.settings['REDIS_PASSWORD'],
#             crawler.spider.settings['REDIS_DB'],
#         )
