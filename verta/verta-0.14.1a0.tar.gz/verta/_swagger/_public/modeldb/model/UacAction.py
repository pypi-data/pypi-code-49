# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacAction(dict):
  def __init__(self, service=None, role_service_action=None, authz_service_action=None, modeldb_service_action=None):
    self.service = service
    self.role_service_action = role_service_action
    self.authz_service_action = authz_service_action
    self.modeldb_service_action = modeldb_service_action

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
