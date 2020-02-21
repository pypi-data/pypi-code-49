# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningPagination(dict):
  def __init__(self, page_number=None, page_limit=None):
    self.page_number = page_number
    self.page_limit = page_limit

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
