# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbFindHydratedDatasetsByOrganization(dict):
  def __init__(self, find_datasets=None, name=None, id=None):
    self.find_datasets = find_datasets
    self.name = name
    self.id = id

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
