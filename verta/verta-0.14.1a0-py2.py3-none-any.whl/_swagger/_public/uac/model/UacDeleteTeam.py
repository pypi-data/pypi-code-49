# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacDeleteTeam(dict):
  def __init__(self, team_id=None):
    self.team_id = team_id

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
