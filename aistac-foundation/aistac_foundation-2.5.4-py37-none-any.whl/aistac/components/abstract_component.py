import os
import re
import platform
from abc import ABC, abstractmethod
from typing import Any

from aistac.intent.abstract_intent import AbstractIntentModel
from aistac.properties.abstract_properties import AbstractPropertyManager
from aistac.handlers.abstract_handlers import ConnectorContract

__author__ = 'Darryl Oatridge'


class AbstractComponent(ABC):
    """ Abstract AI Single Task Application Component (AI-STAC) component class provides all the basic building blocks
    of a components build including property management, augmented knowledge notes and parameterised intent pipeline.

    For convenience there are two Factory Initialisation methods available `from_env(...)` and `from_uri(...)` the
    second being an abstract method. This factory method initialises the concrete PropertyManager and IntentModel
    classes and should use the parent `_init_properties(...)` methods to set the properties connector

    As an example concrete implementation of this method:
    literal blocks::
        def __init__(self, property_manager: ExamplePropertyManager, intent_model: ExampleIntentModel,
                     default_save=None):
            super().__init__(property_manager=property_manager, intent_model=intent_model, default_save=default_save,
                             default_module='aistac.handlers.python_handlers',
                             default_source_handler='PythonSourceHandler',
                             default_persist_handler='PythonPersistHandler')

        @classmethod
        def from_uri(cls, task_name: str, uri_pm_path: str, pm_file_type: str=None, pm_module: str=None,
                     pm_handler: str=None, default_save=None, template_source_path: str=None,
                     template_persist_path: str=None, template_source_module: str=None,
                     template_persist_module: str=None, template_source_handler: str=None,
                     template_persist_handler: str=None, **kwargs):
            _pm = ExamplePropertyManager(task_name=task_name)
            _intent_model = ExampleIntentModel(property_manager=_pm)
            super()._init_properties(property_manager=_pm, uri_pm_path=uri_pm_path, **kwargs)
            super()._add_templates(property_manager=_pm, is_source=True, path=template_source_path,
                                   module=template_source_module, handler=template_source_handler)
            super()._add_templates(property_manager=_pm,is_source=False, path=template_persist_path,
                                   module=template_persist_module, handler=template_persist_handler)
            return cls(property_manager=_pm, intent_model=_intent_model, default_save=default_save)

    it is also worth overloading the class retrieval methods 'intent_model' and 'pm' to return the appropriate sub class
    literal blocks::
        @property
        def pm(self) -> ExamplePropertyManager:
            return self._component_pm

        @property
        def intent_model(self) -> ExampleIntentModel:
            return self._intent_model

    To implement a new remote class Factory Method follow the method naming convention '_from_remote_<schema>()'
    where <schema> is the uri schema name. this method should be a @classmethod and return a tuple of
    module_name and handler.
    For example if we were using an AWS S3 where the schema is s3:// the Factory method be similar to:
    literal blocks::
        @classmethod
        def _from_remote_s3(cls) -> (str, str):
            _module_name = 'ds_discovery.handlers.aws_s3_handlers'
            _handler = 'AwsS3PersistHandler'
            return _module_name, _handler

    """

    # default module and handlers
    DEFAULT_MODULE: str
    DEFAULT_SOURCE_HANDLER: str
    DEFAULT_PERSIST_HANDLER: str
    # template connectors
    TEMPLATE_SOURCE = 'template_source'
    TEMPLATE_PERSIST = 'template_persist'
    # environment statics
    _ENV_PM_PATH = 'AISTAC_PM_PATH'
    _ENV_PM_TYPE = 'AISTAC_PM_TYPE'
    _ENV_PM_MODULE = 'AISTAC_PM_MODULE'
    _ENV_PM_HANDLER = 'AISTAC_PM_HANDLER'
    _ENV_DEFAULT_PATH_SOURCE = 'AISTAC_DEFAULT_SOURCE_PATH'
    _ENV_DEFAULT_PATH_PERSIST = 'AISTAC_DEFAULT_PERSIST_PATH'
    _ENV_DEFAULT_PATH = 'AISTAC_DEFAULT_PATH'
    _ENV_DEFAULT_MODULE_SOURCE = 'AISTAC_DEFAULT_SOURCE_MODULE'
    _ENV_DEFAULT_MODULE_PERSIST = 'AISTAC_DEFAULT_PERSIST_MODULE'
    _ENV_DEFAULT_MODULE = 'AISTAC_DEFAULT_MODULE'
    _ENV_DEFAULT_HANDLER_SOURCE = 'AISTAC_DEFAULT_SOURCE_HANDLER'
    _ENV_DEFAULT_HANDLER_PERSIST = 'AISTAC_DEFAULT_PERSIST_HANDLER'

    def __init__(self, property_manager: AbstractPropertyManager, intent_model: AbstractIntentModel, default_save=None,
                 default_module: str=None, default_source_handler: str=None, default_persist_handler: str=None):
        """ initialisation of the abstract components providing both the property manager and the components
        parameterizable intent model. The optional parameters allow default references to be overridden by a
        concrete implementations of the abstract.
        The default module and handlers replace the root default static values for DEFAULT_MODULE,
        DEFAULT_SOURCE_HANDLER, DEFAULT_PERSIST_HANDLER and provide implementation specific default references but are
        also used in methods where the module and handlers are optional parameters.
        The default save allows a component to be run in memory or persisted as a default behaviour.

        :param property_manager: The contract property manager instance for this components
        :param intent_model: the model codebase containing the parameterizable intent
        :param default_save: (optional) The default behaviour of persisting the contracts:
                    if True: all contract properties are persisted
                    if False: The connector contracts are kept in memory (useful for restricted file systems)
        :param default_module: (optional) a convenience static assigned to DEFAULT_MODULE
        :param default_source_handler: (optional) a convenience static assigned to DEFAULT_SOURCE_HANDLER
        :param default_persist_handler: (optional) a convenience static assigned to DEFAULT_PERSIST_HANDLER
        """
        if not isinstance(property_manager, AbstractPropertyManager):
            raise ValueError("The contract_pm must be a concrete implementation of the AbstractPropertyManager")
        if not isinstance(intent_model, AbstractIntentModel):
            raise ValueError("The intent_model must be a concrete implementation of the AbstractIntent")
        # set instance references
        self._component_pm = property_manager
        self._intent_model = intent_model
        # set templates
        self._default_save = default_save if isinstance(default_save, bool) else True
        _module = 'aistac.handlers.python_handlers'
        self.DEFAULT_MODULE = default_module if isinstance(default_module, str) else _module
        _source = 'PythonSourceHandler'
        self.DEFAULT_SOURCE_HANDLER = default_source_handler if isinstance(default_source_handler, str) else _source
        _persist = 'PythonPersistHandler'
        self.DEFAULT_PERSIST_HANDLER = default_persist_handler if isinstance(default_persist_handler, str) else _persist

    @classmethod
    @abstractmethod
    def from_uri(cls, task_name: str, uri_pm_path: str, pm_file_type: str=None, pm_module: str=None,
                 pm_handler: str=None, default_save=None, template_source_path: str=None,
                 template_persist_path: str=None, template_source_module: str=None, template_persist_module: str=None,
                 template_source_handler: str=None, template_persist_handler: str=None, **kwargs):
        """ Class Factory Method to instantiates the components application. The Factory Method handles the
        instantiation of the Properties Manager, the Intent Model and the persistence of the uploaded properties.
        See class inline docs for an example method

         :param task_name: The reference name that uniquely identifies a task or subset of the property manager
         :param uri_pm_path: A URI that identifies the resource path for the property manager.
         :param pm_file_type: (optional) defines a specific file type for the property manager
         :param pm_module: (optional) the module or package name where the handler can be found
         :param pm_handler: (optional) the handler for retrieving the resource
         :param default_save: (optional) if the configuration should be persisted. default to 'True'
         :param template_source_path: (optional) a default source root path for the source canonicals
         :param template_persist_path: (optional) a default source root path for the persisted canonicals
         :param template_source_module: (optional) a default module package path for the source handlers
         :param template_persist_module: (optional) a default module package path for the persist handlers
         :param template_source_handler: (optional) a default read only source handler
         :param template_persist_handler: (optional) a default read write persist handler
         :param kwargs: to pass to the ConnectorContract as its kwargs
         :return: the initialised class instance
         """

    @classmethod
    def _init_properties(cls, property_manager: AbstractPropertyManager, uri_pm_path: str, pm_file_type: str=None,
                         pm_module: str=None, pm_handler: str=None, **kwargs) -> (str, str):
        """ initialisation and set up of the property connector contract into the property manager instance

        :param property_manager: the instance of the property manager
        :param uri_pm_path: the URI path to where property contract are help.
        :param pm_file_type: (optional) defines a specific file type for the property manager
        :param pm_module: (optional) the module or package name where the handler can be found
        :param pm_handler: (optional) the handler for retrieving the resource
        :return: a tuple of the selected module_name, handler and file type
        """
        if not isinstance(uri_pm_path, str) or len(uri_pm_path) == 0:
            raise ValueError("The URI must be a valid string representation of a URI")
        _uri = uri_pm_path
        _schema, _, _path = ConnectorContract.parse_address_elements(uri=_uri)
        _file_type = pm_file_type if isinstance(pm_file_type, str) else 'pickle'
        if isinstance(pm_module, str) and isinstance(pm_handler, str):
            _module_name = pm_module
            _handler = pm_handler
        elif len(_schema) > 0 and not str(_schema).lower().startswith('file'):
            try:
                _module_name, _handler = exec(f"cls._from_remote_{_schema}()")
            except:
                raise NotImplementedError("The method '_from_remote_{}()' has not been implemented. "
                                          "See method docs for help".format(_schema))
            _address = ConnectorContract.parse_address(uri=uri_pm_path)
        else:
            _module_name = 'aistac.handlers.python_handlers'
            _handler = 'PythonPersistHandler'
        _data_uri = os.path.join(_path, "aistac_pm_{}_{}.{}".format(property_manager.manager_name(),
                                                                    property_manager.task_name, _file_type))
        _query_kw = ConnectorContract.parse_query(uri=uri_pm_path)
        kwargs = kwargs if isinstance(kwargs, dict) else {}
        kwargs.update(_query_kw)
        _connector = ConnectorContract(uri=_data_uri, module_name=_module_name, handler=_handler, **kwargs)
        property_manager.set_property_connector(connector_contract=_connector)
        if property_manager.get_connector_handler(property_manager.CONNECTOR_PM_CONTRACT).exists():
            property_manager.load_properties(replace=False)
        # set the default source and persist
        return _module_name, _handler, _file_type

    @classmethod
    def _add_templates(cls, property_manager: AbstractPropertyManager, source_path: str=None, persist_path: str=None,
                       module: str=None, source_handler: str=None, persist_handler: str=None, save=None):
        """ add a template Connector Contract to the properties

        :param property_manager: the property manager to save the template to
        :param is_source: if the connector contract is for a source or persist connector
        :param path: a path
        :param module: a module package
        :param handler: a connector handler
        """
        save = save if isinstance(save, bool) else True
        _root = os.environ['AppData'] if platform.system().lower().startswith("Windows") else '/tmp'
        _path = os.path.join(_root, 'aistac', 'data')
        source_path = source_path if isinstance(source_path, str) else _path
        persist_path = persist_path if isinstance(persist_path, str) else _path
        module = module if isinstance(module, str) else 'aistac.handlers.python_handlers'
        source_handler = source_handler if isinstance(source_handler, str) else 'PythonSourceHandler'
        persist_handler = persist_handler if isinstance(persist_handler, str) else 'PythonPersistHandler'
        connector_contract = ConnectorContract(uri=source_path, module_name=module, handler=source_handler)
        if property_manager.has_connector(connector_name=cls.TEMPLATE_SOURCE):
            property_manager.remove_connector_contract(connector_name=cls.TEMPLATE_SOURCE)
        property_manager.set_connector_contract(connector_name=cls.TEMPLATE_SOURCE,
                                                connector_contract=connector_contract)
        connector_contract = ConnectorContract(uri=persist_path, module_name=module, handler=persist_handler)
        if property_manager.has_connector(connector_name=cls.TEMPLATE_PERSIST):
            property_manager.remove_connector_contract(connector_name=cls.TEMPLATE_PERSIST)
        property_manager.set_connector_contract(connector_name=cls.TEMPLATE_PERSIST,
                                                connector_contract=connector_contract)
        if save:
            property_manager.persist_properties()
        return

    @classmethod
    def from_environ(cls, task_name: str, uri_pm_path: str, pm_file_type: str=None, pm_module: str=None,
                     pm_handler: str=None, default_save=None, template_source_path: str=None,
                     template_persist_path: str=None, template_source_module: str=None,
                     template_persist_module: str=None, template_source_handler: str=None,
                     template_persist_handler: str=None, **kwargs):
        """ a pre-process that substitutes a pattern in the URI, module_name and handler with an environment variable.
        the pattern should start with a dollar sign ($) with the environment variable name wrapped by two curly braces
        '${<environ>}'.
        for example '${MODULE_NAME}' would look for the environment variable 'os.environ['MODULE_NAME']'

        This method calls the Factory Method 'from_uri(...)' returning the initialised class instance

         :param task_name: The reference name that uniquely identifies a task or subset of the property manager
         :param uri_pm_path: A URI that identifies the resource path for the property manager.
         :param pm_file_type: (optional) defines a specific file type for the property manager
         :param pm_module: (optional) the module or package name where the handler for the properties can be found
         :param pm_handler: (optional) the handler for retrieving the properties
         :param default_save: (optional) if the configuration should be persisted. default to 'True'
         :param template_source_path: (optional) a default source root path for the source canonicals
         :param template_persist_path: (optional) a default source root path for the persisted canonicals
         :param template_source_module: (optional) a default module package path for the source handlers
         :param template_persist_module: (optional) a default module package path for the persist handlers
         :param template_source_handler: (optional) a default read only source handler
         :param template_persist_handler: (optional) a default read write persist handler
         :param kwargs: to pass to the ConnectorContract as its kwargs
         :return: the initialised class instance
        """
        pattern = r'\${([A-Za-z_0-9\-]+)}'
        # test they are all environment variables
        for label in re.findall(pattern, " ".join([uri_pm_path, str(pm_module), str(pm_handler),
                                                   str(template_source_path), str(template_persist_path),
                                                   str(template_source_module), str(template_persist_module),
                                                   str(template_source_handler), str(template_source_handler)])):
            if label not in os.environ.keys():
                raise EnvironmentError(f"The environment variable '{label}' has not been set")
        uri_pm_path = re.sub(pattern, lambda m: os.getenv(m.group(1)), uri_pm_path)
        if isinstance(pm_module, str):
            pm_module = re.sub(pattern, lambda m: os.getenv(m.group(1)), pm_module)
        if isinstance(pm_handler, str):
            pm_handler = re.sub(pattern, lambda m: os.getenv(m.group(1)), pm_handler)
        if isinstance(template_source_path, str):
            template_source_path = re.sub(pattern, lambda m: os.getenv(m.group(1)), template_source_path)
        if isinstance(template_persist_path, str):
            template_persist_path = re.sub(pattern, lambda m: os.getenv(m.group(1)), template_persist_path)
        if isinstance(template_source_module, str):
            template_source_module = re.sub(pattern, lambda m: os.getenv(m.group(1)), template_source_module)
        if isinstance(template_persist_module, str):
            template_persist_module = re.sub(pattern, lambda m: os.getenv(m.group(1)), template_persist_module)
        if isinstance(template_source_handler, str):
            template_source_handler = re.sub(pattern, lambda m: os.getenv(m.group(1)), template_source_handler)
        if isinstance(template_persist_handler, str):
            template_persist_handler = re.sub(pattern, lambda m: os.getenv(m.group(1)), template_persist_handler)
        return cls.from_uri(task_name=task_name, uri_pm_path=uri_pm_path, pm_file_type=pm_file_type,
                            pm_module=pm_module, pm_handler=pm_handler, default_save=default_save,
                            template_source_path=template_source_path, template_persist_path=template_persist_path,
                            template_source_module=template_source_module,
                            template_persist_module=template_persist_module,
                            template_source_handler=template_source_handler,
                            template_persist_handler=template_persist_handler, **kwargs)

    @classmethod
    def from_env(cls, task_name: str, default_save=None, **kwargs):
        """ Class Factory Method that builds the connector handlers taking the property contract path from
        the os.environ['AISTAC_PM_PATH'] or, if not found, uses the system default,
                    for Linux and IOS '/tmp/components/contracts
                    for Windows 'os.environ['AppData']\\components\\contracts'
        and pm file type from os.environ['AISTAC_PM_TYPE'] or sets as 'pickle' if not found
        This method calls to the Factory Method 'from_environ(...)' returning the initialised class instance

         :param task_name: The reference name that uniquely identifies a task or subset of the property manager
         :param default_save: (optional) if the configuration should be persisted
         :return: the initialised class instance
         """
        pm_file_type = os.environ.get(cls._ENV_PM_TYPE, 'pickle')
        pm_uri = os.environ.get(cls._ENV_PM_PATH, None)
        if pm_uri is None:
            if platform.system().lower().startswith("Windows"):
                pm_uri = os.path.join(os.environ['AppData'], 'components', 'contracts')
            else:
                pm_uri = os.path.join('/tmp', 'components', 'contracts')

        module_name = os.environ.get(cls._ENV_PM_MODULE, None)
        handler = os.environ.get(cls._ENV_PM_HANDLER, None)
        template_source_path = os.environ.get(cls._ENV_DEFAULT_PATH_SOURCE, os.environ.get(cls._ENV_DEFAULT_PATH, None))
        template_persist_path = os.environ.get(cls._ENV_DEFAULT_PATH_PERSIST, os.environ.get(cls._ENV_DEFAULT_PATH, None))
        template_source_module = os.environ.get(cls._ENV_DEFAULT_MODULE_SOURCE,
                                                os.environ.get(cls._ENV_DEFAULT_MODULE, None))
        template_persist_module = os.environ.get(cls._ENV_DEFAULT_MODULE_PERSIST,
                                                 os.environ.get(cls._ENV_DEFAULT_MODULE, None))
        template_source_handler = os.environ.get(cls._ENV_DEFAULT_HANDLER_SOURCE, None)
        template_persist_handler = os.environ.get(cls._ENV_DEFAULT_HANDLER_PERSIST, None)
        return cls.from_environ(task_name=task_name, uri_pm_path=pm_uri, pm_file_type=pm_file_type,
                                pm_module=module_name, pm_handler=handler, default_save=default_save,
                                template_source_path=template_source_path, template_persist_path=template_persist_path,
                                template_source_module=template_source_module,
                                template_persist_module=template_persist_module,
                                template_source_handler=template_source_handler,
                                template_persist_handler=template_persist_handler, **kwargs)

    """
        PROPERTY MANAGER SECTION
    """
    @staticmethod
    def report_environ():
        """returns a report on the foundation environment variables"""
        ac = AbstractComponent
        report = {'environ': [], 'value': []}
        for environ in [ac._ENV_PM_PATH, ac._ENV_PM_TYPE, ac._ENV_PM_MODULE, ac._ENV_PM_HANDLER,
                        ac._ENV_DEFAULT_PATH, ac._ENV_DEFAULT_PATH_SOURCE, ac._ENV_DEFAULT_PATH_PERSIST,
                        ac._ENV_DEFAULT_MODULE, ac._ENV_DEFAULT_MODULE_SOURCE, ac._ENV_DEFAULT_MODULE_PERSIST,
                        ac._ENV_DEFAULT_HANDLER_SOURCE, ac._ENV_DEFAULT_HANDLER_PERSIST,
                        ]:
            report['environ'].append(environ)
            report['value'].append(os.environ.get(environ, 'Not Set'))
        return report

    @property
    def intent_model(self):
        """The intent model instance"""
        return self._intent_model

    @property
    def pm(self):
        """The properties manager instance"""
        return self._component_pm

    def pm_persist(self, save=None):
        """Saves the current configuration to file"""
        if not isinstance(save, bool):
            save = self._default_save
        if save:
            self.pm.persist_properties()
        return

    @property
    def pm_name(self) -> str:
        """The contract name of this transition instance"""
        return self._component_pm.contract_name

    def pm_reset(self, save: bool=None):
        """ resets the contract back to a default. This does not remove the Property Manager Connector Contract or
        any snapshots

        :param save: override of the default save action set at initialisation.
        """
        if not isinstance(save, bool):
            save = self._default_save
        self.pm.reset_all()
        self.pm_persist(save)
        return

    """
        CONNECTOR CONTRACTS SECTION
    """
    def add_connector_contract(self, connector_name: str, connector_contract: ConnectorContract, save: bool=None):
        """ Sets a named connector contract

        :param connector_name: the name or label to identify and reference the connector
        :param connector_contract: a Connector Contract for the properties persistence
        :param save: override of the default save action set at initialisation.
        :return: if load is True, returns a Pandas.DataFrame else None
        """
        save = save if isinstance(save, bool) else self._default_save
        if self.pm.has_connector(connector_name):
            self.pm.remove_connector_contract(connector_name)
        self.pm.set_connector_contract(connector_name=connector_name, connector_contract=connector_contract)
        self.pm_persist(save)
        return

    def add_connector_from_template(self, connector_name: str, uri_file: str, template_name: str,  save: bool=None,
                                    **kwargs):
        """ Adds a connector using settings from a template connector. By default a self.TEMPLATE_SOURCE and
        self.TEMPLATE_PERSIST are added at initialisation

        :param connector_name: the name or label to identify and reference the connector
        :param uri_file: the name of the file to append to the end of the default path
        :param template_name: the name of the template connector
        :param save: override of the default save action set at initialisation.
        :param kwargs: any kwargs to add to the default connector
        :return:
        """
        if not self.pm.has_connector(connector_name=template_name):
            raise ValueError(f"The template connector '{template_name}' could not be found")
        template = self.pm.get_connector_contract(connector_name=template_name)
        uri = os.path.join(template.path, uri_file)
        if not isinstance(kwargs, dict):
            kwargs = {}
        template.kwargs.update(kwargs)
        cc = ConnectorContract(uri=uri, module_name=template.module_name, handler=template.handler, **kwargs)
        self.add_connector_contract(connector_name=connector_name, connector_contract=cc, save=save)
        return

    def remove_connector_contract(self, connector_name: str, save: bool=None):
        """removes a named connector contract

        :param connector_name: the name or label to identify and reference the connector
        :param save: override of the default save action set at initialisation.
        """
        if not isinstance(save, bool):
            save = self._default_save
        self.pm.remove_connector_contract(connector_name)
        self.pm_persist(save)
        return

    def modify_connector_uri(self, connector_names: [str, list], old_pattern: str, new_pattern: str, save: bool=None):
        """ modifies the uri of a connector contract and resets

        :param connector_names: a name or list of names of connector contract to modify
        :param old_pattern: the old pattern to find
        :param new_pattern: the new pattern to replace the old pattern
        :param save: override of the default save action set at initialisation.
        """
        if not isinstance(save, bool):
            save = self._default_save
        for name in self.pm.list_formatter(connector_names):
            self.pm.modify_connector_uri(connector_name=name, old_pattern=old_pattern, new_pattern=new_pattern)
        self.pm_persist(save)
        return

    def set_connector_version(self, connector_names: [str, list], version: str, save: bool=None):
        """ modifies the uri of a connector contract and resets

        :param connector_names: a name or list of names of connector contract to modify
        :param version: the new version number
        :param save: override of the default save action set at initialisation.
        """
        if not isinstance(save, bool):
            save = self._default_save
        for name in self.pm.list_formatter(connector_names):
            self.pm.set_connector_version(connector_name=name, version=version)
        self.pm_persist(save)
        return

    """
        INTENT SECTION
    """
    def add_run_book(self, book_name: str, run_levels: [str, list], save: bool=None):
        """ sets a named run book, the run levels are a list of levels and the order they are run in

        :param book_name: the name of the run_book
        :param run_levels: the name or list of levels to be run
        :param save: (optional) override of the default save action set at initialisation.
       """
        save = save if isinstance(save, bool) else self._default_save
        self.pm.set_run_book(book_name=book_name, run_levels=run_levels)
        self.pm_persist(save)

    def remove_intent(self, intent_param: [str, dict]=None, level: [int, str]=None, save: bool=None):
        """ removes part or all the intent contract.
                if only intent then all references in all levels of that named intent will be removed
                if only level then that level is removed
                if both level and intent then that specific intent on that level is removed

        :param intent_param: (optional) removes the method contract
        :param level: (optional) removes the level contract
        :param save: (optional) override of the default save action set at initialisation.
        :return True if removed, False if not
        """
        save = save if isinstance(save, bool) else self._default_save
        result = self.pm.remove_intent(intent_param=intent_param, level=level)
        self.pm_persist(save)
        return result

    """
        CANONICAL SECTION
    """
    def load_canonical(self, connector_name: str, **kwargs) -> Any:
        """returns the canonical of the referenced connector

        :param connector_name: the name or label to identify and reference the connector
        :param kwargs: arguments to be passed to the handler on load
        """
        if self.pm.has_connector(connector_name):
            handler = self.pm.get_connector_handler(connector_name)
            canonical = handler.load_canonical(**kwargs)
            self.pm.set_modified(connector_name, handler.get_modified())
            return canonical
        raise ConnectionError("The connector name {} can't be found.".format(connector_name))

    def persist_canonical(self, connector_name: str, canonical: Any, **kwargs):
        """persists the canonical to the referenced connector

        :param connector_name: the name or label to identify and reference the connector
        :param canonical: the canonical data to persist
        :param kwargs: arguments to be passed to the handler on persist
        """
        if self.pm.has_connector(connector_name):
            handler = self.pm.get_connector_handler(connector_name)
            handler.persist_canonical(canonical, **kwargs)
            return
        raise ConnectionError("The connector name {} can't be found.".format(connector_name))

    def backup_canonical(self, connector_name: str, canonical: Any, uri: str, **kwargs):
        """persists the canonical to the referenced connector as a backup using the URI to
        replace the current Connecto Contract URI.

        :param connector_name: the name or label to identify and reference the connector
        :param canonical: the canonical data to persist
        :param uri: an alternative uri to the one in the ConnectorContract
        :param kwargs: arguments to be passed to the handler on persist
        """
        if self.pm.has_connector(connector_name):
            _handler = self.pm.get_connector_handler(connector_name)
            _cc = self.pm.get_connector_contract(connector_name)
            _address = _cc.parse_address(uri=_cc.uri)
            _path, _, _ext = _address.rpartition('.')
            _handler.backup_canonical(canonical=canonical, uri=uri, **kwargs)
            return
        raise ConnectionError("The connector name {} was not found.".format(connector_name))

    def remove_canonical(self, connector_name: str, **kwargs):
        """removes the current persisted canonical.

        :param connector_name: the name or label to identify and reference the connector
        :param kwargs: arguments to be passed to the handler on remove
        """
        if self.pm.has_connector(connector_name):
            handler = self.pm.get_connector_handler(connector_name)
            handler.remove_canonical()
            return
        raise ConnectionError("The connector name {} was not found.".format(connector_name))

    """
        SNAPSHOT SECTION, DESCRIPTION AND VERSIONS
    """
    def set_version(self, version, save=None):
        """ sets the version
        :param version: the version to be set
        :param save: override of the default save action set at initialisation.
        """
        if not isinstance(save, bool):
            save = self._default_save
        self.pm.set_version(version=version)
        self.pm_persist(save)
        return

    def set_description(self, description, save=None):
        """ sets the description of this component task
        :param description: a brief description of this component task
        :param save: override of the default save action set at initialisation.
        """
        if not isinstance(save, bool):
            save = self._default_save
        self.pm.set_description(description=description)
        self.pm_persist(save)
        return

    def create_snapshot(self, suffix: str=None, version: str=None, save: bool=None):
        """ creates a snapshot of contracts configuration. The name format will be <contract_name>_#<suffix>.

        :param suffix: (optional) adds the suffix to the end of the contract name. if None then date & time used
        :param version: (optional) changes the version number of the current contract
        :param save: override of the default save action set at initialisation.
        :return: a list of current contract snapshots
        """
        if not isinstance(save, bool):
            save = self._default_save
        result = self.pm.set_snapshot(suffix)
        if version is not None:
            self.set_version(version=version)
        self.pm_persist(save)
        return result

    def recover_snapshot(self, snapshot_name: str, overwrite: bool=None, save: bool=None) -> bool:
        """ recovers a snapshot back to the current. The snapshot must be from this root contract.
        by default the original root contract will be overwitten unless the overwrite is set to False.
        if overwrite is False a timestamped snapshot is created

        :param snapshot_name:the name of the snapshot (use self.contract_snapshots to get list of names)
        :param overwrite: (optional) if the original contract should be overwritten. Default to True
        :param save: override of the default save action set at initialisation.
        :return: True if the contract was recovered, else False
        """
        if not isinstance(save, bool):
            save = self._default_save
        result = self.pm.recover_snapshot(snapshot_name=snapshot_name, overwrite=overwrite)
        self.pm_persist(save)
        return result

    def delete_snapshot(self, snapshot_name: str, save: bool=None):
        """ deletes a snapshot

        :param snapshot_name: the name of the snapshot
        :param save: override of the default save action set at initialisation.
        :return: True if successful, False is not found or not deleted
        """
        if not isinstance(save, bool):
            save = self._default_save
        self.pm.remove_snapshot(snapshot_name=snapshot_name)
        self.pm_persist(save)
        return

    """
        NOTES SECTION
    """
    @property
    def notes_catalog(self) -> list:
        """returns the list of allowed catalog names"""
        return self.pm.knowledge_catalog

    def add_notes(self, catalog: str, label: [str, list], text: str, constraints: list=None,
                  save=None):
        """ add's a note to the augmented knowledge.
                if no label is given then a journal date of 'year-month' is provided
                if no catalog is given then the default catalogue name is given

        :param catalog: a catalog name
        :param label: a sub key label or list of labels to separate different information strands
        :param text: the text to add
        :param constraints: (optional) a list of allowed label values, if None then any value allowed
        :param save: if True, save to file. Default is True
        """
        if not isinstance(save, bool):
            save = self._default_save
        self.pm.set_knowledge(catalog=catalog, label=label, text=text, constraints=constraints)
        self.pm_persist(save)

    def remove_notes(self, catalog: str, label: str=None, save=None):
        """ removes a all entries for a labeled note

        :param catalog: the type of note to delete, if left empyt all notes removed
        :param label: (Optional) the name of the label to be removed
        :param save: (Optional) if True, save to file. Default is True
        :return: True is successful, False if not
        """
        if not isinstance(save, bool):
            save = self._default_save
        self.pm.remove_knowledge(catalog=catalog, label=label)
        self.pm_persist(save)

    def upload_notes(self, data: Any, catalog: str, constraints: list=None, save=None):
        """ Allows bulk upload of notes. Assumes a dictionary of key value pairs where the key is the
        label and the value the text

        :param data: a dictionary of where the key is the label and value is the text
        :param catalog: (optional) the section these notes should be put in
        :param constraints: (optional) the limited list of acceptable labels. If not in list then ignored
        :param save: if True, save to file. Default is True
        """
        self.pm.bulk_upload_knowledge(data, catalog=catalog, constraints=constraints)
        self.pm_persist(save)
