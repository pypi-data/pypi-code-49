from __future__ import annotations
from dpsql.table.model.criterion_obj import Criterion


class CaseObjectContent(object):
    def __init__(self, **kwargs):
        self._when_criteria: Criterion = kwargs.get('when', None)
        self._then: str = kwargs.get('then', '')

    @property
    def when_criteria_(self):
        return self._when_criteria

    @property
    def then_(self):
        return self._then

    @when_criteria_.setter
    def when_criteria_(self, param):
        self._when_criteria = param

    @then_.setter
    def then_(self, param):
        self._then = param
