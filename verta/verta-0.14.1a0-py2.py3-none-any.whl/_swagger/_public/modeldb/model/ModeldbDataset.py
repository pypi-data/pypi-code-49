# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbDataset(dict):
  def __init__(self, id=None, name=None, owner=None, description=None, tags=None, dataset_visibility=None, dataset_type=None, attributes=None, time_created=None, time_updated=None, workspace_id=None, workspace_type=None):
    self.id = id
    self.name = name
    self.owner = owner
    self.description = description
    self.tags = tags
    self.dataset_visibility = dataset_visibility
    self.dataset_type = dataset_type
    self.attributes = attributes
    self.time_created = time_created
    self.time_updated = time_updated
    self.workspace_id = workspace_id
    self.workspace_type = workspace_type

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
