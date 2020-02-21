# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbCreateJob(dict):
  def __init__(self, description=None, start_time=None, end_time=None, metadata=None, job_status=None, job_type=None):
    self.description = description
    self.start_time = start_time
    self.end_time = end_time
    self.metadata = metadata
    self.job_status = job_status
    self.job_type = job_type

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
