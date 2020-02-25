import inspect

from aistac.components.abstract_component import AbstractComponent
from aistac.intent.abstract_intent import AbstractIntentModel
from aistac.properties.abstract_properties import AbstractPropertyManager

__author__ = 'Darryl Oatridge'


class MasterLedgerPropertyManager(AbstractPropertyManager):

    def __init__(self, task_name: str):
        """Abstract Class for the Master Properties"""
        root_keys = ['components']
        knowledge_keys = []
        super().__init__(task_name=task_name, root_keys=root_keys, knowledge_keys=knowledge_keys)

    @classmethod
    def manager_name(cls) -> str:
        """returns the name of the property manager"""
        return 'master'

    def register_component(self, property_manager: AbstractPropertyManager):
        """ registers a component

        :param property_manager: the property manager of the component
        """
        manager = property_manager.manager_name()
        task = property_manager.task_name
        connector_contract = property_manager.get_connector_contract(self.CONNECTOR_PM_CONTRACT)
        self._create_abstract_properties()
        self.set(self.join(self.KEY.components_key, manager, task, 'description'), property_manager.description)
        self.set(self.join(self.KEY.components_key, manager, task, 'uri'), connector_contract.uri_raw)
        self.set(self.join(self.KEY.components_key, manager, task, 'module_name'), connector_contract.module_name)
        self.set(self.join(self.KEY.components_key, manager, task, 'handler'), connector_contract.handler)
        self.set(self.join(self.KEY.connectors_key, manager, task, 'version'), connector_contract.version)
        self.set(self.join(self.KEY.components_key, manager, task, 'kwargs'), connector_contract.kwargs)


class MasterLedgerIntentModel(AbstractIntentModel):

    def __init__(self, property_manager: AbstractPropertyManager, default_save_intent: bool=None,
                 default_intent_level: [str, int, float]=None, default_replace_intent: bool=None,
                 intent_type_additions: list=None):
        """initialisation of the Intent class.

        :param property_manager: the property manager class that references the intent contract.
        :param default_save_intent: (optional) The default action for saving intent in the property manager
        :param default_intent_level: (optional) The default intent level
        :param intent_type_additions: (optional) if the intent parameters have extra types beyond standard
        """
        default_save_intent = default_save_intent if isinstance(default_save_intent, bool) else True
        default_intent_level = default_intent_level if isinstance(default_intent_level, (str, int, float)) else 0
        default_replace_intent = default_replace_intent if isinstance(default_replace_intent, bool) else True
        intent_param_exclude = ['inplace', 'canonical']
        intent_type_additions = intent_type_additions if isinstance(intent_type_additions, list) else list()
        super().__init__(property_manager=property_manager, default_save_intent=default_save_intent,
                         intent_param_exclude=intent_param_exclude, default_intent_level=default_intent_level,
                         default_replace_intent=default_replace_intent, intent_type_additions=intent_type_additions)

    def run_intent_pipeline(self, run_book: [int, str, list], **kwargs):
        pass

    def replace_uri(self, property_names_list: list, old: str, new: str, save_intent: bool=True,
                    intent_level: [int, str]=None):
        """ resets the list of contract names provided

        :param property_names_list: list of contract property names
        :param old: the old uri or part uri
        :param new: the new uri or part uri to replace the old with
        :param save_intent (optional) if the intent contract should be saved to the property manager
        :param intent_level: (optional) a level to place the intent
        :return:
        """
        # resolve intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   intent_level=intent_level, save_intent=save_intent)

        # intend code block on the canonical


class MasterLedger(AbstractComponent):

    @classmethod
    def from_uri(cls, task_name: str, uri_pm_path: str, pm_file_type: str=None, module_name: str=None,
                 pm_handler: str=None, default_save=None, **kwargs):
        _pm = MasterLedgerPropertyManager(task_name=task_name)
        _intent_model = MasterLedgerIntentModel(property_manager=_pm)
        super()._init_properties(property_manager=_pm, uri_pm_path=uri_pm_path, pm_module=module_name,
                                 pm_handler=pm_handler, pm_file_type=pm_file_type, **kwargs)
        return cls(property_manager=_pm, intent_model=_intent_model, default_save=True)

    @classmethod
    def from_env(cls, task_name: str=None, default_save=None, **kwargs):
        """

        :param task_name: (optional) a name option for the Master Ledger
        :param default_save: (optional) if the configuration should be persisted
        :return: the initialised class instance
        """
        task_name = task_name if isinstance(task_name, str) else 'master_ledger'
        return super().from_env(task_name=task_name, default_save=default_save)

