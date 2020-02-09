'''
Test various emitter configurations
'''

### Imports ###

import layouts
import layouts.emitter

from tests.layoutstest import layout_mgr



### Functions ###

def test_c_defines(layout_mgr):
    '''
    Make sure we can generate c defines
    '''
    layout_name = 'default'
    layout = layout_mgr.get_layout(layout_name)

    assert layouts.emitter.basic_c_defines(layout)

