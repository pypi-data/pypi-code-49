# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacDeleteUser(dict):
  def __init__(self, user_id=None):
    self.user_id = user_id

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
