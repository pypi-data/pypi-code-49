import copy

from features_factory.dependencies_error import DependenciesError
from features_factory.input_data_error import InputDataError


class StackError:
    """
    Class that collect and organize the Stack errors.
    It is composed of two set of errors: InputDataError and DependenciesError
    """

    def __init__(self):
        self._input_data_error = InputDataError()
        self._dependencies_error = DependenciesError()

    def __add__(self, other):
        new_bbe = copy.deepcopy(self)
        new_bbe._input_data_error += other.get_input_data_error()
        new_bbe._dependencies_error += other.get_dependencies_error()
        return new_bbe

    def is_empty(self) -> bool:
        return all((self._input_data_error.is_empty(), self._dependencies_error.is_empty()))

    def get_input_data_error(self) -> InputDataError:
        return copy.deepcopy(self._input_data_error)

    def get_dependencies_error(self) -> DependenciesError:
        return copy.deepcopy(self._dependencies_error)

    def add_input_data_error(self, ie: InputDataError):
        self._input_data_error += ie

    def add_dependency_error(self, de: DependenciesError):
        self._dependencies_error += de

    def to_string(self) -> str:
        return '\n'.join([self._input_data_error.to_string(),
                          self._dependencies_error.to_string()])
