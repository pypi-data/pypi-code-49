# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningPathDatasetDiff(dict):
  def __init__(self, deleted=None, added=None, A=None, B=None):
    self.deleted = deleted
    self.added = added
    self.A = A
    self.B = B

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
