# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbCreateDataset(dict):
  def __init__(self, name=None, description=None, tags=None, attributes=None, dataset_visibility=None, dataset_type=None, workspace_name=None, time_created=None):
    self.name = name
    self.description = description
    self.tags = tags
    self.attributes = attributes
    self.dataset_visibility = dataset_visibility
    self.dataset_type = dataset_type
    self.workspace_name = workspace_name
    self.time_created = time_created

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
