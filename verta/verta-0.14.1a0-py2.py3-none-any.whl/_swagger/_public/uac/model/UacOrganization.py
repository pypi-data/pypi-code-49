# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacOrganization(dict):
  def __init__(self, id=None, name=None, short_name=None, description=None, owner_id=None, created_timestamp=None, updated_timestamp=None):
    self.id = id
    self.name = name
    self.short_name = short_name
    self.description = description
    self.owner_id = owner_id
    self.created_timestamp = created_timestamp
    self.updated_timestamp = updated_timestamp

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
