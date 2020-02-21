# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbGetUrlForArtifact(dict):
  def __init__(self, id=None, key=None, method=None, artifact_type=None):
    self.id = id
    self.key = key
    self.method = method
    self.artifact_type = artifact_type

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
