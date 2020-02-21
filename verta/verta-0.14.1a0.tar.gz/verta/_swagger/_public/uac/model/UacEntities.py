# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacEntities(dict):
  def __init__(self, user_ids=None, org_ids=None, team_ids=None):
    self.user_ids = user_ids
    self.org_ids = org_ids
    self.team_ids = team_ids

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
