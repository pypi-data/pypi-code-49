# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ArtifactstoreStoreArtifactWithStreamResponse(dict):
  def __init__(self, cloud_file_key=None, cloud_file_path=None):
    self.cloud_file_key = cloud_file_key
    self.cloud_file_path = cloud_file_path

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
