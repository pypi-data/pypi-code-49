# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacCreateUser(dict):
  def __init__(self, info=None, password=None):
    self.info = info
    self.password = password

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
