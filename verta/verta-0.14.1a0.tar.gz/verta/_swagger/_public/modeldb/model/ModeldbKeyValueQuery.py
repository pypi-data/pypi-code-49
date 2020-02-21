# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbKeyValueQuery(dict):
  def __init__(self, key=None, value=None, value_type=None, operator=None):
    self.key = key
    self.value = value
    self.value_type = value_type
    self.operator = operator

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
