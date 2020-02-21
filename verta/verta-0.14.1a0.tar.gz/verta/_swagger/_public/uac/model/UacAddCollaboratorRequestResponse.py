# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacAddCollaboratorRequestResponse(dict):
  def __init__(self, self_allowed_actions=None, status=None, collaborator_user_info=None, collaborator_organization=None, collaborator_team=None):
    self.self_allowed_actions = self_allowed_actions
    self.status = status
    self.collaborator_user_info = collaborator_user_info
    self.collaborator_organization = collaborator_organization
    self.collaborator_team = collaborator_team

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
