import os
import time
import unittest

from shutil import copy
from subprocess import Popen, PIPE

CONFIG_FILE_BASE_NAME = 'DKCloudCommandConfig'

EMAIL_SUFFIX = '+dk@datakitchen.io'
EMAIL_DOMAIN = 'datakitchen.io'

BASE_PATH = os.environ.get('DK_CLI_SMOKE_TEST_BASE_PATH')
if BASE_PATH is None:
    raise Exception('Missing environment variable: DK_CLI_SMOKE_TEST_BASE_PATH')

EMAIL = os.environ.get('DK_CLI_SMOKE_TEST_EMAIL')
if EMAIL is None:
    raise Exception('Missing environment variable: DK_CLI_SMOKE_TEST_EMAIL')


class BaseCLISystemTest(unittest.TestCase):

    # ---------------------------- Helper methods ---------------------------
    def dk_kitchen_config_add(self, kitchen_name, key, value, checks=None, add_params=False):
        if checks is None:
            checks = list()
        checks.append('%s added with value \'%s\'' % (key, value))
        command = 'dk kitchen-config'
        if add_params:
            command += ' --kitchen %s' % kitchen_name
        command += ' --add %s %s' % (key, value)
        sout = self.run_command(command, checks)
        return sout

    def dk_kitchen_config_unset(self, kitchen_name, key, checks=None, add_params=False):
        if checks is None:
            checks = list()
        checks.append('%s unset' % key)
        command = 'dk kitchen-config'
        if add_params:
            command += ' --kitchen %s' % kitchen_name
        command += ' -u %s' % key
        sout = self.run_command(command, checks)
        return sout

    def dk_kitchen_delete(self, kitchen_name, checks=None, ignore_checks=False):
        if checks is None:
            checks = list()
        if not ignore_checks:
            checks.append('Kitchen %s has been deleted' % kitchen_name)
        command = 'dk kitchen-delete %s --yes' % kitchen_name
        sout = self.run_command(command, checks, ignore_checks=True)
        return sout

    def dk_kitchen_merge_preview(self, source_kitchen, target_kitchen, checks=None):
        if checks is None:
            checks = list()
        checks.append(
            '- Previewing merge Kitchen %s into Kitchen %s' % (source_kitchen, target_kitchen)
        )
        checks.append('Merge Preview Results (only changed files are being displayed):')
        checks.append('--------------------------------------------------------------')
        checks.append('Kitchen merge preview done.')
        command = 'dk kitchen-merge-preview -cpr --source_kitchen %s --target_kitchen %s' % (
            source_kitchen, target_kitchen
        )
        sout = self.run_command(command, checks)
        return sout

    def dk_kitchen_merge(self, source_kitchen, target_kitchen, checks=None):
        if checks is None:
            checks = list()
        checks.append('- Merging Kitchen %s into Kitchen %s' % (source_kitchen, target_kitchen))
        checks.append('Calling Merge ...')
        checks.append(
            'Merge done. You can check your changes in target kitchen and delete the source kitchen.'
        )
        command = 'dk kitchen-merge --source_kitchen %s --target_kitchen %s --yes' % (
            source_kitchen, target_kitchen
        )
        sout = self.run_command(command, checks)
        return sout

    def dk_order_run_info(
            self,
            kitchen_name,
            recipe_name,
            variation,
            order_id,
            checks=None,
            add_params=False,
            expect_to_fail=False,
            orderrun_id=None
    ):
        if checks is None:
            checks = list()
        checks.append(' - Display Order-Run details from kitchen %s' % kitchen_name)
        checks.append('ORDER RUN SUMMARY')
        checks.append('Order ID:\t%s' % order_id)
        if orderrun_id:
            checks.append('Order Run ID:\t%s' % orderrun_id)
        checks.append('Kitchen:\t%s' % kitchen_name)
        checks.append('Variation:\t%s' % variation)
        if expect_to_fail:
            checks.append('SERVING_ERROR')
        else:
            checks.append('COMPLETED_SERVING')
        command = 'dk orderrun-info'
        if add_params:
            command += ' --kitchen %s' % kitchen_name
        if orderrun_id is not None:
            command += ' -ori %s' % orderrun_id
        elif order_id is not None:
            command += ' -o %s' % order_id
        try:
            sout = self.run_command(command, checks)

            # Parse order run id
            if orderrun_id is None:
                try:
                    aux_string = 'Order Run ID:'
                    aux_start_index = sout.find(aux_string)
                    aux_start_index_after_semicolon = aux_start_index + len(aux_string)
                    aux_finish_index = sout.find('\n', aux_start_index_after_semicolon)
                    orderrun_id = sout[aux_start_index_after_semicolon:aux_finish_index].strip()
                except Exception:
                    pass  # sometimes orderrun_id won't be available
        except Exception:
            return False, orderrun_id
        return True, orderrun_id

    def dk_order_run_info_all(
            self, kitchen_name, recipe_name, variation, order_id, checks=None, add_params=False
    ):
        if checks is None:
            checks = list()
        checks.append(' - Display Order-Run details from kitchen %s' % kitchen_name)
        checks.append('TEST RESULTS')
        checks.append('STEP STATUS')
        checks.append('TIMING RESULTS')
        checks.append('LOG')
        command = 'dk orderrun-info -at -o %s' % order_id
        if add_params:
            command += ' --kitchen %s' % kitchen_name
        return self.run_command(command, checks)

    def dk_order_run_info_node_status(
            self, kitchen_name, recipe_name, variation, order_id, checks=None, add_params=False
    ):
        if checks is None:
            checks = list()
        checks.append(' - Display Order-Run details from kitchen %s' % kitchen_name)
        checks.append('STEP STATUS')
        command = 'dk orderrun-info -ns -o %s' % order_id
        if add_params:
            command += ' --kitchen %s' % kitchen_name
        return self.run_command(command, checks)

    def dk_order_run(
            self, kitchen_name, recipe_name, variation, checks=None, add_params=False,
            environment='dk'
    ):
        if checks is None:
            checks = list()
        checks.append(' - Create an Order')
        checks.append('Kitchen: %s' % kitchen_name)
        checks.append('Recipe: %s' % recipe_name)
        checks.append('Variation: %s' % variation)
        checks.append('Order ID is:')
        kitchen_param_str = ''
        recipe_param_str = ''
        if add_params:
            kitchen_param_str = ' --kitchen %s ' % kitchen_name
            recipe_param_str = '--recipe %s' % recipe_name
        command = 'dk order-run%s%s %s --yes' % (kitchen_param_str, recipe_param_str, variation)
        sout = self.run_command(command, checks)

        # Parse order id
        aux_string = 'Order ID is: '
        aux_index = sout.find(aux_string)
        order_id = sout[aux_index + len(aux_string):-1].strip()

        return order_id

    def dk_order_run_resume(self, kitchen_name, orderrun_id, checks=None, add_params=False):
        if checks is None:
            checks = list()
        checks.append('- Resuming Order-Run %s' % orderrun_id)
        checks.append('DKCloudCommand.order_resume %s succeeded' % orderrun_id)
        kitchen_param_str = ''
        recipe_param_str = ''
        if add_params:
            kitchen_param_str = ' --kitchen %s ' % kitchen_name
        command = 'dk orderrun-resume%s%s %s --yes' % (
            kitchen_param_str, recipe_param_str, orderrun_id
        )
        sout = self.run_command(command, checks)
        return sout

    def dk_file_update(self, kitchen_name, recipe_name, file_name, message, checks=None):
        if checks is None:
            checks = list()
        checks.append('Updating File(s)')
        checks.append(
            'in Recipe (%s) in Kitchen(%s) with message (%s)' %
            (recipe_name, kitchen_name, message)
        )
        checks.append('DKCloudCommand.update_file for %s succeeded' % file_name)
        command = 'dk file-update --message "%s" %s' % (message, file_name)
        sout = self.run_command(command, checks)
        return sout

    def dk_recipe_status(
            self,
            kitchen_name,
            recipe_name,
            qty_of_unchanged_files=None,
            qty_of_local_changed_files=None,
            checks=None
    ):
        if checks is None:
            checks = list()

        checks.append(
            '- Getting the status of Recipe \'%s\' in Kitchen \'%s\'' % (recipe_name, kitchen_name)
        )
        if qty_of_unchanged_files is not None:
            checks.append('%d files are unchanged' % qty_of_unchanged_files)
        if qty_of_local_changed_files is not None:
            checks.append('%d files are modified on local' % qty_of_local_changed_files)

        command = 'dk recipe-status'
        sout = self.run_command(command, checks)
        return sout

    def dk_kitchen_which(self, expected_kitchen_name, checks=None):
        if checks is None:
            checks = list()
        checks.append('You are in kitchen \'%s\'' % expected_kitchen_name)
        command = 'dk kitchen-which'
        sout = self.run_command(command, checks)
        return sout

    def dk_recipe_variation_list(self, kitchen_name, recipe_name, checks=None):
        if checks is None:
            checks = list()
        checks.append(
            ' - Listing variations for recipe %s in Kitchen %s' % (recipe_name, kitchen_name)
        )
        checks.append('Variations:')
        command = 'dk recipe-variation-list'
        sout = self.run_command(command, checks)
        return sout

    def dk_recipe_get(self, kitchen_name, recipe_name, checks=None):
        if checks is None:
            checks = list()
        checks.append(
            ' - Getting the latest version of Recipe \'%s\' in Kitchen \'%s\'' %
            (recipe_name, kitchen_name)
        )
        checks.append('DKCloudCommand.get_recipe has')
        checks.append('sections')
        command = 'dk recipe-get %s' % recipe_name
        sout = self.run_command(command, checks)
        return sout

    def dk_recipe_create(self, kitchen_name, recipe_name, checks=None):
        time.sleep(20)
        if checks is None:
            checks = list()
        checks.append('- Creating Recipe %s for Kitchen \'%s\'' % (recipe_name, kitchen_name))
        checks.append('DKCloudCommand.recipe_create created recipe %s' % recipe_name)
        command = 'dk recipe-create %s' % recipe_name
        sout = self.run_command(command, checks)
        return sout

    def dk_recipe_list(self, kitchen_name, checks=None):
        if checks is None:
            checks = list()
        checks.append('- Getting the list of Recipes for Kitchen \'%s\'' % kitchen_name)
        checks.append('DKCloudCommand.list_recipe returned')
        checks.append('recipes')
        command = 'dk recipe-list'
        sout = self.run_command(command, checks)
        return sout

    def dk_kitchen_get(self, kitchen_name, checks=None):
        if checks is None:
            checks = list()
        checks.append(' - Getting kitchen \'%s\'' % kitchen_name)
        checks.append('Got Kitchen \'%s\'' % kitchen_name)
        command = 'dk kitchen-get %s' % kitchen_name
        sout = self.run_command(command, checks)
        return sout

    def dk_kitchen_create(self, kitchen_name, parent='master', checks=None):
        if checks is None:
            checks = list()
        checks.append(' - Creating kitchen %s from parent kitchen %s' % (kitchen_name, parent))
        checks.append('DKCloudCommand.create_kitchen created %s' % kitchen_name)
        command = 'dk kitchen-create -p %s %s' % (parent, kitchen_name)
        sout = self.run_command(command, checks)
        return sout

    def dk_config_list(self, checks=None):
        if checks is None:
            checks = list()
        checks.append(EMAIL_SUFFIX)
        checks.append('Username')  # skip-secret-check
        checks.append('Password')  # skip-secret-check
        checks.append('Cloud IP')
        checks.append('Cloud Port')
        checks.append('Config Location')
        checks.append('General Config Location')
        checks.append('Merge Tool')
        checks.append('Diff Tool')
        sout = self.run_command('dk config-list', checks)
        return sout

    def dk_context_list(self, checks=None):
        if checks is None:
            checks = list()
        checks.append('default')
        checks.append('test')
        checks.append('Current context is: test')
        sout = self.run_command('dk context-list', checks)
        return sout

    def dk_user_info(self, checks=None):
        if checks is None:
            checks = list()
        checks.append('Name:')
        checks.append('Email:')
        checks.append('Customer Name:')
        checks.append('Support Email:')
        checks.append('Role:')

        sout = self.run_command('dk user-info', checks)
        return sout

    def dk_help(self, checks=None):
        if checks is None:
            checks = list()
        checks.append('Usage: dk [OPTIONS] COMMAND [ARGS]...')
        checks.append('config-list (cl)')
        checks.append('user-info (ui)')
        sout = self.run_command('dk --help', checks)
        return sout

    def dk_kitchen_list(self, checks=None):
        if checks is None:
            checks = list()
        checks.append('Getting the list of kitchens')
        checks.append('+---- master')
        sout = self.run_command('dk kl', checks)
        return sout

    def run_command(self, command, checks=None, ignore_checks=False):
        if checks is None:
            checks = list()
        p = Popen(['/bin/sh'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
        sout, serr = p.communicate((command + '\n').encode('utf-8'))
        sout = sout.decode('utf-8')
        serr = serr.decode('utf-8')
        if not ignore_checks and serr != '':
            message = 'Command %s failed. Standard error is %s' % (command, serr)
            raise Exception(message)
        for s in checks:
            self.assertIn(s, sout)
        return sout

    def set_working_directory(self, path):
        os.chdir(path)
        cwd = os.getcwd()
        self.assertIn(path, cwd)

    # ---------------------------- Start up and Tear down helper methods ---------------------------
    def switch_user_config(self, base_path, configuration):
        if configuration not in ['dk', 'dc']:
            raise Exception('Invalid configuration: %s.\n Should be dk or dc')

        dk_config_base_path = os.path.join(BASE_PATH, '.dk')
        dk_config_source_file_name = '%s-%s.json' % (CONFIG_FILE_BASE_NAME, configuration.upper())
        dk_config_source_file_path = os.path.join(dk_config_base_path, dk_config_source_file_name)

        dk_config_target_file_name = '%s.json' % CONFIG_FILE_BASE_NAME
        dk_config_target_file_path = os.path.join(dk_config_base_path, dk_config_target_file_name)

        copy(dk_config_source_file_path, dk_config_target_file_path)

        time.sleep(5)

    def delete_kitchens_in_tear_down(self, kitchens):
        print('\n----- Delete Kitchens -----')
        for kitchen_name in kitchens:
            if kitchen_name is not None:
                print('-> Deleting kitchen %s' % kitchen_name)
                self.dk_kitchen_delete(kitchen_name, ignore_checks=True)

        if len(kitchens) > 0:
            print('-> Checking that kitchens are not in kitchen list any more')
            command_output = self.dk_kitchen_list()
            for kitchen_name in kitchens:
                self.assertTrue(kitchen_name not in command_output)

    def delete_kitchen_path_in_tear_down(self, kitchens_path):
        if kitchens_path is not None:
            print('-> Removing local files from path %s' % kitchens_path)
            command = 'rm -rf %s' % kitchens_path
            self.run_command(command)

    def assert_response(self, assertions, output):
        total_stages = len(assertions)
        splitted_output = output.split('\n')

        index = 0
        stage = 0
        while stage < total_stages and index < len(splitted_output):
            if assertions[stage] in splitted_output[index]:
                stage += 1
            index += 1
        message = 'Could only reach stage %d of %d %s' % (stage, total_stages, os.linesep)
        expected = ''
        for assertion in assertions:
            expected += '%s%s' % (assertion, os.linesep)
        message += 'Expected Array: %s %s' % (str(assertions), os.linesep)
        message += 'Expected Values: %s %s' % (expected, os.linesep)
        message += 'Actual Values: %s %s' % (str(output), os.linesep)
        self.assertEqual(total_stages, stage, message)
