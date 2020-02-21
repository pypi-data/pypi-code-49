# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbSetParentExperimentRunId(dict):
  def __init__(self, experiment_run_id=None, parent_id=None):
    self.experiment_run_id = experiment_run_id
    self.parent_id = parent_id

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
