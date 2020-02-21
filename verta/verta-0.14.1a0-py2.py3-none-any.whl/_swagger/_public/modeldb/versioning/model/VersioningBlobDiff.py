# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningBlobDiff(dict):
  def __init__(self, path=None, dataset=None):
    self.path = path
    self.dataset = dataset

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
