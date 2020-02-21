# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbArtifact(dict):
  def __init__(self, key=None, path=None, path_only=None, artifact_type=None, linked_artifact_id=None, filename_extension=None):
    self.key = key
    self.path = path
    self.path_only = path_only
    self.artifact_type = artifact_type
    self.linked_artifact_id = linked_artifact_id
    self.filename_extension = filename_extension

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
