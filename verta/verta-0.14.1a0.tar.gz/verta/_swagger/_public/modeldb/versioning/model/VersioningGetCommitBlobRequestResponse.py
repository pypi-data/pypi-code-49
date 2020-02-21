# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningGetCommitBlobRequestResponse(dict):
  def __init__(self, blob=None):
    self.blob = blob

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
