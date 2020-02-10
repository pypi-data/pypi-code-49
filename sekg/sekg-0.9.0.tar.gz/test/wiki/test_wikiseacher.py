from unittest import TestCase

from sekg.wiki.search_domain_wiki.wikidata_searcher import AsyncWikiSearcher


class TestWikiSearcher(TestCase):

    def test_wiki_searcher(self):
        test_set = set()
        test_set.add("Peer alarm")
        test_set.add("Keyboard")
        test_set.add("File")
        test_set.add("Java")
        test_set.add("keyboard")
        test_set.add('Shoutbox')
        searcher = AsyncWikiSearcher(proxy_server="http://127.0.0.1:1080")
        ids = ['Q1670525']
        titles = test_set
        searcher.search_title(titles)
        print(searcher.get_title_cache())
        title_path = "title.bin"
        searcher.save(title_save_path=title_path)
        searcher.update(title_path, type=searcher.TYPE_TITLE)

        searcher.fetch_item(ids)
        print(searcher.get_item_cache())
        item_path = "item.bin"
        searcher.save(item_save_path=item_path)
        searcher.update(item_path, type=searcher.TYPE_ITEM)
        searcher.fetch_item_for_cache_title_search()
        searcher.fetch_item_neighbor(["Q21028"])
        searcher.fetch_item_neighbor()
        print(searcher.get_item_cache())

        searcher.fetch_wikipedia_context(titles)
        print(searcher.get_wikipedia_cache())
        wiki_path = "wikipedia_context.bin"
        searcher.save(wikipedia_content_save_path=wiki_path)
        searcher.update(wiki_path, type=searcher.TYPE_WIKIPEDIA)

        searcher.fetch_wikipedia_context_for_wikidata(ids)
        print(searcher.get_wikidata_wikipedia_context_cache())

        searcher.fetch_wikipedia_context_html(titles)
        print(searcher.get_wikipedia_content_html())

        searcher.fetch_wikidata_item_by_wikipedia_title(["Prototype-based_programming"])
        print("item cache=", searcher.item_cache)
        print("title search cache=", searcher.get_title_cache())

        print("search for Keyboard:", searcher.search_wd_ids_by_keywords("Keyboard"))
        print("search for keyboard:", searcher.search_wd_ids_by_keywords("keyboard"))
        print("search for File:", searcher.search_wd_ids_by_keywords("File"))
        print("search for file:", searcher.search_wd_ids_by_keywords("file"))
        print("search for Java:", searcher.search_wd_ids_by_keywords("Java"))

        print("search for java:", searcher.search_wd_ids_by_keywords("java"))
        print("search for file:", searcher.search_wikidata_items_by_keywords("file"))
        print("search for Keyboard:", searcher.search_wikidata_items_by_keywords("Keyboard"))
        print("search for keyboard:", searcher.search_wikidata_items_by_keywords("keyboard"))
        print("search for Java:", searcher.search_wikidata_items_by_keywords("Java"))
