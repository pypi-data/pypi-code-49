# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningRepositoryIdentification(dict):
  def __init__(self, named_id=None, repo_id=None):
    self.named_id = named_id
    self.repo_id = repo_id

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
