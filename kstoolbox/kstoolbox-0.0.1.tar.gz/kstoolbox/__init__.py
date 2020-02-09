from fastai.vision import *
from fastai.metrics import error_rate
from fastai.widgets import *
from pathlib import Path
from google_images_download.google_images_download import google_images_download
import shutil
import os
from PIL import Image


import requests


 # to update ubuntu to correctly run apt install

import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
wd.get("https://www.webite-url.com")

from igramscraper.instagram import Instagram
instagram = Instagram()

path_img = Path('/content/image_data')

def create_databunch():
    return ImageDataBunch.from_folder(path_img,valid_pct=0.2, bs = 64, ds_tfms=get_transforms(), size=224).normalize(imagenet_stats)

def download_from_google_images(keywords : str, limit : int, dir : str):
    
    if(limit>1000):
      print('Too much images')
      return
    response = google_images_download.googleimagesdownload()   #class instantiation
    keywords = keywords+" filetype:jpg"
    arguments = {"keywords":keywords,"limit":limit,"print_urls":False, "chromedriver": "/usr/lib/chromium-browser/chromedriver"}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    #print(paths)
    
    if(os.path.isdir(f'/content/image_data/{dir}')):  #move to image_data
      for p in paths[0][keywords] :
        img_file = p.rsplit('/', 1)[1]
        if not (os.path.exists(f'/content/image_data/{dir}/{img_file}')):
          shutil.move(p, f'/content/image_data/{dir}')
    else:
       os.mkdir(f'/content/image_data/{dir}')
       for p in paths[0][keywords]:
         img_file = p.rsplit('/', 1)[1]
         if not (os.path.exists(f'/content/image_data/{dir}/{img_file}')):
          shutil.move(p, f'/content/image_data/{dir}')
    shutil.rmtree("/content/downloads")
    
    img_dir = f"/content/image_data/{dir}" #clean corrupted
    filelist = os.listdir(img_dir)
    for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
      if not(fichier.endswith(".png")):
          filelist.remove(fichier)
    for filename in filelist:
        try :
            with Image.open(img_dir + "/" + filename) as im:
                print('', end ="")
        except :
            print("removed corrupted : " + filename)
            os.remove(img_dir + "/" + filename)

def delete_classe(dir : str):
  if(os.path.isdir(f'/content/image_data/{dir}')):
    shutil.rmtree(f'/content/image_data/{dir}')
  else:
    print(f"{dir} doesn't exist")

def download_from_insta_account(account : str, limit : int, dir : str):
    if(limit>1000):
      print("Trop d'images à télécharger")
      return
    if not (os.path.isdir(f'/content/image_data/{dir}')):
      os.mkdir(f'/content/image_data/{dir}')
    medias = instagram.get_medias_from_feed(account, count=limit)
    i=0
    for x in range(len(medias)):
      if(medias[x].image_high_resolution_url is not None):
        f = open(f'{path_img}/{dir}/{x}.jpg','wb')
        f.write(requests.get(medias[x].image_high_resolution_url).content)
        f.close()
      elif(medias[x].image_standard_resolution_url is not None):
        f = open(f'{path_img}/{dir}/{x}.jpg','wb')
        f.write(requests.get(medias[x].image_standard_resolution_url).content)
        f.close()
      elif(medias[x].image_low_resolution_url is not None):
        f = open(f'{path_img}/{dir}/{x}.jpg','wb')
        f.write(requests.get(medias[x].image_low_resolution_url).content)
        f.close()
      else:
        continue
      i+=1
    
    print(str(i) + ' images téléchargées dans la classes ' + dir)

def download_from_insta_hashtag(hashtag : str, limit : int, dir : str):
    if(limit>1000):
      print("Trop d'images à télécharger")
      return
    
    if not (os.path.isdir(f'/content/image_data/{dir}')):
      os.mkdir(f'/content/image_data/{dir}')

    medias = instagram.get_medias_by_tag(hashtag, count=limit)
    i=0
    for x in range(len(medias)):
      if(medias[x].image_high_resolution_url is not None):
        f = open(f'{path_img}/{dir}/{x}.jpg','wb')
        f.write(requests.get(medias[x].image_high_resolution_url).content)
        f.close()
      elif(medias[x].image_standard_resolution_url is not None):
        f = open(f'{path_img}/{dir}/{x}.jpg','wb')
        f.write(requests.get(medias[x].image_standard_resolution_url).content)
        f.close()
      elif(medias[x].image_low_resolution_url is not None):
        f = open(f'{path_img}/{dir}/{x}.jpg','wb')
        f.write(requests.get(medias[x].image_low_resolution_url).content)
        f.close()
      else:
        continue
      i+=1
    
    print(str(i) + ' images téléchargées dans la classes ' + dir)

def dl_from_insta_account(account : str, limit : int, dir : str):
  
    if(limit>1000):
      print("Trop d'images à télécharger")
      return

    path = f'/content/image_data/{dir}'

    if not (os.path.isdir(path)):
      os.mkdir(path)
    
    bashCommand = f"instagram-scraper {account} --maximum {limit} --destination {path}"
    output = subprocess.check_output(['bash','-c', bashCommand])

def dl_from_insta_hashtag(hashtag : str, limit : int, dir : str):
    if(limit>1000):
      print("Trop d'images à télécharger")
      return
    
    if not (os.path.isdir(f'/content/image_data/{dir}')):
      os.mkdir(f'/content/image_data/{dir}')

    medias = instagram.get_medias_by_tag(hashtag, count=limit)
    i=0
    for x in range(len(medias)):
      if(medias[x].image_high_resolution_url is not None):
        f = open(f'{path_img}/{dir}/{x}.jpg','wb')
        f.write(requests.get(medias[x].image_high_resolution_url).content)
        f.close()
      elif(medias[x].image_standard_resolution_url is not None):
        f = open(f'{path_img}/{dir}/{x}.jpg','wb')
        f.write(requests.get(medias[x].image_standard_resolution_url).content)
        f.close()
      elif(medias[x].image_low_resolution_url is not None):
        f = open(f'{path_img}/{dir}/{x}.jpg','wb')
        f.write(requests.get(medias[x].image_low_resolution_url).content)
        f.close()
      else:
        continue
      i+=1
    
    print(str(i) + ' images téléchargées dans la classes ' + dir)    
