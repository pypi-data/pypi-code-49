# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbFindHydratedProjectsByUser(dict):
  def __init__(self, find_projects=None, email=None, username=None, verta_id=None):
    self.find_projects = find_projects
    self.email = email
    self.username = username
    self.verta_id = verta_id

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
