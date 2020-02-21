# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbCollaboratorUserInfo(dict):
  def __init__(self, collaborator_user_info=None, collaborator_organization=None, collaborator_team=None, collaborator_type=None, can_deploy=None, entity_type=None):
    self.collaborator_user_info = collaborator_user_info
    self.collaborator_organization = collaborator_organization
    self.collaborator_team = collaborator_team
    self.collaborator_type = collaborator_type
    self.can_deploy = can_deploy
    self.entity_type = entity_type

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
