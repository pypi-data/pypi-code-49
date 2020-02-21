# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbAddComment(dict):
  def __init__(self, entity_id=None, date_time=None, message=None):
    self.entity_id = entity_id
    self.date_time = date_time
    self.message = message

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
