# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbHydratedProject(dict):
  def __init__(self, project=None, collaborator_user_infos=None, owner_user_info=None, allowed_actions=None):
    self.project = project
    self.collaborator_user_infos = collaborator_user_infos
    self.owner_user_info = owner_user_info
    self.allowed_actions = allowed_actions

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
