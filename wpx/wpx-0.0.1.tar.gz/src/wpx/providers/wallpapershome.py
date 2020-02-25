# -*- coding: utf8 -*-
# Copyright (c) 2020 Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from nr.databind.core import create_struct_class, Field, Struct
from nr.databind.json import JsonFieldName
from nr.interface import implements
from urllib.parse import parse_qs, urljoin
from typing import Iterable, Tuple
from wpx.providers import IImage, IImageProvider
import bs4
import logging
import posixpath
import random
import requests

logger = logging.getLogger(__name__)


class PicPreview(Struct):
  preview_image_url = Field(str)
  details_page_url = Field(str)
  description = Field(str)
  tags = Field([str])


class Pic(Struct):
  Tag = create_struct_class('Tag',
    {'name': Field(str), 'category': Field(str)})
  Uploader = create_struct_class('Uploader',
    {'name': Field(str), 'id': Field(int)})

  class Resolution(Struct):
    width = Field(int)
    height = Field(int)
    name = Field(str)
    url = Field(str)

    @classmethod
    def parse(cls, res: str, name: str, url: str) -> 'Resolution':
      width, height = res.lower().partition('x')[::2]
      return cls(int(width), int(height), name, url)

  resolutions = Field([Resolution], default=list)
  tags = Field([Tag], default=list)
  uploader = Field(Uploader)


class PicsList(Struct):
  page_num = Field(int)
  max_pages = Field(int)
  items = Field([PicPreview], default=list)


class WallpapersHomeClient:

  WALLPAPERSHOME_BASE_URL = 'https://wallpapershome.com'

  def __init__(self, session: requests.Session = None, base_url: str = None):
    self.session = session or requests.Session()
    self.base_url = (base_url or self.WALLPAPERSHOME_BASE_URL).rstrip('/')

  def get_pics(self, category: str = None, page: int = 1) -> [PicPreview]:
    """ Fetches the list of pictures for the *category* and *page*. """

    if page < 1:
      raise ValueError('page must be >= 1 (got: {})'.format(page))
    url = self.base_url + '/'
    if category:
      url += category.strip('/') + '/'
    params = {'page': int(page)}

    response = self.session.get(url, params=params)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    pics_list = soup.find('div', {'id': 'pics-list'})
    if pics_list is None:
      raise RuntimeError('unable to find pics-list in response.')

    # Need to also check if the page numbers align. If they don't, then
    # we exceeded the number of available pages.
    pages = soup.find('p', {'class': 'pages'})
    if not pages:
      raise RuntimeError('unable to find pages in response.')
    current_page = int(pages.find('strong').text)
    if current_page != page:
      raise ValueError('page {} does not exist'.format(page))

    last_page = next(
      int(x.text) for x in reversed(pages.find_all('a'))
      if x.text.isdigit())

    pics = PicsList(page_num=page, max_pages=last_page)
    for node in pics_list.find_all('p'):
      tags = [x.lower().strip() for x in node.find('span').text.split(',')]
      pics.items.append(PicPreview(
        details_page_url=urljoin(url, node.find('a')['href']),
        preview_image_url=urljoin(url, node.find('img')['src']),
        description = node.find('img')['alt'],
        tags=tags))

    return pics

  def get_pic(self, pic_preview: PicPreview) -> Pic:
    url = pic_preview.details_page_url
    response = self.session.get(url)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    resolutions = []
    node = soup.find('div', {'class': 'block-download__resolutions--6'})
    for item in node.find_all('p'):
      name = item.find('span').text
      res = item.find('a').text
      image_url = urljoin(url, item.find('a')['href'])
      resolutions.append(Pic.Resolution.parse(res, name, image_url))

    tags = [
      Pic.Tag(x.text.lower().strip(), x['href'].lstrip('/'))
      for x in soup.find('p', {'class': 'tags'}).find_all('a')
    ]

    author = soup.find('p', {'class': 'author'}).find_all('a')[-1]
    author_id = int(parse_qs(author['href'].partition('?')[-1])['uploaded'][0])
    uploader = Pic.Uploader(author.text, author_id)

    return Pic(
      resolutions=resolutions,
      tags=tags,
      uploader=uploader)


@implements(IImageProvider)
class WallpapersHomeProvider(Struct):
  #: Allows you to specify a category, otherwise it will pick an image from
  #: the "All Wallpapers" section.
  category = Field(str, default=None)

  #: Allows you to overwrite the page to retrieve an image from. This is only
  #: really relevant to the daily image.
  page = Field(int, default=None)

  #: The name of the preferred resolution to download. Defaults to "4K".
  preferred_resolution = Field(str,
    JsonFieldName('preferredResolution'), default='4K')

  #: Conditions that should apply to the image. Only images that match all
  #: of the conditions are picked. Note that too strict conditions, or picking
  #: a condition that doesn't match any image would cause the provider to
  #: walk through all available pages in the category and eventually not find
  #: a single match.
  conditions = Field({
    #: The image must be tagged with any of these tags.
    'mustHaveTagsAny': Field([str], default=list),
    #: The image must not be tagged with any of these tags.
    'mustNotHaveTags': Field([str], default=list)
  }, default=Field.DEFAULT_CONSTRUCT)

  client = WallpapersHomeClient()

  def _get_pics(self, page_num: int) -> PicsList:
    return self.client.get_pics(self.category, page_num)

  def _iter_pics(self, pics: PicsList, offset: int) -> Iterable[Tuple[PicsList, PicPreview]]:
    page_offset = pics.page_num - 1
    page_max = pics.max_pages
    for page_index in range(1, page_max + 1):
      for pic_index in range(0, len(pics.items)):
        logger.debug('page %s, pic %s', pics.page_num, (pic_index + offset) % len(pics.items))
        yield pics, pics.items[(pic_index + offset) % len(pics.items)]
      offset = 0
      pics = self._get_pics(((page_index + page_offset) % page_max) + 1)

  def _provide(self, pic: Pic) -> IImage:
    """ Returns an #IImage for the specified #PicPreview object. """

    res = next((x for x in pic.resolutions
      if x.name == self.preferred_resolution), None)
    if not res:
      # TODO: Pick an alternative resolution?
      raise RuntimeError('resolution {} not found'.format(
        self.preferred_resolution))

    response = requests.head(res.url)
    response.raise_for_status()
    if 'text/html' in response.headers['Content-type']:
      raise ValueError('image is unavailable in resolution {}'.format(
        pic.res.name))

    return IImage(filename=posixpath.basename(res.url),
      open=lambda: requests.get(res.url, stream=True).raw)

  def _match_preview_conditions(self, preview: PicPreview) -> bool:
    has_tags = set(preview.tags)
    if self.conditions.mustHaveTagsAny:
      tags = set(map(str.lower, self.conditions.mustHaveTagsAny))
      if not (tags & has_tags):
        logger.info('  Does not have any of the required tags: %s', tags)
        return False
    if self.conditions.mustNotHaveTags:
      tags = set(map(str.lower, self.conditions.mustNotHaveTags))
      if tags & has_tags:
        logger.info('  Has unwanted tags: %s', tags & has_tags)
        return False
    return True

  def _match_pic_conditions(self, pic: Pic) -> bool:
    if not any(r.name == self.preferred_resolution for r in pic.resolutions):
      logger.info('  Does not provide resolution "%s"', self.preferred_resolution)
      return False
    return True

  def _pick_first_matching(self, pics: PicsList, start_index: int) -> IImage:
    for pics, preview in self._iter_pics(pics, start_index):
      logger.info('Testing "%s" ...', preview.details_page_url)
      if not self._match_preview_conditions(preview):
        continue
      pic = self.client.get_pic(preview)
      if not self._match_pic_conditions(pic):
        continue
      logger.info('Passed.')
      return self._provide(pic)
    raise RuntimeError('no pic found')

  def get_daily_image(self) -> IImage:
    pics = self.client.get_pics(self.category, self.page or 1)
    return self._pick_first_matching(pics, 0)

  def get_random_image(self) -> IImage:
    # Pick a random page.
    pics = self._get_pics(1)
    page_num = random.randint(1, pics.max_pages)
    if page_num != 1:
      pics = self._get_pics(page_num)

    start_index = random.randint(0, len(pics.items))
    logger.info(
      'Starting from page %s, index %s in category %s.',
      page_num, start_index, self.category)

    return self._pick_first_matching(pics, start_index)
