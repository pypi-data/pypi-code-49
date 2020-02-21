# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbObservation(dict):
  def __init__(self, attribute=None, artifact=None, timestamp=None):
    self.attribute = attribute
    self.artifact = artifact
    self.timestamp = timestamp

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
