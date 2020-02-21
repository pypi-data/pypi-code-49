# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningFolder(dict):
  def __init__(self, blobs=None, sub_folders=None):
    self.blobs = blobs
    self.sub_folders = sub_folders

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
