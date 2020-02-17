import json
import os
import requests
import six

from requests import RequestException
from six.moves.urllib.parse import quote

from DKCloudCommand.modules.DKCloudCommandConfig import DKCloudCommandConfig
from DKCommon.api_utils.DKApiHelper import DKApiHelper
from DKCommon.api_utils.api_utils import validate_and_get_response, get_issue_messages
from DKCommon.Constants import VAULT_GLOBAL
from DKCommon.DKFileEncode import DKFileEncode
from DKCommon.DKPathUtils import (
    normalize,
    normalize_dict_keys,
    normalize_dict_value,
    normalize_get_compiled_file,
    normalize_recipe_dict,
    normalize_recipe_dict_kmp,
    normalize_recipe_validate,
    UNIX,
    WIN,
)
from DKCloudCommand.modules.DKFileHelper import DKFileHelper
from DKCloudCommand.modules.DKRecipeDisk import (
    DKRecipeDisk,
    compare_sha,
    get_directory_sha,
)
from DKCloudCommand.modules.DKReturnCode import DKReturnCode, convert_return_code

__author__ = 'DataKitchen, Inc.'
"""
NOMENCLATURE

Some example files:

abspath
  /tmp/test/simple/description.json
  /tmp/test/simple/resources/cools.sql

Here are what the parts are called:

file_name
    description.json
    cools.sql

recipe_name
  simple

filepath # as known to the user
api_file_key # specifies the file to create/update/delete
             # relative to being in the top recipe directory
             # i.e. file name and path to the file name, relative to the recipe root
             # recipe root = cd /tmp/test/simple
  resources/cool.sql
  cool.sql

recipe_file_key # used as a key to the dictionary
  simple/resources # for cool.sql
  simple # for description.json

recipe_file # location on disk including the recipe name
  simple/resources/cool.sql
  simple/description.json

filedir # the directory portion between the recipe and the file_name
  resources


For the CLI, assume the user has CD to the top of the recipe
e.g.
  cd /var/tmp/test/simple

"""


class DKCloudAPI(object):
    _use_https = False
    DKAPP_KITCHEN_FILE = 'kitchen.json'
    DKAPP_KITCHENS_DIR = 'kitchens'
    MESSAGE = 'message'
    FILEPATH = 'filepath'
    TEMPLATENAME = 'templatename'
    FILE = 'file'
    FILES = 'files'
    FILENAME = 'filename'
    JSON = 'json'
    TEXT = 'text'
    SHA = 'sha'
    LAST_UPDATE_TIME = 'last_update_time'
    DESCRIPTION = 'description'

    def __init__(self, dk_cli_config):
        if isinstance(dk_cli_config, DKCloudCommandConfig):
            self._config = dk_cli_config
            self._role = None
            self._customer_name = None
            self._api_helper = None

    def get_ignore(self):
        return self._config.get_ignore()

    def get_config(self):
        return self._config

    def get_url_for_direct_rest_call(self):
        if self._use_https is False:
            return '%s:%s' % (self._config.get_ip(), self._config.get_port())
        else:
            return "must use http"

    def login(self):
        try:

            url = self.get_url_for_direct_rest_call()

            token = self._config.get_jwt()

            if not token or not DKApiHelper.valid_token(url, token):

                token = DKApiHelper.login(
                    url, self._config.get_username(), self._config.get_password()
                )

                self._config.set_jwt(token)

            self._api_helper = DKApiHelper(url, token)

            return token

        except Exception as e:
            print(str(e))
            return None

    def _get_common_headers(self, one_time_token=None):
        if one_time_token is not None:
            return {'Authorization': 'Bearer %s' % one_time_token}
        else:
            return {'Authorization': 'Bearer %s' % self._config.get_jwt()}

    def get_user_info(self, id_token):
        url = '%s/v2/userinfo' % (self.get_url_for_direct_rest_call())
        try:
            response = requests.get(url, headers=self._get_common_headers(id_token))
        except (RequestException, ValueError, TypeError) as c:
            print("userinfo: exception: %s" % str(c))
            return None

        try:
            parsed_response = validate_and_get_response(response)
        except Exception as e:
            return None

        if response is not None:
            if 'role' in parsed_response:
                self._role = parsed_response['role']
            else:
                self._role = None
                print("role not found in user_info")

            if 'customer_name' in parsed_response:
                self._customer_name = parsed_response['customer_name']
            else:
                self._customer_name = None
                print("customer_name not found in user_info")
            return parsed_response
        else:
            print('userinfo: response is empty')
            return None

    def get_user_role(self):
        if self._role is None:
            id_token = self._config.get_jwt()
            self.get_user_info(id_token)
        return self._role

    def is_user_role(self, role):
        current_role = self.get_user_role()
        if current_role is None or role is None:
            return False
        if current_role != role:
            return False
        return True

    def get_customer_name(self):
        if not self._customer_name:
            id_token = self._config.get_jwt()
            self.get_user_info(id_token)
        return self._customer_name

    def get_merge_dir(self):
        return self._config.get_merge_dir()

    def get_diff_dir(self):
        return self._config.get_diff_dir()

    # implementation ---------------------------------
    @staticmethod
    def rude():
        return '**rude**'

    # It looks like this is only called from TestCloudAPI.py.  Consider moving this function
    # return kitchen dict
    def get_kitchen_dict(self, kitchen_name):
        return self._api_helper.get_kitchen_dict(kitchen_name)

    # returns a list of kitchens
    # '/v2/kitchen/list', methods=['GET'])
    def list_kitchen(self):
        return convert_return_code(self._api_helper.list_kitchen())

    def vault_info(self, kitchen_name):
        req_dict = dict()
        if kitchen_name:
            req_dict['kitchens'] = kitchen_name
        url = '%s/v2/vault/config' % self.get_url_for_direct_rest_call()
        response = requests.get(url, data=json.dumps(req_dict), headers=self._get_common_headers())
        return validate_and_get_response(response)

    def vault_config(self, kitchen_name, in_dict):
        req_dict = dict()
        req_dict['config'] = dict()
        if kitchen_name:
            req_dict['config'][kitchen_name] = in_dict
        else:
            req_dict['config'][VAULT_GLOBAL] = in_dict
        url = '%s/v2/vault/config' % self.get_url_for_direct_rest_call()
        response = requests.post(url, data=json.dumps(req_dict), headers=self._get_common_headers())
        return validate_and_get_response(response)

    def vault_delete(self, kitchen_name):
        url = '%s/v2/vault/config/%s' % (self.get_url_for_direct_rest_call(), kitchen_name)
        response = requests.delete(url, headers=self._get_common_headers())
        return validate_and_get_response(response)

    def secret_list(self, path, kitchen_name):
        path = path or ''
        url = '%s/v2/secret/%s' % (self.get_url_for_direct_rest_call(), path)
        req_dict = dict()
        if kitchen_name:
            req_dict['kitchens'] = kitchen_name
        response = requests.get(url, data=json.dumps(req_dict), headers=self._get_common_headers())
        return validate_and_get_response(response)

    def secret_write(self, path, value, kitchen_name):
        rc = DKReturnCode()
        path = path or ''
        url = '%s/v2/secret/%s' % (self.get_url_for_direct_rest_call(), path)
        try:
            pdict = {'value': value}
            if kitchen_name:
                pdict['kitchen'] = kitchen_name
            response = requests.post(
                url, data=json.dumps(pdict), headers=self._get_common_headers()
            )
            validate_and_get_response(response)
            rc.set(rc.DK_SUCCESS, None, None)
            return rc
        except (RequestException, ValueError, TypeError) as c:
            s = "secret_write: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc

    def secret_delete(self, path, kitchen_name):
        rc = DKReturnCode()
        path = path or ''
        url = '%s/v2/secret/%s' % (self.get_url_for_direct_rest_call(), path)
        try:
            request_dict = dict()
            if kitchen_name:
                request_dict['kitchen'] = kitchen_name
            response = requests.delete(
                url, data=json.dumps(request_dict), headers=self._get_common_headers()
            )
            validate_and_get_response(response)
            rc.set(rc.DK_SUCCESS, None, None)
            return rc
        except (RequestException, ValueError, TypeError) as c:
            s = "secret_delete: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc

    # '/v2/kitchen/update/<string:kitchenname>', methods=['POST'])
    def update_kitchen(self, update_kitchen, message):
        return self._api_helper.update_kitchen(update_kitchen, message)

    # '/v2/kitchen/create/<string:existingkitchenname>/<string:newkitchenname>', methods=['GET'])
    def create_kitchen(self, existing_kitchen_name, new_kitchen_name, description, message):
        return convert_return_code(
            self._api_helper.create_kitchen(
                existing_kitchen_name, new_kitchen_name, description, message=message
            )
        )

    # '/v2/kitchen/delete/<string:existingkitchenname>', methods=['DELETE'])
    def delete_kitchen(self, existing_kitchen_name, message):
        return convert_return_code(
            self._api_helper.delete_kitchen(existing_kitchen_name, message=message)
        )

    def modify_kitchen_settings(self, kitchen_name, add=(), unset=()):
        rc = self.get_kitchen_settings(kitchen_name)
        if not rc.ok():
            return rc

        kitchen_json = rc.get_payload()
        overrides = kitchen_json['recipeoverrides']

        msg = ''
        commit_message = ''

        msg_lines = []
        commit_msg_lines = []

        if len(add) > 0:
            if isinstance(overrides, list):
                for add_this in add:
                    matches = [
                        existing_override for existing_override in overrides
                        if existing_override['variable'] == add_this[0]
                    ]
                    if len(matches) == 0:
                        overrides.append({
                            'variable': add_this[0],
                            'value': add_this[1],
                            'category': 'from_command_line'
                        })
                    else:
                        matches[0]['value'] = add_this[1]

                    msg_lines.append("{} added with value '{}'\n".format(add_this[0], add_this[1]))
                    commit_msg_lines.append("{} added".format(add_this[0]))
            else:
                for add_this in add:
                    overrides[add_this[0]] = add_this[1]
                    msg_lines.append("{} added with value '{}'\n".format(add_this[0], add_this[1]))
                    commit_msg_lines.append("{} added".format(add_this[0]))

        # tom_index = next(index for (index, d) in enumerate(lst) if d["name"] == "Tom")
        # might be a string?
        if len(unset) > 0:
            if isinstance(overrides, list):
                if isinstance(unset, list) or isinstance(unset, tuple):
                    for unset_this in unset:
                        match_index = next((
                            index for (index, d) in enumerate(overrides)
                            if d["variable"] == unset_this
                        ), None)
                        if match_index is not None:
                            del overrides[match_index]
                            msg_lines.append("{} unset".format(unset_this))
                            commit_msg_lines.append("{} unset".format(unset_this))
                else:
                    match_index = next(
                        (index for (index, d) in enumerate(overrides) if d["variable"] == unset),
                        None
                    )
                    if match_index is not None:
                        del overrides[match_index]
                        msg_lines.append("{} unset".format(unset))
                        commit_msg_lines.append("{} unset".format(unset))
            else:
                msg_lines = []
                if isinstance(unset, list) or isinstance(unset, tuple):
                    for unset_this in unset:
                        if unset_this in overrides:
                            del overrides[unset_this]
                        msg_lines.append("{} unset".format(unset_this))
                        commit_msg_lines.append("{} unset".format(unset_this))
                else:
                    if unset in overrides:
                        del overrides[unset]
                    msg_lines.append("{} unset".format(unset))
                    commit_msg_lines.append("{} unset".format(unset))

        msg = '\n'.join(msg_lines)
        commit_message = ' ; '.join(commit_msg_lines)

        rc = self.put_kitchen_settings(kitchen_name, kitchen_json, commit_message)
        if not rc.ok():
            return rc

        rc = DKReturnCode()
        rc.set(rc.DK_SUCCESS, msg, overrides)
        return rc

    def get_kitchen_settings(self, kitchen_name):
        rc = DKReturnCode()
        url = '%s/v2/kitchen/settings/%s' % (self.get_url_for_direct_rest_call(), kitchen_name)
        try:
            response = requests.get(url, headers=self._get_common_headers())
        except (RequestException, ValueError, TypeError) as c:
            rc.set(rc.DK_FAIL, 'settings_kitchen: exception: %s' % str(c))
            return rc
        rdict = validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None, rdict)
        return rc

    def put_kitchen_settings(self, kitchen_name, kitchen_dict, msg):
        rc = DKReturnCode()

        try:
            kitchen_json = json.dumps(kitchen_dict)
        except ValueError as ve:
            # Make sure this is valid json
            rc.set(rc.DK_FAIL, str(ve))
            return rc

        d1 = dict()
        d1['kitchen.json'] = kitchen_dict
        d1['message'] = msg
        url = '%s/v2/kitchen/settings/%s' % (self.get_url_for_direct_rest_call(), kitchen_name)
        try:
            response = requests.put(url, headers=self._get_common_headers(), data=json.dumps(d1))
        except (RequestException, ValueError, TypeError) as c:
            rc.set(rc.DK_FAIL, 'settings_kitchen: exception: %s' % str(c))
            return rc
        rdict = validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None, rdict)
        return rc

    def kitchen_settings_json_update(self, kitchen, filepath):
        rc = DKReturnCode()

        # Open local file to see contents
        msg = ''
        try:
            with open(filepath[0], 'r') as f:
                file_contents = json.load(f)
        except IOError as e:
            if len(msg) != 0:
                msg += '\n'
            msg += '%s' % (str(e))
            rc.set(rc.DK_FAIL, msg)
            return rc
        except ValueError as e:
            if len(msg) != 0:
                msg += '\n'
            msg += 'ERROR: %s' % str(e)
            rc.set(rc.DK_FAIL, msg)
            return rc

        # send new version to backend
        pdict = dict()
        pdict[self.FILEPATH] = filepath
        pdict[self.FILE] = file_contents
        url = '%s/v2/kitchen/settings/json/%s' % (self.get_url_for_direct_rest_call(), kitchen)
        try:
            response = requests.post(
                url, data=json.dumps(pdict), headers=self._get_common_headers()
            )
        except (RequestException, ValueError, TypeError) as c:
            s = "kitchen_settings_json_update: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc
        validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None)
        return rc

    def kitchen_settings_json_get(self, kitchen):
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen parameter')
            return rc

        url = '%s/v2/kitchen/settings/json/%s' % (self.get_url_for_direct_rest_call(), kitchen)
        try:
            response = requests.get(url, headers=self._get_common_headers())
            pass
        except (RequestException, ValueError, TypeError) as c:
            s = "kitchen_settings_json_get: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc
        rdict = validate_and_get_response(response)
        try:
            full_dir = os.getcwd()
            DKRecipeDisk.write_files(full_dir, rdict)
            rc.set(rc.DK_SUCCESS, None, rdict)
            return rc
        except Exception as e:
            s = "kitchen_settings_json_get: unable to write file: %s\n%s\n" % (
                str(rdict['filename'], e)
            )
            rc.set(rc.DK_FAIL, s)
            return rc

    def list_recipe(self, kitchen):
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen parameter')
            return rc
        url = '%s/v2/kitchen/recipenames/%s' % (self.get_url_for_direct_rest_call(), kitchen)
        try:
            response = requests.get(url, headers=self._get_common_headers())
        except (RequestException, ValueError, TypeError) as c:
            s = "list_recipe: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc

        rdict = validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None, rdict['recipes'])
        return rc

    def recipe_create(self, kitchen, name, template=None):
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen parameter')
            return rc

        pdict = dict()
        pdict[self.TEMPLATENAME] = template

        url = '%s/v2/recipe/create/%s/%s' % (self.get_url_for_direct_rest_call(), kitchen, name)
        try:
            response = requests.post(
                url, data=json.dumps(pdict), headers=self._get_common_headers()
            )
        except (RequestException, ValueError, TypeError) as c:
            s = "recipe_create: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc

        validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None)
        return rc

    def recipe_copy(self, kitchen, source, name):
        rc = DKReturnCode()
        for item in [kitchen, source, name]:
            if item is None or isinstance(item, six.string_types) is False:
                rc.set(rc.DK_FAIL, 'not all parameters present')
                return rc

        url = '%s/v2/recipe/copy/%s/%s/%s' % (
            self.get_url_for_direct_rest_call(), kitchen, source, name
        )
        try:
            response = requests.post(url, headers=self._get_common_headers())
        except (RequestException, ValueError, TypeError) as c:
            s = "recipe_copy: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc

        validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None)
        return rc

    def recipe_delete(self, kitchen, name):
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen parameter')
            return rc
        url = '%s/v2/recipe/%s/%s' % (self.get_url_for_direct_rest_call(), kitchen, name)
        try:
            response = requests.delete(url, headers=self._get_common_headers())
        except (RequestException, ValueError, TypeError) as c:
            s = "recipe_delete: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc
        validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None)
        return rc

    # returns a recipe
    # api.add_resource(GetRecipeV2, '/v2/recipe/get/<string:kitchenname>/<string:recipename>',
    #             methods=['GET', 'POST'])
    # get() gets all files in a recipe
    # post() gets a list of files in a recipe in the post as a 'recipe-files' list of dir / file names
    def get_recipe(self, kitchen, recipe, list_of_files=None):
        return convert_return_code(
            self._api_helper.get_recipe(kitchen, recipe, list_of_files=list_of_files)
        )

    def update_file(self, kitchen, recipe, message, api_file_key, file_contents):
        """
        returns success or failure (True or False)
        '/v2/recipe/update/<string:kitchenname>/<string:recipename>', methods=['POST']
        :param self: DKCloudAPI
        :param kitchen: basestring
        :param recipe: basestring  -- kitchen name, basestring
        :param message: basestring message -- commit message, basestring
        :param api_file_key:  -- the recipe based file path (recipe_name/node1/data_sources, e.g.)
        :param file_contents: -- character string of the recipe file to update

        :rtype: boolean
        """
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen parameter')
            return rc
        if recipe is None or isinstance(recipe, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with recipe parameter')
            return rc
        if api_file_key is None or isinstance(api_file_key, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with api_file_key parameter')
            return rc
        if six.PY2:
            if file_contents is None or isinstance(file_contents, six.string_types) is False:
                rc.set(rc.DK_FAIL, 'issue with file_contents parameter')
                return rc

        pdict = dict()
        pdict[self.MESSAGE] = message
        if DKFileEncode.is_binary(api_file_key):
            file_contents = DKFileEncode.b64encode(file_contents)
        pdict[self.FILEPATH] = normalize(api_file_key, UNIX)
        if six.PY3 and isinstance(file_contents, six.binary_type):  # decode bytes to unicode:
            file_contents = file_contents.decode('utf-8')
        pdict[self.FILE] = file_contents
        url = '%s/v2/recipe/update/%s/%s' % (self.get_url_for_direct_rest_call(), kitchen, recipe)
        try:
            response = requests.post(
                url, data=json.dumps(pdict), headers=self._get_common_headers()
            )
            pass
        except (RequestException, ValueError, TypeError) as c:
            s = "update_file: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc
        rdict = validate_and_get_response(response)
        rdict['formatted_files'] = normalize_dict_keys(rdict['formatted_files'], WIN)
        rc.set(rc.DK_SUCCESS, get_issue_messages(rdict), payload=rdict)
        return rc

    def _decode_contents_in_changees_dictionary(self, changes):
        for file_key, val_dict in six.iteritems(changes):
            if isinstance(val_dict, dict):
                if 'contents' in val_dict:
                    if isinstance(val_dict['contents'], six.binary_type):
                        val_dict['contents'] = val_dict['contents'].decode('utf-8')

    def update_files(self, kitchen, recipe, message, changes):
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen parameter')
            return rc
        if recipe is None or isinstance(recipe, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with recipe parameter')
            return rc
        pdict = dict()
        pdict[self.MESSAGE] = message
        if six.PY3:
            self._decode_contents_in_changees_dictionary(changes)

        pdict[self.FILES] = normalize_dict_keys(changes, UNIX)
        url = '%s/v2/recipe/update/%s/%s' % (self.get_url_for_direct_rest_call(), kitchen, recipe)
        try:
            response = requests.post(
                url, data=json.dumps(pdict), headers=self._get_common_headers()
            )
            pass
        except (RequestException, ValueError, TypeError) as c:
            s = "update_file: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc

        rdict = validate_and_get_response(response)
        rdict = normalize_dict_keys(
            rdict, WIN, ignore=['status', 'issues', 'branch', 'formatted_files']
        )
        rdict['formatted_files'] = normalize_dict_keys(rdict['formatted_files'], WIN)
        rc.set(rc.DK_SUCCESS, None, rdict)
        return rc

    # Create a file in a recipe
    def add_file(self, kitchen, recipe, message, api_file_key, file_contents):
        """
        returns True for success or False for failure
        '/v2/recipe/create/<string:kitchenname>/<string:recipename>', methods=['PUT']
        :param self: DKCloudAPI
        :param kitchen: basestring
        :param recipe: basestring  -- kitchen name, basestring
        :param message: basestring message -- commit message, basestring
        :param api_file_key:  -- file name and path to the file name, relative to the recipe root
        :param file_contents: -- character string of the recipe file to update

        :rtype: boolean
        """
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen parameter')
            return rc
        if recipe is None or isinstance(recipe, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with recipe parameter')
            return rc
        if api_file_key is None or isinstance(api_file_key, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with api_file_key parameter')
            return rc
        if six.PY2:
            if file_contents is None or isinstance(file_contents, six.string_types) is False:
                rc.set(rc.DK_FAIL, 'issue with file_contents parameter')
                return rc

        pdict = dict()
        pdict[self.MESSAGE] = message
        if DKFileEncode.is_binary(api_file_key):
            file_contents = DKFileEncode.b64encode(file_contents)
        if six.PY3 and isinstance(file_contents, six.binary_type):  # decode bytes to unicode:
            file_contents = file_contents.decode('utf-8')
        pdict[self.FILE] = file_contents
        pdict[self.FILEPATH] = normalize(api_file_key, UNIX)
        url = '%s/v2/recipe/create/%s/%s' % (self.get_url_for_direct_rest_call(), kitchen, recipe)
        try:
            response = requests.put(url, data=json.dumps(pdict), headers=self._get_common_headers())
        except (RequestException, ValueError, TypeError) as c:
            s = "add_file: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc

        validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None)
        return rc

    # api.add_resource(DeleteRecipeFileV2, '/v2/recipe/delete/<string:kitchenname>/<string:recipename>',
    #              methods=['DELETE'])
    def delete_file(self, kitchen, recipe, message, recipe_file_key, recipe_file):
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen parameter')
            return rc
        if recipe is None or isinstance(recipe, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with recipe parameter')
            return rc
        if recipe_file_key is None or isinstance(recipe_file_key, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with recipe_file_key parameter')
            return rc
        if recipe_file is None or isinstance(recipe_file, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with recipe_file parameter')
            return rc
        pdict = dict()
        pdict[self.MESSAGE] = message
        pdict[self.FILEPATH] = normalize(recipe_file_key, UNIX)
        pdict[self.FILE] = recipe_file
        url = '%s/v2/recipe/delete/%s/%s' % (self.get_url_for_direct_rest_call(), kitchen, recipe)
        try:
            response = requests.delete(
                url, data=json.dumps(pdict), headers=self._get_common_headers()
            )
        except (RequestException, ValueError, TypeError) as c:
            s = "delete_file: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc

        validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None)
        return rc

    def get_compiled_order_run(self, kitchen, recipe_name, variation_name):
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen')
            return rc
        if recipe_name is None or isinstance(recipe_name, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with recipe_name')
            return rc
        if variation_name is None or isinstance(variation_name, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with variation_name')
            return rc
        url = '%s/v2/servings/compiled/get/%s/%s/%s' % (
            self.get_url_for_direct_rest_call(), kitchen, recipe_name, variation_name
        )
        try:
            response = requests.get(url, headers=self._get_common_headers())
        except (RequestException, ValueError, TypeError) as c:
            rc.set(rc.DK_FAIL, "get_compiled_order_run: exception: %s" % str(c))
            return rc
        rdict = validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None, rdict[recipe_name])
        return rc

    def get_compiled_file(self, kitchen, recipe_name, variation_name, file_data):
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen')
            return rc
        if recipe_name is None or isinstance(recipe_name, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with recipe_name')
            return rc
        if variation_name is None or isinstance(variation_name, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with variation_name')
            return rc

        url = '%s/v2/recipe/compile/%s/%s/%s' % (
            self.get_url_for_direct_rest_call(), kitchen, recipe_name, variation_name
        )

        try:
            data = {'file': normalize_get_compiled_file(file_data, UNIX)}
            response = requests.post(url, data=json.dumps(data), headers=self._get_common_headers())
        except (RequestException, ValueError, TypeError) as c:
            rc.set(rc.DK_FAIL, "get_compiled_file: exception: %s" % str(c))
            return rc

        rdict = validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None, rdict)
        return rc

    def get_file(self, kitchen, recipe, file_path):
        rc = DKReturnCode()
        file_path = normalize(file_path, UNIX)
        url = '%s/v2/recipe/file/%s/%s/%s' % (
            self.get_url_for_direct_rest_call(), kitchen, recipe, file_path
        )
        response = requests.get(url, headers=self._get_common_headers())
        rdict = validate_and_get_response(response)
        return rdict['contents']

    def get_file_history(self, kitchen, recipe_name, file_path, change_count):
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen')
            return rc
        if recipe_name is None or isinstance(recipe_name, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with recipe_name')
            return rc

        url = '%s/v2/recipe/history/%s/%s/%s?change_count=%d' % (
            self.get_url_for_direct_rest_call(), kitchen, recipe_name, normalize(file_path,
                                                                                 UNIX), change_count
        )

        try:
            response = requests.get(url, headers=self._get_common_headers())
        except (RequestException, ValueError, TypeError) as c:
            rc.set(rc.DK_FAIL, "get_compiled_file: exception: %s" % str(c))
            return rc

        rdict = validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None, rdict)
        return rc

    def recipe_validate(self, kitchen, recipe_name, variation_name, changed_files):
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen')
            return rc
        if recipe_name is None or isinstance(recipe_name, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with recipe_name')
            return rc
        if variation_name is None or isinstance(variation_name, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with variation_name')
            return rc
        url = '%s/v2/recipe/validate/%s/%s/%s' % (
            self.get_url_for_direct_rest_call(), kitchen, recipe_name, variation_name
        )
        try:
            payload = {'files': normalize_dict_keys(changed_files, UNIX)}

            response = requests.post(
                url, headers=self._get_common_headers(), data=json.dumps(payload)
            )
        except (RequestException, ValueError, TypeError) as c:
            rc.set(rc.DK_FAIL, "recipe_validate: exception: %s" % str(c))
            return rc

        rdict = validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None, normalize_recipe_validate(rdict['results'], WIN))
        return rc

    def kitchen_merge_preview(self, from_kitchen, to_kitchen):
        """
        preview of kitchen merge
        '/v2/kitchen/merge/<string:kitchenname>/<string:parentkitchen>', methods=['GET']
        :param self: DKCloudAPI
        :param from_kitchen: string
        :param to_kitchen: string
        :rtype: dict
        """
        url = '%s/v2/kitchen/merge/%s/%s' % (
            self.get_url_for_direct_rest_call(), from_kitchen, to_kitchen
        )
        response = requests.get(url, headers=self._get_common_headers())
        rdict = validate_and_get_response(response)
        return normalize_recipe_dict_kmp(rdict, WIN)

    def kitchens_merge(self, from_kitchen, to_kitchen, resolved_conflicts=None):
        """
        '/v2/kitchen/merge/<string:kitchenname>/<string:parentkitchen>', methods=['POST']
        :param self: DKCloudAPI
        :param from_kitchen: string
        :param to_kitchen: string
        :param resolved_conflicts: dict
        :rtype: dict
        """
        url = '%s/v2/kitchen/merge/%s/%s' % (
            self.get_url_for_direct_rest_call(), from_kitchen, to_kitchen
        )

        pdict = {'files': normalize_dict_keys(resolved_conflicts, UNIX)}
        working_dir = os.path.join(self.get_merge_dir(), '%s_to_%s' % (from_kitchen, to_kitchen))
        pdict['source_kitchen_sha'] = DKFileHelper.read_file(
            os.path.join(working_dir, 'source_kitchen_sha')
        )
        pdict['target_kitchen_sha'] = DKFileHelper.read_file(
            os.path.join(working_dir, 'target_kitchen_sha')
        )
        response = requests.post(url, data=json.dumps(pdict), headers=self._get_common_headers())
        rdict = validate_and_get_response(response)

        if 'merge-kitchen-result' not in rdict or\
                        'status' not in rdict['merge-kitchen-result'] or \
                        rdict['merge-kitchen-result']['status'] != 'success':
            raise Exception("kitchen_merge_manual: backend returned with error status.\n")

        return '%s:%s/%s' % (
            self.get_config().get_ip(), self.get_config().get_port(),
            rdict['merge-kitchen-result']['url']
        )

    def merge_file(self, kitchen, recipe, file_path, file_contents, orig_head, last_file_sha):
        """
        Returns the result of merging a local file with the latest version on the remote.
        This does not cause any side-effects on the server, and no actual merge is performed in the remote repo.
        /v2/file/merge/<string:kitchenname>/<string:recipename>/<path:filepath>, methods=['POST']
        :param kitchen: name of the kitchen where this file lives
        :param recipe: name of the recipe that owns this file
        :param file_path: path to the file, relative to the recipe
        :param file_contents: contents of the file
        :param orig_head: sha of commit head of the branch when this file was obtained.
        :param last_file_sha: The sha of the file when it was obtained from the server.
        :return: dict
        """
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False or \
                recipe is None or isinstance(recipe, six.string_types) is False or \
                file_path is None or isinstance(file_path, six.string_types) is False or \
                orig_head is None or isinstance(orig_head, six.string_types) is False or \
                last_file_sha is None or isinstance(last_file_sha, six.string_types) is False or \
                file_contents is None:
            rc.set(rc.DK_FAIL, 'One or more parameters is invalid. ')
            return rc

        params = dict()
        params['orig_head'] = orig_head
        params['last_file_sha'] = last_file_sha
        params['content'] = file_contents.decode('utf-8')
        adjusted_file_path = normalize(file_path, UNIX)
        url = '%s/v2/file/merge/%s/%s/%s' % (
            self.get_url_for_direct_rest_call(), kitchen, recipe, adjusted_file_path
        )
        try:
            response = requests.post(
                url, data=json.dumps(params), headers=self._get_common_headers()
            )
        except (RequestException, ValueError, TypeError) as c:
            print("merge_file: exception: %s" % str(c))
            return None

        rdict = validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None, normalize_dict_value(rdict, 'file_path', WIN))
        return rc

    def recipe_status(self, kitchen, recipe, local_dir=None):
        """
        gets the status of a recipe
        :param self: DKCloudAPI
        :param kitchen: string
        :param recipe: string
        :param local_dir: string --
        :rtype: dict
        """
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen parameter')
            return rc
        if recipe is None or isinstance(recipe, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with recipe parameter')
            return rc
        url = '%s/v2/recipe/tree/%s/%s' % (self.get_url_for_direct_rest_call(), kitchen, recipe)
        try:
            response = requests.get(url, headers=self._get_common_headers())
        except (RequestException, ValueError, TypeError) as c:
            s = "get_recipe: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc

        rdict = validate_and_get_response(response)
        normalize_recipe_dict(rdict, WIN)

        # Now get the local sha.
        if local_dir is None:
            check_path = os.getcwd()
        else:
            if os.path.isdir(local_dir) is False:
                print('Local path %s does not exist' % local_dir)
                return None
            else:
                check_path = local_dir
        local_sha = get_directory_sha(self.get_ignore(), check_path)

        if recipe not in rdict['recipes']:
            raise Exception('Recipe %s does not exist on remote.' % recipe)

        remote_sha = rdict['recipes'][recipe]

        rv = compare_sha(self.get_ignore(), remote_sha, local_sha, local_dir, recipe)
        rv['recipe_sha'] = rdict['ORIG_HEAD']
        rc.set(rc.DK_SUCCESS, None, rv)
        return rc

    # returns a recipe
    def recipe_tree(self, kitchen, recipe):
        """
        gets the status of a recipe
        :param self: DKCloudAPI
        :param kitchen: string
        :param recipe: string
        :rtype: dict
        """
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen parameter')
            return rc
        if recipe is None or isinstance(recipe, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with recipe parameter')
            return rc
        url = '%s/v2/recipe/tree/%s/%s' % (self.get_url_for_direct_rest_call(), kitchen, recipe)
        try:
            response = requests.get(url, headers=self._get_common_headers())
        except (RequestException, ValueError, TypeError) as c:
            s = "recipe_tree: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc
        rdict = validate_and_get_response(response)
        remote_sha = rdict['recipes'][recipe]
        rc.set(rc.DK_SUCCESS, None, remote_sha)
        return rc

    # --------------------------------------------------------------------------------------------------------------------
    #  Order commands
    # --------------------------------------------------------------------------------------------------------------------
    #  Cook a recipe varation in a kitchen
    def create_order(self, kitchen, recipe_name, variation_name, node_name=None, parameters=None):
        return self._api_helper.create_order(
            kitchen, recipe_name, variation_name, node_name=node_name, parameters=parameters
        )

    def order_resume(self, kitchen, serving_hid):
        rc = DKReturnCode()
        if serving_hid is None or isinstance(serving_hid, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with orderrun_id')
            return rc

        pdict = dict()
        pdict['serving_hid'] = quote(serving_hid)
        pdict['kitchen_name'] = kitchen
        orderrun_id = None

        url = '%s/v2/order/resume/%s' % (self.get_url_for_direct_rest_call(), orderrun_id)
        try:
            response = requests.put(url, data=json.dumps(pdict), headers=self._get_common_headers())
        except (RequestException, ValueError) as c:
            s = "orderrun_delete: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc

        rdict = validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None, rdict['order_id'])
        return rc

    # Get the details about a Order-Run (fka Serving)
    def orderrun_detail(self, kitchen, pdict, return_all_data=False):
        """
        api.add_resource(OrderDetailsV2, '/v2/order/details/<string:kitchenname>', methods=['POST'])
        :param self: DKCloudAPI
        :param kitchen: string
        :param pdict: dict
        :param return_all_data: boolean
        :rtype: DKReturnCode
        """
        return convert_return_code(self._api_helper.orderrun_detail(kitchen, pdict))

    def get_order_run_full_log(self, kitchen, order_run_id):
        url = '%s/v2/order/export/logs/%s/%s' % (
            self.get_url_for_direct_rest_call(), kitchen, quote(order_run_id)
        )
        try:
            response = requests.get(url, headers=self._get_common_headers())
        except (RequestException, ValueError) as c:
            s = "get_order_run_full_log: exception: %s" % str(c)
            raise Exception(s)
        rdict = validate_and_get_response(response)
        return rdict['log']

    def list_order(
            self, kitchen, order_count=5, order_run_count=3, start=0, recipe=None, save_to_file=None
    ):
        """
        List the orders for a kitchen or recipe
        """
        rc = DKReturnCode()
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with kitchen parameter')
            return rc

        if recipe:
            url = '%s/v2/order/status/%s?start=%d&count=%d&scount=%d&r=%s' % (
                self.get_url_for_direct_rest_call(), kitchen, start, order_count, order_run_count,
                recipe
            )
        else:
            url = '%s/v2/order/status/%s?start=%d&count=%d&scount=%d' % (
                self.get_url_for_direct_rest_call(), kitchen, start, order_count, order_run_count
            )
        try:
            response = requests.get(url, headers=self._get_common_headers())
        except (RequestException, ValueError, TypeError) as c:
            s = "get_recipe: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc
        rdict = validate_and_get_response(response)
        if save_to_file is not None:
            import pickle
            pickle.dump(rdict, open(save_to_file, "wb"))

        rc.set(rc.DK_SUCCESS, None, rdict)
        return rc

    def order_delete_all(self, kitchen):
        """
        api.add_resource(OrderDeleteAllV2, '/v2/order/deleteall/<string:kitchenname>', methods=['DELETE'])
        :param self: DKCloudAPI
        :param kitchen: string
        :rtype: DKReturnCode
        """
        return convert_return_code(self._api_helper.order_delete_all(kitchen))

    def order_delete_one(self, kitchen, serving_book_hid):
        """
        api.add_resource(OrderDeleteV2, '/v2/order/delete/<string:orderid>', methods=['DELETE'])
        :param self: DKCloudAPI
        :param order_id: string
        :rtype: DKReturnCode
        """
        rc = DKReturnCode()
        if serving_book_hid is None or isinstance(serving_book_hid, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with order_id')
            return rc
        order_id = None
        pdict = dict()
        serving_book_hid2 = quote(serving_book_hid)
        pdict['serving_book_hid'] = serving_book_hid2
        pdict['kitchen_name'] = kitchen
        url = '%s/v2/order/delete/%s' % (self.get_url_for_direct_rest_call(), order_id)
        try:
            response = requests.delete(
                url, data=json.dumps(pdict), headers=self._get_common_headers()
            )
        except (RequestException, ValueError) as c:
            s = "order_delete_one: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc
        validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None, None)
        return rc

    # Get the details about a Order-Run (fka Serving)
    def delete_orderrun(self, kitchen, serving_hid):
        """
        api.add_resource(ServingDeleteV2, '/v2/serving/delete/<string:servingid>', methods=['DELETE'])
        """
        rc = DKReturnCode()
        if serving_hid is None or isinstance(serving_hid, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with orderrun_id')
            return rc
        pdict = dict()
        pdict['serving_hid'] = quote(serving_hid)
        pdict['kitchen_name'] = kitchen
        orderrun_id = None

        url = '%s/v2/serving/delete/%s' % (self.get_url_for_direct_rest_call(), orderrun_id)
        try:
            response = requests.delete(
                url, data=json.dumps(pdict), headers=self._get_common_headers()
            )
            validate_and_get_response(response)
            rc.set(rc.DK_SUCCESS, None, None)
            return rc
        except (RequestException, ValueError) as c:
            s = "orderrun_delete: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc

    def order_stop(self, kitchen, serving_book_hid):
        """
        api.add_resource(OrderStopV2, '/v2/order/stop/<string:orderid>', methods=['PUT'])
        """
        rc = DKReturnCode()
        if serving_book_hid is None or isinstance(serving_book_hid, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with order id')
            return rc
        pdict = dict()
        serving_book_hid2 = quote(serving_book_hid)
        pdict['serving_book_hid'] = serving_book_hid2
        pdict['kitchen_name'] = kitchen
        order_id = None
        url = '%s/v2/order/stop/%s' % (self.get_url_for_direct_rest_call(), order_id)
        try:
            response = requests.put(url, data=json.dumps(pdict), headers=self._get_common_headers())
        except (RequestException, ValueError) as c:
            s = "order_stop: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc

        validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None, None)
        return rc

    def orderrun_stop(self, kitchen, orderrun_id):
        """
        api.add_resource(ServingStopV2, '/v2/serving/stop/<string:servingid>', methods=['Put'])
        """
        rc = DKReturnCode()
        if orderrun_id is None or isinstance(orderrun_id, six.string_types) is False:
            rc.set(rc.DK_FAIL, 'issue with orderrun_id')
            return rc

        pdict = dict()
        pdict['serving_hid'] = quote(orderrun_id)
        pdict['kitchen_name'] = kitchen

        url = '%s/v2/serving/stop/%s' % (self.get_url_for_direct_rest_call(), orderrun_id)
        try:
            response = requests.put(url, data=json.dumps(pdict), headers=self._get_common_headers())
        except (RequestException, ValueError) as c:
            s = "order_stop: exception: %s" % str(c)
            rc.set(rc.DK_FAIL, s)
            return rc
        validate_and_get_response(response)
        rc.set(rc.DK_SUCCESS, None, None)
        return rc

    # --------------------------------------------------------------------------------------------------------------------
    #  Agent Status
    # --------------------------------------------------------------------------------------------------------------------
    def agent_status(self):
        url = '%s/v2/sys/agent' % self.get_url_for_direct_rest_call()
        response = requests.get(url, headers=self._get_common_headers())
        return validate_and_get_response(response)
