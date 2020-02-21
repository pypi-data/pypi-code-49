# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbAdvancedQueryDatasetVersionsResponse(dict):
  def __init__(self, hydrated_dataset_versions=None, total_records=None):
    self.hydrated_dataset_versions = hydrated_dataset_versions
    self.total_records = total_records

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
