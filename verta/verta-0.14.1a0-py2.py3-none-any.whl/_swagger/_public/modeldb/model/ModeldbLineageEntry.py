# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbLineageEntry(dict):
  def __init__(self, `type`=None, external_id=None):
    self.`type` = `type`
    self.external_id = external_id

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
