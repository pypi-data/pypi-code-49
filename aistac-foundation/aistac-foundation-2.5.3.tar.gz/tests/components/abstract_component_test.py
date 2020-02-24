import inspect
import unittest
import os
import shutil
from datetime import datetime
from pprint import pprint
import platform

import pandas as pd

from aistac.components.abstract_component import AbstractComponent
from aistac.handlers.abstract_handlers import ConnectorContract
from aistac.intent.python_cleaners_intent import PythonCleanersIntentModel
from aistac.properties.abstract_properties import AbstractPropertyManager
from aistac.properties.property_manager import PropertyManager


class ControlPropertyManager(AbstractPropertyManager):

    def __init__(self, task_name):
        # set additional keys
        root_keys = []
        knowledge_keys = []
        super().__init__(task_name=task_name, root_keys=root_keys, knowledge_keys=knowledge_keys)


class ControlComponent(AbstractComponent):

    @classmethod
    def from_uri(cls, task_name: str, uri_pm_path: str, pm_file_type: str = None, pm_module: str = None,
                 pm_handler: str = None, default_save=None, template_source_path: str = None,
                 template_persist_path: str = None, template_source_module: str = None,
                 template_persist_module: str = None, template_source_handler: str = None,
                 template_persist_handler: str = None, **kwargs):
        _pm = ControlPropertyManager(task_name=task_name)
        _intent_model = PythonCleanersIntentModel(property_manager=_pm)
        super()._init_properties(property_manager=_pm, uri_pm_path=uri_pm_path, **kwargs)
        super()._add_templates(property_manager=_pm, is_source=True, path=template_source_path,
                               module=template_source_module, handler=template_source_handler)
        super()._add_templates(property_manager=_pm,is_source=False, path=template_persist_path,
                               module=template_persist_module, handler=template_persist_handler)
        return cls(property_manager=_pm, intent_model=_intent_model, default_save=default_save)


class AbstractComponentTest(unittest.TestCase):

    def setUp(self):
        os.environ['AISTAC_PM_PATH'] = os.path.join(os.environ['PWD'], 'work')
        os.environ['AISTAC_PM_TYPE'] = 'yaml'
        self.pm_uri = os.environ.get('AISTAC_PM_PATH')
        PropertyManager._remove_all()

    def tearDown(self):
        try:
            shutil.rmtree(os.path.join(os.environ['PWD'], 'work'))
        except:
            pass

    def test_runs(self):
        """Basic smoke test"""
        ControlComponent.from_env('test')

    def test_intent_report(self):
        instance = ControlComponent.from_env('test')
        data = {'A': [1,2,3,4,5], 'B': [4,2,6,1,3]}
        data = instance.intent_model.auto_clean_header(data, case='upper')
        data = instance.intent_model.auto_remove_columns(data, predominant_max=0.98)
        result = instance.pm.report_intent()
        control = {'level': ['0', '0'], 'intent': ['auto_clean_header', 'auto_remove_columns'],
                   'parameters': [['case=upper'], ['predominant_max=0.98']]}
        self.assertDictEqual(control, result)

    def test_report_connectors(self):
        pm = ControlPropertyManager('task')
        im = PythonCleanersIntentModel(pm)
        instance = ControlComponent(pm, im)
        report = instance.pm.report_connectors()
        for value in report.values():
            self.assertCountEqual(value, [])
        instance = ControlComponent.from_env('task')
        report = instance.pm.report_connectors()
        self.assertEqual(pm.CONNECTOR_PM_CONTRACT, report['connector_name'][0])
        self.assertEqual(instance.DEFAULT_MODULE, report['module_name'][0])
        self.assertEqual(instance.DEFAULT_PERSIST_HANDLER, report['handler'][0])
        persist = ConnectorContract(instance.pm.file_pattern('persist'), instance.DEFAULT_MODULE, instance.DEFAULT_PERSIST_HANDLER)
        instance.add_connector_contract('persist', persist)
        report = instance.pm.report_connectors()
        self.assertIn('persist', report['connector_name'])

    def test_from_environ(self):
        os.environ['TASK'] = 'task'
        os.environ['MODULE'] = 'aistac.handlers.python_handlers'
        os.environ['HANDLER'] = 'PythonPersistHandler'
        instance = ControlComponent.from_environ('task', uri_pm_path="${AISTAC_PM_PATH}/contracts/${TASK}", pm_module="${MODULE}", pm_handler="${HANDLER}")
        uri = instance.pm.report_connectors().get('uri')
        module_name = instance.pm.report_connectors().get('module_name')
        handler = instance.pm.report_connectors().get('handler')
        control = [os.path.join(os.environ['AISTAC_PM_PATH'], "contracts/task/aistac_pm_control_task.pickle"), "/tmp/aistac/data", "/tmp/aistac/data"]
        self.assertCountEqual(control, uri)
        self.assertCountEqual([instance.DEFAULT_MODULE]*3, module_name)
        self.assertCountEqual([instance.DEFAULT_PERSIST_HANDLER]*2 + [instance.DEFAULT_SOURCE_HANDLER], handler)
        os.environ.pop('TASK')
        os.environ.pop('MODULE')
        os.environ.pop('HANDLER')

    def test_connector_file_pattern(self):
        manager = ControlComponent.from_env('task')
        state_connector = ConnectorContract(
            uri=manager.pm.file_pattern(prefix=f"{os.environ['AISTAC_PM_PATH']}/data/", connector_name='version', versioned=True),
            module_name=manager.DEFAULT_MODULE,
            handler=manager.DEFAULT_PERSIST_HANDLER,
            version="v1.01")
        temporal_connector = ConnectorContract(
            uri=manager.pm.file_pattern(prefix=f"{os.environ['AISTAC_PM_PATH']}/data/", connector_name='temporal', stamped='DAYS'),
            module_name=manager.DEFAULT_MODULE,
            handler=manager.DEFAULT_PERSIST_HANDLER)
        manager.add_connector_contract(connector_name='persist_book_state', connector_contract=state_connector)
        manager.add_connector_contract(connector_name='temporal_state', connector_contract=temporal_connector)
        manager.persist_canonical(connector_name='persist_book_state', canonical=pd.DataFrame({'A': [1,2,3,4]}))
        self.assertTrue(os.path.exists(f"{os.environ['AISTAC_PM_PATH']}/data/aistac_control_task_version_v1.01.pickle"))
        manager.persist_canonical(connector_name='temporal_state', canonical=pd.DataFrame({'A': [1,2,3,4]}))
        dt = datetime.now().strftime("%Y%m%d")
        self.assertTrue(os.path.exists(f"{os.environ['AISTAC_PM_PATH']}/data/aistac_control_task_temporal_{dt}.pickle"))

    def test_set_connector_uri(self):
        manager = ControlComponent.from_env('task')
        cc = ConnectorContract(uri="/usr/jdoe/code/local_file.pickle", module_name=manager.DEFAULT_MODULE,handler=manager.DEFAULT_PERSIST_HANDLER)
        manager.add_connector_contract(connector_name='connector', connector_contract=cc)
        self.assertEqual("/usr/jdoe/code/local_file.pickle", manager.pm.get_connector_contract(connector_name='connector').uri)
        manager.modify_connector_uri(connector_names='connector', old_pattern='/usr/jdoe/code', new_pattern="s3://bucket/path")
        self.assertEqual("s3://bucket/path/local_file.pickle", manager.pm.get_connector_contract(connector_name='connector').uri)

    def test_set_connector_version(self):
        manager = ControlComponent.from_env('task')
        cc = ConnectorContract(uri="local_file.pickle", module_name=manager.DEFAULT_MODULE,handler=manager.DEFAULT_PERSIST_HANDLER, version="v1.01")
        manager.add_connector_contract(connector_name='connector', connector_contract=cc)
        self.assertEqual("v1.01", manager.pm.get_connector_contract(connector_name='connector').version)
        manager.set_connector_version(connector_names='connector', version="v2.11")
        self.assertEqual("v2.11", manager.pm.get_connector_contract(connector_name='connector').version)

    def test_report_eviron(self):
        result = ControlComponent.from_env('test', default_save=False).report_environ()
        environ = ['AISTAC_PM_PATH', 'AISTAC_PM_TYPE', 'AISTAC_PM_MODULE', 'AISTAC_PM_HANDLER', 'AISTAC_DEFAULT_PATH',
                   'AISTAC_DEFAULT_SOURCE_PATH', 'AISTAC_DEFAULT_PERSIST_PATH','AISTAC_DEFAULT_MODULE',
                   'AISTAC_DEFAULT_SOURCE_MODULE','AISTAC_DEFAULT_PERSIST_MODULE','AISTAC_DEFAULT_SOURCE_HANDLER',
                   'AISTAC_DEFAULT_PERSIST_HANDLER']
        self.assertEqual(environ, result.get('environ'))

    def test_default_connector(self):
        manager = ControlComponent.from_env('task')
        # source
        connector = manager.pm.get_connector_contract(manager.TEMPLATE_SOURCE)
        self.assertEqual('/tmp/aistac/data', connector.uri)
        self.assertEqual('aistac.handlers.python_handlers', connector.module_name)
        self.assertEqual('PythonSourceHandler', connector.handler)
        # persist
        manager = ControlComponent.from_env('task')
        connector = manager.pm.get_connector_contract(manager.TEMPLATE_PERSIST)
        self.assertEqual('/tmp/aistac/data', connector.uri)
        self.assertEqual('aistac.handlers.python_handlers', connector.module_name)
        self.assertEqual('PythonPersistHandler', connector.handler)
        # set source
        manager.add_connector_from_template(connector_name='source', uri_file='mysource.pickle', template_name=manager.TEMPLATE_SOURCE)
        connector = manager.pm.get_connector_contract('source')
        self.assertEqual('/tmp/aistac/data/mysource.pickle', connector.uri)
        self.assertEqual('aistac.handlers.python_handlers', connector.module_name)
        self.assertEqual('PythonSourceHandler', connector.handler)
        # set persist
        manager.add_connector_from_template(connector_name='persist', uri_file='mypersist.pickle', template_name=manager.TEMPLATE_PERSIST)
        connector = manager.pm.get_connector_contract('persist')
        self.assertEqual('/tmp/aistac/data/mypersist.pickle', connector.uri)
        self.assertEqual('aistac.handlers.python_handlers', connector.module_name)
        self.assertEqual('PythonPersistHandler', connector.handler)


if __name__ == '__main__':
    unittest.main()
