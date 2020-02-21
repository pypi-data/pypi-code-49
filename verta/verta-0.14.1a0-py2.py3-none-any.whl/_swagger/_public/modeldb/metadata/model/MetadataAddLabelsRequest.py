# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class MetadataAddLabelsRequest(dict):
  def __init__(self, id=None, labels=None):
    self.id = id
    self.labels = labels

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
