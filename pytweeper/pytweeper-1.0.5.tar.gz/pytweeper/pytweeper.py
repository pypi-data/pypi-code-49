from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from progress.bar import ChargingBar
import tweepy
import pickle
import os
from datetime import datetime
from pathlib import Path
from .twitter import *
from .operation import *

root_folder = Path(__file__).resolve().parent
timeline_path = Path.joinpath(root_folder,'timeline.pkl')
key_path = Path.joinpath(root_folder,'key.pkl')

def pickle_dump(x, name):
  with open(name, 'wb') as f:
    pickle.dump([status._json for status in x], f)

def save_key(key):
  with open(key_path, 'wb') as f:
    pickle.dump(key, f)

def load_key():
  try:
    with open(key_path, 'rb') as f:
      return pickle.load(f)
  except FileNotFoundError:
    return {}

def remove_access_token():
  try:
    with open(key_path, 'rb') as f:
      key = pickle.load(f)
    del key['access_token']
    del key['access_secret']
    del key['name']
    del key['id']
    del key['error']
    with open(key_path, 'wb') as f:
      pickle.dump(key, f)
    return True
  except FileNotFoundError:
    return False

def check_key(obj, key):
  try:
    if obj[key]:
      return True
  except KeyError:
    return False

class Tweeper:
  def __init__(self):
    self.files = {
      'timeline': 'timeline.pkl'
    }
    self.authorize = False
    self.twitter_auth = TwitterAuth()
  
  def logout(self):
    if remove_access_token():
      self.authorize = False

  def initialize_api(self):
    key = load_key()
    if check_key(key, 'consumer_key') and check_key(key, 'consumer_secret'):
      self.twitter_auth.set_comsumer_keys(key['consumer_key'], key['consumer_secret'])
      if not(check_key(key, 'access_token') or check_key(key, 'access_secret')): # Already has keys
        key = self.twitter_auth.auth()
      if not key['error']:
        save_key(key)
        auth = tweepy.OAuthHandler(key['consumer_key'], key['consumer_secret'])
        auth.set_access_token(key['access_token'], key['access_secret'])
        self.api = tweepy.API(auth, wait_on_rate_limit=True)
        self.authorize = True
    else:
      print("Unauthorize please set consumer keys by run 'pytweeper init'")
  
  def set_file(self, name, file):
    self.files[name] = file
  
  def get_me(self):
    return self.api.me()
  
  def get_home_timeline(self, end_page=1):
    timeline = []
    bar = ChargingBar('Crawling', max=end_page)
    for page in range(1, end_page+1):
      timeline += self.api.home_timeline(page=page, count=200)
      pickle_dump(timeline, self.files['timeline'])
      bar.next()
    bar.finish()
    return timeline

def main():
  import argparse
  parser = argparse.ArgumentParser(description='PyTweeper (Twitter crawler)')
  parser.add_argument('command', nargs='?', help='command or mode')
  parser.add_argument('-p', type=int, help='page count for crawler')
  parser.add_argument('-o', type=str, help='output destination')
  parser.add_argument('--logout', action='store_true', help='output destination')

  today = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
  args = vars(parser.parse_args())
  command = args['command']
  page = args['p'] or 10
  output = Path.joinpath(Path(args['o'] or Path.cwd()).resolve(), 'pytweeper', today)
  logout = args['logout']

  consumer_key = None
  consumer_secret = None

  client = Tweeper()
  if logout:
    client.logout()
  elif command == 'init':
    consumer_key = input("Consumer key: ")
    consumer_secret = input("Consumer secret: ")
    with open(key_path, 'wb') as f:
      pickle.dump({ "consumer_key": consumer_key, "consumer_secret": consumer_secret }, f)
  else:
    client.initialize_api()
    if client.authorize:
      client.set_file('timeline', timeline_path)
      client.get_home_timeline(page)
      read_and_download(timeline_path, output)


if __name__ == "__main__":
  pass
