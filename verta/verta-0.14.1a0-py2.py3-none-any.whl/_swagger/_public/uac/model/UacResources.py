# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacResources(dict):
  def __init__(self, service=None, resource_ids=None, role_service_resource_type=None, authz_service_resource_type=None, modeldb_service_resource_type=None):
    self.service = service
    self.resource_ids = resource_ids
    self.role_service_resource_type = role_service_resource_type
    self.authz_service_resource_type = authz_service_resource_type
    self.modeldb_service_resource_type = modeldb_service_resource_type

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
