# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbGetHydratedDatasetByNameResponse(dict):
  def __init__(self, hydrated_dataset_by_user=None, shared_hydrated_datasets=None):
    self.hydrated_dataset_by_user = hydrated_dataset_by_user
    self.shared_hydrated_datasets = shared_hydrated_datasets

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
