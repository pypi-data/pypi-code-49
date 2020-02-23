from abc import ABC, abstractmethod
from typing import Any
from inspect import signature

from aistac.properties.abstract_properties import AbstractPropertyManager

__author__ = 'Darryl Oatridge'


class AbstractIntentModel(ABC):
    """Abstract AI Single Task Application Component (AI-STAC) Class for Parameterised Intent containing parameterised
    intent registration methods `_intent_builder(...)` and `_set_intend_signature(...)`.

    it is creating a construct initialisation to allow for the control and definition of an `intent_param_exclude`
    list, `default_save_intent` boolean and a `default_intent_level` value.

    As an example of an initialisation method
    literal blocks::
        def __init__(self, property_manager: AbstractPropertyManager, default_save_intent: bool=None,
                     intent_next_available: bool=None, default_replace_intent: bool=None):
            # set all the defaults
            default_save_intent = default_save_intent if isinstance(default_save_intent, bool) else True
            default_replace_intent = default_replace_intent if isinstance(default_replace_intent, bool) else False
            default_intent_level = -1 if isinstance(intent_next_available, bool) and intent_next_available else 0
            intent_param_exclude = ['inplace', 'canonical']
            intent_type_additions = []
            super().__init__(property_manager=property_manager, intent_param_exclude=intent_param_exclude,
                             default_save_intent=default_save_intent, default_intent_level=default_intent_level,
                             default_replace_intent=default_replace_intent, intent_type_additions=intent_type_additions)

    in order to define the run pattern for the component task `run_intent_pipeline(...)` is an abstracted method
    that defines the run pipeline of the intent.

    As an example of a run_pipeline that iteratively updates a canonical with each intent
    literal blocks::
        def run_intent_pipeline(self, canonical, levels: [int, str, list]=None, inplace: bool=False, **kwargs):
            inplace = inplace if isinstance(inplace, bool) else False
            # test if there is any intent to run
            if self._pm.has_intent() and not inplace:
                # create the copy and use this for all the operations
                if not inplace:
                    canonical = deepcopy(canonical)
                # get the list of levels to run
                if isinstance(levels, (int, str, list)):
                    levels = self._pm.list_formatter(levels)
                else:
                    levels = sorted(self._pm.get_intent().keys())
                for level in levels:
                    for method, params in self._pm.get_intent(level=level).items():
                        if method in self.__dir__():
                            if isinstance(kwargs, dict):
                                params.update(kwargs)
                            canonical = eval(f"self.{method}(canonical, inplace=False, save_intent=False, **{params})")
            if not inplace:
                return canonical
            return

    the code signature for an intent method would have the following construct
    literal blocks::
    def <method>(self, <params>..., save_intent: bool=None, replace_intent: bool=None, intent_level: [int, str]=None):
        # resolve intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   intent_level=intent_level, save_intent=save_intent, replace_intent=replace_intent)

        # intend code block on the canonical
        ...

    """

    def __init__(self, property_manager: AbstractPropertyManager, default_save_intent: bool, intent_param_exclude: list,
                 default_intent_level: [str, int, float], default_replace_intent: bool, intent_type_additions: list):
        """ initialisation of the Intent class. The 'intent_param_exclude' is used to exclude commonly used method
         parameters from being included in the intent contract, this is particularly useful if passing a
         non relevant parameters to an intent method pattern. Any named parameter in the `intent_param_exclude` list
         will not be added to the default and excluded from the recorded intent contract for that method.
         By default, key word exclusions are 'self', 'intent_level' and 'save_intent' are excluded from
         the parameters list

        :param intent_type_additions:
        :param property_manager: the property manager class that references the intent contract.
        :param default_save_intent: The default action for saving intent in the property manager
        :param default_intent_level: The default intent level if none is provided
        :param intent_param_exclude: exclusion list of method parameters from the intent contract
        :param default_replace_intent: the default replace strategy for the same intent found at that level
        :param intent_type_additions: a list additional supported types to persist to the contract.
                                by default (str, int, float, list, dict, set, tuple, bool) are supported
        """
        if not isinstance(property_manager, AbstractPropertyManager):
            raise ValueError("The property_manager must be an instance of a concrete "
                             "implementation of AbstractPropertyManager")
        self._pm = property_manager
        intent_param_exclude = intent_param_exclude
        self._intent_param_exclude = {'self', 'save_intent', 'intent_level', 'replace_intent'}
        self._intent_param_exclude.update(intent_param_exclude)
        self._default_intent_level = default_intent_level
        self._default_save_intent = default_save_intent
        self._default_replace_intent = default_replace_intent
        intent_type_additions = intent_type_additions if isinstance(intent_type_additions, list) else list()
        self._intent_supported_types = (str, int, float, list, dict, set, tuple, bool) + tuple(intent_type_additions)

    @classmethod
    def __dir__(cls):
        """returns the list of available methods associated with the parameterized intent"""
        rtn_list = []
        for m in dir(cls):
            if not m.startswith('_'):
                rtn_list.append(m)
        return rtn_list

    @abstractmethod
    def run_intent_pipeline(self, run_book: Any, *args, **kwargs):
        """ Collectively runs all parameterised intent taken from the property manager against the code base as
        defined by the intent_contract.

        :param run_book: a single or list of intent_level to run, if list, run in order given
        """

    def _set_intend_signature(self, intent_params: dict, intent_level: [int, str]=None, replace_intent: bool=None,
                              save_intent: bool=None) -> None:
        """ sets the intent section in the configuration file. Note: by default any identical intent, e.g.
        intent with the same intent (name) and the same parameter values, are removed from any level.

        :param intent_params: a dictionary type set of configuration representing a intent section contract
        :param intent_level: (optional) the level of the intent
                        If None: default's to -1
                        if -1: added to a level above any current instance of the intent section, level 0 if not found
                        if int: added to the level specified, overwriting any that already exist
        :param replace_intent: (optional) if the intent method exists at the level, or default level
                        True - replaces the current intent method with the new
                        False - leaves it untouched, disregarding the new intent
        :param save_intent (optional) if the intent contract should be saved to the property manager
        """
        if not isinstance(save_intent, bool):
            save_intent = self._default_save_intent
        if not isinstance(replace_intent, bool):
            replace_intent = self._default_replace_intent
        if save_intent:
            intent_level = intent_level if isinstance(intent_level, (int, str)) else self._default_intent_level
            self._pm.set_intent(intent_param=intent_params, level=intent_level, replace_intent=replace_intent)
            self._pm.persist_properties()
        return

    def _intent_builder(self, method: str, params: dict, exclude: list=None) -> dict:
        """builds the intent_params. Pass the method name and local() parameters
            Example:
                self._intent_builder(inspect.currentframe().f_code.co_name, **locals())

        :param method: the name of the method (intent). can use 'inspect.currentframe().f_code.co_name'
        :param params: the parameters passed to the method. use `locals()` in the caller method
        :param exclude: (optional) convenience parameter identifying param keys to exclude.
        :return: dict of the intent
        """
        exclude = [] if not isinstance(exclude, list) else exclude
        exclude_params = self._intent_param_exclude.copy()
        if isinstance(exclude, list) and len(exclude) > 0:
            exclude_params.update(exclude)
        intent_signature = dict({method: {}})
        for v in signature(eval("self.{}".format(method))).parameters.values():
            value = params.get(v.name)
            if v.name in exclude_params or value is None:
                continue
            if not isinstance(value, self._intent_supported_types):
                raise TypeError("The intent parameter '{}', type '{}' is not supported".format(v.name, type(value)))
            intent_signature[method].update({v.name: value})
        return intent_signature
