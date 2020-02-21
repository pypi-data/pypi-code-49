# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbHydratedExperimentRun(dict):
  def __init__(self, experiment_run=None, comments=None, owner_user_info=None, experiment=None, allowed_actions=None):
    self.experiment_run = experiment_run
    self.comments = comments
    self.owner_user_info = owner_user_info
    self.experiment = experiment
    self.allowed_actions = allowed_actions

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
