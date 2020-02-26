import copy
from typing import Tuple, Any, Collection


class DependenciesError:
    """
    Class that collect and organize the error originating from the dependency structure of features.
    In a dependency tree, it might happen that a feature misses one or more dependencies.
    In this case, we will call 'victim' the feature that has an unfulfilled dependency requirement.

    E.g.
        consider the dependency tree:

            cost_in_month --- month --- date
                          \
                           -- cost

        if we build the FeatureBuildingBlock with features (cost_in_month, month, cost) then the victim will be
        month, and the missing dependency of month will be date

    """

    def __init__(self):
        self._missing_dependencies_map = dict()

    def __add__(self, other):
        new_de = copy.deepcopy(self)
        for k, v in other._missing_dependencies_map.items():
            if k not in new_de._missing_dependencies_map.keys():
                new_de._missing_dependencies_map[k] = v
            else:
                new_de._missing_dependencies_map[k].union(v)
        return new_de

    def is_empty(self) -> bool:
        return False if self.has_missing_dependencies() else True

    def has_missing_dependencies(self) -> bool:
        return True if sum([len(v) for v in self._missing_dependencies_map.values()]) > 0 else False

    def get_missing_dependencies_victims(self) -> Tuple[Any, ...]:
        return tuple(self._missing_dependencies_map.keys())

    def get_missing_dependency_of_victim(self, victim: str) -> Tuple[str]:
        if victim in self._missing_dependencies_map.keys():
            return tuple(self._missing_dependencies_map[victim])
        else:
            return tuple()

    def add_missing_dependencies(self, victim: str, missing_dependencies: Collection[str]):
        if len(missing_dependencies) > 0:
            if victim not in self._missing_dependencies_map.keys():
                self._missing_dependencies_map[victim] = set()
            self._missing_dependencies_map[victim] = \
                self._missing_dependencies_map[victim].union(set(missing_dependencies))

    def to_string(self) -> str:
        lines = list()
        lines.append('DependenciesError {}'.format('is empty.' if self.is_empty() else 'contains errors:'))

        for victim in self.get_missing_dependencies_victims():
            lines.append(' * {} misses {}'.format(victim, ', '.join(self.get_missing_dependency_of_victim(victim))))

        return '\n'.join(lines)
