# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbDeleteProjectTags(dict):
  def __init__(self, id=None, tags=None, delete_all=None):
    self.id = id
    self.tags = tags
    self.delete_all = delete_all

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
