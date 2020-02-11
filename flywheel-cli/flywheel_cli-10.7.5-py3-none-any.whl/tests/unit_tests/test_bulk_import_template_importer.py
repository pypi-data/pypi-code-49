from flywheel_cli.bulk_import.exceptions import TemplateImporterError
from flywheel_cli.bulk_import.importers import template

import pytest


class MockConfig:
    def __init__(self, config):
        for key, value in config.items():
            setattr(self, key, value)


def test_template_importer_initialize_no_template():
    config = {'template': None}
    importer = template.TemplateImporter(MockConfig(config))
    with pytest.raises(TemplateImporterError):
        importer.initialize()


def test_template_importer_initialize_str_template(mocker):
    config = {'template': '{group}:{project}'}
    importer = template.TemplateImporter(MockConfig(config))

    mocker.patch.object(template.TemplateImporter, 'check_group_reference')
    mocker.patch.object(template, 'parse_template_string')
    importer.initialize()
    template.parse_template_string.assert_called_once()


def test_template_importer_initialize_str_template_err(mocker):
    config = {'template': '{group}:{project}'}
    importer = template.TemplateImporter(MockConfig(config))

    mocker.patch.object(template, 'parse_template_string', side_effect=ValueError)
    with pytest.raises(TemplateImporterError):
        importer.initialize()


def test_template_importer_initialize_dict_template(mocker):
    config = {'template': [{'pattern': '{group}'}, {'pattern': '{project}'}]}
    importer = template.TemplateImporter(MockConfig(config))

    mocker.patch.object(template.TemplateImporter, 'check_group_reference')
    mocker.patch.object(template, 'parse_template_list')
    importer.initialize()
    template.parse_template_list.assert_called_once()


class MockPattern:
    def __init__(self, pattern):
        self.pattern = pattern


class MockNode:
    def __init__(self, pattern, next_node=None):
        self.template = MockPattern(pattern)
        self.next_node = next_node


def test_template_importer_check_group_reference():
    importer = template.TemplateImporter(MockConfig({'group': None}))
    importer.root_node = MockNode('{group}')
    importer.check_group_reference()


def test_template_importer_check_group_reference_no_group():
    importer = template.TemplateImporter(MockConfig({'group': None}))

    importer.root_node = MockNode('{project}')
    with pytest.raises(TemplateImporterError):
        importer.check_group_reference()
