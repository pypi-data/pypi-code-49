# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ArtifactstoreStoreArtifactResponse(dict):
  def __init__(self, artifact_store_key=None, artifact_store_path=None):
    self.artifact_store_key = artifact_store_key
    self.artifact_store_path = artifact_store_path

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
