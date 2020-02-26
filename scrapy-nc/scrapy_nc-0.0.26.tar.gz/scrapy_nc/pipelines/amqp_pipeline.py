# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
import pika
import os
import json

class AMQPPipeline(object):
    def __init__(self,
                 mq_dev_user,
                 mq_dev_password,
                 mq_dev_host,
                 mq_dev_port,
                 mq_dev_vhost,
                 mq_prod_user,
                 mq_prod_password,
                 mq_prod_host,
                 mq_prod_port,
                 mq_prod_vhost):
        self.parameters_dev = pika.URLParameters(
            f'amqp://{mq_dev_user}:{mq_dev_password}@{mq_dev_host}:{mq_dev_port}/{mq_dev_vhost}') if mq_dev_host else None
        self.parameters_prod = pika.URLParameters(
            f'amqp://{mq_prod_user}:{mq_prod_password}@{mq_prod_host}:{mq_prod_port}/{mq_prod_vhost}') if mq_prod_host else None
        self.queue_names_dev = []
        self.queue_names_prod = []

    def process_item(self, item, spider):
        cralab_env = os.environ.get('CRAWLAB_ENV')
        if cralab_env == 'HK':
            return item
        queue_names = item.queue_names()
        if len(queue_names) == 0:
            spider.logger.info(
                f"queue name length is 0, item url {item.get('url')}")
            # raise DropItem(f"empty queue_name item {item.get('url')}")
            return item
        for queue_name in queue_names:
            tasks = []
            if queue_name.endswith('.dev'):
                tasks.append({
                    "env": "dev",
                    "queue_name": queue_name
                })
            elif queue_name.endswith('.prod'):
                tasks.append({
                    "env": "prod",
                    "queue_name": queue_name
                })
            else:
                tasks.append({
                    "env": "dev",
                    "queue_name": queue_name + '.dev'
                })
                tasks.append({
                    "env": "prod",
                    "queue_name": queue_name + '.prod'
                })
            for task in tasks:
                env = task['env']
                queue_name = task['queue_name']
                queue_data = json.dumps({
                    "filename": item.get('oss_filename'),
                    "channel": spider.name,
                    "source_id": item.get('unique_id'),
                }, ensure_ascii=False)
                if env == 'dev':
                    if not self.channel_dev:
                        continue
                    try:
                        if not queue_name in self.queue_names_dev:
                            self.channel_dev.queue_declare(queue_name,
                                                        passive=False,
                                                        durable=True,
                                                        exclusive=False,
                                                        auto_delete=False,
                                                        arguments=None,
                                                        )
                            self.queue_names_dev.append(queue_name)
                        spider.logger.info(f'declare queue {queue_name}')
                        self.channel_dev.basic_publish('',
                                                    queue_name,
                                                    queue_data,
                                                    pika.BasicProperties(
                                                        content_type='application/json',
                                                        delivery_mode=2),
                                                    )
                    except:
                        pass
                else:
                    if not self.channel_prod:
                        continue
                    if not queue_name in self.queue_names_prod:
                        self.channel_prod.queue_declare(queue_name,
                                                        passive=False,
                                                        durable=True,
                                                        exclusive=False,
                                                        auto_delete=False,
                                                        arguments=None,
                                                        )
                        self.queue_names_prod.append(queue_name)
                    spider.logger.info(f'declare queue {queue_name}')
                    self.channel_prod.basic_publish('',
                                                    queue_name,
                                                    queue_data,
                                                    pika.BasicProperties(
                                                        content_type='application/json',
                                                        delivery_mode=2),
                                                    )

        return item

    def open_spider(self, spider):
        self.connection_dev = pika.BlockingConnection(
            self.parameters_dev) if self.parameters_dev else None
        self.connection_prod = pika.BlockingConnection(
            self.parameters_prod) if self.parameters_prod else None
        spider.logger.info(f'connect amqp success')
        self.channel_dev = self.connection_dev.channel() if self.connection_dev else None
        self.channel_prod = self.connection_prod.channel() if self.connection_prod else None
        spider.logger.info(f'create channel success')

    def close_spider(self, spider):
        if self.channel_dev:
            self.channel_dev.close()
        if self.channel_prod:
            self.channel_prod.close()
        spider.logger.info(f'close connection success')

    @classmethod
    def from_crawler(cls, crawler):
        mq_dev_user = crawler.spider.settings.get('MQ_DEV_USER') if crawler.spider.settings.get(
            'MQ_DEV_USER') else os.environ.get('MQ_DEV_USER')
        mq_dev_password = crawler.spider.settings.get('MQ_DEV_PASSWORD') if crawler.spider.settings.get(
            'MQ_DEV_PASSWORD') else os.environ.get('MQ_DEV_PASSWORD')
        mq_dev_host = crawler.spider.settings.get('MQ_DEV_HOST') if crawler.spider.settings.get(
            'MQ_DEV_HOST') else os.environ.get('MQ_DEV_HOST')
        mq_dev_port = crawler.spider.settings.get('MQ_DEV_PORT') if crawler.spider.settings.get(
            'MQ_DEV_PORT') else os.environ.get('MQ_DEV_PORT')
        mq_dev_vhost = crawler.spider.settings.get('MQ_DEV_VHOST') if crawler.spider.settings.get(
            'MQ_DEV_VHOST') else os.environ.get('MQ_DEV_VHOST')

        mq_prod_user = crawler.spider.settings.get('MQ_PROD_USER') if crawler.spider.settings.get(
            'MQ_PROD_USER') else os.environ.get('MQ_PROD_USER')
        mq_prod_password = crawler.spider.settings.get('MQ_PROD_PASSWORD') if crawler.spider.settings.get(
            'MQ_PROD_PASSWORD') else os.environ.get('MQ_PROD_PASSWORD')
        mq_prod_host = crawler.spider.settings.get('MQ_PROD_HOST') if crawler.spider.settings.get(
            'MQ_PROD_HOST') else os.environ.get('MQ_PROD_HOST')
        mq_prod_port = crawler.spider.settings.get('MQ_PROD_PORT') if crawler.spider.settings.get(
            'MQ_PROD_PORT') else os.environ.get('MQ_PROD_PORT')
        mq_prod_vhost = crawler.spider.settings.get('MQ_PROD_VHOST') if crawler.spider.settings.get(
            'MQ_PROD_VHOST') else os.environ.get('MQ_PROD_VHOST')

        return cls(
            mq_dev_user,
            mq_dev_password,
            mq_dev_host,
            mq_dev_port,
            mq_dev_vhost,
            mq_prod_user,
            mq_prod_password,
            mq_prod_host,
            mq_prod_port,
            mq_prod_vhost
        )
