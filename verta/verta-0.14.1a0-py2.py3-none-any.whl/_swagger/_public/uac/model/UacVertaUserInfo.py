# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacVertaUserInfo(dict):
  def __init__(self, individual_user=None, username=None, refresh_timestamp=None, last_login_timestamp=None, user_id=None, publicProfile=None):
    self.individual_user = individual_user
    self.username = username
    self.refresh_timestamp = refresh_timestamp
    self.last_login_timestamp = last_login_timestamp
    self.user_id = user_id
    self.publicProfile = publicProfile

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
