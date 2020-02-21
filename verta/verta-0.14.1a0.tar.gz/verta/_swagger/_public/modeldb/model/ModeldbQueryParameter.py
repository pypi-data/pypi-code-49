# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbQueryParameter(dict):
  def __init__(self, parameter_name=None, parameter_type=None, value=None):
    self.parameter_name = parameter_name
    self.parameter_type = parameter_type
    self.value = value

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
