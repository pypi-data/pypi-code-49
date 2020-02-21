# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbSetProjectReadme(dict):
  def __init__(self, id=None, readme_text=None):
    self.id = id
    self.readme_text = readme_text

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
