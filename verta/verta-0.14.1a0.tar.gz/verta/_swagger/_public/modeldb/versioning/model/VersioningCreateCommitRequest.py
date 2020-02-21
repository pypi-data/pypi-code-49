# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningCreateCommitRequest(dict):
  def __init__(self, repository_id=None, commit=None, blobs=None):
    self.repository_id = repository_id
    self.commit = commit
    self.blobs = blobs

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
