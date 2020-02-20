from seeq.sdk import *

from ._item import Item
from ._data import StoredItem

from .. import _common
from .. import _login

ORIGINAL_OWNER = '__original__'
FORCE_ME_AS_OWNER = '__me__'


class ItemWithOwnerAndAcl(Item):
    def decide_owner(self, datasource_maps, item_map, *, owner=None, current_owner_id=None):
        requires_admin = True
        if _common.is_guid(owner):
            owner_id = owner
        elif owner is None:
            requires_admin = False
            if current_owner_id is None:
                owner_id = _login.user.id
            else:
                owner_id = current_owner_id
        elif owner == ORIGINAL_OWNER:
            owner_id = Identity.find_identity(self['Owner'], datasource_maps=datasource_maps, item_map=item_map)
        elif owner == FORCE_ME_AS_OWNER:
            owner_id = _login.user.id
        else:
            raise ValueError('Invalid owner: %s' % owner)

        if current_owner_id is None or current_owner_id == owner_id:
            requires_admin = False

        if requires_admin and not _login.user.is_admin:
            raise RuntimeError("Logged in user must be an admin as a result of owner='%s'" % owner)

        return owner_id

    def _pull_owner_and_acl(self, owner_id):
        items_api = ItemsApi(_login.client)

        self['Owner'] = User.pull(owner_id).definition

        acl_output = items_api.get_access_control(id=self['ID'])  # type: AclOutputV1
        access_control = list()

        if acl_output.acl is not None:
            for ace_output in acl_output.acl:  # type: AceOutputV1
                ace_dict = Item._dict_via_attribute_map(ace_output, {
                    'access_level': 'Access Level',
                    'created_at': 'Created At',
                    'id': 'ID'
                })

                if ace_output.identity.type == 'User':
                    identity = User.pull(ace_output.identity.id)
                else:
                    identity = UserGroup.pull(ace_output.identity.id)

                ace_dict['Identity'] = identity.definition
                access_control.append(ace_dict)

        self.definition['Access Control'] = access_control

    def _push_owner_and_location(self, item_output, owner_id, folder_id):
        items_api = ItemsApi(_login.client)
        folders_api = FoldersApi(_login.client)

        if item_output.owner.id != owner_id:
            items_api.change_owner(item_id=item_output.id, new_owner_id=owner_id)

        if folder_id == _common.PATH_ROOT:
            if item_output.parent_folder_id:
                folders_api.remove_item_from_folder(folder_id=item_output.parent_folder_id,
                                                    item_id=item_output.id)
        elif folder_id is not None:
            folders_api.move_item_to_folder(folder_id=folder_id, item_id=item_output.id)

    def _push_acl(self, pushed_id, datasource_maps, item_map, access_control):
        replace = False
        strict = False
        if access_control:
            treatment_parts = access_control.split(',')
            for treatment_part in treatment_parts:
                if treatment_part == 'add':
                    replace = False
                elif treatment_part == 'replace':
                    replace = True
                elif treatment_part == 'loose':
                    strict = False
                elif treatment_part == 'strict':
                    strict = True
                else:
                    raise RuntimeError("access_control argument must be 'add' or 'replace' comma 'loose' or 'strict'. "
                                       "For example: replace,strict")

        if 'Access Control' not in self:
            return

        items_api = ItemsApi(_login.client)
        acl_output = items_api.get_access_control(id=pushed_id)  # type: AclOutputV1
        for acl_to_push in self['Access Control']:
            found = False

            try:
                identity_id = Identity.find_identity(acl_to_push['Identity'], datasource_maps, item_map)
            except _common.DependencyNotFound:
                if strict:
                    raise

                continue

            for existing_acl in acl_output.acl:  # type: AceOutputV1
                if existing_acl.access_level != acl_to_push['Access Level']:
                    continue

                if existing_acl.identity.id != identity_id:
                    continue

                found = True
                setattr(existing_acl, 'used', True)
                break

            if found:
                continue

            items_api.add_access_control_entry(id=pushed_id,
                                               body=AceInputV1(access_level=acl_to_push['Access Level'],
                                                               identity_id=identity_id))

        if replace:
            for existing_acl in acl_output.acl:  # type: AceOutputV1
                if hasattr(existing_acl, 'used') and getattr(existing_acl, 'used'):
                    continue

                items_api.remove_access_control_entry(id=pushed_id, ace_id=existing_acl.id)

    def _pull_ancestors(self, ancestors):
        if ancestors is None:
            return

        self.definition['Ancestors'] = [ancestor.id for ancestor in ancestors]

    def _scrape_auth_datasources(self):
        referenced_datasources = set()

        def _scrape_auth_datasource(d, key):
            if key in d and 'Datasource Class' in d[key] and 'Datasource ID' in d[key]:
                referenced_datasources.add((d[key]['Datasource Class'], d[key]['Datasource ID']))

        _scrape_auth_datasource(self, 'Owner')
        if 'Access Control' in self:
            for acl in self['Access Control']:
                _scrape_auth_datasource(acl, 'Identity')

        return referenced_datasources


class Identity(StoredItem):
    @staticmethod
    def find_identity(identity_dict, datasource_maps, item_map):
        # type: (...) -> str
        if identity_dict['ID'] in item_map:
            return item_map[identity_dict['ID']]

        if identity_dict['Type'] == 'User':
            identity = User(identity_dict)
        else:
            identity = UserGroup(identity_dict)

        pushed_identity = identity.push(datasource_maps=datasource_maps, item_map=item_map)

        return pushed_identity.id

    def pull_datasource(self, identity):
        # noinspection PyBroadException
        try:
            if identity.type == 'User':
                auth_api = AuthApi(_login.client)
                auth_providers_output = auth_api.get_auth_providers()  # type: AuthProvidersOutputV1
                users_api = UsersApi(_login.client)
                user_output = users_api.get_user(id=identity.id)  # type: UserOutputV1

                for auth_provider in auth_providers_output.auth_providers:  # DatasourceOutputV1
                    if auth_provider.name == user_output.datasource_name:
                        self['Datasource Class'] = auth_provider.datasource_class
                        self['Datasource ID'] = auth_provider.datasource_id
                        self['Datasource Name'] = auth_provider.name
                        break
            else:
                # In .45, groups will come from different datasources. For now, hard-code it.
                # user_groups_api = UserGroupsApi(_login.client)
                # user_group_output = user_groups_api.get_user_group(id=identity.id)  # type: UserGroupOutputV1
                self['Datasource Class'] = 'Auth'
                self['Datasource ID'] = 'Seeq'
                self['Datasource Name'] = 'Seeq'
        except KeyboardInterrupt:
            raise
        except BaseException:
            # If we can't get extra data on the user, that's OK
            pass


class User(Identity):
    @staticmethod
    def pull(item_id, *, allowed_types=None, status=None):
        users_api = UsersApi(_login.client)
        user_output = users_api.get_user(id=item_id)  # type: UserOutputV1

        item = User({
            'ID': user_output.id,
            'Type': user_output.type,
            'Name': user_output.name,
            'Username': user_output.username,
            'First Name': user_output.first_name,
            'Last Name': user_output.last_name,
            'Email': user_output.email,
            'Is Admin': user_output.is_admin
        })

        item.pull_datasource(user_output)
        return item


class UserGroup(Identity):
    @staticmethod
    def pull(item_id, *, allowed_types=None, status=None):
        usergroups_api = UserGroupsApi(_login.client)
        usergroup_output = usergroups_api.get_user_group(user_group_id=item_id)  # type: UserGroupOutputV1

        item = UserGroup({
            'ID': usergroup_output.id,
            'Type': usergroup_output.type,
            'Name': usergroup_output.name
        })

        item.pull_datasource(usergroup_output)
        return item
