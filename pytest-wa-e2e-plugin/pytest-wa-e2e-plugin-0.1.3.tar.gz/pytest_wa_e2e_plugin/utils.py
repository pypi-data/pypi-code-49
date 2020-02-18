import time
import yaml
import logging
import operator

from py_wa_adb.wa_adb import WA_ADB, datetime_to_epoch
from py_wa_adb.wa_sqlite import WA_SQLITE


class WAEndToEnd(object):
    """ Base Class that will contain any related 
    information needed for the tests.
    """

    def __init__(self, wa_bot_number):
        """ Constructor method.
        Defines wa_bot_number to the value recived in the wa_bot_number argument
        """
        self.wa_bot_number = wa_bot_number


def parse_yaml_data_file(file_path):
    """ Read the contents of of the file located at `file_path`
    and return the yaml parsed object from it.
    """
    with open(file_path, "r+") as f:
        content = f.read()
        yaml_input = yaml.load(content, Loader=yaml.Loader)
    return yaml_input




def log_received_messages(messages, last_n_messages):
    for i, message in enumerate(messages[last_n_messages * -1:], 1):
        logging.info("Received message {}:\n {} \n---------------\n".format(i,message[-2].decode()))

def log_sent_message(message):
    logging.info("SENDING MESSAGE:\n {} \n---------------\n".format(message))


def wait_for_n_messages(wa_adb_instance, expected_n_messages, n_iterations=10, iteration_sleep_time=3):
    for _ in range(n_iterations):
        try:
            post_restart_messages = wa_adb_instance.get_messages()
            len_post_messages = len(post_restart_messages)
            if expected_n_messages == len_post_messages:
                break
            else:
                time.sleep(iteration_sleep_time)
        except Exception as e:
            
            time.sleep(iteration_sleep_time)
    else:
        wait_time = n_iterations * iteration_sleep_time
        err_message = f"Failed got {len_post_messages} absolute messages in {wait_time} seconds when "\
        f"{expected_n_messages} absolute messages were expected"
        logging.info(err_message)
        raise TimeoutError(err_message)


def send_expect_n_and_validate(
    TEXT_TO_BE_SENT, EXPECT_N_MESSAGES, VALIDATE_FUNCTION, *args
):
    wa_adb = WA_ADB()

    def inner_wrapper(received_function):
        
        def double_wrapper(test_run_instance):
            
            received_function(test_run_instance)
            # ttbs (text to be sent)
            if TEXT_TO_BE_SENT is not None:
                ttbs = TEXT_TO_BE_SENT if type(TEXT_TO_BE_SENT) is str else TEXT_TO_BE_SENT(test_run_instance)
            else:
                ttbs = None
            log_sent_message(ttbs)
            prev_messages = wa_adb.get_messages()
            if ttbs:
                wa_adb.send_text_message(test_run_instance.wa_bot_number, ttbs)
            if EXPECT_N_MESSAGES is not None:
                starting_offset = len(prev_messages) + (0 if not TEXT_TO_BE_SENT else 1)
                try:
                    wait_for_n_messages(
                        wa_adb,
                        starting_offset + EXPECT_N_MESSAGES
                    )
                except TimeoutError as e:
                    post_wait_messages = wa_adb.get_messages()
                    received_relative_messages = len(post_wait_messages[starting_offset:])
                    log_received_messages(post_wait_messages, received_relative_messages)
                    
                    # Original error message.
                    timeout_error_message = e.args[0]
                    timeout_error_message += f"\n Received {received_relative_messages} relative messages "
                    timeout_error_message += f"when {EXPECT_N_MESSAGES} relative messages were expected \n"
                    timeout_error_message += f"\n Received messages: \n"
                    for i, received_message in enumerate(post_wait_messages[starting_offset:], 1):
                        timeout_error_message += f"Message no. {i}: "
                        timeout_error_message += received_message[-2].decode()
                        timeout_error_message += "\n"
                    raise TimeoutError(timeout_error_message)
            post_wait_messages = wa_adb.get_messages()
            if EXPECT_N_MESSAGES is not None:
                log_received_messages(post_wait_messages, EXPECT_N_MESSAGES)
            VALIDATE_FUNCTION(post_wait_messages, test_run_instance,*args)
        
        return double_wrapper

    return inner_wrapper

def assert_helper(
    compared_message, expected_message, apply_operator,
    err_message=None
):
    """ Applies an expected operator function or
    any given function with compared_message and expected_message
    as it's arguments and using this result with an assert 
    statement and a given err_message for it if `err_message`
    is not None
    """
    if err_message:
        assert apply_operator(compared_message, expected_message) , \
        err_message
    else:
        assert apply_operator(compared_message, expected_message)

def assert_equals(compared_message, expected_message, 
    apply_operator=operator.eq
):
    """ Calls assert helper with default operator equals
    and custom error message 
    """
    assert_helper(
        compared_message,
        expected_message,
        apply_operator=apply_operator,
        err_message="{} is not equal to expected message: {}".format(
            compared_message, expected_message
        )
    )

def assert_contains(
    compared_message, expected_message, 
    apply_operator=operator.contains
):
    """ Calls assert helper with default operator contains
    and custom error message 
    """
    assert_helper(
        compared_message,
        expected_message,
        apply_operator=apply_operator,
        err_message="{} expected message is not in received message: {}".format(expected_message, compared_message)
    )