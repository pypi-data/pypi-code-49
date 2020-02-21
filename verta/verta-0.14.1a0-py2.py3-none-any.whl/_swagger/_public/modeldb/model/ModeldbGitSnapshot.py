# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbGitSnapshot(dict):
  def __init__(self, filepaths=None, repo=None, hash=None, is_dirty=None):
    self.filepaths = filepaths
    self.repo = repo
    self.hash = hash
    self.is_dirty = is_dirty

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
