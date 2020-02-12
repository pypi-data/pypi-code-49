# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
import pika
import os

class AMQPPipeline(object):
    def __init__(self, mq_user, mq_password, mq_host, mq_port, mq_vhost, mq_name_suffix):
        self.parameters = pika.URLParameters(
            f'amqp://{mq_user}:{mq_password}@{mq_host}:{mq_port}/{mq_vhost}')
        self.queue_names = []
        self.mq_name_suffix = mq_name_suffix

    def process_item(self, item, spider):
        queue_names = item.queue_names()
        if len(queue_names) == 0:
            spider.logger.info(
                f"queue name length is 0, item url {item.get('url')}")
            raise DropItem(f"empty queue_name item {item.get('url')}")
        for queue_name in queue_names:
            queue_name = f'{queue_name}.{self.mq_name_suffix}'
            if not queue_name in self.queue_names:
                self.channel.queue_declare(queue_name,
                                           passive=False,
                                           durable=True,
                                           exclusive=False,
                                           auto_delete=False,
                                           arguments=None,
                                           )
                self.queue_names.append(queue_name)
                spider.logger.info(f'declare queue {queue_name}')
            data = item
            self.channel.basic_publish('',
                                       queue_name,
                                       data.to_json_str(),
                                       pika.BasicProperties(
                                           content_type='application/json',
                                           delivery_mode=2),
                                       )

        return item

    def open_spider(self, spider):
        self.connection = pika.BlockingConnection(self.parameters)
        spider.logger.info(f'connect amqp success')
        self.channel = self.connection.channel()
        spider.logger.info(f'create channel success')
        self.channel.queue_declare('spider.config_news.prod')

    def close_spider(self, spider):
        self.connection.close()
        spider.logger.info(f'close connection success')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.spider.settings['MQ_USER'],
            crawler.spider.settings['MQ_PASSWORD'],
            crawler.spider.settings['MQ_HOST'],
            crawler.spider.settings['MQ_PORT'],
            crawler.spider.settings['MQ_VHOST'],
            crawler.spider.settings['MQ_NAME_SUFFIX']
        )
