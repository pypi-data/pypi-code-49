# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacGetRoleBindingByNameResponse(dict):
  def __init__(self, role_binding=None):
    self.role_binding = role_binding

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
