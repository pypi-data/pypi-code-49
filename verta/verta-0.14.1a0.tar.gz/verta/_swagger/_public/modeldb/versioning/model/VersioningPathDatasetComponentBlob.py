# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningPathDatasetComponentBlob(dict):
  def __init__(self, path=None, size=None, last_modified_at_source=None, sha256=None, md5=None):
    self.path = path
    self.size = size
    self.last_modified_at_source = last_modified_at_source
    self.sha256 = sha256
    self.md5 = md5

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
