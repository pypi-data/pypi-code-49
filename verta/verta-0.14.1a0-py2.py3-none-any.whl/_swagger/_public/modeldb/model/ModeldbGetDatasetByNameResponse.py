# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbGetDatasetByNameResponse(dict):
  def __init__(self, dataset_by_user=None, shared_datasets=None):
    self.dataset_by_user = dataset_by_user
    self.shared_datasets = shared_datasets

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
