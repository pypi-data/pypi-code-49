# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbExperimentRun(dict):
  def __init__(self, id=None, project_id=None, experiment_id=None, name=None, description=None, date_created=None, date_updated=None, start_time=None, end_time=None, code_version=None, code_version_snapshot=None, parent_id=None, tags=None, attributes=None, hyperparameters=None, artifacts=None, datasets=None, metrics=None, observations=None, features=None, job_id=None, owner=None):
    self.id = id
    self.project_id = project_id
    self.experiment_id = experiment_id
    self.name = name
    self.description = description
    self.date_created = date_created
    self.date_updated = date_updated
    self.start_time = start_time
    self.end_time = end_time
    self.code_version = code_version
    self.code_version_snapshot = code_version_snapshot
    self.parent_id = parent_id
    self.tags = tags
    self.attributes = attributes
    self.hyperparameters = hyperparameters
    self.artifacts = artifacts
    self.datasets = datasets
    self.metrics = metrics
    self.observations = observations
    self.features = features
    self.job_id = job_id
    self.owner = owner

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
