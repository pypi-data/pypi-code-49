# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbLogArtifact(dict):
  def __init__(self, id=None, artifact=None):
    self.id = id
    self.artifact = artifact

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
