# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbFindAllInputsOutputs(dict):
  def __init__(self, items=None):
    self.items = items

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
