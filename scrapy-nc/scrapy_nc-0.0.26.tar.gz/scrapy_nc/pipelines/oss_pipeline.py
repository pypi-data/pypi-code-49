import hashlib
import oss2
from urllib.parse import urlparse
import os
import datetime
from scrapy.exceptions import DropItem

class OSSPipeline(object):

    def __init__(self, access_key_id, access_key_secret, endpoint, bucket_name):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.endpoint = endpoint
        self.bucket_name = bucket_name

    def get_hash(self, url):
        return hashlib.md5(url.encode('utf8')).hexdigest()

    def process_item(self, item, spider):
        unique_id = item['unique_id']
        if not unique_id:
            raise DropItem('unique_id is None')
        item['crawled_at'] = datetime.datetime.utcnow().replace(
            tzinfo=datetime.timezone.utc).astimezone().isoformat()
        oss_filename = item.get('oss_filename')
        if not oss_filename:
            # url = item.get('url')
            # if not url:
            #     raise DropItem('item missing url')
            # hash_id = self.get_hash(url)
            # hostname = urlparse(url).hostname
            oss_filename = f'{spider.name}/{unique_id}'
            item['oss_filename'] = oss_filename
        # to maintain rule data in item, execute deepcopy method before to_json_str
        result = self.bucket.put_object(oss_filename, item.deepcopy().to_json_str(), headers={
            'Content-Type': 'application/json',
        })
        spider.logger.info(
            f'upload data to oss: {oss_filename}, status: {result.status}')
        # 存完 oss 后如果有 html ，清空
        if item.get('html'):
            item['html'] = None
        return item

    def open_spider(self, spider):
        auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        self.bucket = oss2.Bucket(auth, self.endpoint, self.bucket_name)
        spider.logger.info('connnect and auth oss success')

    def close_spider(self, spider):
        spider.logger.info(f'spider {spider.name} oss pipeline closed')

    @classmethod
    def from_crawler(cls, crawler):
        OSS_ACCESS_KEY_ID = crawler.spider.settings.get('OSS_ACCESS_KEY_ID') if crawler.spider.settings.get(
            'OSS_ACCESS_KEY_ID') else os.environ.get('OSS_ACCESS_KEY_ID')
        OSS_ACCESS_KEY_SECRET = crawler.spider.settings.get('OSS_ACCESS_KEY_SECRET') if crawler.spider.settings.get(
            'OSS_ACCESS_KEY_SECRET') else os.environ.get('OSS_ACCESS_KEY_SECRET')
        OSS_END_POINT = crawler.spider.settings.get('OSS_END_POINT') if crawler.spider.settings.get(
            'OSS_END_POINT') else os.environ.get('OSS_END_POINT')
        OSS_BUCKET_NAME = crawler.spider.settings.get('OSS_BUCKET_NAME') if crawler.spider.settings.get(
            'OSS_BUCKET_NAME') else os.environ.get('OSS_BUCKET_NAME')
        return cls(
            OSS_ACCESS_KEY_ID,
            OSS_ACCESS_KEY_SECRET,
            OSS_END_POINT,
            OSS_BUCKET_NAME
        )
