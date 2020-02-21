# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbUpdateExperimentNameOrDescription(dict):
  def __init__(self, id=None, name=None, description=None):
    self.id = id
    self.name = name
    self.description = description

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
