from requests_oauthlib import OAuth1Session
import webbrowser

class TwitterAuth:
  def __init__(self):
    self.consumer_key = ''
    self.consumer_secret = ''
    self.resource_owner_key = ''
    self.resource_owner_secret = ''

  def set_comsumer_keys(self, consumer_key, consumer_secret):
    self.consumer_key = consumer_key
    self.consumer_secret = consumer_secret
  
  def get_oauth_request_token(self):
    request_token = OAuth1Session(client_key=self.consumer_key, client_secret=self.consumer_secret)
    url = 'https://api.twitter.com/oauth/request_token'
    data = request_token.get(url)
    if data.status_code == 200:
      data_token = str.split(data.text, '&')
      ro_key = str.split(data_token[0], '=')
      ro_secret = str.split(data_token[1], '=')
      self.resource_owner_key = ro_key[1]
      self.resource_owner_secret = ro_secret[1]
      auth_url = "https://api.twitter.com/oauth/authenticate?oauth_token={}".format(self.resource_owner_key)
      print("Please open this link on your browser: ", auth_url)
      webbrowser.open(auth_url, new=0, autoraise=True)
      return True
    else:
      print("Consumer tokens are invalid please set consumer keys again.")
      return False

  def get_oauth_token(self, verifier):
    oauth_token = OAuth1Session(client_key=self.consumer_key,
                                client_secret=self.consumer_secret,
                                resource_owner_key=self.resource_owner_key,
                                resource_owner_secret=self.resource_owner_secret)
    url = 'https://api.twitter.com/oauth/access_token'
    data = {"oauth_verifier": verifier}
    access_token_data = oauth_token.post(url, data=data)
    if (access_token_data.status_code == 200):
      access_token_list = str.split(access_token_data.text, '&')
      access_token_key = str.split(access_token_list[0], '=')
      access_token_secret = str.split(access_token_list[1], '=')
      access_token_name = str.split(access_token_list[3], '=')
      access_token_id = str.split(access_token_list[2], '=')
      key = access_token_key[1]
      secret = access_token_secret[1]
      name = access_token_name[1]
      id = access_token_id[1]
      return {"consumer_key": self.consumer_key, "consumer_secret": self.consumer_secret, "access_token": key, "access_secret": secret, "name": name, "id": id, "error": False}
    else:
      error = "Verfy code is invalid please try again."
      print(error)
      return {"error": error}

  def auth(self):
    if self.get_oauth_request_token():
      try:
        verifier = input("Verify code: ")
        result = self.get_oauth_token(verifier)
        return result
      except KeyboardInterrupt:
        pass
    return {"error": "Unauthorize"}

if __name__ == '__main__':
  print("Twitter Authentication (OAuth) module")