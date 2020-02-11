import json
import os
import re

import pandas as pd

from seeq.sdk import *
from seeq.sdk.rest import ApiException
from seeq.base import util

from ._item import Item

from .. import _common
from .. import _login
from .. import _search

from .._common import DependencyNotFound


class StoredOrCalculatedItem(Item):
    def __init__(self, definition=None):
        super().__init__(definition)

        self.scoped_to = None

    def _populate_asset_and_path(self, item_id):
        try:
            trees_api = TreesApi(_login.client)
            asset_tree_output = trees_api.get_tree(id=item_id)  # type: AssetTreeOutputV1
            ancestors = [a.name for a in asset_tree_output.item.ancestors]
            if len(ancestors) >= 2:
                self.definition['Path'] = _common.path_list_to_string(ancestors[0:-1])
                self.definition['Asset'] = ancestors[-1]
            elif len(ancestors) == 1:
                self.definition['Path'] = None
                self.definition['Asset'] = ancestors[0]
            else:
                self.definition['Path'] = None
                self.definition['Asset'] = None
        except ApiException as e:
            # We'll get a 404 if the item is not in a tree
            if e.status != 404:
                raise

    def _pull(self, item_id):
        super()._pull(item_id)

        if 'Path' not in self.definition:
            self._populate_asset_and_path(item_id)

    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None, override_max_interp=False,
             scope_globals_to_workbook=False):
        raise RuntimeError('Pushed called but StoredOrCalculatedItem.push() not overloaded')

    def push_ancillaries(self, original_workbook_id, pushed_workbook_id, item_map):
        if 'Ancillaries' not in self:
            return

        if self.id not in item_map:
            raise RuntimeError(f'push_ancillaries() called before push() -- {self.id} is not in item_map')

        items_api = ItemsApi(_login.client)
        pushed_item = items_api.get_item_and_all_properties(id=item_map[self.id])  # type: ItemOutputV1

        ancillaries_api = AncillariesApi(_login.client)

        for ancillary_dict in self['Ancillaries']:
            if _common.get(ancillary_dict, 'Scoped To') not in [None, original_workbook_id]:
                continue

            found_item_ancillary_output = None
            for item_ancillary_output in pushed_item.ancillaries:  # type: ItemAncillaryOutputV1
                if item_ancillary_output.name == ancillary_dict['Name'] and \
                        item_ancillary_output.scoped_to == pushed_workbook_id:
                    found_item_ancillary_output = item_ancillary_output
                    break

            ancillary_input = AncillaryInputV1()
            ancillary_input.name = ancillary_dict['Name']
            ancillary_input.scoped_to = pushed_workbook_id
            ancillary_input.item_id = pushed_item.id

            ancillary_input.ancillaries = list()
            for ancillary_item_dict in ancillary_dict['Items']:
                ancillary_item_input = AncillaryItemInputV1()
                if ancillary_item_dict['ID'] not in item_map:
                    raise DependencyNotFound(ancillary_item_dict['ID'])

                ancillary_item_input.id = item_map[ancillary_item_dict['ID']]
                ancillary_item_input.name = ancillary_item_dict['Name']
                ancillary_item_input.order = ancillary_item_dict['Order']
                ancillary_input.ancillaries.append(ancillary_item_input)

            if found_item_ancillary_output is None:
                ancillaries_api.create_ancillary(body=ancillary_input)
            else:
                ancillaries_api.update_ancillary(id=found_item_ancillary_output.id,
                                                 body=ancillary_input)

    @staticmethod
    def _find_datasource_name(datasource_class, datasource_id, datasource_maps):
        for datasource_map in datasource_maps:
            if datasource_map['Datasource Class'] == datasource_class and \
                    datasource_map['Datasource ID'] == datasource_id:
                return datasource_map['Datasource Name']

        raise RuntimeError('Could not find Datasource Class "%s" and Datasource ID "%s" in datasource maps' %
                           (datasource_class, datasource_id))

    @staticmethod
    def _execute_regex_map(old_definition, regex_map, *, allow_missing_properties=False):
        capture_groups = dict()
        for prop, regex in regex_map['Old'].items():
            if prop not in StoredItem.SEARCHABLE_PROPS:
                searchable_props_string = '\n'.join(StoredItem.SEARCHABLE_PROPS)
                raise RuntimeError(
                    f'Datasource map contains an unsearchable property "{prop}".'
                    f'Searchable properties:\n{searchable_props_string}')

            if prop not in old_definition:
                if allow_missing_properties:
                    continue
                else:
                    return None

            regex = util.pythonize_regex_capture_group_names(regex)
            match = re.fullmatch(regex, old_definition[prop])
            if not match:
                return None

            capture_groups.update(match.groupdict())

        new_definition = dict()
        for prop, regex in regex_map['New'].items():
            new_definition[prop] = util.replace_tokens_in_regex(regex, capture_groups, escape=False)

        return new_definition

    def _lookup_item_via_datasource_map(self, pushed_workbook_id, datasource_maps):
        logging = list()
        items_api = ItemsApi(_login.client)

        # First, we process the "overrides". These are the cases where, even if the item with the ID exists in the
        # destination, we still want to map to something else. Useful for swapping datasources on the same server.
        item = self._lookup_in_datasource_map(
            pushed_workbook_id, [m for m in datasource_maps if _common.get(m, 'Override', default=False)], logging)

        if item is not None:
            return item

        # Second, we just try to look the item up by its ID. This case will occur when the user pulls a workbook,
        # makes a change, and pushes it back.
        try:
            item = items_api.get_item_and_all_properties(id=self.id)  # type: ItemOutputV1
        except ApiException:
            logging.append('ID %s not found directly' % self.id)

        if item is not None:
            return item

        # Finally, we try to use the non-override maps to find the item. This case will occur mostly when
        # transferring workbooks between servers.
        item = self._lookup_in_datasource_map(
            pushed_workbook_id, [m for m in datasource_maps if not _common.get(m, 'Override', default=False)], logging)

        if item is None:
            raise _common.DependencyNotFound(
                str(self), 'No match for item with ID %s:\n%s' % (self.id, '\n'.join(logging)))

        return item

    def _lookup_in_datasource_map(self, pushed_workbook_id, datasource_maps, logging):
        item = None
        for i in range(0, len(datasource_maps)):
            if item is not None:
                break

            datasource_map = datasource_maps[i]
            if 'Item-Level Map Files' in datasource_map:
                item = self._lookup_in_item_level_map_files(datasource_map, logging)

            if item is not None:
                break

            if 'RegEx-Based Maps' in datasource_map:
                item = self._lookup_in_regex_based_map(datasource_map, datasource_maps, logging, pushed_workbook_id, i)

        return item

    def _lookup_in_item_level_map_files(self, datasource_map, logging):
        items_api = ItemsApi(_login.client)

        item = None
        item_level_map_files = datasource_map['Item-Level Map Files']
        if not isinstance(item_level_map_files, list):
            item_level_map_files = [item_level_map_files]

        if 'DataFrames' not in datasource_map:
            datasource_map['DataFrames'] = dict()

        df_map = datasource_map['DataFrames']

        for item_level_map_file in item_level_map_files:
            if item_level_map_file not in df_map:
                if not os.path.exists(item_level_map_file):
                    raise ValueError('Item-Level Map File "%s" does not exist' % item_level_map_file)

                df_map[item_level_map_file] = pd.read_csv(item_level_map_file)

            df = df_map[item_level_map_file]

            if 'Old ID' not in df.columns or 'New ID' not in df.columns:
                raise ValueError('Item-Level Map File must have "Old ID" and "New ID" columns')

            mapped_row = df[df['Old ID'] == self.id]

            if len(mapped_row) > 1:
                raise ValueError('Ambiguous map: %d rows in "%s" match "Old ID" == "%s"\n%s' % (
                    len(mapped_row), item_level_map_file, self.id, mapped_row))

            if len(mapped_row) == 0:
                logging.append('Item-Level Map File "%s" did not match for "Old ID" value "%s"' % (
                    item_level_map_file, self.id))
                continue

            new_id = mapped_row.iloc[0]['New ID']

            item = items_api.get_item_and_all_properties(id=new_id)
            break

        return item

    def _lookup_in_regex_based_map(self, datasource_map, datasource_maps, logging, pushed_workbook_id, i):
        items_api = ItemsApi(_login.client)

        item = None
        new_definition = None
        for regex_map in datasource_map['RegEx-Based Maps']:
            old_definition = dict(self.definition)

            if 'Type' not in old_definition:
                raise ValueError('"Type" property required in "Old" datasource map definitions')

            if 'Datasource Class' in old_definition and 'Datasource ID' in old_definition:
                old_definition['Datasource Name'] = \
                    StoredOrCalculatedItem._find_datasource_name(old_definition['Datasource Class'],
                                                                 old_definition['Datasource ID'],
                                                                 datasource_maps)

            new_definition = StoredOrCalculatedItem._execute_regex_map(
                old_definition, regex_map, allow_missing_properties=self.type.endswith('Datasource'))

            if new_definition is not None:
                break

        if new_definition is None:
            logging.append('RegEx-Based Map %d did not match %s for "Old" values' % (i, self))
            return None

        if 'Type' not in new_definition:
            raise ValueError('"Type" property required in "New" datasource map definitions')

        if 'Datasource Name' in new_definition:
            if 'Datasource ID' not in new_definition:
                if 'Datasource Class' not in new_definition:
                    raise RuntimeError('"Datasource Class" required with "Datasource Name" in map:\n%s' %
                                       json.dumps(new_definition))

                datasource_results = items_api.search_items(
                    filters=['Datasource Class==%s&&Name==%s' % (new_definition['Datasource Class'],
                                                                 new_definition['Datasource Name']),
                             '@includeUnsearchable'],
                    types=['Datasource'],
                    limit=2)  # type: ItemSearchPreviewPaginatedListV1

                if len(datasource_results.items) > 1:
                    raise RuntimeError(
                        new_definition['Datasource Name'],
                        'Multiple datasources found that match "%s"' % new_definition['Datasource Name'])
                elif len(datasource_results.items) == 0:
                    raise RuntimeError(
                        new_definition['Datasource Name'],
                        'No datasource found that matches "%s"' % new_definition['Datasource Name'])

                new_datasource = datasource_results.items[0]  # type: ItemSearchPreviewV1
                new_definition['Datasource ID'] = items_api.get_property(
                    id=new_datasource.id, property_name='Datasource ID').value
            del new_definition['Datasource Name']

        # Simplify the types so that the search will find stored or calculated signals/conditions etc. This
        # helps when mapping, for example, an AF tree to a Data Lab tree.
        for t in ['Signal', 'Condition', 'Scalar', 'Datasource']:
            if t in new_definition['Type']:
                new_definition['Type'] = t

        if new_definition['Type'] not in ['User', 'UserGroup']:
            query_df = pd.DataFrame([new_definition])
            if 'Path' in new_definition:
                # If we're matching based on path, unfortunately we will not be able to match against archived items
                # due to a limitation of the API. See CRAB-18439.
                search_df = _search.search(query_df, workbook=pushed_workbook_id, recursive=False, quiet=True)
            else:
                search_df = _search.search(query_df, workbook=pushed_workbook_id, include_archived=True, quiet=True)

            # If several things are returned, but some of them are archived, then filter out the archived ones.
            # Tested by spy.workbooks.tests.test_push.test_datasource_map_by_name()
            if len(search_df) > 1 and 'Archived' in search_df.columns:
                search_df = search_df[~search_df['Archived']]

            if len(search_df) == 0:
                logging.append('RegEx-Based Map %d did not match %s filters:\n%s' % (i, self, new_definition))
            elif len(search_df) > 1:
                logging.append(
                    'RegEx-Based Map %d multiple matches %s filters:\n%s' % (i, self, new_definition))
            else:
                item = items_api.get_item_and_all_properties(
                    id=search_df.iloc[0]['ID'])
        else:
            if new_definition['Type'] == 'User':
                try:
                    users_api = UsersApi(_login.client)
                    item = users_api.get_user_from_username(
                        auth_datasource_class=new_definition['Datasource Class'],
                        auth_datasource_id=new_definition['Datasource ID'],
                        username=new_definition['Username'])
                except ApiException:
                    # Fall through, item not found
                    pass
            else:
                user_groups_api = UserGroupsApi(_login.client)
                user_groups = user_groups_api.get_user_groups()  # type: ItemPreviewListV1
                for user_group in user_groups.items:  # type: ItemPreviewV1
                    if user_group.name == new_definition['Name']:
                        item = user_group
                        break

        return item


class StoredItem(StoredOrCalculatedItem):
    SEARCHABLE_PROPS = ['Datasource Class', 'Datasource ID', 'Datasource Name', 'Data ID',
                        'Type', 'Name', 'Description', 'Username', 'Path', 'Asset']

    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None, override_max_interp=False,
             scope_globals_to_workbook=False):
        item = self._lookup_item_via_datasource_map(pushed_workbook_id, datasource_maps)

        item_map[self.id.upper()] = item.id.upper()

        if item.type not in ['User', 'UserGroup']:
            # We need to exclude Example Data, because it is set explicitly by the connector
            datasource_class_prop = Item._property_output_from_item_output(item, 'Datasource Class')
            datasource_id_prop = Item._property_output_from_item_output(item, 'Datasource ID')
            is_example_data = (datasource_class_prop and datasource_class_prop.value == 'Time Series CSV Files' and
                               datasource_id_prop and datasource_id_prop.value == 'Example Data')

            if override_max_interp and item.type == 'StoredSignal' and not is_example_data and \
                    'Maximum Interpolation' in self:
                src_max_interp = Item._property_input_from_scalar_str(self['Maximum Interpolation'])
                dst_max_interp_prop = Item._property_output_from_item_output(item, 'Maximum Interpolation')
                if dst_max_interp_prop:
                    dst_max_interp = Item._property_input_from_scalar_str(dst_max_interp_prop.value)
                    if src_max_interp.unit_of_measure != dst_max_interp.unit_of_measure or \
                            src_max_interp.value != dst_max_interp.value:
                        items_api = ItemsApi(_login.client)
                        items_api.set_property(id=item.id,
                                               property_name='Override Maximum Interpolation',
                                               body=src_max_interp)

        return item


class Datasource(StoredItem):
    @staticmethod
    def from_datasource_id(datasource_class, datasource_id):
        _filters = ['Datasource Class==' + datasource_class,
                    'Datasource ID==' + datasource_id]

        filters_arg = [' && '.join(_filters), '@includeUnsearchable']

        items_api = ItemsApi(_login.client)
        item_search_list = items_api.search_items(
            types=['Datasource'],
            filters=filters_arg,
            limit=1)  # type: ItemSearchPreviewPaginatedListV1

        if len(item_search_list.items) != 1:
            raise RuntimeError(
                'Datasource Class "%s" and Datasource ID "%s" not found' % (datasource_class, datasource_id))

        return Item.pull(item_search_list.items[0].id)


class TableDatasource(Datasource):
    pass


class CalculatedItem(StoredOrCalculatedItem):
    def _check_for_reference_item(self, pushed_workbook_id, datasource_maps, item_map):
        # If a calculated item is not part of these datasources, then it's likely coming from a connector and so we
        # should try to look it up in the datasource map. E.g. Tree File, AF Scalars
        user_defined_datasources = [None, 'cassandraV2', 'Seeq - FileSignal', _common.DEFAULT_DATASOURCE_CLASS]

        if _common.get(self, 'Datasource Class') not in user_defined_datasources or \
                _common.get(self, 'Reference', default=False):
            item = self._lookup_item_via_datasource_map(pushed_workbook_id, datasource_maps)
            item_map[self.id.upper()] = item.id.upper()
            return item

        return None

    def _find(self, label, pushed_workbook_id):
        item_output = self.find_me(label)

        if item_output is None and self.provenance == Item.CONSTRUCTOR:
            item_output = self._find_by_name(pushed_workbook_id)

        return item_output

    def _find_by_name(self, workbook_id):
        items_api = ItemsApi(_login.client)

        _filters = ['Name==%s' % self.name,
                    '@includeUnsearchable']

        search_results = items_api.search_items(
            filters=_filters,
            scope=workbook_id,
            types=[self.type],
            offset=0,
            limit=1)  # type: ItemSearchPreviewPaginatedListV1

        if len(search_results.items) == 0:
            return None

        return search_results.items[0]

    def _create_calculated_item_input(self, clazz, item_map, scoped_to, scope_globals_to_workbook):
        item_input = clazz()
        item_input.name = self.definition['Name']
        if 'Description' in self.definition:
            item_input.description = self.definition['Description']
        item_input.formula = Item.formula_string_from_list(self.definition['Formula'])

        parameters = list()
        if 'Formula Parameters' in self.definition:
            for parameter_name, parameter_id in self.definition['Formula Parameters'].items():
                if parameter_id not in item_map:
                    raise DependencyNotFound(parameter_id)

                parameters.append('%s=%s' % (parameter_name, item_map[parameter_id.upper()]))

        for _attr_name in ['formula_parameters', 'parameters']:
            if hasattr(item_input, _attr_name):
                setattr(item_input, _attr_name, parameters)

        if 'Number Format' in self.definition:
            item_input.number_format = self.definition['Number Format']

        if scope_globals_to_workbook or _common.present(self.definition, 'Scoped To'):
            item_input.scoped_to = scoped_to

        return item_input

    def _set_ui_config(self, _id):
        items_api = ItemsApi(_login.client)
        if 'UIConfig' in self.definition:
            items_api.set_property(id=_id, property_name='UIConfig',
                                   body=PropertyInputV1(value=json.dumps(self.definition['UIConfig'])))


class StoredSignal(StoredItem):
    pass


class CalculatedSignal(CalculatedItem):
    def _pull(self, item_id):
        super()._pull(item_id)
        signals_api = SignalsApi(_login.client)
        signal_output = signals_api.get_signal(id=item_id)  # type: SignalOutputV1
        self._pull_formula_based_item(signal_output)

    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None, override_max_interp=False,
             scope_globals_to_workbook=False):
        item = self._check_for_reference_item(pushed_workbook_id, datasource_maps, item_map)
        if item:
            return item

        signals_api = SignalsApi(_login.client)

        item_output = self._find(label, pushed_workbook_id)

        signal_input = self._create_calculated_item_input(
            SignalInputV1, item_map,
            pushed_workbook_id, scope_globals_to_workbook)  # type: SignalInputV1

        if item_output is None:
            signal_output = signals_api.put_signal_by_data_id(datasource_class=_common.DEFAULT_DATASOURCE_CLASS,
                                                              datasource_id=_common.DEFAULT_DATASOURCE_ID,
                                                              data_id=self._construct_data_id(label),
                                                              body=signal_input)  # type: SignalOutputV1
        else:
            signal_output = signals_api.put_signal(id=item_output.id,
                                                   body=signal_input)  # type: SignalOutputV1

        self._set_ui_config(signal_output.id)

        item_map[self.id.upper()] = signal_output.id.upper()

        return signal_output


class StoredCondition(StoredItem):
    pass


class CalculatedCondition(CalculatedItem):
    def _pull(self, item_id):
        super()._pull(item_id)
        conditions_api = ConditionsApi(_login.client)
        condition_output = conditions_api.get_condition(id=item_id)  # type: ConditionOutputV1
        self._pull_formula_based_item(condition_output)

    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None, override_max_interp=False,
             scope_globals_to_workbook=False):
        item = self._check_for_reference_item(pushed_workbook_id, datasource_maps, item_map)
        if item:
            return item

        conditions_api = ConditionsApi(_login.client)

        item_output = self._find(label, pushed_workbook_id)

        condition_input = self._create_calculated_item_input(
            ConditionInputV1, item_map,
            pushed_workbook_id, scope_globals_to_workbook)  # type: ConditionInputV1

        if item_output is None:
            condition_input.datasource_class = _common.DEFAULT_DATASOURCE_CLASS
            condition_input.datasource_id = _common.DEFAULT_DATASOURCE_ID
            condition_input.data_id = self._construct_data_id(label)
        else:
            # There is no easy way to update a Condition by its ID, so we have to retrieve its data id triplet
            condition_output = conditions_api.get_condition(id=item_output.id)  # type: ConditionOutputV1
            condition_input.datasource_class = condition_output.datasource_class
            condition_input.datasource_id = condition_output.datasource_id
            condition_input.data_id = condition_output.data_id

        item_batch_output = conditions_api.put_conditions(
            body=ConditionBatchInputV1(conditions=[condition_input]))  # type: ItemBatchOutputV1

        item_update_output = item_batch_output.item_updates[0]  # type: ItemUpdateOutputV1
        if item_update_output.error_message is not None:
            raise RuntimeError('Could not push condition "%s": %s' %
                               (self.definition['Name'], item_update_output.error_message))

        self._set_ui_config(item_update_output.item.id)

        item_map[self.id.upper()] = item_update_output.item.id.upper()

        return item_update_output.item


class CalculatedScalar(CalculatedItem):
    def _pull(self, item_id):
        super()._pull(item_id)
        scalars_api = ScalarsApi(_login.client)
        calculated_item_output = scalars_api.get_scalar(id=item_id)  # type: CalculatedItemOutputV1
        self._pull_formula_based_item(calculated_item_output)

    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None, override_max_interp=False,
             scope_globals_to_workbook=False):
        item = self._check_for_reference_item(pushed_workbook_id, datasource_maps, item_map)
        if item:
            return item

        scalars_api = ScalarsApi(_login.client)
        items_api = ItemsApi(_login.client)

        item_output = self._find(label, pushed_workbook_id)

        scalar_input = self._create_calculated_item_input(
            ScalarInputV1, item_map,
            pushed_workbook_id, scope_globals_to_workbook)  # type: ScalarInputV1

        if item_output is None:
            datasource_class = _common.DEFAULT_DATASOURCE_CLASS
            datasource_id = _common.DEFAULT_DATASOURCE_ID
            scalar_input.data_id = self._construct_data_id(label)
            item_batch_output = scalars_api.put_scalars(
                body=PutScalarsInputV1(datasource_class=datasource_class,
                                       datasource_id=datasource_id,
                                       scalars=[scalar_input]))  # type: ItemBatchOutputV1

            item_update_output = item_batch_output.item_updates[0]  # type: ItemUpdateOutputV1
            if item_update_output.error_message is not None:
                raise RuntimeError('Could not push scalar "%s": %s' %
                                   (self.definition['Name'], item_update_output.error_message))

            self._set_ui_config(item_update_output.item.id)
            item_map[self.id.upper()] = item_update_output.item.id.upper()

            return item_update_output.item

        else:
            # There is no easy way to update a Scalar by its ID, so we have to use ItemsApi
            items_api.set_formula(id=item_output.id, body=FormulaInputV1(formula=scalar_input.formula,
                                                                         parameters=scalar_input.parameters))
            if scalar_input.scoped_to:
                items_api.set_scope(id=item_output.id, workbook_id=scalar_input.scoped_to)
            else:
                items_api.set_scope(id=item_output.id)
            props = [ScalarPropertyV1(name='Name', value=scalar_input.name)]
            if 'Definition' in self:
                props.append(ScalarPropertyV1(name='Description', value=scalar_input.description))
            if 'Number Format' in self:
                props.append(ScalarPropertyV1(name='Number Format', value=scalar_input.number_format))
            items_api.set_properties(id=item_output.id, body=props)
            self._set_ui_config(item_output.id)
            item_map[self.id.upper()] = item_output.id

            return item_output


class Chart(CalculatedItem):
    def _pull(self, item_id):
        super()._pull(item_id)
        formulas_api = FormulasApi(_login.client)
        calculated_item_output = formulas_api.get_function(id=item_id)  # type: CalculatedItemOutputV1

        self._pull_formula_based_item(calculated_item_output)

        if 'FormulaParameters' in self.definition:
            # Charts have these superfluous properties
            del self.definition['FormulaParameters']

    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None,
             override_max_interp=False, scope_globals_to_workbook=False):
        item = self._check_for_reference_item(pushed_workbook_id, datasource_maps, item_map)
        if item:
            return item

        formulas_api = FormulasApi(_login.client)
        items_api = ItemsApi(_login.client)

        item_output = self._find(label, pushed_workbook_id)

        function_input = FunctionInputV1()
        function_input.name = self.definition['Name']
        function_input.type = self.definition['Type']
        function_input.formula = Item.formula_string_from_list(self.definition['Formula'])
        function_input.parameters = list()
        for parameter_name, parameter_id in self.definition['Formula Parameters'].items():
            if _common.is_guid(parameter_id):
                if parameter_id not in item_map:
                    raise DependencyNotFound(parameter_id)

                function_input.parameters.append(FormulaParameterInputV1(name=parameter_name,
                                                                         id=item_map[parameter_id.upper()]))
            else:
                function_input.parameters.append(FormulaParameterInputV1(name=parameter_name,
                                                                         formula=parameter_id,
                                                                         unbound=True))

        if 'Description' in self.definition:
            function_input.description = self.definition['Description']

        function_input.scoped_to = pushed_workbook_id
        function_input.data_id = self._construct_data_id(label)

        if item_output is None:
            calculated_item_output = formulas_api.create_function(body=function_input)  # type: CalculatedItemOutputV1

            items_api.set_properties(
                id=calculated_item_output.id,
                body=[ScalarPropertyV1(name='Datasource Class', value=_common.DEFAULT_DATASOURCE_CLASS),
                      ScalarPropertyV1(name='Datasource ID', value=_common.DEFAULT_DATASOURCE_ID),
                      ScalarPropertyV1(name='Data ID', value=function_input.data_id)])
        else:
            calculated_item_output = formulas_api.update_function(id=item_output.id,
                                                                  body=function_input)  # type: CalculatedItemOutputV1

        self._set_ui_config(calculated_item_output.id)

        item_map[self.id.upper()] = calculated_item_output.id.upper()

        return calculated_item_output


class ThresholdMetric(CalculatedItem):
    def _pull(self, item_id):
        super()._pull(item_id)
        metrics_api = MetricsApi(_login.client)
        metric = metrics_api.get_metric(id=item_id)  # type: ThresholdMetricOutputV1

        formula_parameters = dict()
        if metric.aggregation_function is not None:
            formula_parameters['Aggregation Function'] = metric.aggregation_function
        if metric.bounding_condition is not None:
            formula_parameters['Bounding Condition'] = metric.bounding_condition.id
        if metric.bounding_condition_maximum_duration is not None:
            formula_parameters['Bounding Condition Maximum Duration'] = \
                Item._dict_from_scalar_value_output(metric.bounding_condition_maximum_duration)
        if metric.duration is not None:
            formula_parameters['Duration'] = Item._dict_from_scalar_value_output(metric.duration)
        if metric.measured_item is not None:
            formula_parameters['Measured Item'] = metric.measured_item.id
        if metric.measured_item_maximum_duration is not None:
            formula_parameters['Measured Item Maximum Duration'] = \
                Item._dict_from_scalar_value_output(metric.measured_item_maximum_duration)
        if hasattr(metric, 'number_format') and metric.number_format is not None:
            formula_parameters['Number Format'] = metric.number_format
        if metric.period is not None:
            formula_parameters['Period'] = Item._dict_from_scalar_value_output(metric.period)
        if metric.process_type is not None:
            formula_parameters['Process Type'] = metric.process_type

        def _add_thresholds(_thresholds_name, _threshold_output_list):
            formula_parameters[_thresholds_name] = list()
            for threshold in _threshold_output_list:  # type: ThresholdOutputV1
                threshold_dict = dict()
                if threshold.priority is not None:
                    priority = threshold.priority  # type: PriorityV1
                    threshold_dict['Priority'] = {
                        'Name': priority.name,
                        'Level': priority.level,
                        'Color': priority.color
                    }

                if not threshold.is_generated and threshold.item:
                    threshold_dict['Item ID'] = threshold.item.id

                if threshold.value is not None:
                    if isinstance(threshold.value, ScalarValueOutputV1):
                        threshold_dict['Value'] = Item._dict_from_scalar_value_output(threshold.value)
                    else:
                        threshold_dict['Value'] = threshold.value

                formula_parameters[_thresholds_name].append(threshold_dict)

        if metric.thresholds:
            _add_thresholds('Thresholds', metric.thresholds)

        # These properties come through in the GET /items/{id} call, and for clarity's sake we remove them
        for ugly_duplicate_property in ['AggregationFunction', 'BoundingConditionMaximumDuration',
                                        'MeasuredItemMaximumDuration']:
            if ugly_duplicate_property in self.definition:
                del self.definition[ugly_duplicate_property]

        self.definition['Formula'] = '<ThresholdMetric>'
        self.definition['Formula Parameters'] = formula_parameters

    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None, override_max_interp=False,
             scope_globals_to_workbook=False):
        item = self._check_for_reference_item(pushed_workbook_id, datasource_maps, item_map)
        if item:
            return item

        items_api = ItemsApi(_login.client)
        metrics_api = MetricsApi(_login.client)

        parameters = self['Formula Parameters']

        new_item = ThresholdMetricInputV1()
        new_item.name = self.name
        new_item.scoped_to = pushed_workbook_id

        def _add_scalar_value(_attr, _key):
            if _common.present(parameters, _key):
                setattr(new_item, _attr, Item._str_from_scalar_value_dict(parameters[_key]))

        def _add_mapped_item(_attr, _key):
            if _common.present(parameters, _key):
                if parameters[_key] not in item_map:
                    raise DependencyNotFound(parameters[_key])

                setattr(new_item, _attr, item_map[parameters[_key].upper()])

        def _add_thresholds(_list, _key):
            if not _common.present(parameters, _key):
                return

            for threshold_dict in parameters[_key]:
                threshold_value = _common.get(threshold_dict, 'Value')
                if threshold_value is not None:
                    if isinstance(threshold_value, dict):
                        _list.append('%s=%s' % (threshold_dict['Priority']['Level'],
                                                Item._str_from_scalar_value_dict(threshold_value)))
                    else:
                        _list.append('%s=%s' % (threshold_dict['Priority']['Level'], threshold_value))
                elif _common.present(threshold_dict, 'Item ID'):
                    if threshold_dict['Item ID'] not in item_map:
                        raise DependencyNotFound(threshold_dict['Item ID'])

                    _list.append('%s=%s' % (threshold_dict['Priority']['Level'],
                                            item_map[threshold_dict['Item ID'].upper()]))

        new_item.aggregation_function = _common.get(parameters, 'Aggregation Function')

        _add_mapped_item('bounding_condition', 'Bounding Condition')
        _add_scalar_value('bounding_condition_maximum_duration', 'Bounding Condition Maximum Duration')
        _add_scalar_value('duration', 'Duration')
        _add_mapped_item('measured_item', 'Measured Item')
        _add_scalar_value('measured_item_maximum_duration', 'Measured Item Maximum Duration')
        new_item.number_format = _common.get(parameters, 'Number Format')
        _add_scalar_value('period', 'Period')

        new_item.thresholds = list()
        _add_thresholds(new_item.thresholds, 'Thresholds')

        item_output = self._find(label, pushed_workbook_id)

        while True:
            try:
                if item_output is None:
                    threshold_metric_output = metrics_api.create_threshold_metric(
                        body=new_item)  # type: ThresholdMetricOutputV1

                    items_api.set_properties(
                        id=threshold_metric_output.id,
                        body=[ScalarPropertyV1(name='Datasource Class', value=_common.DEFAULT_DATASOURCE_CLASS),
                              ScalarPropertyV1(name='Datasource ID', value=_common.DEFAULT_DATASOURCE_ID),
                              ScalarPropertyV1(name='Data ID', value=self._construct_data_id(label))])
                else:
                    threshold_metric_output = metrics_api.put_threshold_metric(
                        id=item_output.id,
                        body=new_item)  # type: ThresholdMetricOutputV1

                break

            except ApiException as e:
                # We have to handle a case where a condition on which a metric depends has been changed from bounded
                # to unbounded. In the UI, it automatically fills in the default of 40h when you edit such a metric,
                # so we do roughly the same thing here. This is tested by test_push.test_bad_metric().
                exception_text = _common.format_exception(e)
                if 'Maximum Capsule Duration for Measured Item must be provided' in exception_text:
                    new_item.measured_item_maximum_duration = '40h'
                elif 'Maximum Capsule Duration for Bounding Condition must be provided' in exception_text:
                    new_item.bounding_condition_maximum_duration = '40h'
                else:
                    raise

        self._set_ui_config(threshold_metric_output.id)

        item_map[self.id.upper()] = threshold_metric_output.id.upper()

        return threshold_metric_output
