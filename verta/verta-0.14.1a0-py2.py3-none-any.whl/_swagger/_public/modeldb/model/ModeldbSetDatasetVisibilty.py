# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbSetDatasetVisibilty(dict):
  def __init__(self, id=None, dataset_visibility=None):
    self.id = id
    self.dataset_visibility = dataset_visibility

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
