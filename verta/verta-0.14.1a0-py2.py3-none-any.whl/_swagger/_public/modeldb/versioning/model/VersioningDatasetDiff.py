# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningDatasetDiff(dict):
  def __init__(self, s3=None, path=None):
    self.s3 = s3
    self.path = path

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
