# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbLastModifiedExperimentRunSummary(dict):
  def __init__(self, name=None, last_updated_time=None):
    self.name = name
    self.last_updated_time = last_updated_time

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
