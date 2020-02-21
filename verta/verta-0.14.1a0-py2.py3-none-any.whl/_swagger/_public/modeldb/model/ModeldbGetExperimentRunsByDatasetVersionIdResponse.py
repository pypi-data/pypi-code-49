# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbGetExperimentRunsByDatasetVersionIdResponse(dict):
  def __init__(self, experiment_runs=None, total_records=None):
    self.experiment_runs = experiment_runs
    self.total_records = total_records

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
