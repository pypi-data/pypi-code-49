import copy
import json
import glob
import os

from . import _item
from . import _search
from ._data import Datasource, StoredOrCalculatedItem
from ._item import Item, Reference
from ._folder import Folder
from ._worksheet import Worksheet, AnalysisWorksheet, TopicDocument
from ._user import ItemWithOwnerAndAcl

from .. import _common
from .. import _config
from .. import _login
from .._common import Status

from seeq.base import system
from seeq.sdk import *
from seeq.sdk.rest import ApiException


class ItemJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Item):
            return o.definition
        else:
            return o


class Workbook(ItemWithOwnerAndAcl):
    def __new__(cls, *args, **kwargs):
        if cls is Workbook:
            raise TypeError("Workbook may not be instantiated directly, create either Analysis or Topic")

        return object.__new__(cls)

    def __init__(self, definition=None, *, status=None):
        if isinstance(definition, str):
            definition = {'Name': definition}

        super().__init__(definition)

        self.status = Status.validate(status)
        self.item_inventory = dict()
        self.item_errors = set()
        self.worksheets = list()
        self.datasource_maps = list()
        self.scoped_items = None
        self.datasource_inventory = dict()
        if 'Workbook Type' not in self.definition:
            self.definition['Workbook Type'] = self.__class__.__name__
        if 'Data' not in self.definition:
            self.definition['Data'] = dict() if self['Workbook Type'] == 'Analysis' else {'isReportBinder': True}
        if 'Name' not in self.definition:
            self.definition['Name'] = _common.DEFAULT_WORKBOOK_NAME

    @property
    def url(self):
        # Note that 'URL' won't be filled in if a workbook/worksheet hasn't been pushed/pulled. That's because the
        # IDs may change from the placeholders that get generated.
        return self['URL']

    @property
    def path(self):
        if 'Ancestors' not in self:
            return ''

        return _common.path_list_to_string(self.item_inventory[folder_id].name for folder_id in self['Ancestors'])

    @property
    def item_errors_str(self):
        return '\n'.join(['%s: %s' % (_it, _str) for _it, _str in self.item_errors])

    def update_status(self, result, count_increment):
        if self.status.current_df_index is None and len(self.status.df) == 0:
            self.status.df.at[0, :] = None
            self.status.current_df_index = 0
        current_count = self.status.get('Count') if \
            'Count' in self.status.df and self.status.get('Count') is not None else 0
        self.status.put('Count', current_count + count_increment)
        self.status.put('Time', self.status.get_timer())
        self.status.put('Result', result)

        self.status.update('[%d/%d] Processing %s "%s"' %
                           (len(self.status.df[self.status.df['Result'] != 'Queued']),
                            len(self.status.df), self['Workbook Type'], self['Name']),
                           Status.RUNNING)

    def refresh_from(self, new_item, item_map):
        super().refresh_from(new_item, item_map)

        for worksheet in self.worksheets:
            new_worksheet_id = item_map[worksheet.id]
            new_worksheet_list = [w for w in new_item.worksheets if w.id == new_worksheet_id]
            if len(new_worksheet_list) == 1:
                worksheet.refresh_from(new_worksheet_list[0], item_map)

        new_inventory = new_item.item_inventory.copy()
        for inventory_item_id, inventory_item in self.item_inventory.copy().items():
            if inventory_item_id not in item_map:
                if inventory_item.type == 'Folder':
                    # Folders may not have been pushed (depending on spy.workbooks.push arguments) and therefore won't
                    # be in the map, so skip them.
                    continue

                raise RuntimeError('Item "%s" not found in item_map' % inventory_item)

            new_inventory_item_id = item_map[inventory_item_id]
            new_inventory_item = new_inventory[new_inventory_item_id]
            inventory_item.refresh_from(new_inventory_item, item_map)
            del self.item_inventory[inventory_item_id]
            self.item_inventory[new_inventory_item_id] = inventory_item

        # Transfer the remaining (new) inventory over. This often includes new folders.
        for new_inventory_item_id, new_inventory_item in new_inventory.items():
            if new_inventory_item_id not in self.item_inventory:
                self.item_inventory[new_inventory_item_id] = new_inventory_item

        self.datasource_maps = self.datasource_maps

    @staticmethod
    def _instantiate(definition=None, status=None):
        if 'Data' not in definition or _common.get_workbook_type(definition['Data']) == 'Analysis':
            return Analysis(definition, status=status)
        else:
            return Topic(definition, status=status)

    @staticmethod
    def pull(item_id, *, status=None, extra_workstep_tuples=None, include_inventory=True):
        definition = Item._dict_from_id(item_id)
        workbook = Workbook._instantiate(definition, status)
        workbook._pull(workbook.id, extra_workstep_tuples=extra_workstep_tuples,
                       include_inventory=include_inventory)
        return workbook

    def _pull(self, workbook_id=None, extra_workstep_tuples=None, include_inventory=True):
        if workbook_id is None:
            workbook_id = self.id
        workbooks_api = WorkbooksApi(_login.client)
        workbook_output = workbooks_api.get_workbook(id=workbook_id)  # type: WorkbookOutputV1

        self.definition['Path'] = _common.path_list_to_string([a.name for a in workbook_output.ancestors])
        self.definition['Workbook Type'] = _common.get_workbook_type(workbook_output.data)

        self.provenance = Item.PULL

        self._pull_owner_and_acl(workbook_output.owner.id)
        self._pull_ancestors(workbook_output.ancestors)

        self.update_status('Pulling workbook', 1)

        self.definition['Data'] = json.loads(workbook_output.data)
        if 'workbookState' in self.definition:
            self.definition['workbookState'] = json.loads(self.definition['workbookState'])
        self.definition['Original Server URL'] = _item.get_canonical_server_url()

        self.worksheets = list()

        worksheet_ids = Workbook._pull_worksheet_ids(workbook_id)

        if extra_workstep_tuples:
            for workbook_id, worksheet_id, workstep_id in extra_workstep_tuples:
                if workbook_id == self.id and worksheet_id not in worksheet_ids:
                    worksheet_ids.append(worksheet_id)

        for worksheet_id in worksheet_ids:
            self.update_status('Pulling worksheets', 0)
            Worksheet.pull(worksheet_id, workbook=self, extra_workstep_tuples=extra_workstep_tuples)
            self.update_status('Pulling worksheets', 1)

        self['URL'] = None
        if len(self.worksheets) > 0:
            link_url = '%s/%sworkbook/%s/worksheet/%s' % (
                _config.get_api_url().replace('/api', ''),
                (self['Ancestors'][-1] + '/') if len(self['Ancestors']) > 0 else '',
                workbook_id,
                self.worksheets[0].id
            )
            self['URL'] = link_url

        self.item_inventory = dict()
        if include_inventory:
            self._scrape_item_inventory()
            self._scrape_datasource_inventory()
            self._construct_default_datasource_maps()
        else:
            # Need to at least scrape folders so we know what the path is
            self._scrape_folder_inventory()

    @staticmethod
    def _pull_worksheet_ids(workbook_id):
        workbooks_api = WorkbooksApi(_login.client)

        offset = 0
        limit = 1000
        worksheet_ids = list()
        while True:
            worksheet_output_list = workbooks_api.get_worksheets(
                workbook_id=workbook_id,
                offset=offset,
                limit=limit)  # type: WorksheetOutputListV1

            for worksheet_output in worksheet_output_list.worksheets:  # type: WorksheetOutputV1
                worksheet_ids.append(worksheet_output.id)

            if len(worksheet_output_list.worksheets) < limit:
                break

            offset = offset + limit

        return worksheet_ids

    def _find_by_name(self, folder_id):
        workbooks_api = WorkbooksApi(_login.client)
        if folder_id is not None and folder_id != _common.PATH_ROOT:
            folders = _search.get_folders(content_filter='owner', folder_id=folder_id)
        else:
            folders = _search.get_folders(content_filter='owner')

        for content in folders['content']:
            if content['name'].lower() == self.name.lower() and \
                    content['type'] == 'Workbook' and \
                    _common.get_workbook_type(content['data']) == self.definition['Workbook Type']:
                return workbooks_api.get_workbook(id=content['id'])

        return None

    def push(self, *, owner=None, folder_id=None, item_map=None, label=None,
             access_control=None, override_max_interp=False, include_inventory=True,
             scope_globals_to_workbook=False, status=None):
        self.status = Status.validate(status)

        if len(self.worksheets) == 0:
            raise ValueError('Workbook %s must have at least one worksheet before pushing' % self)

        workbook_item = self.find_me(label)

        if workbook_item is None and self.provenance == Item.CONSTRUCTOR:
            workbook_item = self._find_by_name(folder_id)

        workbooks_api = WorkbooksApi(_login.client)
        items_api = ItemsApi(_login.client)
        datasources_api = DatasourcesApi(_login.client)

        datasource_input = _common.get_data_lab_datasource_input()
        datasources_api.create_datasource(body=datasource_input)

        props = list()
        existing_worksheet_identifiers = dict()

        if not workbook_item:
            workbook_input = WorkbookInputV1()
            workbook_input.name = self.definition['Name']
            workbook_input.description = _common.get(self.definition, 'Description')
            workbook_input.folder_id = folder_id if folder_id != _common.PATH_ROOT else None
            workbook_input.owner_id = self.decide_owner(self.datasource_maps, item_map, owner=owner)
            if 'Data' in self.definition:
                workbook_input.data = json.dumps(self.definition['Data'])
            elif self['Workbook Type'] == 'Topic':
                workbook_input.data = '{"isReportBinder":true}'
            else:
                workbook_input.data = '{}'
            workbook_input.branch_from = _common.get(self.definition, 'Branch From')
            workbook_output = workbooks_api.create_workbook(body=workbook_input)  # type: WorkbookOutputV1

            items_api.set_properties(id=workbook_output.id, body=[
                ScalarPropertyV1(name='Datasource Class', value=_common.DEFAULT_DATASOURCE_CLASS),
                ScalarPropertyV1(name='Datasource ID', value=_common.DEFAULT_DATASOURCE_ID),
                ScalarPropertyV1(name='Data ID', value=self._construct_data_id(label)),
                ScalarPropertyV1(name='workbookState', value=_common.DEFAULT_WORKBOOK_STATE)])

        else:
            workbook_output = workbooks_api.get_workbook(id=workbook_item.id)  # type: WorkbookOutputV1

            # If the workbook happens to be archived, un-archive it. If you're pushing a new copy it seems likely
            # you're intending to revive it.
            items_api.set_properties(id=workbook_output.id, body=[ScalarPropertyV1(name='Archived', value=False)])

            for is_archived in [False, True]:
                offset = 0
                limit = 1000
                while True:
                    worksheet_output_list = workbooks_api.get_worksheets(workbook_id=workbook_output.id,
                                                                         is_archived=is_archived,
                                                                         offset=offset,
                                                                         limit=limit)  # type: WorksheetOutputListV1

                    for worksheet_output in worksheet_output_list.worksheets:  # type: WorksheetOutputV1
                        item_output = items_api.get_item_and_all_properties(
                            id=worksheet_output.id)  # type: ItemOutputV1
                        data_id = [p.value for p in item_output.properties if p.name == 'Data ID']
                        if len(data_id) == 0:
                            continue

                        existing_worksheet_identifiers[worksheet_output.id] = worksheet_output.id
                        existing_worksheet_identifiers[data_id[0]] = worksheet_output.id
                        existing_worksheet_identifiers[worksheet_output.name] = worksheet_output.id

                    if len(worksheet_output_list.worksheets) < limit:
                        break

                    offset = offset + limit

            owner_id = self.decide_owner(self.datasource_maps, item_map, owner=owner,
                                         current_owner_id=workbook_output.owner.id)

            self._push_owner_and_location(workbook_output, owner_id, folder_id)

        self.status.put('Pushed Workbook ID', workbook_output.id)

        if item_map is None:
            item_map = dict()

        item_map[self.id.upper()] = workbook_output.id.upper()

        if access_control:
            self._push_acl(workbook_output.id, self.datasource_maps, item_map, access_control)

        if include_inventory:
            self._push_inventory(item_map, label, override_max_interp, scope_globals_to_workbook, workbook_output)

        props.append(ScalarPropertyV1(name='Name', value=self.definition['Name']))
        if _common.present(self.definition, 'Description'):
            props.append(ScalarPropertyV1(name='Description', value=self.definition['Description']))
        if _common.present(self.definition, 'Data'):
            props.append(ScalarPropertyV1(name='Data', value=json.dumps(self.definition['Data'])))
        if _common.present(self.definition, 'workbookState'):
            props.append(ScalarPropertyV1(name='workbookState', value=json.dumps(self.definition['workbookState'])))

        items_api.set_properties(id=workbook_output.id, body=props)

        if len(set(self.worksheets)) != len(self.worksheets):
            raise ValueError('Worksheet list within Workbook "%s" is not unique: %s' % (self, self.worksheets))

        first_worksheet_id = None
        for worksheet in self.worksheets:
            self.update_status('Pushing worksheet', 1)
            worksheet_output = worksheet.push(workbook_output.id, item_map, existing_worksheet_identifiers,
                                              include_inventory, label=label)
            if first_worksheet_id is None:
                first_worksheet_id = worksheet_output.id

        # Pull the set of worksheets and re-order them
        remaining_pushed_worksheet_ids = Workbook._pull_worksheet_ids(workbook_output.id)
        next_worksheet_id = None
        for worksheet in reversed(self.worksheets):
            pushed_worksheet_id = item_map[worksheet.id]
            if next_worksheet_id is None:
                workbooks_api.move_worksheet(workbook_id=workbook_output.id, worksheet_id=pushed_worksheet_id)
            else:
                workbooks_api.move_worksheet(workbook_id=workbook_output.id, worksheet_id=pushed_worksheet_id,
                                             next_worksheet_id=item_map[next_worksheet_id])

            if pushed_worksheet_id in remaining_pushed_worksheet_ids:
                remaining_pushed_worksheet_ids.remove(pushed_worksheet_id)

            next_worksheet_id = worksheet.id

        # Archive any worksheets that are no longer active
        for remaining_pushed_worksheet_id in remaining_pushed_worksheet_ids:
            items_api.set_property(id=remaining_pushed_worksheet_id, property_name='Archived',
                                   body=PropertyInputV1(value=True))

        # Now go back through all the worksheets to see if any worksteps weren't resolved
        dependencies_not_found = set()
        for worksheet in self.worksheets:
            for workstep_tuple in worksheet.referenced_worksteps:
                referenced_workbook_id, referenced_worksheet_id, referenced_workstep_id = workstep_tuple
                if referenced_workstep_id not in item_map:
                    dependencies_not_found.add(
                        'Workbook %s, Worksheet %s, Workstep %s' % (
                            referenced_workbook_id, referenced_worksheet_id, referenced_workstep_id))

        if first_worksheet_id is not None:
            link_url = '%s/%sworkbook/%s/worksheet/%s' % (
                _config.get_api_url().replace('/api', ''),
                (folder_id + '/') if folder_id is not None else '',
                workbook_output.id,
                first_worksheet_id
            )
            self.status.put('URL', link_url)

        if len(dependencies_not_found) > 0:
            raise _common.DependencyNotFound(None, '\n'.join(dependencies_not_found))

        self.status.update('Success', Status.SUCCESS)
        return workbook_output

    def _push_inventory(self, item_map, label, override_max_interp, scope_globals_to_workbook, workbook_output):
        remaining_inventory = dict(self.item_inventory)
        while len(remaining_inventory) > 0:
            at_least_one_thing_pushed = False
            dependencies_not_found = list()
            dict_iterator = dict(remaining_inventory)
            for item_id, item in dict_iterator.items():
                if item['Type'] in ['Folder']:
                    at_least_one_thing_pushed = True
                    del remaining_inventory[item_id]
                    continue

                # noinspection PyBroadException
                try:
                    item.push(self.datasource_maps,
                              pushed_workbook_id=workbook_output.id, item_map=item_map,
                              label=label, override_max_interp=override_max_interp,
                              scope_globals_to_workbook=scope_globals_to_workbook)
                    self.update_status('Pushing item inventory', 1)
                    at_least_one_thing_pushed = True
                    del remaining_inventory[item_id]
                except _common.DependencyNotFound as e:
                    dependencies_not_found.append(e.identifier)
                except KeyboardInterrupt:
                    raise
                except BaseException:
                    self.item_errors.add((item, _common.format_exception()))

            if not at_least_one_thing_pushed:
                for dependency_not_found in dependencies_not_found:
                    self.item_errors.add((dependency_not_found, 'Not found (dependency)'))
                for remaining_item in remaining_inventory.values():
                    self.item_errors.add((remaining_item, 'Not able to push'))
                break

    def push_containing_folders(self, item_map, use_full_path, parent_folder_id, owner, label, access_control):
        if 'Ancestors' not in self:
            return parent_folder_id

        keep_skipping = parent_folder_id in self['Ancestors']
        create_folders_now = False

        for ancestor_id in self['Ancestors']:
            if keep_skipping and parent_folder_id == ancestor_id:
                keep_skipping = False
                continue

            if use_full_path or 'Search Folder ID' not in self:
                create_folders_now = True

            if create_folders_now:
                if ancestor_id in self.item_inventory:
                    folder = self.item_inventory[ancestor_id]  # type: Folder
                    parent_folder = folder.push(parent_folder_id, self.datasource_maps, item_map,
                                                owner=owner, label=label, access_control=access_control)
                    parent_folder_id = parent_folder.id
            elif self['Search Folder ID'] == ancestor_id:
                create_folders_now = True

        return parent_folder_id

    @property
    def referenced_items(self):
        referenced_items = list()
        for worksheet in self.worksheets:
            referenced_items.extend(worksheet.referenced_items)

        if self.scoped_items is not None:
            referenced_items.extend(self.scoped_items)

        return referenced_items

    @property
    def referenced_workbooks(self):
        references = dict()
        for worksheet in self.worksheets:
            for (workbook_id, worksheet_id, workstep_id) in worksheet.referenced_worksteps:
                if workbook_id not in references:
                    references[workbook_id] = set()

                references[workbook_id].add((workbook_id, worksheet_id, workstep_id))

        return references

    def find_workbook_links(self):
        # This should only be called during a pull operation, because it requires a connection to the original
        # database in order to resolve the workbook in a view-only link. (See Annotation class.)
        links = dict()
        for worksheet in self.worksheets:
            links.update(worksheet.find_workbook_links())

        return links

    def push_fixed_up_workbook_links(self, item_map):
        for worksheet in self.worksheets:
            worksheet.push_fixed_up_workbook_links(item_map)

    def _get_default_workbook_folder(self):
        return os.path.join(os.getcwd(), 'Workbook_%s' % self.id)

    @staticmethod
    def _get_workbook_json_file(workbook_folder):
        return os.path.join(workbook_folder, 'Workbook.json')

    @staticmethod
    def _get_items_json_file(workbook_folder):
        return os.path.join(workbook_folder, 'Items.json')

    @staticmethod
    def _get_datasources_json_file(workbook_folder):
        return os.path.join(workbook_folder, 'Datasources.json')

    @staticmethod
    def _get_datasource_map_json_file(workbook_folder, datasource_map):
        return os.path.join(
            workbook_folder, system.cleanse_filename(
                'Datasource_Map_%s_%s_%s.json' % (datasource_map['Datasource Class'],
                                                  datasource_map['Datasource ID'],
                                                  datasource_map['Datasource Name'])))

    def save(self, workbook_folder=None, overwrite=False):
        if not workbook_folder:
            workbook_folder = self._get_default_workbook_folder()

        if os.path.exists(workbook_folder):
            if overwrite:
                system.removetree(workbook_folder, keep_top_folder=True)
            else:
                raise RuntimeError('"%s" folder exists, use clean=True argument to overwrite it' %
                                   workbook_folder)

        os.makedirs(workbook_folder, exist_ok=True)

        workbook_json_file = Workbook._get_workbook_json_file(workbook_folder)

        definition_dict = dict(self.definition)
        definition_dict['Worksheets'] = list()
        for worksheet in self.worksheets:
            worksheet.save(workbook_folder)
            definition_dict['Worksheets'].append(worksheet.id)

        with open(workbook_json_file, 'w', encoding='utf-8') as f:
            json.dump(definition_dict, f, indent=4)

        items_json_file = Workbook._get_items_json_file(workbook_folder)
        with open(items_json_file, 'w', encoding='utf-8') as f:
            json.dump(self.item_inventory, f, indent=4, sort_keys=True, cls=ItemJSONEncoder)

        datasources_json_file = Workbook._get_datasources_json_file(workbook_folder)
        with open(datasources_json_file, 'w', encoding='utf-8') as f:
            json.dump(self.datasource_inventory, f, indent=4, sort_keys=True, cls=ItemJSONEncoder)

        for datasource_map in self.datasource_maps:
            datasource_map_file = Workbook._get_datasource_map_json_file(workbook_folder, datasource_map)
            with open(datasource_map_file, 'w', encoding='utf-8') as f:
                json.dump(datasource_map, f, indent=4)

    @staticmethod
    def load(workbook_folder):
        if not os.path.exists(workbook_folder):
            raise RuntimeError('Workbook folder "%s" does not exist' % workbook_folder)

        workbook_json_file = Workbook._get_workbook_json_file(workbook_folder)
        if not os.path.exists(workbook_json_file):
            raise RuntimeError('Workbook JSON file "%s" does not exist' % workbook_json_file)

        with open(workbook_json_file, 'r', encoding='utf-8') as f:
            definition = json.load(f)

        workbook = Workbook._instantiate(definition)
        workbook._load(workbook_folder)

        return workbook

    def _load(self, workbook_folder):
        self.provenance = Item.LOAD

        self.worksheets = list()
        for worksheet_id in self.definition['Worksheets']:
            Worksheet.load_from_workbook_folder(self, workbook_folder, worksheet_id)

        del self.definition['Worksheets']

        self.item_inventory = Workbook._load_inventory(Workbook._get_items_json_file(workbook_folder))
        for scope_item in self.item_inventory.values():
            scope_item.scoped_to = self

        self.datasource_inventory = Workbook._load_inventory(Workbook._get_datasources_json_file(workbook_folder))
        self.datasource_maps = Workbook.load_datasource_maps(workbook_folder)

    @staticmethod
    def load_datasource_maps(folder):
        if not os.path.exists(folder):
            raise ValueError('Datasource map folder "%s" does not exist' % folder)

        datasource_map_files = glob.glob(os.path.join(folder, 'Datasource_Map_*.json'))
        datasource_maps = list()
        for datasource_map_file in datasource_map_files:
            with open(datasource_map_file, 'r', encoding='utf-8') as f:
                datasource_maps.append(json.load(f))

        return datasource_maps

    @staticmethod
    def _load_inventory(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            loaded_inventory = json.load(f)

        inventory_dict = dict()
        for item_id, item_def in loaded_inventory.items():
            inventory_dict[item_id] = Item.load(item_def)

        return inventory_dict

    def _scrape_datasource_inventory(self):
        referenced_datasources = self._scrape_auth_datasources()
        for item in self.item_inventory.values():  # type: Item
            referenced_datasources.update(item._scrape_auth_datasources())
            if 'Datasource Class' in item and 'Datasource ID' in item:
                referenced_datasources.add((item['Datasource Class'], item['Datasource ID']))

        self.datasource_inventory = dict()
        for datasource_class, datasource_id in referenced_datasources:
            datasource = Datasource.from_datasource_id(datasource_class, datasource_id)
            self.datasource_inventory[datasource.id] = datasource

        return self.datasource_inventory

    def _construct_default_datasource_maps(self):
        self.datasource_maps = list()
        for _id, datasource in self.datasource_inventory.items():
            datasource_map = {
                'Datasource Class': datasource['Datasource Class'],
                'Datasource ID': datasource['Datasource ID'],
                'Datasource Name': datasource['Name'],
                'Item-Level Map Files': list(),
                'RegEx-Based Maps': [
                    {
                        'Old': {
                            'Type': r'(?<type>.*)',
                            'Datasource Class': datasource['Datasource Class'],
                            'Datasource Name': datasource['Name']
                        },
                        'New': {
                            'Type': '${type}',
                            'Datasource Class': datasource['Datasource Class'],
                            'Datasource Name': datasource['Name']
                        }
                    }
                ]
            }

            if datasource['Datasource Class'] in ['Auth', 'Windows Auth', 'LDAP', 'OAuth 2.0']:
                datasource_map['RegEx-Based Maps'].append(copy.deepcopy(datasource_map['RegEx-Based Maps'][0]))

                datasource_map['RegEx-Based Maps'][0]['Old']['Type'] = 'User'
                datasource_map['RegEx-Based Maps'][0]['Old']['Username'] = r'(?<username>.*)'
                datasource_map['RegEx-Based Maps'][0]['New']['Type'] = 'User'
                datasource_map['RegEx-Based Maps'][0]['New']['Username'] = '${username}'

                datasource_map['RegEx-Based Maps'][1]['Old']['Type'] = 'UserGroup'
                datasource_map['RegEx-Based Maps'][1]['Old']['Name'] = r'(?<name>.*)'
                datasource_map['RegEx-Based Maps'][1]['New']['Type'] = 'UserGroup'
                datasource_map['RegEx-Based Maps'][1]['New']['Name'] = '${name}'
            else:
                datasource_map['RegEx-Based Maps'][0]['Old']['Data ID'] = r'(?<data_id>.*)'
                datasource_map['RegEx-Based Maps'][0]['New']['Data ID'] = '${data_id}'

            self.datasource_maps.append(datasource_map)

    def _scrape_item_inventory(self):
        self._scrape_references_from_scope()

        self._scrape_folder_inventory()

        for reference in self.referenced_items:
            self._scrape_inventory_from_item(reference.id)

        self._scrape_inventory_from_ancillaries()

    def _scrape_folder_inventory(self):
        if 'Ancestors' in self:
            for ancestor_id in self['Ancestors']:
                self.update_status('Scraping folders', 0)

                try:
                    item = Item.pull(ancestor_id, allowed_types=['Folder'])
                except ApiException as e:
                    if e.status == 404:
                        continue

                    raise

                if item is None:
                    continue

                self.update_status('Scraping folders', 1)

                self.add_to_scope(item)

    def _scrape_inventory_from_item(self, item_id):
        if item_id in self.item_inventory:
            return

        allowed_types = [
            'StoredSignal',
            'CalculatedSignal',
            'StoredCondition',
            'CalculatedCondition',
            'CalculatedScalar',
            'Chart',
            'ThresholdMetric',
            'TableDatasource'
        ]

        self.update_status('Scraping item inventory', 0)

        try:
            item = Item.pull(item_id, allowed_types=allowed_types)
        except ApiException as e:
            if e.status == 404:
                return

            raise

        if item is None:
            return

        if 'Is Generated' in item and item['Is Generated']:
            return

        self.update_status('Scraping item inventory', 1)

        self.add_to_scope(item)

        dependencies = self._scrape_references_from_dependencies(item_id)

        for dependency in dependencies:
            if dependency.id in self.item_inventory:
                continue

            self.update_status('Scraping item dependency', 0)

            try:
                dep_item = Item.pull(dependency.id, allowed_types=allowed_types)
            except ApiException as e:
                if e.status == 404:
                    continue

                raise

            if dep_item is None:
                continue

            if 'Is Generated' in dep_item and dep_item['Is Generated']:
                continue

            self.update_status('Scraping item dependency', 1)

            self.add_to_scope(dep_item)

    def _scrape_references_from_scope(self):
        items_api = ItemsApi(_login.client)

        self.update_status('Scraping scope references', 0)

        self.scoped_items = list()
        offset = 0
        while True:
            search_results = items_api.search_items(
                filters=['', '@excludeGloballyScoped'],
                scope=self.id,
                offset=offset,
                limit=_config.options.search_page_size,
            )  # type: ItemSearchPreviewPaginatedListV1

            self.scoped_items.extend([Reference(item.id, Reference.SCOPED) for item in search_results.items])

            if len(search_results.items) < search_results.limit:
                break

            offset += search_results.limit

    def _scrape_references_from_dependencies(self, item_id):
        items_api = ItemsApi(_login.client)
        referenced_items = list()

        self.update_status('Scraping dependencies', 0)

        try:
            dependencies = items_api.get_formula_dependencies(id=item_id)  # type: ItemDependencyOutputV1
        except ApiException as e:
            if e.status == 404:
                # For some reason, the item_id is unknown. We've seen this at Exxon, so just skip it.
                return referenced_items

            raise

        for dependency in dependencies.dependencies:  # type: ItemParameterOfOutputV1
            referenced_items.append(Reference(
                dependency.id,
                Reference.DEPENDENCY
            ))

        return referenced_items

    def _scrape_inventory_from_ancillaries(self):
        self.update_status('Scraping ancillaries', 0)

        current_inventory = list(self.item_inventory.values())
        for item in current_inventory:
            if 'Ancillaries' not in item:
                continue

            for ancillary_dict in item['Ancillaries']:
                if 'Items' not in ancillary_dict:
                    continue

                # Only scrape ancillaries that are globally scoped or scoped to this workbook
                scoped_to = _common.get(ancillary_dict, 'Scoped To')
                if scoped_to is not None and scoped_to != self.id:
                    continue

                for ancillary_item_dict in ancillary_dict['Items']:
                    self._scrape_inventory_from_item(_common.get(ancillary_item_dict, 'ID'))

    def add_to_scope(self, item):
        if not isinstance(item, (StoredOrCalculatedItem, Folder)):
            raise TypeError('Workbook.add_to_scope only accepts Stored or Calculated items. You tried to add:\n%s',
                            item)

        self.item_inventory[item.id] = item

        if not isinstance(item, Folder):
            item.scoped_to = self

    def _get_worksheet(self, name):
        for worksheet in self.worksheets:
            if worksheet.name == name:
                return worksheet

        return None


class Analysis(Workbook):
    def worksheet(self, name, create=True):
        existing_worksheet = self._get_worksheet(name)
        if existing_worksheet:
            return existing_worksheet
        elif not create:
            return None

        return AnalysisWorksheet(self, {'Name': name})


class Topic(Workbook):
    def document(self, name, create=True):
        existing_document = self._get_worksheet(name)
        if existing_document:
            return existing_document
        elif not create:
            return None

        return TopicDocument(self, {'Name': name})
