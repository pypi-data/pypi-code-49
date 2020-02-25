import os
import shutil
import unittest
from pprint import pprint

from aistac.handlers.abstract_handlers import ConnectorContract

from aistac.properties.abstract_properties import AbstractPropertyManager, AbstractProperty
from aistac.properties.property_manager import PropertyManager


class ControlPropertyManager(AbstractPropertyManager):

    def __init__(self, task_name: str, root_keys: list=None, knowledge_keys: list=None):
        root_keys = root_keys if isinstance(root_keys, list) else []
        knowledge_keys = knowledge_keys if isinstance(knowledge_keys, list) else []
        root_keys += ['cleaners']
        super().__init__(task_name, root_keys, knowledge_keys)

    @classmethod
    def manager_name(cls) -> str:
        return str(cls.__name__).lower().replace('propertymanager', '')


class AbstractPropertiesManagerTest(unittest.TestCase):
    """Test: """

    def setUp(self):
        self.connector = ConnectorContract(uri='properties/config_contract.pkl?sep=.&encoding=Latin1',
                                         module_name='aistac.handlers.python_handlers',
                                         handler='PythonPersistHandler', name='darryl', password='mypass')
        try:
            os.makedirs('properties')
        except:
            pass
        PropertyManager._remove_all()

    def tearDown(self):
        try:
            shutil.rmtree('properties')
        except:
            pass

    def test_runs(self):
        """Basic smoke test"""
        ControlPropertyManager('test_abstract_properties')

    def test_manager_name(self):
        manager = ControlPropertyManager('test_abstract_properties')
        self.assertEqual('control', manager.manager_name())

    def test_keys(self):
        augmented_keys = ['observations', 'notes']
        manager = ControlPropertyManager('test_abstract_properties', knowledge_keys=augmented_keys)
        result = manager.KEY.keys()
        self.assertIn('knowledge.observations_key', result)
        self.assertIn('knowledge.notes_key', result)
        self.assertIn("knowledge.schema_key", result)
        self.assertIn('cleaners_key', result)
        self.assertIn('version_key', result)
        control = 'control.test_abstract_properties.version'
        result = manager.KEY.version_key
        self.assertEqual(control, result)
        control = 'control.test_abstract_properties.knowledge.notes'
        result = manager.KEY.knowledge.notes_key
        self.assertEqual(control, result)

    def test_persist(self):
        pm = ControlPropertyManager('test_abstract_properties')
        pm.set(pm.join(pm.KEY.contract_key, 'test_key'), 'test value')
        result = pm.get(pm.join(pm.KEY.contract_key, 'test_key'))
        self.assertEqual('test value', result)
        # create the connection
        pm.set_property_connector(self.connector)
        self.assertFalse(os.path.exists('properties/config_contract.p'))
        pm.set_version('test_version')
        pm.persist_properties()
        self.assertTrue(os.path.exists('properties/config_contract.pkl'))
        self.assertEqual(['pm_control_test_abstract_properties'], pm.connector_contract_list)
        self.assertEqual('test_version', pm.version)
        pm.reset_all()
        self.assertEqual('v0.00', pm.version)
        self.assertEqual(['pm_control_test_abstract_properties'], pm.connector_contract_list)

    def test_abstract_key(self):
        keys = ['connectors', 'values']
        ab = AbstractProperty(keys, manager='contract', contract='subset')
        self.assertEqual('contract.subset', ab.contract_key)
        self.assertEqual('contract.subset.connectors', ab.connectors_key)

        ab = AbstractProperty(keys, manager='contract')
        self.assertEqual('contract', ab.manager_key)
        self.assertEqual('contract.connectors', ab.connectors_key)

        ab = AbstractProperty(keys)
        self.assertEqual('connectors', ab.connectors_key)
        self.assertEqual('values', ab.values_key)

    def test_abstract_key_complex(self):
        keys = [{'connectors': ['one', 'two']}]
        ab = AbstractProperty(keys, manager='contract', contract='subset')
        self.assertEqual('contract.subset', ab.contract_key)
        self.assertEqual('contract.subset.connectors', ab.connectors_key)
        self.assertEqual('contract.subset.connectors.one', ab.connectors.one_key)

    def test_reset_abstract_properties(self):
        keys = ['connectors', 'intent', 'overview']
        pm = ControlPropertyManager(task_name='contract', root_keys=keys, knowledge_keys=[])
        pm.set(pm.KEY.intent_key, 'some value')
        pm.set_version('v1')
        control = {'description': "", 'cleaners': {}, 'connectors': {}, 'intent': 'some value', 'overview': {}, 'run_book': {},'snapshot': {}, 'version': 'v1',
                   'knowledge': {'schema': {}}}
        self.assertEqual(control, pm.get(pm.KEY.contract_key))
        pm.reset_all()
        control = {'description': "", 'cleaners': {}, 'connectors': {}, 'intent': {}, 'overview': {}, 'run_book': {},'snapshot': {}, 'version': 'v0.00',
                   'knowledge': {'schema': {}}}
        self.assertEqual(control, pm.get(pm.KEY.contract_key))

    def test_connection_handler(self):
        pm = ControlPropertyManager('test_abstract_properties', root_keys=[], knowledge_keys=[])
        control_connector = self.connector
        pm.set_connector_contract(connector_name='control', connector_contract=self.connector)
        result = pm.get_connector_contract(connector_name='control')
        self.assertEqual(control_connector, result)
        # connections should be empty as not requested a handler
        self.assertEqual([], pm.connector_handler_list)
        self.assertEqual(['control'], pm.connector_contract_list)
        pm.get_connector_handler(connector_name='control')
        self.assertEqual(['control'], pm.connector_handler_list)
        pm.remove_connector_contract(connector_name='control')
        control = {'description': '', 'cleaners': {}, 'connectors': {},  'intent': {}, 'run_book': {}, 'snapshot': {}, 'version': 'v0.00',
                   'knowledge': {'schema': {}}}
        self.assertEqual(control, pm.get(pm.KEY.contract_key))

    def test_set_property(self):
        pm = ControlPropertyManager('test_abstract_properties')
        pm.set_property_connector(self.connector)
        control = {'handler': 'PythonPersistHandler',
                                 'kwargs': {'name': 'darryl',
                                            'password': 'mypass'},
                                 'module_name': 'aistac.handlers.python_handlers',
                                 'uri_raw': 'properties/config_contract.pkl?sep=.&encoding=Latin1',
                                 'version': 'v00',
                                 'uri_parsed': {'address': 'properties/config_contract.pkl',
                                                'fragment': '',
                                                'netloc': '',
                                                'params': [],
                                                'path': 'properties/config_contract.pkl',
                                                'query': {'encoding': 'Latin1', 'sep': '.'},
                                                'schema': ''}}
        self.assertDictEqual(control, pm.get_connector_contract(pm.CONNECTOR_PM_CONTRACT).to_dict())

    def test_reset(self):
        pm = ControlPropertyManager('test_abstract_properties')
        pm.reset_all()
        pm.set_property_connector(self.connector)
        control = pm.get(pm.KEY.connectors_key)
        pm.set_version('latest')
        version = pm.version
        self.assertEqual('latest', pm.version)
        pm.reset_all()
        result = pm.get(pm.KEY.connectors_key)
        self.assertEqual(control, result)
        self.assertNotEqual(version, pm.version)
        self.assertEqual('v0.00', pm.version)
        # add new properties and check the connector is not removed
        pm.set(pm.KEY.cleaners_key, {'clean_header': {'case': 'title', 'rename': {'surname: last_name'}}})
        pm.set(pm.KEY.version_key, 'v1.00')
        self.assertEqual(['pm_control_test_abstract_properties'], list(pm.get(pm.KEY.connectors_key).keys()))
        self.assertEqual(['clean_header'], list(pm.get(pm.KEY.cleaners_key).keys()))
        self.assertEqual('v1.00', pm.get(pm.KEY.version_key))
        pm.reset_all()
        self.assertEqual(['pm_control_test_abstract_properties'], list(pm.get(pm.KEY.connectors_key).keys()))
        self.assertEqual({}, pm.get(pm.KEY.cleaners_key))
        self.assertEqual('v0.00', pm.get(pm.KEY.version_key))

    def test_multi_instance(self):
        dpm = ControlPropertyManager('test_abstract_properties')
        self.assertEqual('v0.00', dpm.get(dpm.KEY.version_key))
        self.assertEqual([], list(dpm.get(dpm.KEY.cleaners_key).keys()))
        dpm.set_connector_contract('raw_source', connector_contract=self.connector)
        dpm.set(dpm.KEY.cleaners_key, {'clean_header': {'case': 'title', 'rename': {'surname: last_name'}}})
        dpm.set(dpm.KEY.version_key, '5.01')
        self.assertEqual('5.01', dpm.get(dpm.KEY.version_key))
        self.assertEqual(['clean_header'], list(dpm.get(dpm.KEY.cleaners_key).keys()))
        #now load a new instance
        dpm2 = ControlPropertyManager('test_abstract_properties')
        self.assertEqual('5.01', dpm2.get(dpm.KEY.version_key))
        self.assertEqual(['clean_header'], list(dpm.get(dpm.KEY.cleaners_key).keys()))

    def test_connector_handler(self):
        connector_name = 'raw_source'
        dpm = ControlPropertyManager('test_abstract_properties')
        dpm.set_connector_contract(connector_name=connector_name, connector_contract=self.connector)
        handler = dpm.get_connector_handler(connector_name)
        self.assertEqual("<class 'aistac.handlers.python_handlers.PythonPersistHandler'>", str(type(handler)))

    def test_set_connector_contract(self):
        connector_name = 'raw_source'
        dpm = ControlPropertyManager('test_abstract_properties')
        dpm.set_connector_contract(connector_name=connector_name, connector_contract=self.connector)
        result = dpm.get_connector_contract(connector_name)
        self.assertEqual(self.connector.uri_raw, result.uri_raw)
        self.assertEqual(self.connector.module_name, result.module_name)
        self.assertEqual(self.connector.handler, result.handler)
        self.assertEqual(self.connector.get_key_value('sep'), result.get_key_value('sep'))
        self.assertEqual(self.connector.get_key_value('encoding'), result.get_key_value('encoding'))

    def test_set_version(self):
        dpm = ControlPropertyManager('test_abstract_properties')
        self.assertEqual('v0.00', dpm.get(dpm.KEY.version_key))
        dpm.set(dpm.KEY.version_key, '1.00')
        self.assertEqual('1.00', dpm.get(dpm.KEY.version_key))
        self.assertEqual(dpm.get(dpm.KEY.version_key), dpm.version)

    def test_set_description(self):
        dpm = ControlPropertyManager('test_abstract_properties')
        self.assertEqual('', dpm.get(dpm.KEY.description_key))
        dpm.set(dpm.KEY.description_key, 'This Task description')
        self.assertEqual('This Task description', dpm.get(dpm.KEY.description_key))
        self.assertEqual(dpm.get(dpm.KEY.description_key), dpm.description)

    def test_set_snapshot(self):
        dpm = ControlPropertyManager('test_abstract_properties')
        dpm.set_snapshot('3.00.001')
        control = ['description', 'cleaners', 'snapshot', 'intent', 'version', 'run_book','connectors', 'knowledge']
        self.assertCountEqual(control, list(dpm.get(dpm.KEY.contract_key).keys()))
        result = list(dpm.get(dpm.KEY.snapshot_key).keys())
        control = ['test_abstract_properties_#3_00_001']
        self.assertCountEqual(control, result)
        result = list(dpm.get(dpm.KEY.snapshot_key).get('test_abstract_properties_#3_00_001').keys())
        # check the snapshot hasn't been copied to the snapshot
        control = ['description', 'cleaners', 'intent', 'version', 'run_book','connectors', 'knowledge']
        self.assertCountEqual(control, result)

    def test_recover_snapshot(self):
        dpm = ControlPropertyManager('test_abstract_properties')
        version = '1.00.000'
        dpm.set(dpm.KEY.version_key, version)
        self.assertEqual(version, dpm.version)
        snap_name = dpm.set_snapshot("test")
        control = '1.00.001'
        dpm.set(dpm.KEY.version_key, control)
        self.assertEqual(control, dpm.version)
        dpm.recover_snapshot(snap_name)
        self.assertEqual(version, dpm.version)

    def test_get_snapshot(self):
        dpm = ControlPropertyManager('test_abstract_properties')
        control = []
        result = dpm.snapshots
        self.assertEqual(control, result)
        dpm.set_snapshot('3.00.001')
        dpm.set_snapshot('test')
        control = ['test_abstract_properties_#3_00_001', 'test_abstract_properties_#test']
        result = dpm.snapshots
        self.assertEqual(control, result)
        dpm2 = ControlPropertyManager('new_abstract_properties')
        dpm2.set_snapshot('2018-06-12')
        control = ['new_abstract_properties_#2018-06-12']
        result = dpm2.snapshots
        self.assertEqual(control, result)
        control = ['test_abstract_properties_#3_00_001', 'test_abstract_properties_#test']
        result = dpm.snapshots
        self.assertEqual(control, result)

    def test_add_and_remove_knowledge(self):
        keys = ['overview', 'notes', 'observations', 'attribute', 'dictionary', 'tor']
        manager = ControlPropertyManager('test_abstract_properties', knowledge_keys=keys)
        manager.set_knowledge(text="My Note", label='age', catalog='notes')
        manager.set_knowledge(text="general note", label='comment', catalog='notes')
        result = manager.knowledge_filter(catalog='notes', label='age')
        self.assertEqual(["My Note"], list(result.get('notes').get('age').values()))
        #remove
        result = manager.reset_knowledge()
        self.assertEqual({}, manager.knowledge_filter(catalog='notes'))

    def test_has_knowledge(self):
        keys = ['overview', 'notes', 'observations', 'attribute', 'dictionary', 'tor']
        manager = ControlPropertyManager('test_abstract_properties', knowledge_keys=keys)
        result = manager.has_knowledge()
        self.assertFalse(result)
        manager.set_knowledge('overview', 'label', 'text')
        result = manager.has_knowledge()
        self.assertTrue(result)

    def test_bulk_upload_and_filter(self):
        keys = ['overview', 'notes', 'observations', 'attribute', 'dictionary', 'tor']
        manager = ControlPropertyManager('test_abstract_properties', knowledge_keys=keys)
        upload = {'one': 'comment one', 'two': 'comment two', 'three': 'comment three'}
        manager.bulk_upload_knowledge(upload, catalog='notes')
        self.assertCountEqual(['one', 'two', 'three'], list(manager.knowledge_filter(catalog='notes').get('notes').keys()))
        result = manager.knowledge_filter(regex='one')
        self.assertCountEqual(['notes'], result.keys())
        self.assertCountEqual(['one'], result.get('notes').keys())
        self.assertCountEqual(['comment one'], list(result.get('notes').get('one').values()))
        result = manager.knowledge_filter(regex='comment')
        self.assertCountEqual(['notes'], result.keys())
        self.assertCountEqual(['one', 'two', 'three'], result.get('notes').keys())
        result = manager.knowledge_filter(label=['two', 'three'], regex='comment')
        self.assertCountEqual(['notes'], result.keys())
        self.assertCountEqual(['two', 'three'], result.get('notes').keys())

    def test_set_intent(self):
        dpm = ControlPropertyManager('test_abstract_properties')
        with self.assertRaises(ValueError) as context:
            dpm.set_intent(intent_param=[])
        self.assertTrue("The intent section must be a dictionary" in str(context.exception))
        dpm.set_intent(intent_param={})
        control = {}
        self.assertEqual(control, dpm.get_intent())
        # add values
        cleaner1 = {'clean_01': {'headers': 'h1', 'dtype': ['number', 'str']}}
        dpm.set_intent(cleaner1)
        control = {'0': {'clean_01': {'dtype': ['number', 'str'], 'headers': 'h1'}}}
        self.assertEqual(control, dpm.get_intent())
        # adding the same cleaner should not change anything
        dpm.set_intent(cleaner1)
        self.assertEqual(control, dpm.get_intent())
        # same cleaner differtent intent
        cleaner1 = {'clean_01': {'headers': 'h4'}}
        control = {'0': {'clean_01': {'dtype': ['number', 'str'], 'headers': 'h1'}}}
        dpm.set_intent(cleaner1, replace_intent=False)
        self.assertEqual(control, dpm.get_intent())
        control = {'0': {'clean_01': {'headers': 'h4'}}}
        dpm.set_intent(cleaner1, replace_intent=True)
        self.assertEqual(control, dpm.get_intent())
        # second cleaner
        cleaner2 = {'clean_02': {'headers': ['h2', 'h3'], 'regex': 'text'}}
        dpm.set_intent(cleaner2)
        control = {'0': {'clean_01': {'headers': 'h4'},
                         'clean_02': {'headers': ['h2', 'h3'], 'regex': 'text'}}}
        self.assertEqual(control, dpm.get_intent())
        cleaner1 = {'clean_01': {'headers': 'h1', 'dtype': ['number', 'str']}}
        dpm.set_intent(cleaner1, replace_intent=True)
        control = {'0': {'clean_01': {'dtype': ['number', 'str'], 'headers': 'h1'},
                         'clean_02': {'headers': ['h2', 'h3'], 'regex': 'text'}}}
        self.assertEqual(control, dpm.get_intent())

    def test_set_intent_levels(self):
        dpm = ControlPropertyManager('test_abstract_properties')
        cleaner1 = {'clean_01': {'headers': 'h1'}}
        dpm.set_intent(cleaner1, level=0)
        control = {'0': {'clean_01': {'headers': 'h1'}}}
        self.assertEqual(control, dpm.get_intent())
        dpm.set_intent(cleaner1, level=1)
        control = {'1': {'clean_01': {'headers': 'h1'}}}
        self.assertEqual(control, dpm.get_intent())
        # change params
        cleaner1 = {'clean_01': {'headers': 'h3'}}
        dpm.set_intent(cleaner1, level=0)
        control = {'0': {'clean_01': {'headers': 'h3'}},
                   '1': {'clean_01': {'headers': 'h1'}}}
        self.assertEqual(control, dpm.get_intent())
        # used -1 same intent, different params
        cleaner1 = {'clean_01': {'headers': 'h4'}}
        dpm.set_intent(cleaner1, level=-1)
        control = {'0': {'clean_01': {'headers': 'h3'}},
                   '1': {'clean_01': {'headers': 'h1'}},
                   '2': {'clean_01': {'headers': 'h4'}}}
        self.assertEqual(control, dpm.get_intent())
        # replace just one of them using -1
        cleaner1 = {'clean_01': {'headers': 'h1'}}
        dpm.set_intent(cleaner1, level=-1)
        self.assertEqual(control, dpm.get_intent())

    def test_remove_intent(self):
        dpm = ControlPropertyManager('test_abstract_properties')
        # setup
        dpm.set_intent({'clean_01': {'headers': 'h1'}})
        control = {'0': {'clean_01': {'headers': 'h1'}}}
        self.assertEqual(control, dpm.get_intent())
        # remove by label
        dpm.remove_intent('clean_01')
        self.assertEqual({}, dpm.get_intent())
        dpm.set_intent({'clean_01': {'headers': 'h1'}}, level=0)
        dpm.set_intent({'clean_01': {'headers': 'h4'}}, level=1)
        control = {'0': {'clean_01': {'headers': 'h1'}},
                   '1': {'clean_01': {'headers': 'h4'}}}
        self.assertEqual(control, dpm.get_intent())
        dpm.remove_intent('clean_01')
        self.assertEqual({}, dpm.get_intent())
        # remove by cleaner
        dpm.set_intent({'clean_01': {'headers': 'h1'}}, level=0)
        dpm.set_intent({'clean_01': {'headers': 'h4'}}, level=1)
        control = {'0': {'clean_01': {'headers': 'h1'}}}
        dpm.remove_intent({'clean_01': {'headers': 'h4'}})
        self.assertEqual(control, dpm.get_intent())
        # remove all
        dpm.set_intent({'clean_01': {'headers': 'h1'}})
        dpm.set_intent({'clean_02': {'headers': 'h4'}})
        dpm.set_intent({'clean_03': {'headers': 'h3'}}, level=1)
        dpm.reset_intents()
        self.assertEqual({}, dpm.get_intent())
        # test restricted remove
        dpm.set_intent({'clean_01': {'headers': 'h1'}}, level=0)
        dpm.set_intent({'clean_02': {'headers': 'h4'}}, level=1)
        dpm.remove_intent(level=2)
        control = {'0': {'clean_01': {'headers': 'h1'}},
                   '1': {'clean_02': {'headers': 'h4'}}}
        self.assertDictEqual(control, dpm.get_intent())
        dpm.remove_intent(level=1)
        control = {'0': {'clean_01': {'headers': 'h1'}}}
        self.assertDictEqual(control, dpm.get_intent())
        dpm.remove_intent(level=0)
        self.assertEqual({}, dpm.get_intent())

    def test_get_intent(self):
        dpm = ControlPropertyManager('test_abstract_properties')
        dpm.set_intent({'remove_head': {'headers': ['one', 'two']}, 'to_str' : {'headers': ['five', 'six']}})
        dpm.set_intent({'clean_03': {'headers': 'h3'}}, level=1)
        self.assertDictEqual({'remove_head': {'headers': ['one', 'two']}, 'to_str': {'headers': ['five', 'six']}}, dpm.get_intent(level=0))
        self.assertDictEqual({'clean_03': {'headers': 'h3'}}, dpm.get_intent(level=1))
        result = dpm.get_intent(level=0, intent='remove_head')
        self.assertDictEqual({'remove_head': {'headers': ['one', 'two']}}, result)
        result = dpm.get_intent(level=1, intent='remove_head')
        self.assertEqual({}, result)

    def test_intent_report(self):
        dpm = ControlPropertyManager('test_abstract_properties')
        dpm.set_intent({'clean_03': {'headers': 'h3'}}, level=1)
        dpm.set_intent({'clean_02': {'dtype': ['number', 'str'], 'headers': 'h1'}}, level=-1)
        dpm.set_intent({'clean_01': {'headers': 'h1'}})
        report = dpm.report_intent()
        self.assertCountEqual(['clean_01', 'clean_02', 'clean_03'], report['intent'])
        self.assertCountEqual(['0', '0', '1'], report['level'])
        self.assertCountEqual([['headers=h1'], ["dtype=['number', 'str']", 'headers=h1'], ['headers=h3']], report['parameters'])

    def test_run_book(self):
        pm = ControlPropertyManager('test_abstract_properties')
        result = pm.report_run_book()
        self.assertDictEqual({'name': [], 'run_book': []}, result)
        pm.set_run_book('run1', [1,5,3])
        self.assertEqual([1,5,3], pm.get_run_book('run1'))
        pm.set_run_book('run2', ['A', 'B'])
        self.assertEqual(['A', 'B'], pm.get_run_book('run2'))
        pm.set_run_book('run1', [1, 2, 3])
        self.assertEqual([1,2,3], pm.get_run_book('run1'))
        result = pm.report_run_book()
        self.assertDictEqual({'name': ['run2', 'run1'], 'run_book': ['A, B', '1, 2, 3']}, result)

    def test_schema(self):
        pm = ControlPropertyManager('test_abstract_properties')
        self.assertEqual([], pm.canonical_schemas)
        schema1 =  dict({'att1': ['type', 'nulls']})
        schema2 =  dict({'A': [1, 0.98]})
        pm.set_canonical_schema('root', schema1)
        pm.set_canonical_schema('schema', schema2)
        self.assertDictEqual(schema1, pm.get_canonical_schema('root'))
        self.assertDictEqual(schema2, pm.get_canonical_schema('schema'))
        self.assertCountEqual(['root', 'schema'], pm.canonical_schemas)
        self.assertFalse(pm.remove_canonical_schema('name'))
        self.assertTrue(pm.remove_canonical_schema('schema'))
        self.assertCountEqual(['root'], pm.canonical_schemas)
        self.assertDictEqual(schema1, pm.get_canonical_schema('root'))
        self.assertDictEqual({}, pm.get_canonical_schema('schema'))

    def test_file_pattern(self):
        pm = ControlPropertyManager('task')
        result = pm.file_pattern(connector_name='source')
        self.assertEqual('aistac_control_task_source.pickle', result)
        result = pm.file_pattern(connector_name='source',file_type='yaml')
        self.assertEqual('aistac_control_task_source.yaml', result)
        result = pm.file_pattern(connector_name='source', stamped="hours")
        self.assertEqual('aistac_control_task_source${TO_HOURS}.pickle', result)
        result = pm.file_pattern(connector_name='source', versioned=True, stamped="minutes")
        self.assertEqual('aistac_control_task_source${VERSION}${TO_MINUTES}.pickle', result)
        result = pm.file_pattern(connector_name='source', versioned=True)
        self.assertEqual('aistac_control_task_source${VERSION}.pickle', result)
        # Check it works with connector contract
        cc = ConnectorContract(uri=result, module_name="", handler="", version="v1.01")
        self.assertEqual("aistac_control_task_source_v1.01.pickle", cc.uri)
        # test prefix & suffix
        result = pm.file_pattern(connector_name='source', prefix="prefix_")
        self.assertEqual('prefix_aistac_control_task_source.pickle', result)
        result = pm.file_pattern(connector_name='source', suffix="?name=fred&type=male")
        self.assertEqual('aistac_control_task_source.pickle?name=fred&type=male', result)
        result = pm.file_pattern(connector_name='source', prefix="prefix_", suffix="?name=fred&type=male")
        self.assertEqual('prefix_aistac_control_task_source.pickle?name=fred&type=male', result)
        # test path
        result = pm.file_pattern(connector_name='source', path="s3://bucket/path")
        self.assertEqual('s3://bucket/path/aistac_control_task_source.pickle', result)
        result = pm.file_pattern(connector_name='source', path=["s3://bucket", "path"])
        self.assertEqual('s3://bucket/path/aistac_control_task_source.pickle', result)

    def test_modify_connector_uri(self):
        pm = ControlPropertyManager('task')
        connector_name = 'connector'
        uri = "s3://bucket/path/aistac_control_task_connector.pickle?name=fred&value=45"
        cc = ConnectorContract(uri=uri, module_name='module.package', handler='Handler')
        pm.set_connector_contract(connector_name=connector_name, connector_contract=cc)
        control = "http://git.com/aistac/aistac_control_task_connector.pickle?name=fred&value=45"
        result = pm.modify_connector_uri(connector_name=connector_name, old_pattern="s3://bucket/path/", new_pattern="http://git.com/aistac/")
        self.assertEqual(control, pm.get_connector_contract(connector_name=connector_name).uri)

    def test_reset_each(self):
        pm = ControlPropertyManager('task')
        pm.reset_canonical_schemas()
        pm.reset_connector_contracts()
        pm.reset_intents()
        pm.reset_knowledge()
        pm.reset_run_books()
        pm.reset_snapshots()
        result = pm.get(pm.KEY.contract_key)
        control = {'cleaners': {}, 'description': '', 'version': 'v0.00', 'connectors': {}, 'intent': {},
                   'knowledge': {'schema': {}}, 'run_book': {}, 'snapshot': {}}
        self.assertDictEqual(control, result)

    def test_remove_restricted(self):
        pm = ControlPropertyManager('task')
        pm.remove(pm.join(pm.KEY.intent_key, 'fred'))



if __name__ == '__main__':
    unittest.main()