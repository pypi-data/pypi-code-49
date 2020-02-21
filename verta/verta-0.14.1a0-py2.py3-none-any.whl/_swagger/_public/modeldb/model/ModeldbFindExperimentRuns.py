# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbFindExperimentRuns(dict):
  def __init__(self, project_id=None, experiment_id=None, experiment_run_ids=None, predicates=None, ids_only=None, page_number=None, page_limit=None, ascending=None, sort_key=None):
    self.project_id = project_id
    self.experiment_id = experiment_id
    self.experiment_run_ids = experiment_run_ids
    self.predicates = predicates
    self.ids_only = ids_only
    self.page_number = page_number
    self.page_limit = page_limit
    self.ascending = ascending
    self.sort_key = sort_key

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
