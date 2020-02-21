# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacRoleBinding(dict):
  def __init__(self, id=None, name=None, scope=None, entities=None, resources=None, role_id=None):
    self.id = id
    self.name = name
    self.scope = scope
    self.entities = entities
    self.resources = resources
    self.role_id = role_id

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
