# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class MetadataIdentificationType(dict):
  def __init__(self, id_type=None, int_id=None, string_id=None):
    self.id_type = id_type
    self.int_id = int_id
    self.string_id = string_id

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
