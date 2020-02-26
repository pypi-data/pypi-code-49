from scrapy_nc.crawlab import get_task_id
from scrapy_nc.db import spider_collection

class MongoPipeline(object):

    def process_item(self, item, spider):
        if not spider_collection:
            pass
        item_dict = dict(item)
        item_dict['task_id'] = get_task_id()
        spider_collection.save(item_dict)
        return item

    def open_spider(self, spider):
        if not spider_collection:
            pass
        try:
            index_keys = [index_spec['key'] for index_spec in
                          spider_collection.list_indexes()]
        except:
            index_keys = []
        if 'unique_id' not in index_keys:
            spider_collection.create_index('unique_id', unique=True)
