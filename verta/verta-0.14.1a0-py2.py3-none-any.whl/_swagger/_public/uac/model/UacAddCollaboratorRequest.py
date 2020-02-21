# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacAddCollaboratorRequest(dict):
  def __init__(self, entity_ids=None, share_with=None, collaborator_type=None, message=None, date_created=None, date_updated=None, can_deploy=None, authz_entity_type=None):
    self.entity_ids = entity_ids
    self.share_with = share_with
    self.collaborator_type = collaborator_type
    self.message = message
    self.date_created = date_created
    self.date_updated = date_updated
    self.can_deploy = can_deploy
    self.authz_entity_type = authz_entity_type

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
