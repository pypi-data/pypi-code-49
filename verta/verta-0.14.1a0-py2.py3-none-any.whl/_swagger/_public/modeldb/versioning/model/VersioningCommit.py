# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningCommit(dict):
  def __init__(self, parent_shas=None, message=None, date_created=None, author=None):
    self.parent_shas = parent_shas
    self.message = message
    self.date_created = date_created
    self.author = author

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
