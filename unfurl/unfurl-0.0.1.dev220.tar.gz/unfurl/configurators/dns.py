from ..configurator import Configurator, Status
from octodns.manager import Manager

"""
config.yaml
 env/DO_TOKEN
zones/
 zone.yaml

DO_TOKEN # digital ci

Note: YAML file of Octodns is the only source of truth, will delete other records
work-around? dump and compare

quirks and recommendations:
* protect master branch, require pull requests and approvals
"""

class DnsConfigurator(Configurator):
    def run(self, task):
        args = task.inputs
        manager = Manager(args.config_file)
        # eligible_targets = Limit sync to the specified target(s)'
        manager.sync(eligible_zones=args.zone, # list of zones
                     eligible_targets=args.target,
                     dry_run=self.dryRun, force=True)

    def cantRun(self, task):
        return False

    def canDryRun(self, task):
      return True
