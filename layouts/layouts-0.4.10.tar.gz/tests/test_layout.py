'''
Test various layout configurations
'''

### Imports ###

import layouts
import pytest

from tests.layoutstest import layout_mgr



### Functions ###

@pytest.fixture
def default_layout(layout_mgr):
    '''
    Retrieve default layout
    '''
    layout_name = 'default'
    return layout_mgr.get_layout(layout_name)

def test_list_layouts(layout_mgr):
    '''
    Make sure we can retrieve at least one layout
    '''
    assert layout_mgr.list_layouts()

def test_default_layout(default_layout):
    '''
    Make sure we can retrieve the default layout
    '''
    layout_name = 'default'
    assert default_layout.name() == layout_name

def test_locale_lookup(layout_mgr):
    '''
    Make sure the HID locale lookup is behaving correctly
    '''
    layout_name = 'default'
    layout = layout_mgr.get_layout(layout_name)
    assert layout.locale() == (0, 'Undefined')

    layout_name = 'en_US'
    layout = layout_mgr.get_layout(layout_name)
    assert layout.locale() == (33, 'US')

def test_usb_hid_keyboard_code_squash(layout_mgr):
    '''
    Test to make sure HID keyboard codes are squashed as expected
    '''
    layout_default = layout_mgr.get_layout('default')
    assert int(layout_default.json()['from_hid_keyboard']['Z'], 0) == 0x1D

    layout_squash = layout_mgr.get_layout('de_DE')
    assert int(layout_default.json()['from_hid_keyboard']['Z'], 0) == 0x1D # Make sure datastructures are still ok
    assert int(layout_squash.json()['from_hid_keyboard']['Z'], 0) == 0x1C

    # de_DE remaps Z to the Y position (on an ANSI keyboard), make sure the layouts don't match
    assert layout_default.json()['from_hid_keyboard']['Z'] != layout_squash.json()['from_hid_keyboard']['Z']

def test_string_compose(default_layout):
    '''
    Test string compose from a layout
    '''
    test_string = 'Hello World!'
    result = default_layout.compose(test_string)

    # Empty combos are used to clear key-state
    compare = [
        ["Shift", "H"], ["No Event"],
        ["E"], ["No Event"],
        ["L"], ["No Event"],
        ["L"], ["No Event"],
        ["O"], ["No Event"],
        ["Space"], ["No Event"],
        ["Shift", "W"], ["No Event"],
        ["O"], ["No Event"],
        ["R"], ["No Event"],
        ["L"], ["No Event"],
        ["D"], ["No Event"],
        ["Shift", "1"], ["No Event"],
    ]

    # Convert list of list to a list of tuples
    result_set = map(tuple, result)
    compare_set = map(tuple, compare)

    # Compare elements
    failed_compares = []
    for item in zip(result_set, compare_set):
        print(item)
        if item[0] != item[1]:
            failed_compares.append(item)

    assert not failed_compares

def test_string_compose_minimal(default_layout):
    '''
    Test string compose from a layout, using minimal clears
    '''
    test_string = 'Hello World!'
    result = default_layout.compose(test_string, minimal_clears=True)

    # Empty combos are used to clear key-state
    compare = [
        ["Shift", "H"],
        ["E"],
        ["L"], ["No Event"],
        ["L"],
        ["O"],
        ["Space"],
        ["Shift", "W"],
        ["O"],
        ["R"],
        ["L"],
        ["D"],
        ["Shift", "1"], ["No Event"],
    ]

    # Convert list of list to a list of tuples
    result_set = map(tuple, result)
    compare_set = map(tuple, compare)

    # Compare elements
    failed_compares = []
    for item in zip(result_set, compare_set):
        print(item)
        if item[0] != item[1]:
            failed_compares.append(item)

    assert not failed_compares

