import scrapy
import json

class BaseItem(scrapy.Item):
    crawled_at = scrapy.Field()

    def to_dict(self):
        dt = self.__dict__['_values']
        return dt

    def to_json_str(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)
