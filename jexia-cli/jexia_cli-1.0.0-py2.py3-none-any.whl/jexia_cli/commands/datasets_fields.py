#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json

from jexia_cli.base import (ProjectServiceFieldList,
                            ProjectServiceFieldCommand,
                            ProjectServiceFieldDelete)
from jexia_cli.formatters import formatter_constraints


LOG = logging.getLogger(__name__)


class List(ProjectServiceFieldList):
    '''
    Show fields of dataset
    '''

    columns = ['id', 'name', 'type', 'immutable', 'properties', 'constraints']
    _formatters = {
        'properties': lambda v: json.dumps(v),
        'constraints': formatter_constraints,
    }
    resource = 'dataset'
    svc_url = 'mimir/ds'


class Create(ProjectServiceFieldCommand):
    '''
    Create new field in dataset.
    '''

    columns = ['id', 'name', 'type', 'immutable', 'properties', 'constraints']
    _formatters = {
        'properties': lambda v: json.dumps(v),
        'constraints': formatter_constraints,
    }
    resource = 'dataset'
    field_action = 'create'
    svc_url = 'mimir/ds'


class Update(ProjectServiceFieldCommand):
    '''
    Update the field's constraints in dataset.
    '''

    columns = ['id', 'name', 'type', 'immutable', 'properties', 'constraints']
    _formatters = {
        'properties': lambda v: json.dumps(v),
        'constraints': formatter_constraints,
    }
    resource = 'dataset'
    field_action = 'update'
    svc_url = 'mimir/ds'


class Delete(ProjectServiceFieldDelete):
    '''
    Delete field from the dataset
    '''

    resource = 'dataset'
    svc_url = 'mimir/ds'
