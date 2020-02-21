# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningRepository(dict):
  def __init__(self, id=None, name=None, date_created=None, date_updated=None, workspace_id=None, workspace_type=None):
    self.id = id
    self.name = name
    self.date_created = date_created
    self.date_updated = date_updated
    self.workspace_id = workspace_id
    self.workspace_type = workspace_type

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
