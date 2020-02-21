# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbDatasetPartInfo(dict):
  def __init__(self, path=None, size=None, checksum=None, last_modified_at_source=None):
    self.path = path
    self.size = size
    self.checksum = checksum
    self.last_modified_at_source = last_modified_at_source

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
