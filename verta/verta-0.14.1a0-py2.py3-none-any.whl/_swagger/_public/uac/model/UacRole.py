# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacRole(dict):
  def __init__(self, id=None, name=None, scope=None, resource_action_groups=None):
    self.id = id
    self.name = name
    self.scope = scope
    self.resource_action_groups = resource_action_groups

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
