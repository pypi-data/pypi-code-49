"""
test the integer field
"""
import asyncio

from gerridae import Item, Spider, TextField
from gerridae.log import get_logger

logger = get_logger(__name__)


class TestBaseField:
    def test_spider(self):
        class TestItem(Item):
            command = TextField(css_select="#pip-command")

        class TestSpider(Spider):
            start_urls = "https://pypi.org/project/gerridae/"

            async def parse(self, resp):
                text = await resp.text(encoding='utf-8')
                result = TestItem.get_item(html=text)
                return result

        results = asyncio.run(TestSpider.start())
        assert "pip install gerridae" == results[0].command

    def test_spider_with_many(self):
        class TestItem(Item):
            command = TextField(css_select="#pip-command", many=True)

        class TestSpider(Spider):
            start_urls = "https://pypi.org/project/gerridae/"

            async def parse(self, resp):
                text = await resp.text(encoding='utf-8')
                result = TestItem.get_item(html=text)
                return result

        results = asyncio.run(TestSpider.start())
        assert ["pip install gerridae"] == results[0].command
