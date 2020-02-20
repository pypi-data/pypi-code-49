# Implementation libs
# Copyright Netflix, 2019
import sys
from logging import getLogger
from typing import Callable

logger = getLogger("kaiju-automator-lib")

NO_DEVICE_ID = "No device locator was provided"
BAD_DEVICE_ID = "Failed to lookup device"
CANCEL_OR_TRY_LATER = "Device is currently busy"
DEVICE_NEVER_STARTED = "INT did not receive any events from the device"
DEVICE_STOPPED_AFTER_STARTING = "INT has not received any events from the device in over"
REQUEST_STATUS_FAILED = "The automator request failed without talking to the automator."
INCOMPLETE_PLAN_REQUEST_ERROR = "body missing"
MISSING_RAE_TARGET = "rae id missing"

user_guidance_map = {
    NO_DEVICE_ID: "\tIt looks like you didn't provide a device identifier in your request to the automator. Make sure you "
    'provide something like this: "target": {"esn":"foo"}',
    BAD_DEVICE_ID: "\tThe device ID you provided is missing from Network Agent and/or the ADB module. Open the RAE web UI and "
    "validate it responds to start and stop commands, copy-paste the ESN back to your command, and if that "
    "doesn't work, restart all the automator related modules.",
    CANCEL_OR_TRY_LATER: "\tThe automator thinks the device is busy. You can issue a cancel to stop what it is doing and then "
    "issue a new request.",
    DEVICE_NEVER_STARTED: "\tThe automator told the device to start, but the device never started sending messages to the "
    "automator. DIAL or ADB may need assistance to get the device to a known good state, such as "
    "trusting ADB or using DIAL stop and start commands to get the device into a state known to DIAL.",
    DEVICE_STOPPED_AFTER_STARTING: "\tThe device started running tests, but stopped responding before the test ended. This "
    "usually means a test crashed outright.",
    REQUEST_STATUS_FAILED: "\tThe request to the automator failed without actually reaching the automator. This can mean the broker is "
    "unreachable, or that the automator is not responding. Open the RAE web UI on the target RAE and make sure the "
    "Automator module is running, and that this computer can ping the target broker.",
    INCOMPLETE_PLAN_REQUEST_ERROR: '\tThe test plan response came back without response["body"]["error"]: File a ticket and we can help '
    "diagnose this and provide hints.",
    MISSING_RAE_TARGET: "\tThe RAE ID was missing or invalid. We accept the hostname form: r3000111.raehub.com or the name of a security "
    "configuration directory from ~/.config/netflix",
    "Connection refused": "\tThe remote MQTT broker actively refused requests to connect. This could mean an incorrect broker or RAE argument, "
    "or networking problems.",
}


def guide_user(error_string: str) -> None:
    """
    Provide user guidance for errors from the automator.

    Always raises ValueError, but with a user prompt.
    Patterns and user prompts are stored above.

    :param error_string: A string to print help for, and then raise ValueError
    :return:
    """
    logger.error("")

    for pattern in user_guidance_map.keys():
        if pattern in error_string:
            logger.error("\tReceived this error:")
            logger.error("==========")
            logger.error(error_string)
            logger.error("==========")
            logger.error("")
            logger.error("")
            logger.error(user_guidance_map[pattern] + "\n")
            logger.error("==========")
            return

    logger.error("\tReceived this error:")
    logger.error("==========")
    logger.error(error_string)
    logger.error("==========")


def user_guidance_decorator(func: Callable):
    """
    Handle uncaught errors by printing helpful messages.
    """

    def print_help_and_exit(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except BaseException as ee:
            guide_user(str(ee))

    return print_help_and_exit


def hide_stacktraces_decorator(func: Callable):
    """
    Handle uncaught errors by forcefully exiting the process.

    This is meant to be the last line of defense against uncaught errors.
    """

    def just_exit(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except BaseException:
            sys.exit(-1)

    return just_exit
