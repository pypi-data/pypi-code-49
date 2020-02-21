# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbComment(dict):
  def __init__(self, id=None, user_id=None, date_time=None, message=None, user_info=None, verta_id=None):
    self.id = id
    self.user_id = user_id
    self.date_time = date_time
    self.message = message
    self.user_info = user_info
    self.verta_id = verta_id

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
