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

from nr.databind.core import (
  DateType,
  DatetimeType,
  Field,
  MixinDecoration,
  Struct)
from nr.databind.json import JsonFieldName
from nr.interface import implements
from typing import Iterable, List, Tuple
from wpx.providers import IImage, IImageProvider
import datetime
import re
import requests


class BingImage(Struct):
  MixinDecoration('json')
  startdate = Field(datetime.date, DateType.Format('%Y%m%d'))
  fullstartdate = Field(datetime.datetime, DatetimeType.Format('%Y%m%d%H%M'))
  enddate = Field(datetime.date, DateType.Format('%Y%m%d'))
  url = Field(str)
  urlbase = Field(str)
  copyright = Field(str)
  copyrightlink = Field(str)
  title = Field(str)
  quiz = Field(str)
  hsh = Field(str)

  def get_image_url(self) -> str:
    return 'https://www.bing.com' + self.url

  def get_image_hd_url(self) -> str:
    return 'https://www.bing.com/hpwp/' + self.hsh

  def get_name_and_suffix(self) -> Tuple[str, str]:
    return re.search('OHR.(.+?)_.*\.(\w+)&', self.url).groups()

  def get_filename(self):
    return '.'.join(self.get_name_and_suffix())

  def open(self):
    response = requests.get(self.get_image_hd_url(), stream=True)
    if response.status_code != 200:
      response = requests.get(self.get_image_url(), stream=True)
      response.raise_for_status()
    return response.raw


class BingImageClient:

  BING_BASE_URL = 'https://www.bing.com'

  def __init__(self, session: requests.Session = None, base_url: str = None,
               market: str = 'EN-IN'):
    self.session = session or requests.Session()
    self.base_url = base_url or self.BING_BASE_URL
    self.market = market

  def get_image(self, index: int = 0, market: str = None) -> BingImage:
    """ Returns the most recent Bing image (or the image at the specified
    *index* if set to a non-zero value). """

    return self.get_images(index, 1, market)[0]

  def get_images(self, index: int = 0, count: int = 1,
                 market: str = None) -> List[BingImage]:
    """ Returns the *count* of the latest Bing images starting at the
    specified *index*. At the time of writing this docstring, Bing only
    returns images for up to 15 days in the past and up to 8 images per API
    call (2020-02-10).

    The images are returned in ascending chronological order (that is oldest
    to newest image). """

    url = self.base_url + '/HPImageArchive.aspx'
    params = {
      'format': 'js',
      'idx': int(index),
      'n': int(count),
      'mkt': market or self.market}
    response = self.session.get(url, params=params).json()
    images = [BingImage.from_json(x) for x in response['images']]
    images.sort(key=lambda img: img.startdate)
    return images

  def get_images_since(self, start_date: datetime.date,
                       market: str = None) -> Iterable[BingImage]:
    """ Yields #BingImage objects since from the Bing image of the day API
    since the specified *start_date* (inclusive). """

    days = (datetime.date.today() - start_date).days + 1
    batch_size = min(10, days)
    index = days - batch_size

    # Get the first batch, we can only go back so far...
    images = self.get_images(index, batch_size, market)
    if images[0].startdate > start_date:
      # Adjust the index accordingly.
      days = (datetime.date.today() - images[0].startdate).days + 1
      index = days - len(images)
      assert index >= 0

    while True:
      yield from filter(lambda img: img.startdate >= start_date, images)
      if index == 0:
        break
      index = max(0, index - len(images))
      images = self.get_images(index, batch_size, market)


@implements(IImageProvider)
class BingImageProvider(Struct):
  index = Field(int, default=0)
  market = Field(str, default='EN-IN')
  date_in_filename = Field(bool, JsonFieldName('dateInFilename'), default=True)

  def __init__(self, *args, **kwargs):
    super(BingImageProvider, self).__init__(*args, **kwargs)
    self.client = BingImageClient(market=self.market)

  def get_daily_image(self) -> IImage:
    image = self.client.get_image(self.index)
    filename = image.get_filename()
    if self.date_in_filename:
      filename = image.startdate.strftime('%Y-%m-%d-') + filename
    return IImage(filename=filename, open=image.open)

  def get_random_image(self) -> IImage:
    raise NotImplementedError
