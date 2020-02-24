import time
import unittest

from DKCloudCommand.tests.system_tests.BaseCLISystemTest import (
    BaseCLISystemTest,
    BASE_PATH,
    EMAIL_DOMAIN,
)


class TestResumeVariablesOverride(BaseCLISystemTest):
    # ---------------------------- Test setUp and tearDown methods ---------------------------
    def setUp(self):
        print('\n\n####################### Setup #######################')
        print('BASE_PATH: %s' % BASE_PATH)
        self.kitchens_path = BASE_PATH + '/CLISmokeTestDemoKitchens'

    def tearDown(self):
        print('\n####################### Test has finished #######################')
        print('\n\n####################### TearDown #######################')

    # ---------------------------- System tests ---------------------------
    def test_resume_variables_override(self):
        print(
            '\n\n####################### Starting Resume Variables Override #######################'
        )

        # --------------------------------------------
        print('----> Check logged user')
        configuration = 'st'
        checks = list()
        checks.append('+%s@%s' % (configuration, EMAIL_DOMAIN))
        sout = self.dk_user_info(checks)

        print('logged user info: \n%s' % sout)

        # --------------------------------------------
        print('-> Make sure CLI is working')
        self.dk_help()

        # --------------------------------------------
        print('-> Configure master kitchen, unset pass_the_resume_recipe')
        kitchen_name = 'master'
        key = 'pass_the_resume_recipe'
        self.dk_kitchen_config_unset(kitchen_name, key, add_params=True)

        # --------------------------------------------
        print('-> Configure master kitchen, pass_the_resume_recipe = false')
        value = 'false'
        self.dk_kitchen_config_add(kitchen_name, key, value, add_params=True)

        # --------------------------------------------
        print('-> Run the order')
        recipe_name = 'test_rt_vars_override_resume'
        variation = 'run_now'
        order_id = self.dk_order_run(kitchen_name, recipe_name, variation, add_params=True)
        print('Order id = %s' % order_id)

        # --------------------------------------------
        print('-> Start Polling the order run, we expect the order run will fail')
        retry_qty = 5
        order_run_completed = False
        seconds = 60
        while not order_run_completed and retry_qty > 0:
            retry_qty = retry_qty - 1
            print('-> Waiting for %d seconds ' % seconds)
            time.sleep(seconds)

            print('-> Pull order run status for %s' % order_id)
            order_run_completed, orderrun_id = self.dk_order_run_info(
                kitchen_name,
                recipe_name,
                variation,
                order_id,
                add_params=True,
                expect_to_fail=True
            )

        self.assertTrue(
            order_run_completed,
            msg='Order run has not shown as completed after multiple status fetch'
        )
        print('Order Run id = %s' % orderrun_id)

        # --------------------------------------------
        print('-> Check that the failing node is "control_failure"')
        results = self.dk_order_run_info_node_status(
            kitchen_name, recipe_name, variation, order_id, add_params=True
        )
        self.assertTrue("container1\tDKNodeStatus_completed_production" in results, results)
        self.assertTrue("container2\tDKNodeStatus_completed_production" in results, results)
        self.assertTrue("container3\tDKNodeStatus_ready_for_production" in results, results)
        self.assertTrue("control_failure\tDKNodeStatus_production_error" in results, results)

        # --------------------------------------------
        print('-> Configure master kitchen, pass_the_resume_recipe = true')
        value = 'true'
        self.dk_kitchen_config_add(kitchen_name, key, value, add_params=True)

        # --------------------------------------------
        print('-> Resume the order')
        checks = list()
        self.dk_order_run_resume(kitchen_name, orderrun_id, checks=checks, add_params=True)

        # --------------------------------------------
        print('-> Start Polling the order run, we expect the order run to succeed')
        retry_qty = 5
        order_run_completed = False
        seconds = 60
        while not order_run_completed and retry_qty > 0:
            retry_qty = retry_qty - 1
            print('\tWaiting for %d seconds ' % seconds)
            time.sleep(seconds)

            print('\tPull order run status for order %s' % order_id)
            order_run_completed, orderrun_id = self.dk_order_run_info(
                kitchen_name, recipe_name, variation, order_id, add_params=True
            )

        self.assertTrue(
            order_run_completed,
            msg='Order run has not shown as completed after multiple status fetch'
        )
        print('Order run completed after resumed order run: %s' % orderrun_id)

        # --------------------------------------------
        print('-> Check all nodes are OK and all tests passed')
        results = self.dk_order_run_info_all(
            kitchen_name, recipe_name, variation, order_id, add_params=True
        )
        self.assertTrue("container1\tDKNodeStatus_completed_production" in results, results)
        self.assertTrue("container2\tDKNodeStatus_completed_production" in results, results)
        self.assertTrue("container3\tDKNodeStatus_completed_production" in results, results)
        self.assertTrue("control_failure\tDKNodeStatus_completed_production" in results, results)

        assertions = list()
        assertions.append('TEST RESULTS')
        assertions.append('Tests: Failed')
        assertions.append('No Tests Failed')
        assertions.append('Tests: Warning')
        assertions.append('No Tests Gave Warning Messages')
        self.assert_response(assertions, results)


if __name__ == '__main__':
    print('Running CLI smoke tests - Resume Variables Override')
    print('To configure, set this environment variables, otherwise will use default values:')
    print('\tTEST BASE PATH: %s' % BASE_PATH)
    unittest.main()
