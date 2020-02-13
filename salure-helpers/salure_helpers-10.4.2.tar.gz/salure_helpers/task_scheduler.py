import sys
import datetime
import inspect
import time
from salure_helpers import MySQL, MailClient
from salure_helpers.salure_functions import SalureFunctions
import warnings
import re


class TaskScheduler(object):

    def __init__(self, host, user, password, database, task_id, email_after_errors=False, mandrill_api_token=None, loglevel='INFO'):
        """
        The TaskScheduler is responsible for the logging to the database. Based on this logging, the next reload will
        start or not and warning will be given or not
        :param host: The MySQL host of the customer database
        :param user: MySQL user of the customer
        :param password: MySQL password of the customer
        :param database: the customer database
        :param task_id: The ID from the task as saved in the task_scheduler table in the customer database
        :param email_after_errors: a True or False value. When True, there will be send an email to a contactperson of the customer (as given in the database) with the number of errors
        :param mandrill_api_token: When an email should be send after the errors, there is a mandrill API token needed with which the mails could be send
        :param loglevel: Chose on which level you want to store the logs. Default is INFO. that means that a logline
        with level DEBUG not is stored
        """
        self.mysql = MySQL(host, user, password, database)
        self.email_after_errors = email_after_errors
        self.mandrill_api_token = mandrill_api_token
        self.task_id = task_id
        self.loglevel = loglevel
        self.run_id = int(round(time.time() * 100000))
        self.started_at = datetime.datetime.now()
        self.error_count = 0

        # Check if the task is started on schedule or manual. store in a variable to use later in the script
        self.task_manual_started = self.check_if_task_manual_started

        # Check if the log tables exists in the customer database. If not, create them
        # Mysql throws a warning when a table already exists. We don't care so we ignore warnings. (not exceptions!)
        warnings.filterwarnings('ignore')
        self.check_if_logging_tables_exists()
        
        # Start the task and setup the data in the database
        self.start_task()

    def check_if_logging_tables_exists(self):
        """
        This function checks if all the needed tables for the task_scheduler exists. If they don't, this function
        creates the needed tables
        :return: nothing
        """
        # Check if the table task_scheduler exists. If not, create it
        new_table_query = 'CREATE TABLE IF NOT EXISTS `task_scheduler` (' \
                          '`id`                 int(11)         NOT NULL AUTO_INCREMENT,' \
                          '`title`              varchar(50)     NOT NULL,' \
                          '`description`        varchar(255)    NOT NULL,' \
                          '`docker_image`       varchar(255)    DEFAULT NULL,' \
                          '`runfile_path`       varchar(255)    DEFAULT NULL,' \
                          '`next_reload`        timestamp       NULL DEFAULT NULL,' \
                          '`frequency`          varchar(255)    DEFAULT \'{"month":0,"day":1,"hour":0,"minute":0}\',' \
                          '`last_reload`        timestamp       NULL DEFAULT NULL,' \
                          '`last_error_message` varchar(255)    DEFAULT NULL,' \
                          '`status`             varchar(255)    DEFAULT \'IDLE\',' \
                          '`disabled`           tinyint(4)      DEFAULT \'1\',' \
                          '`run_instant`        tinyint(1)      DEFAULT \'0\',' \
                          '`sftp_mapping`       varchar(255)    NOT NULL DEFAULT \'[]\',' \
                          '`step_nr`            int             NOT NULL DEFAULT \'0\',' \
                          'PRIMARY KEY (`id`),' \
                          'UNIQUE KEY `task_scheduler_id_uindex` (`id`)' \
                          ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
        self.mysql.raw_query(new_table_query)

        # Check if the table task_scheduler_log exists. If not, create it
        new_table_query = 'CREATE TABLE IF NOT EXISTS `task_scheduler_log` (' \
                          '`reload_id`      bigint          NOT NULL,' \
                          '`task_id`        int             NULL,' \
                          '`reload_status`  varchar(255)    NULL,' \
                          '`started_at`     datetime        NULL,' \
                          '`finished_at`    datetime        NULL' \
                          ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
        self.mysql.raw_query(new_table_query)

        # Check if the table check_task_execution_log exists. If not, create it
        new_table_query = 'CREATE TABLE IF NOT EXISTS `task_execution_log`(' \
                          '`reload_id`   bigint       NOT NULL,' \
                          '`task_id`     int          NULL,' \
                          '`log_level`   varchar(255) NULL,' \
                          '`created_at`  datetime     NULL,' \
                          '`line_number` int          NULL,' \
                          '`message`     longtext     NULL)' \
                          'ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
        self.mysql.raw_query(new_table_query)

        # Check if the table check_task_execution_steps exists. If not, create it
        new_table_query = 'CREATE TABLE IF NOT EXISTS `task_execution_steps`(' \
                          '`id`          bigint       NOT NULL AUTO_INCREMENT,' \
                          '`task_id`     int          NULL,' \
                          '`nr`          int          DEFAULT 0 NOT NULL,' \
                          '`description` varchar(255) DEFAULT \'ZzZzZz...\' NOT NULL,' \
                          'PRIMARY KEY (`id`),' \
                          'UNIQUE KEY `task_execution_steps_id_uindex` (`id`),' \
                          'UNIQUE INDEX `task_execution_steps_task_id_nr_uindex` (`task_id`, `nr`))' \
                          'ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
        self.mysql.raw_query(new_table_query)

        new_table_query = 'CREATE TABLE IF NOT EXISTS `task_variables`(' \
                          'id INT NOT NULL AUTO_INCREMENT,' \
                          'task_id INT NOT NULL,' \
                          'name VARCHAR(150) NOT NULL,' \
                          'type ENUM(\'INT\', \'TINYINT\', \'BIGINT\', \'FLOAT\', \'DOUBLE\', \'DATETIME\', \'TIMESTAMP\', \'TIME\', \'VARCHAR\', \'BLOB\', \'TEXT\', \'LONGBLOB\') NOT NULL,' \
                          'value VARCHAR(600) NOT NULL,' \
                          'temp_value VARCHAR(600) NOT NULL,' \
                          'PRIMARY KEY (`id`),' \
                          'UNIQUE KEY `task_variables_id_uindex` (`id`),' \
                          'UNIQUE INDEX `task_variables_name_value_uindex` (`task_id`, `name`, `value`), ' \
                          'INDEX `task_variables_name_index` (`name`),' \
                          'CONSTRAINT task_variables_task_scheduler_id_fk ' \
                          'FOREIGN KEY (`task_id`) REFERENCES task_scheduler (`id`) ON DELETE CASCADE)' \
                          'ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
        self.mysql.raw_query(new_table_query)

        # Add the variable 'email_errors_to' as default to the new added table if it doesn't exist for the current task
        response = self.mysql.select('task_variables', 'temp_value', f'WHERE name = \'email_errors_to\' AND task_id = {self.task_id}')
        if len(response) == 0:
            new_variables = f"INSERT INTO `task_variables` (`task_id`, `name`, `type`, `value`, `temp_value`) " \
                            f"VALUES ({self.task_id}, 'email_errors_to', 'TEXT', 'example@salure.nl, example2@salure.nl', 'example@salure.nl, example2@salure.nl')"
            self.mysql.raw_query(new_variables, insert=True)

    def create_task_execution_steps(self, step_details: list):
        """
        Check if the given steps already exists in the task_execution_steps table. If not, update or insert the values in the table
        :param step_details: list of dicts. Each dict must contain task details according to required_fields.
        Example: step_details = [
                                    {'nr': 1, 'description': 'test'},
                                    {'nr': 2, 'description': 'test2'}
                                ]
        :return: error (str) or response of mysql
        """

        # Check if the required fiels are available in the given list
        required_fields = ['nr', 'description']
        for step in step_details:
            for field in required_fields:
                if field not in step.keys():
                    return 'Field {field} is required in step {step}. Required fields are: {required_fields}'.format(field=field, step=step, required_fields=tuple(required_fields))

        # Reformat the list of dictionaries to a valid MySQL query
        values = ','.join(str((self.task_id, step['nr'], step['description'])) for step in step_details)
        response = self.mysql.raw_query("INSERT INTO task_execution_steps (`task_id`, `nr`, `description`) "
                                        "VALUES {step_values} ON DUPLICATE KEY UPDATE `description` = VALUES(description)".format(step_values=values), insert=True)
        return response
    
    def check_if_task_manual_started(self):
        """
        Check if the task manual is started of on schedule. If it's manual started, that's important for the variables in the db_variables function.
        In that case the dynamic variables should be used instead of the static ones
        :return: True of False
        """
        response = self.mysql.select('task_scheduler', 'run_instant', f'WHERE id = {self.task_id}')[0][0]
        if response == 1:
            return True
        else:
            return False
        
    def start_task(self):
        """
        Start the task and write this to the database. While the status is running, the task will not start again
        :return: if the update to the database is successful or not
        """
        return self.mysql.update('task_scheduler', ['status', 'step_nr'], ['RUNNING', 1], 'WHERE `id` = {}'.format(self.task_id))

    def db_variable(self, variable_name: str):
        """
        Get a value from the task_variables table corresponding with the given name. If the task is manually started
        (run_instant = 1), then the temp_value will be returned. This is to give the possibility for users in the frontend to run
        a task once manual with other values then normal without overwriting the normal values.
        :param variable_name: the name of the variable
        :return: the value of the given variable.
        """
        if self.task_manual_started:
            response = self.mysql.select('task_variables', 'temp_value', f'WHERE name = \'{variable_name}\' AND task_id = {self.task_id}')
        else:
            response = self.mysql.select('task_variables', 'value', f'WHERE name = \'{variable_name}\' AND task_id = {self.task_id}')
        if len(response) == 0:
            raise Exception(f'Variable with name \'{variable_name}\' does not exist')
        else:
            value = response[0][0]
            return value

    def write_execution_log(self, message: str, loglevel='INFO'):
        """
        Writes messages to the database. Give the message and the level of the log
        :param message: A string with a message for the log
        :param loglevel: You can choose between DEBUG, INFO, ERROR or CRITICAL (DEBUG is most granulated, CRITICAL the less)
        :return: If the write to the database is successful or not
        """
        allowed_loglevels = ['DEBUG', 'INFO', 'ERROR', 'CRITICAL']
        if loglevel not in allowed_loglevels:
            raise Exception('You\'ve entered a not allowed loglevel. Choose one of: {}'.format(allowed_loglevels))
        else:
            # Get the linenumber from where the logline is executed. Get the stacktrace of this action, jump 1 file up and pick then the linenumber (second item)
            linenumber = inspect.getouterframes(inspect.currentframe())[1][2]
            # Write the logline to the database, depends on the chosen loglevel in the task
            print('{} at line: {}'.format(message, linenumber))
            # Remove quotes from message since these break the query
            message = re.sub("[']", '', message)
            if self.loglevel == 'DEBUG':
                # Count the errors
                if loglevel == 'ERROR' or loglevel == 'CRITICAL':
                    self.error_count += 1
                return self.mysql.raw_query(
                    "INSERT INTO `task_execution_log` VALUES ({}, {}, '{}', '{}', {}, '{}')".format(self.run_id, self.task_id, loglevel, datetime.datetime.now(), linenumber, message), insert=True)
            elif self.loglevel == 'INFO' and (loglevel == 'INFO' or loglevel == 'ERROR' or loglevel == 'CRITICAL'):
                # Count the errors
                if loglevel == 'ERROR' or loglevel == 'CRITICAL':
                    self.error_count +=1
                return self.mysql.raw_query(
                    "INSERT INTO `task_execution_log` VALUES ({}, {}, '{}', '{}', {}, '{}')".format(self.run_id, self.task_id, loglevel, datetime.datetime.now(), linenumber, message), insert=True)
            elif self.loglevel == 'ERROR' and (loglevel == 'ERROR' or loglevel == 'CRITICAL'):
                self.error_count += 1
                return self.mysql.raw_query(
                    "INSERT INTO `task_execution_log` VALUES ({}, {}, '{}', '{}', {}, '{}')".format(self.run_id, self.task_id, loglevel, datetime.datetime.now(), linenumber, message), insert=True)
            elif self.loglevel == 'CRITICAL' and loglevel == 'CRITICAL':
                self.error_count += 1
                return self.mysql.raw_query(
                    "INSERT INTO `task_execution_log` VALUES ({}, {}, '{}', '{}', {}, '{}')".format(self.run_id, self.task_id, loglevel, datetime.datetime.now(), linenumber, message), insert=True)

    def update_execution_step(self, step_number: int):
        """
        Update the current step number in the task_scheduler table so that user's in the frontend of SalureConnect can see where a task is at any moment
        :param step_number: Give only a number
        :return: nothing
        """
        # Update the step number in the task_scheduler table
        return self.mysql.update('task_scheduler', ['step_nr'], [step_number], 'WHERE `id` = {}'.format(self.task_id))

    def error_handling(self, e: Exception, breaking=True):
        """
        This function handles errors that occur in the scheduler. Logs the traceback, updates run statuses and notifies users
        :param e: the Exception that is to be handled
        :param task_id: The scheduler task id
        :param mysql_con: The connection which is used to update the scheduler task status
        :param logger: The logger that is used to write the logging status to
        :param breaking: Determines if the error is breaking or code will continue
        :param started_at: Give the time the task is started
        :return: nothing
        """
        # Format error to a somewhat readable format
        exc_type, exc_obj, exc_tb = sys.exc_info()
        error = str(e)[:400].replace('\'', '').replace('\"', '') + ' | Line: {}'.format(exc_tb.tb_lineno)
        # Get scheduler task details for logging
        task_details = self.mysql.select('task_scheduler', 'docker_image, runfile_path', 'WHERE id = {}'.format(self.task_id))[0]
        taskname = task_details[0]
        customer = task_details[1].split('/')[-1].split('.')[0]

        if breaking:
            # Set scheduler status to failed
            self.mysql.update('task_scheduler', ['status', 'last_reload', 'last_error_message', 'step_nr'],
                              ['IDLE', datetime.datetime.now(), 'Failed', 0],
                              'WHERE `id` = {}'.format(self.task_id))
            # Log to database
            self.mysql.raw_query(
                "INSERT INTO `task_execution_log` VALUES ({}, {}, 'CRITICAL', '{}', {}, '{}')".format(self.run_id, self.task_id,
                                                                                                      datetime.datetime.now(),
                                                                                                      exc_tb.tb_lineno,
                                                                                                      error),
                insert=True)
            self.mysql.raw_query(
                "INSERT INTO `task_scheduler_log` VALUES ({}, {}, 'Failed', '{}', '{}')".format(self.run_id, self.task_id,
                                                                                                self.started_at,
                                                                                                datetime.datetime.now()),
                insert=True)
            # Notify users on Slack and If the variable self.send_mail_after_errors is set to True, send an email with the message that the task is failed
            SalureFunctions.send_error_to_slack(customer, taskname, 'failed')
            if self.email_after_errors:
                self.email_errors(failed=True)
            raise Exception(error)
        else:
            self.mysql.raw_query(
                "INSERT INTO `task_execution_log` VALUES ({}, {}, 'CRITICAL', '{}', {}, '{}')".format(self.run_id, self.task_id,
                                                                                                      datetime.datetime.now(),
                                                                                                      exc_tb.tb_lineno,
                                                                                                      error),
                insert=True)
            SalureFunctions.send_error_to_slack(customer, taskname, 'contains an error')
        self.error_count += 1


    def finish_task(self, reload_instant=False):
        """
        At the end of the script, write the outcome to the database. Write if the task is finished with or without errors, Email to a contactperson if this variable is given in the
        variables table. Also clean up the execution_log table when the number of lines is more than 1000
        :return:
        """
        # If reload instant is true, this adds an extra field 'run_instant' to the update query, and sets the value to 1. This makes the task reload immediately after it's finished
        field = ['run_instant', 'next_reload'] if reload_instant else []
        value = ['1', datetime.datetime.now()] if reload_instant else []
        if self.error_count > 0:
            self.mysql.update('task_scheduler', ['status', 'last_reload', 'last_error_message', 'step_nr'],
                              ['IDLE', datetime.datetime.now(), 'FinishedWithErrors', 0],
                              'WHERE `id` = {}'.format(self.task_id))
            self.mysql.raw_query(
                "INSERT INTO `task_scheduler_log` VALUES ({}, {}, 'FinishedWithErrors', '{}', '{}')".format(self.run_id, self.task_id, self.started_at, datetime.datetime.now()), insert=True)
            # If the variable self.send_mail_after_errors is set to True, send an email with the number of errors to the given user
            if self.email_after_errors:
                self.email_errors(failed=False)
        else:
            self.mysql.update('task_scheduler', ['status', 'last_reload', 'last_error_message', 'step_nr'] + field,
                              ['IDLE', datetime.datetime.now(), 'FinishedSucces', 0] + value,
                              'WHERE `id` = {}'.format(self.task_id))
            self.mysql.raw_query(
                "INSERT INTO `task_scheduler_log` VALUES ({}, {}, 'FinishedSuccess', '{}', '{}')".format(self.run_id, self.task_id, self.started_at, datetime.datetime.now()), insert=True)
            # Clean up execution log
        self.mysql.delete("task_execution_log",
                          "WHERE task_id = {} AND reload_id NOT IN (SELECT reload_id FROM (SELECT reload_id FROM `task_execution_log` ORDER BY created_at DESC LIMIT 1000) temp)".format(
                              self.task_id))

    def email_errors(self, failed):
        # The mails to email to should be stored in the task_variables table with the variable email_errors_to
        email_to = self.db_variable('email_errors_to').split(',')
        if isinstance(email_to, list):
            # The email_errors_to variable is a simple string. Convert it to a list and add a name because mandrill is asking for it
            email_list = []
            for i in email_to:
                email_list.append({'name': 'SalureConnect User', 'mail': i.strip()})
            # Set the content of the mail and all other stuff
            email_from = 'connect@salure.nl'
            name_from = 'SalureConnect'
            task = self.mysql.select(table='task_scheduler', selection='title', filter=f'WHERE id = {self.task_id}')[0][0]
            finished_at = self.mysql.select(table='task_scheduler', selection='last_reload', filter=f'WHERE id = {self.task_id}')[0][0]
            if failed:
                subject = f'Task \'{task}\' is failed'
                content = f'Task \'{task}\' with ID \'{self.task_id}\' have runned and is stopped at {finished_at}. ' \
                          f'The task is failed. ' \
                          f'Click <a href="https://salureconnect.com/connectors/task-scheduler/">here</a> to visit the scheduler in SalureConnect to check the logs and see more information about this errors.'
            else:
                subject = f'Task \'{task}\' is finished with errors'
                content = f'Task \'{task}\' with ID \'{self.task_id}\' have runned and is finished at {finished_at}. ' \
                          f'The task is finished with {self.error_count} errors. ' \
                          f'Click <a href="https://salureconnect.com/connectors/task-scheduler/">here</a> to visit the scheduler in SalureConnect to check the logs and see more information about this errors.'
            MailClient().send_mail(api_token=self.mandrill_api_token, email_to=email_list, email_from=email_from, name_from=name_from, subject=subject, content=content, language='EN')