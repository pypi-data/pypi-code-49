# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbCreateDatasetVersion(dict):
  def __init__(self, dataset_id=None, parent_id=None, description=None, tags=None, dataset_version_visibility=None, dataset_type=None, attributes=None, version=None, raw_dataset_version_info=None, path_dataset_version_info=None, query_dataset_version_info=None, time_created=None):
    self.dataset_id = dataset_id
    self.parent_id = parent_id
    self.description = description
    self.tags = tags
    self.dataset_version_visibility = dataset_version_visibility
    self.dataset_type = dataset_type
    self.attributes = attributes
    self.version = version
    self.raw_dataset_version_info = raw_dataset_version_info
    self.path_dataset_version_info = path_dataset_version_info
    self.query_dataset_version_info = query_dataset_version_info
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
