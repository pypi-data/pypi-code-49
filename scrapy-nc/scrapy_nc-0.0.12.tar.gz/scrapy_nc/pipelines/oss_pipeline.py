import hashlib
import oss2
from urllib.parse import urlparse

class OSSPipeline(object):

    def __init__(self, access_key_id, access_key_secret, endpoint, bucket_name):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.endpoint = endpoint
        self.bucket_name = bucket_name

    def get_hash(self, url):
        return hashlib.md5(url.encode('utf8')).hexdigest()

    def process_item(self, item, spider):

        url = item['url']
        hash_id = self.get_hash(url)
        hostname = urlparse(url).hostname
        data_key = f'news/{hostname}/{hash_id}'
        # to maintain rule data in item, execute deepcopy method before to_json_str
        result = self.bucket.put_object(data_key, item.deepcopy().to_json_str(), headers={
            'Content-Type': 'application/json',
        })
        spider.logger.info(
            f'upload data to oss: {data_key}, status: {result.status}')
        # item['message_package'] = MessagePackage(
        #     filename=data_key,
        #     url=item['url'],
        #     channel=item['channel'],
        #     queue_name=item['rule']['queue_name'],
        # )
        return item

    def open_spider(self, spider):
        auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        self.bucket = oss2.Bucket(auth, self.endpoint, self.bucket_name)
        spider.logger.info('connnect and auth oss success')

    def close_spider(self, spider):
        spider.logger.info('spider news oss pipeline closed')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.spider.settings['OSS_ACCESS_KEY_ID'],
            crawler.spider.settings['OSS_ACCESS_KEY_SECRET'],
            crawler.spider.settings['OSS_END_POINT'],
            crawler.spider.settings['OSS_BUCKET_NAME'],
        )
