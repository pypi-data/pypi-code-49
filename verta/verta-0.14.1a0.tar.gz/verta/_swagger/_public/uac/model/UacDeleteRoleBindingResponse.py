# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacDeleteRoleBindingResponse(dict):
  def __init__(self, status=None):
    self.status = status

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
