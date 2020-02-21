# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbGetProjectByNameResponse(dict):
  def __init__(self, project_by_user=None, shared_projects=None):
    self.project_by_user = project_by_user
    self.shared_projects = shared_projects

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
