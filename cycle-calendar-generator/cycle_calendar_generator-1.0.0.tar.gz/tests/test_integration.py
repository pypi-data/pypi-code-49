#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Integration test for `cycle_calendar_generator` package."""

import unittest
import os
import sys
import shutil
import subprocess
from pathlib import Path
import datetime

from cycle_calendar_generator import cycle_calendar_generator

import ics
import arrow

CURRENT_WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INTEGRATION_TEST_FOLDER = os.path.join(
    CURRENT_WORKING_DIRECTORY,
    'integration_test'
    )
TEST_FILES_FOLDER = os.path.join(INTEGRATION_TEST_FOLDER, 'testing_files')
TEST_EXPECTED_OUTPUT_FOLDER = os.path.join(INTEGRATION_TEST_FOLDER, 'expected')
TEST_TEMP_FOLDER = os.path.join(INTEGRATION_TEST_FOLDER, 'temp')
TEST_OUTPUT_FOLDER = os.path.join(TEST_TEMP_FOLDER, 'output')
SCRIPT_NAME = 'cycle_calendar_generator'


class Test_integration(unittest.TestCase):
    """Tests function to get folder argument and give default if none given"""

    @classmethod
    def setUpClass(cls):
        if (not os.path.exists(TEST_EXPECTED_OUTPUT_FOLDER)):
            os.mkdir(TEST_EXPECTED_OUTPUT_FOLDER)
        if (not os.path.exists(TEST_TEMP_FOLDER)):
            os.mkdir(TEST_TEMP_FOLDER)

    def setUp(self):
        # copy test input files from TEST_FILES_FOLDER to TEST_TEMP_FOLDER
        for file in cycle_calendar_generator.scandir_with_version_check(
                TEST_FILES_FOLDER,
                cycle_calendar_generator.VERSION_MAJOR,
                cycle_calendar_generator.VERSION_MINOR):
            source_path = file.path
            dest_path = os.path.join(TEST_TEMP_FOLDER, file.name)
            shutil.copy(source_path, dest_path)

    def tearDown(self):
        # delete all files and folders in TEST_TEMP_FOLDER
        for file in cycle_calendar_generator.scandir_with_version_check(
                TEST_TEMP_FOLDER,
                cycle_calendar_generator.VERSION_MAJOR,
                cycle_calendar_generator.VERSION_MINOR):
            if file.is_dir():
                shutil.rmtree(file.path)
            else:
                os.remove(file.path)

    def test_script_works_in_normal_case(self):
        # run script
        exit_code = subprocess.run(['python3', '-m',
                                    SCRIPT_NAME, TEST_TEMP_FOLDER])
        # read output icals into dictionary (user name as key)
        output_files = {}
        for file in cycle_calendar_generator.scandir_with_version_check(
                TEST_OUTPUT_FOLDER,
                cycle_calendar_generator.VERSION_MAJOR,
                cycle_calendar_generator.VERSION_MINOR):
            if file.is_file():
                path, filename = os.path.split(file.path)
                user_name = os.path.splitext(filename)[0]
                with open(file.path) as ical:
                    calendar = ics.Calendar(ical.read())
                sorted_events = sorted(calendar.events,
                                       key=lambda event:event.begin)
                output_files[user_name] = sorted_events
        # read expected output icals into similar dictionary
        expected_files = {}
        for file in cycle_calendar_generator.scandir_with_version_check(
                TEST_EXPECTED_OUTPUT_FOLDER,
                cycle_calendar_generator.VERSION_MAJOR,
                cycle_calendar_generator.VERSION_MINOR):
            if file.is_file():
                path, filename = os.path.split(file.path)
                user_name = os.path.splitext(filename)[0]
                with open(file.path) as ical:
                    calendar = ics.Calendar(ical.read())
                sorted_events = sorted(calendar.events,
                                       key=lambda event:event.begin)
                expected_files[user_name] = sorted_events
        # assert both dicts have same size
        self.assertEqual(len(output_files), len(expected_files))
        # assert each key in output has matching in expected
        for key in output_files.keys():
            self.assertTrue(key in expected_files)
            # assert values from matching keys are the same
            output_events = output_files[key]
            expected_events = expected_files[key]
            for i in range(len(output_events)):
                output_event = output_events[i]
                expected_event = expected_events[i]
                self.assertEqual(output_event.name, expected_event.name)
                # Output times already use local timezone,
                # but expected times use tz in iCal file (China Std. Time)
                # Expected times need to have tz replaced with local tz
                # without changing anything else
                output_event_start = output_event.begin.to('utc')
                expected_event_start = expected_event.begin.replace(
                    tzinfo=cycle_calendar_generator.LOCAL_TIMEZONE
                ).to('utc')
                output_event_end = output_event.end.to('utc')
                expected_event_end = expected_event.end.replace(
                    tzinfo=cycle_calendar_generator.LOCAL_TIMEZONE
                ).to('utc')
                self.assertEqual(output_event_start, expected_event_start)
                self.assertEqual(output_event_end, expected_event_end)
