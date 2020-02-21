# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbGetSummaryResponse(dict):
  def __init__(self, name=None, last_updated_time=None, total_experiment=None, total_experiment_runs=None, last_modified_experimentRun_summary=None, metrics=None):
    self.name = name
    self.last_updated_time = last_updated_time
    self.total_experiment = total_experiment
    self.total_experiment_runs = total_experiment_runs
    self.last_modified_experimentRun_summary = last_modified_experimentRun_summary
    self.metrics = metrics

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
