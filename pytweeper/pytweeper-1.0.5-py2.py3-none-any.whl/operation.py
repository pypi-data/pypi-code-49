import json
import itertools
import requests
import shutil
import os
import pickle
from progress.bar import ChargingBar

def read(file):
  with open(file, 'rb') as f:
    return pickle.load(f)

def make_dir(path):
  if not os.path.exists(path):
      os.makedirs(path)

def download_image(url, image_path):
  response = requests.get(url, stream=True)
  with open(image_path, 'wb+') as out_file:
      shutil.copyfileobj(response.raw, out_file)
  del response


def mapper(d):
  has_image = False
  has_extended_image = False
  image = list()
  extended_image = list()
  try:
    image = list(map(lambda x: x['media_url_https'], d['entities']['media']))
    has_image = True
    extended_image = list(map(lambda x: x['media_url_https'], d['extended_entities']['media']))
    has_extended_image = True
    return image+extended_image
  except KeyError:
    if has_image:
      return image
    else:
      return ''

def read_and_download(file, path):
  data = read(file)

  mapped = list(map(mapper, data))
  merged = list(itertools.chain(*mapped))

  make_dir(path)
  bar = ChargingBar('Downloading', max=len(merged))
  for i, image in enumerate(merged):
    download_image(image, os.path.join(path, image.split('/')[-1]))
    bar.next()
  bar.finish()

if __name__ == '__main__':
  print('filter file!')