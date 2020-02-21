# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacSetOrganization(dict):
  def __init__(self, organization=None, global_collaborator_type=None, global_can_deploy=None):
    self.organization = organization
    self.global_collaborator_type = global_collaborator_type
    self.global_can_deploy = global_can_deploy

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
