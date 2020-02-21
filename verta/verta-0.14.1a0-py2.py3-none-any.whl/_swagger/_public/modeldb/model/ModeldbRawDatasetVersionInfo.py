# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbRawDatasetVersionInfo(dict):
  def __init__(self, size=None, features=None, num_records=None, object_path=None, checksum=None):
    self.size = size
    self.features = features
    self.num_records = num_records
    self.object_path = object_path
    self.checksum = checksum

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
