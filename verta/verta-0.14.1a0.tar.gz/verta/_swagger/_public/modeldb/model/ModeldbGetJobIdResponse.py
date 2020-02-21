# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbGetJobIdResponse(dict):
  def __init__(self, job_id=None):
    self.job_id = job_id

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
