# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacGetUsers(dict):
  def __init__(self, user_ids=None, emails=None, usernames=None):
    self.user_ids = user_ids
    self.emails = emails
    self.usernames = usernames

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
