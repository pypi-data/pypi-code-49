# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningFolderElement(dict):
  def __init__(self, element_name=None, created_by_commit=None):
    self.element_name = element_name
    self.created_by_commit = created_by_commit

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
