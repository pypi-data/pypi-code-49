# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbMetricsSummary(dict):
  def __init__(self, key=None, min_value=None, max_value=None):
    self.key = key
    self.min_value = min_value
    self.max_value = max_value

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
