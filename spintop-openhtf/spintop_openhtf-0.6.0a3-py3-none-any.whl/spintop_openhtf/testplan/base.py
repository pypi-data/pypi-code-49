import os
import sys
import inspect
import datetime
import warnings

from copy import copy
from contextlib import contextmanager

import openhtf as htf

from openhtf.util import conf
from openhtf.plugs import user_input, BasePlug

import webbrowser

from ..storage import SITE_DATA_DIR
from ..callbacks.file_provider import TemporaryFileProvider
from ..callbacks.local_storage import LocalStorageOutput


try:
    import tornado
except ImportError:
    warnings.warn(
        'Tornado not available. GUI server will not work. '
        'If you wish to install it, you may install spintop-openhtf '
        'with the [server] dependency, such as '
        'pip install spintop-openhtf[server]. Do note that this requires '
        'tornado<5.0.'
    )
else:
    from ..callbacks import station_server

from .. import (
    Test,
    # load_component_file,
    # CoverageAnalysis
)

HISTORY_BASE_PATH = os.path.join(SITE_DATA_DIR, 'openhtf-history')

DEFAULT = object()

class TestPlanError(Exception): pass

class TestSequence(object):
    def __init__(self, name):
        self._setup_phases = []
        self._test_phases = []
        self._teardown_phases = []
        self.name = name
    
    def setup(self, name):
        """Decorator factory for a setup function.
        
        ```python
        my_sequence = TestSequence('Parent')
        
        @my_sequence.setup('my-setup-name')
        def setup_fn(test):
            (...)
        
        ```
        """
        return self._decorate_phase(name, self._setup_phases)
    
    def testcase(self, name):
        """Decorator factory for a normal phase. 
        """
        return self._decorate_phase(name, self._test_phases)
    
    def teardown(self, name):
        """Decorator factory for a teardown phase. 
        """
        return self._decorate_phase(name, self._teardown_phases)
    
    def plug(self, *args, **kwargs):
        """Helper method: shortcut to htf.plugs.plug(...)"""
        return htf.plugs.plug(*args, **kwargs)
    
    def measures(self, *args, **kwargs):
        """Helper method: shortcut to htf.measures(...)"""
        return htf.plugs.plug(*args, **kwargs)
    
    def sub_sequence(self, name):
        """Create new empty TestSequence and append it to this sequence.
        
        The following two snippets are equivalent:
        
        ```python
        my_sequence = TestSequence('Parent')
        sub_sequence = my_sequence.sub_sequence('Child')
        ```
        
        ```python
        my_sequence = TestSequence('Parent')
        sub_sequence = TestSequence('Child')
        my_sequence.append(sub_sequence)
        ```
        """
        group = TestSequence(name)
        self.append(group)
        return group
    
    def append(self, phase):
        self._test_phases.append(phase)
        
    def _decorate_phase(self, name, array):
        def _note_fn(fn):
            phase = self._add_phase(fn, name, array)
            return phase
        return _note_fn
    
    def _add_phase(self, fn, name, array):
        phase = ensure_htf_phase(fn)
        phase.options.name = name
        # phase.extra_kwargs['testplan'] = self
        array.append(phase)
        return phase
        
    @property
    def phase_group(self):
        # Recursively get phase groups of sub phases if available, else the phase itself.
        _test_phases = [getattr(phase, 'phase_group', phase) for phase in self._test_phases]
        
        return htf.PhaseGroup(
            setup=self._setup_phases,
            main=_test_phases,
            teardown=self._teardown_phases,
            name=self.name
        )
    
class TestPlan(TestSequence):
    DEFAULT_CONF = dict(
        station_server_port='4444', 
        capture_docstring=True
    )
    def __init__(self, name='testplan', store_result=True):
        super(TestPlan, self).__init__(name=name)
        
        self._execute_test = None
        self._top_level_component = None
        self.coverage = None
        self.file_provider = TemporaryFileProvider()
        self.callbacks = []
        
        # Array but must contain only one phase.
        # Array is for compatibility with self._decorate_phase function of parent class.
        self._trigger_phases = []
        self._no_trigger = False
        
        if store_result:
            self.add_callbacks(LocalStorageOutput(_local_storage_filename_pattern, indent=4))
            
        self.failure_exceptions = (user_input.SecondaryOptionOccured,)

    @property
    def execute_test(self):
        """Returns a function that takes no arguments and that executes the test described by this test plan."""
        if not self._execute_test:
            self.freeze_test()
        return self._execute_test
    
    @property
    def history_path(self):
        path = os.path.join(HISTORY_BASE_PATH, self.name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path
    
    @property
    def is_runnable(self):
        phases = self._test_phases + self._trigger_phases
        return bool(phases)
    
    @property
    def trigger_phase(self):
        return self._trigger_phases[0] if self._trigger_phases else None
        
    @property
    def is_test_frozen(self):
        return bool(self._execute_test)
        
    def image_url(self, url):
        return self.file_provider.create_url(url)
    
    def trigger(self, name):
        """Decorator factory for the trigger phase. 
        
        Similar to `testcase`, except that this function will be used as the test trigger.
        
        The test trigger is a special test phase that is executed before test officialy start.
        Once this phase is complete, the test will start. Usually used to configure the test with
        the DUT id for example."""
        if self.trigger_phase:
            raise TestPlanError('There can only be one @trigger function.')
        
        return self._decorate_phase(name, self._trigger_phases)

    def no_trigger(self):
        self._no_trigger = True
    
    def add_callbacks(self, *callbacks):
        if self.is_test_frozen:
            raise RuntimeError('Cannot add callbacks to the test plan after the test was frozen.')
        self.callbacks += callbacks
    
    def assert_runnable(self):
        if not self.is_runnable:
            # No phases ! Abort now.
            raise RuntimeError('Test is empty, aborting.')
    
    def execute(self):
        """ Execute the configured test using the test_start function as a trigger.
        """
        return self.execute_test()
    
    def run_once(self, launch_browser=True):
        return self.run(launch_browser=launch_browser, once=True)
    
    def run(self, launch_browser=True, once=False):
        self._load_default_conf()
        with self._station_server_context(launch_browser):
            while True:
                try:
                    self.execute()
                except KeyboardInterrupt:
                    break
                finally:
                    if once:
                        break
    
    def freeze_test(self):
        self._execute_test = self._create_execute_test()
        
    @contextmanager
    def _station_server_context(self, launch_browser=True):
        with station_server.StationServer(self.file_provider) as server:
            self.add_callbacks(server.publish_final_state)
            self.assert_runnable() # Check before launching browser
            self.freeze_test()
            
            if launch_browser and conf['station_server_port']:
                webbrowser.open('http://localhost:%s' % conf['station_server_port'])
            
            yield
    
    def _load_default_conf(self):
        conf.load_from_dict(self.DEFAULT_CONF, _override=False)

    def _create_execute_test(self):
        self.assert_runnable()
        
        test = Test(self.phase_group, test_name=self.name, _code_info_after_file=__file__)
        test.configure(failure_exceptions=self.failure_exceptions)
        test.add_output_callbacks(*self.callbacks)
        
        
        trigger_phase = self._build_trigger_phase()
        
        def execute_test():
            return test.execute(test_start=trigger_phase)

        return execute_test
        
    def _build_trigger_phase(self):
        if self.trigger_phase:
            return self.trigger_phase
        elif self._no_trigger:
            return None
        else:
            return create_default_trigger()
    
    def create_plug(self):
        class _SelfReferingPlug(BasePlug):
            def __new__(cls):
                return self
        
        return _SelfReferingPlug
    
    def spintop_plug(self, fn):
        return htf.plugs.plug(spintop=self.create_plug())(fn)
    

def _local_storage_filename_pattern(**test_record):
    folder = '{metadata[test_name]}'.format(**test_record)
    start_time_datetime = datetime.datetime.utcfromtimestamp(test_record['start_time_millis']/1000.0)
    start_time = start_time_datetime.strftime(r"%Y_%m_%d_%H%M%S_%f")
    subfolder = '{dut_id}_{start_time}_{outcome}'.format(start_time=start_time, **test_record)
    return os.path.join(HISTORY_BASE_PATH, folder, subfolder)
    
def create_default_trigger(message='Enter a DUT ID in order to start the test.',
        validator=lambda sn: sn, **state):
    
    @htf.PhaseOptions(timeout_s=None, requires_state=True)
    @htf.plugs.plug(prompts=user_input.UserInput)
    def trigger_phase(state, prompts):
        """Test start trigger that prompts the user for a DUT ID."""
        dut_id = prompts.prompt(message, text_input=True)
        state.test_record.dut_id = validator(dut_id)
        
    return trigger_phase
    
def ensure_htf_phase(fn):
    if not hasattr(fn, 'options'):
        # Not a htf phase, decorate it so it becomes one.
        fn = htf.PhaseOptions()(fn) 
    return fn
