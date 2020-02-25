# import re

# import pendulum
# import requests

# from colins.exceptions import HttpError


# class BaseScraper:
#     def __init__(self, site=None, site_keyword=None, blueprint=None, **kwargs):
#         self.site = site
#         self.site_keyword = site_keyword or self.default_site_keyword
#         if site is None:
#             self.site = get_object_or_None(self.site_model, keyword=self.site_keyword)
#         if self.site is None:
#             raise ValueError('Site object not exists by keyword: {}'.format(self.site_keyword))
#         self.kwargs = kwargs
#         self.site.sync_blueprint()
#         self.blueprint = blueprint or self.site.blueprint
#         self.current_task = None
#
#     def type_parse(self, type, value, **kwargs):
#         if kwargs.get('regex'):
#             matched = re.match(kwargs.get('regex'), value)
#             if matched is None:
#                 return None
#             value = matched[0]
#         if type == 'str':
#             return str(value).strip()
#         elif type == 'int':
#             return int(value)
#         elif type == 'datetime':
#             fmt = kwargs.get('format')
#             if fmt:
#                 return pendulum.from_format(value.strip(), fmt=fmt, tz='Asia/Seoul', locale='ko')
#             return pendulum.parse(value.strip(), tz='Asia/Seoul')
#
#     def get_blueprint_task(self):
#         return self.blueprint.get('tasks', [])
#
#     def save_object(self, **kwargs):
#         pass
#
#     def get_headers(self, **kwargs):
#         headers = self.blueprint.get('headers', {})
#         headers.update(kwargs)
#         return headers
#
#     def get_params(self, **kwargs):
#         return kwargs
#
#     def download(self, url, params=None, headers=None, **kwargs):
#         if params is None:
#             params = dict()
#         if headers is None:
#             headers = dict()
#
#         params = self.get_params(**params)
#         headers = self.get_headers(**headers)
#
#         response = requests.get(url, params=params, headers=headers, **kwargs)
#         if response.status_code == 200:
#             return response.content
#         else:
#             raise HttpError(response.status_code, response.reason)
#
#     def run_task(self, task):
#         pass
#
#     def url_join(self, url, referer):
#         if url.find('http') >= 0:
#             return url
#         else:
#             return requests.compat.urljoin(referer, url)
#
#     def check_runnable(self):
#         return self.site.runnable()
#
#     def is_ignore(self, **kwargs):
#         return False
#
#     def finish_run(self):
#         self.site.last_run_at = pendulum.now()
#         self.site.save()
#         return True
#
#     def run(self):
#         if not self.check_runnable():
#             return False
#
#         print('{} running'.format(self.site.keyword))
#         for task in self.get_blueprint_task():
#             print('Task {} is running'.format(task['name']))
#             self.run_task(task)
#             print('Task {} done.'.format(task['name']))
#
#         self.finish_run()
#         return True
