# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningRepositoryNamedIdentification(dict):
  def __init__(self, name=None, workspace_name=None):
    self.name = name
    self.workspace_name = workspace_name

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
