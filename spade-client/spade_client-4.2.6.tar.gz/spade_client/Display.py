"""Displays the ElementTree instances created as a response from a **SPADE** server.
"""

from __future__ import print_function

def version(application):
    """
    Display the version information of the application

    :param ElementTree application: the application document whose version should be displayed.
    """
    print('Version of SPADE with identity : ' + application.find('status/identity').text)
    specification = application.find('specification')
    print('  SPADE Specification: ' + specification.text)
    implementation = application.find('implementation')
    print('  Implementation version: ' + implementation.text)


def status(application):
    """
    Display the status information of the application

    :param ElementTree application: the application document whose status should be displayed.
    """
    print('Status for SPADE with identity : ' + application.find('status/identity').text)
    execution = application.find('status/execution')
    print('  Executing state: ' + execution.text)


def named_resources(application, xpath, section):
    """
    Displays the name and description of all named resources in the specified xpath

    :param ElementTree application: the application document whose resources should be displayed.
    :param array xpath: the XPath elements used to extract the resources.
    :param string section: the display name of the section.
    """
    print(section)
    namedResources = []
    for x in xpath:
        c = application.findall(x)
        for named_resource in c:
            descriptionElement = named_resource.find('description')
            if None == descriptionElement:
                description = ''
            else:
                description = ' : ' + descriptionElement.text
            namedResources.append('  ' + named_resource.find('name').text + description)
    if 0 == len(namedResources):
	    print('* None *')
    for resource in namedResources:
        print(resource)


def action_result(action, response):
    """
    Display the description of the result of an action
    """
    descriptionElement = action.find('description')
    if None == descriptionElement:
        description = action.find('name').text
    else:
        description = descriptionElement.text
    print('Successfully initiated "' + description + '"')


def bundles_result(result, section):
    print(section)
    bundle_results = []
    bundles = result.findall('bundle')
    for bundle in bundles:
        noteElement = bundle.find('note')
        if None == noteElement:
            note = ''
        else:
            note = ' : ' + noteElement.text
        bundle_results.append('  ' + bundle.find('name').text + note)
    if 0 == len(bundle_results):
	    print('* None *')
    for bundle_result in bundle_results:
        print(bundle_result)
    

def digest(digest, leader):
    print(leader + digest.find('subject').text)
    changes = digest.findall('issue/issued')
    if 0 == len(changes):
        print(leader + '  * Empty *')
    for change in changes:
        print(leader + '  ' + change.find('item').text + ' : ' + change.find('time').text)


