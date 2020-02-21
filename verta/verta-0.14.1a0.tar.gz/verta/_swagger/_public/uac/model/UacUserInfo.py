# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacUserInfo(dict):
  def __init__(self, user_id=None, full_name=None, first_name=None, last_name=None, email=None, id_service_provider=None, roles=None, image_url=None, dev_key=None, verta_info=None):
    self.user_id = user_id
    self.full_name = full_name
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.id_service_provider = id_service_provider
    self.roles = roles
    self.image_url = image_url
    self.dev_key = dev_key
    self.verta_info = verta_info

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
