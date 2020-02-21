# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbPathDatasetVersionInfo(dict):
  def __init__(self, location_type=None, size=None, dataset_part_infos=None, base_path=None):
    self.location_type = location_type
    self.size = size
    self.dataset_part_infos = dataset_part_infos
    self.base_path = base_path

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
