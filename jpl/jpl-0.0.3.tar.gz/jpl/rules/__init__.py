from itertools import chain

from jpl.rules.playbook import info, PlayBookExists
from jpl.rules.pipeline import pipeline
from jpl.rules.task import function, task


rules = list(chain.from_iterable([info.rules, pipeline.rules]))
task_rules = list(chain.from_iterable([function.rules, task.rules]))
