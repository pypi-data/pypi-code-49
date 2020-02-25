# import re
# import time

# from bs4 import BeautifulSoup
# from yarl import URL

# from colins.scrapers.base_scraper import BaseScraper


# class NewsScraper(BaseScraper):
#     def id_extract(self, url, detail):
#         u = URL(url)
#         if detail.get('news_id'):
#             return u.query.get(detail['news_id'])
#         result = re.match(detail['pattern'], url)
#         if not result:
#             return None
#         return result.group('news_id')
#
#     def id2_extract(self, url, detail):
#         if not detail.get('use_id2', False):
#             return None
#         u = URL(url)
#         if detail.get('news_id2'):
#             return u.query.get(detail['news_id2'])
#         result = re.match(detail['pattern'], url)
#         if not result:
#             return None
#         return result.group('news_id2')
#
#     def get_blueprint_detail(self):
#         return self.blueprint['detail']
#
#     def save_object(self, news_id, **kwargs):
#         return self.news_model.create_with_parsed_data(news_id=news_id, site=self.site, **kwargs)
#
#     def field_parsing(self, bs, fields):
#         def inner(_selected, _data):
#             if _data.get('attr'):
#                 _value = _selected.get(_data['attr'])
#             else:
#                 _value = _selected.text
#             return self.type_parse(value=_value, **_data)
#
#         result = {}
#         for name, data in fields.items():
#             tag = bs.select(data['selector'])
#             if len(tag) == 0:
#                 if data.get('skip', False):
#                     continue
#                 else:
#                     raise ValueError('Field {} is not found.'.format(name))
#             if data.get('many', False):
#                 value = '\n'.join([inner(t, data) for t in tag])
#             else:
#                 extract = data.get('extract', [])
#                 tag = tag[0]
#                 for es in extract:
#                     for i in tag.select(es):
#                         i.extract()
#                 value = inner(tag, data)
#
#             if name == 'url':
#                 value = self.url_join(value, self.current_task['url'])
#
#             result[name] = value
#
#         return result
#
#     def run_task(self, task):
#         self.current_task = task
#         page_options = task.get('page')
#         url = task['url']
#         form = task['form']
#         params = task.get('params', dict())
#         headers = task.get('headers', dict())
#
#         if page_options:
#             self.run_paged_list(url, form, page_options, params, headers)
#         else:
#             self.run_list(url, form, params, headers)
#
#     def run_paged_list(self, url, form, page_options, params=None, headers=None):
#         if params is None:
#             params = dict()
#
#         for page in range(page_options.get('start', 1), page_options.get('end', 4)):
#             params[page_options['name']] = page
#             self.run_list(url, form, params, headers)
#             time.sleep(0.3)
#
#     def run_list(self, url, form, params=None, headers=None):
#         if params is None:
#             params = {}
#         params.update(self.blueprint.get('params', {}))
#         source = self.download(url, params=params, headers=headers)
#         bs = BeautifulSoup(source, 'lxml')
#         news_lists = bs.select(form['selector'])
#         for news_tag in news_lists:
#             self.run_detail(news_tag, form)
#
#     def is_ignore(self, result, **kwargs):
#         title = result['title']
#         if not re.findall(r'[ㄱ-ㅣ가-힣]+', title):
#             return True
#
#         return False
#
#     def run_detail(self, item, form):
#         """
#         item 에서 뽑을 수 있는건 다 뽑은 다음에, detail 페이지 들가서 뽑기
#         """
#         fields = form['field']
#         result = self.field_parsing(item, fields)
#         if self.is_ignore(result):
#             return None
#
#         detail = self.get_blueprint_detail()
#         news_id = self.id_extract(result['url'], detail)
#         news_id2 = self.id2_extract(result['url'], detail)
#         if not news_id:
#             return None
#         if not self.news_model.check_news_id_usable(news_id, self.site, news_id2=news_id2):
#             return None
#
#         if detail['form']:
#             source = self.download(result['url'])
#             bs = BeautifulSoup(source, 'lxml')
#             detail_parsed_data = self.field_parsing(bs, detail['form'])
#             result.update(detail_parsed_data)
#             time.sleep(0.3)
#         return self.save_object(news_id=news_id, news_id2=news_id2, **result)
