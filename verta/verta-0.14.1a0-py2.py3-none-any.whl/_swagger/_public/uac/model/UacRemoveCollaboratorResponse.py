# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacRemoveCollaboratorResponse(dict):
  def __init__(self, status=None, self_allowed_actions=None):
    self.status = status
    self.self_allowed_actions = self_allowed_actions

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
