from unittest import TestCase

from sekg.so import SOTagItem

from sekg.so.stackoverflow_tag_searcher import SOTagSearcher


class TestSoTagSearcher(TestCase):

    def test_so_tag_searcher(self):
        searcher = SOTagSearcher()
        print(len(searcher.synonyms_data))
        so_tag_item: SOTagItem = searcher.get_tag_item_for_one_tag("javascript")
        print(so_tag_item.tag_name)
        print(so_tag_item.synonyms)
        print(so_tag_item.short_description)
        searcher.run()
        searcher.save("test.bin")

