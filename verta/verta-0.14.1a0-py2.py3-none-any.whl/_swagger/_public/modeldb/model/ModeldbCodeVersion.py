# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbCodeVersion(dict):
  def __init__(self, git_snapshot=None, code_archive=None, date_logged=None):
    self.git_snapshot = git_snapshot
    self.code_archive = code_archive
    self.date_logged = date_logged

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
