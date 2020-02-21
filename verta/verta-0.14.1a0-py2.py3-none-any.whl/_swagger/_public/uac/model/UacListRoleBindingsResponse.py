# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacListRoleBindingsResponse(dict):
  def __init__(self, role_bindings=None):
    self.role_bindings = role_bindings

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
