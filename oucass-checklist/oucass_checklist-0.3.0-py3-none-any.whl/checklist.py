'''
Routine to run on local ground station for CASS flights
Saves txt files for aircraft information (header) and each individual flight
Written by: Jessica Blunt
Updated: January 2020
Based on code by Brian Greene, November 2019
Center for Autonomous Sensing and Sampling
University of Oklahoma
'''

import os
import sys
import csv
import click
import datetime as dt
from datetime import datetime
from contextlib import suppress
import pickle
import logging
import json


# First see if backup.log exists
if "backup.log" in os.listdir():
    # Is the file complete?
    if "DONE" in open("backup.log").readline():
        os.remove("backup.log")
    # If the file is incomplete, handle in checklist.resume()
# If the file does not exist, nothing needs to be done here


logging.basicConfig(filename="backup.log", level=0)
backup = logging.getLogger("backup")

class ExitException(BaseException):
    def __init__(self):
        return


class UI:

    def __init__(self):
        self.dirname = os.path.dirname(__file__)
        self.ndict_path = os.path.join(self.dirname, "user_settings", "ndict.pkl")
        self.locations_path = os.path.join(self.dirname, "user_settings", "known_locations.pkl")
        self.objectives_path = os.path.join(self.dirname, "user_settings", "objectives.pkl")
        self.step_index = 0
        self.overwrite = False

    def back(self):
        if self.step_index > 0:
            self.step_index -= 1
            self.overwrite = True
            self.to_do.pop(-1)
            raise ExitException

    def get_index(self, list, message=None, free_response=True, multiple=False):
        """ Recursively call until valid index chosen from specified array
        """
        if message is not None:
            print('\n' + message)

        for i in range(len(list)):
            print("\t" + str(i+1) + " - " + str(list[i]))
        print("\t" + str(len(list)+1) + " - Other")
        i_str = input(">> ")
        if i_str in [str(i) for i in range(1, len(list) + 1, 1)] or multiple:
            if multiple and "!" not in i_str:
                elems = i_str.split(";")
                to_return = ''
                for i in range(len(elems)):
                    to_return = to_return + list[int(elems[i]) - 1] + "; "

                to_return = to_return[:-2]

            else:
                to_return = list[int(i_str) - 1]
        elif i_str == str(len(list) + 1):
            if free_response:
                to_return = self.no_commas(message)
            else:
                to_return = "Other"
        elif "!" in i_str:
            self.back()
            raise ExitException
        else:
            print("Please enter valid option")
            to_return = self.get_index(list, message, free_response)
        return to_return


    def no_commas(self, message):
        """ Ensure no commas input
        """
        print(message)
        x = input(">> ")
        while "," in x:
            print("Please enter valid name with no commas")
            x = self.no_commas(message)
        if "!" in x:
            try:
                self.back()
                raise ExitException()
            except Exception:
                print("The \"!\" option is not available right now")
                x = self.no_commas(message)
        if "remarks" not in message and "Remarks" not in message:
            while x in "":
                print("This field is non-optional")
                x = self.no_commas(message)
        return x


# noinspection SpellCheckingInspection
class Checklist(UI):

    def __init__(self):
        #
        # Load existing data
        #
        UI.__init__(self)
        self.ndict = pickle.load(open(self.ndict_path, "rb"))
        self.known_locations = \
            pickle.load(open(self.locations_path, "rb"))

        #
        # Get needed system info
        #
        self.localNextcloud = True
        self.user = os.path.expanduser("~")
        self.dt_now = datetime.now(tz=dt.timezone(dt.timedelta(hours=0)))
        self.dt_today = datetime(day=self.dt_now.day, month=self.dt_now.month,
                                 year=self.dt_now.year)
        try:
            self.log_dir = os.path.join(self.user, "Nextcloud", "Logs")
            if not os.path.exists(self.log_dir):
                os.mkdir(self.log_dir)
        except FileNotFoundError:
            self.localNextcloud = False
            self.log_dir = os.path.join(self.user, "Logs")
            if not os.path.exists(self.log_dir):
                os.mkdir(self.log_dir)


        #
        # Directions
        #
        print("Answer all questions without commas. \nTo go back, enter \"!\"\n"
              "To enter admin mode, set the operator's name to \"admin\"\n")


        #
        # Define to-do list to track progress, allow to go back
        #
        self.to_do = ["operator", "platform", "find_header", "location",
                      "flight_pattern", "objective", "legal",
                      "scoop", "weather", "planned_alt", "preflight_checks",
                      "start_info", "end_info", "emergency",
                      "postflight_checks", "comment", "nextcloud"]
        self.step_index = 0
        self.overwrite = False  # if True, user MUST enter answer for ALL
        # steps, even if the answers have previously been entered

        #
        # Hold all info gathered
        #
        self.flight_info = {}
        self.is_first = False

        # Check if a previous run was left incomplete
        self.recover()

        # start the process...
        while self.step_index < len(self.to_do):
            with suppress(ExitException):
                self.step()

        # Finish
        backup.info("DONE")
        logging.shutdown()
        os.remove("backup.log")

    def step(self):
        self.__getattribute__(self.to_do[self.step_index])()
        self.step_index += 1
        self.overwrite = False
        backup.info(str(self.step_index) + " --- " + str(self.flight_info))

    def get_time(self, date):
        time_str = input(">> ")
        try:
            if (len(time_str) < 4):
                raise ValueError()
            dt = datetime.strptime(f"{date.strftime('%Y%m%d')}_{time_str}",
                                   "%Y%m%d_%H%M")
        except ValueError:
            print("Please enter valid 24-hr time in UTC as HHMM")
            dt = self.get_time(date)
        return dt

    def define_new_loc(self, group):
        """ Allow user to add, remove, and change order of locations

        """
        choice = self.no_commas("Would you like to save this location? [y/n]")
        if choice in "yes" or choice in "YES" or choice in "Yes":
            write_new_loc = True
            if group in self.known_locations.keys():
                region = self.known_locations[group]\
                    [list(self.known_locations[group].keys())[0]]["region"]
                self.flight_info["region"] = region
            else:
                choice = self.no_commas("Are you in North America? [y/n]")
                if choice in "yesYESYes":
                    region = "north_america"
                else:
                    region = self.no_commas("What region from this list are you"
                                            " in?\n"
                                            "http://cfconventions.org/"
                                            "Data/standardized-region-list/"
                                            "standardized-region-list.html")
                self.flight_info["region"] = region

            long_name = self.no_commas("What is the full name of your "
                                       "location?")
            self.flight_info["location_name"] = long_name
            location_id = self.no_commas("What 4-5 character ID would you like "
                                         "to assign to " + long_name + "?")
            self.flight_info["location_id"] = location_id

        elif choice in "no" or choice in "NO" or choice in "No":
            self.flight_info["location_id"] = None
            write_new_loc = False

        lat = self.no_commas("What your latitude?")
        self.flight_info["lat"] = lat
        lon = self.no_commas("What is your longitude?")
        self.flight_info["lon"] = lon
        alt = self.no_commas("What is your altitude in meters?")
        self.flight_info["alt"] = alt
        choice = self.no_commas("Is there a Mesonet station nearby? [y/n]")
        if choice in "yesYesYES":
            mesonet_id = self.no_commas("Enter the station's 4-letter "
                                        "identifier.")
            self.flight_info["mesonet_id"] = mesonet_id
        else:
            mesonet_id = None
            self.flight_info["mesonet_id"] = mesonet_id

        if write_new_loc:
            if group not in self.known_locations.keys():
                self.known_locations[group] = {}
            self.known_locations[group][location_id] = \
                {"location_name": long_name, "lat": lat,
                 "lon": lon, "surface_altitude": alt,
                 "region": region, "mesonet_id": mesonet_id}
            pickle.dump(self.known_locations,
                        open(self.locations_path, "wb"))

            loc_info = {"location_name": long_name, "lat": lat, "lon": lon,
                        "surface_altitude": alt,
                        "region": region, "mesonet_id": mesonet_id}
        else:
            loc_info = {"lat": lat, "lon": lon, "surface_altitude": alt,
                        "mesonet_id": mesonet_id}

        for key in loc_info.keys():
            self.flight_info[key] = loc_info[key]

    def operator(self):
        if "operator" not in self.flight_info or self.overwrite:
            inp = self.no_commas("Name of person filling out checklist: ")
            if inp in "AdminadminADMIN":
                Admin()
                sys.exit()
            else:
                self.flight_info["operator"] = inp

    def find_header(self):

        self.is_first = self.no_commas("Is this your first flight today with "
                                       "this UAV and authorization type? y/n")
        while self.is_first.lower() not in ["y", "n"]:
            self.is_first = self.no_commas("Enter y or n")
        if self.is_first in "y":
            self.is_first = True
            return
        else:
            self.is_first = False

        #
        # find associated header file
        #
        possible_headers = []
        for file in os.listdir(self.log_dir):
            print("Checking if " + file + " could be the header...")
            if self.dt_today.strftime('%Y%m%d') in file \
               and self.flight_info["platform_id"] in file \
               and "log_header.csv" in file \
               and "." not in file[0]:
                possible_headers.append(file)

        if len(possible_headers) < 1:
            print("No header files found. User will be prompted for required "
                  "information.")
            self.is_first = True
            return
        elif len(possible_headers) == 1:
            header_path = os.path.join(self.log_dir, possible_headers[0])
        else:
            header_path = \
                os.path.join(self.log_dir,
                             self.get_index(possible_headers,
                                            message="Which header file should "
                                                    "be used?",
                                            free_response=False))

        header = next(csv.DictReader(open(header_path, newline='')))

        for key in header.keys():
            self.flight_info[key] = header[key]

    def platform(self):
        """ Prompt user for platform ID
        """
        if "platform_id" not in self.flight_info.keys() or self.overwrite:
            id = self.get_index(list(self.ndict.keys()),
                                message="Enter aircraft N number:")
            if id in "Other":
                self.update_ndict()
                self.platform()
            else:
                self.flight_info["platform_id"] = id

    def location(self):
        """ Ask user for location from list
        """
        if "location_id" not in self.flight_info.keys() or self.overwrite:
            loc_keys = list(self.known_locations.keys())

            # Find location group (state or country)
            print("Where are you?")
            group = self.get_index(loc_keys,
                                   "What state (US) or country are you in?")

            if group not in self.known_locations.keys():
                self.define_new_loc(group)

            specific_loc_keys = list(self.known_locations[group].keys())
            print("Which location?")
            location_id = self.get_index(specific_loc_keys, free_response=False)
            if location_id in "Other":
                self.define_new_loc(group)
            else:
                loc_info = self.known_locations[group][location_id]
                self.flight_info["location_id"] = location_id
                for key in loc_info.keys():
                    if loc_info[key] is None:
                        self.flight_info[key] = ""
                    else:
                        self.flight_info[key] = loc_info[key]

    def flight_pattern(self):

        if "flight_pattern" not in self.flight_info.keys() or self.overwrite:
            pattern_list = ["Direct profile", "Helical profile",
                            "Stair step profile",
                            "Hover", "Photogrammetry grid", "Test flight"]
            self.flight_info["flight_pattern"] = \
                self.get_index(pattern_list,
                               message="Enter flight pattern (no commas): ")

    def objective(self):
        if "objective" not in self.flight_info.keys() or self.overwrite:
            print("Chose one or more of the following objectives. If\n"
                  "you chose more than one, separate them with \";\"")
            obj_list = pickle.load(open(self.objectives_path, "rb"))
            self.flight_info["objective"] = \
                self.get_index(obj_list, message="Objective(s): ",
                               multiple=True)

    def legal(self):
        if "authorization_type" not in self.flight_info.keys() \
                or self.overwrite:
            print("Flight permissions: ")
            per_list = ["COA", "Part 107"]
            per_name = self.get_index(per_list, free_response=False)
            self.flight_info["authorization_type"] = per_name
            if per_name == "COA":
                self.flight_info["pilots_on_site"] = \
                    self.no_commas("List names of all pilots on site separated "
                                   "by \";\"")
            else:
                self.flight_info["pilots_on_site"] = ""
        if "PIC" not in self.flight_info.keys() \
                or self.overwrite:
            self.flight_info["PIC"] = self.no_commas("Pilot in Command: ")

    def scoop(self):
        if "scoop" not in self.flight_info.keys() or self.overwrite:
            if self.ndict[self.flight_info["platform_id"]]:
                print("Scoop ID:")
                self.flight_info["scoop_id"] = \
                    self.get_index(["A", "B", "C", "D"],
                                   message="Enter scoop number: ")
            else:
                self.flight_info["scoop_id"] = ""

    def weather(self):
        if "cloud" not in self.flight_info.keys() or self.overwrite:
            print("Cloud cover: ")
            sky_list = ["0%", "1-25%", "26-50%", "51-75%", "76-100%"]
            cloud = self.get_index(sky_list, free_response=False)
            if "76-100%" in cloud:  # swapped order - 0% is in 10 0%
                r = self.no_commas("Is it precipitating? If yes be sure to "
                                   "denote type in remarks. y/n")
                while r not in ["y", "n"]:
                    r = self.no_commas("Enter y or n")
                if r == "y":
                    rain = "yes"
                else:
                    rain = "no"
            else:
                rain = "no"
            self.flight_info["cloud"] = cloud
            self.flight_info["rain"] = rain

        if self.flight_info["mesonet_id"] in "":  # this is in locations
            self.flight_info["wind_from_direction"] = \
                self.no_commas("What direction (in degrees) is the "
                               "wind coming from?")
            self.flight_info["wind_speed"] = \
                self.no_commas("What is the ambient wind speed (in m/s)?")
            self.flight_info["wind_speed_gust"] = \
                self.no_commas("About how fast is the wind gusting to? "
                               "(in m/s)")
        else:
            self.flight_info["wind_from_direction"] = ""
            self.flight_info["wind_speed"] = ""
            self.flight_info["wind_speed_gust"] = ""

    def planned_alt(self):
        if "max_planned_alt" not in self.flight_info or self.overwrite:
            self.flight_info["max_planned_alt"] = self.no_commas("Planned "
                                                                 "maximum "
                                                                 "altitude in "
                                                                 "meters AGL: ")

    def preflight_checks(self):
        if self.is_first:
            checklist = [
                "Check for visual obstacles and potential source of "
                "interference (antennas, electrical lines, metal structures) ",
                "Clear and agree on a takeoff and landing zone ",
                "Check current wind speed and humidity at the location, decide "
                "if flight safe",
                "Perform visual inspection of the vehicle - props not damaged, "
                "props tight, \ncenter of gravity, orientation and connection "
                "of RH, GPS, data transfer antennas, \nmechanical check ",
                "Check Mission Planner laptop battery charge ",
                "Turn on controller and check voltage ",
                "Confirm a fresh battery is on the UAS",
                "Plug in the UAV's battery and let it boot up stationary for "
                "20 seconds ",
                "Launch CASS live data streaming software",
                "Confirm real-time plotter is running and data is showing up "
                "and in correct range",
                "Run Mission Planner",
                "Connect telemetry (TCP connection, confirm heartbeat) ",
                "Confirm no error messages with Mission Planner ",
                "BATTERY",
                "Confirm GPS fix type (outdoors must get 3D fix) ",
                "Check flight data logging in Mission Planner",
                "Place vehicle at launch point",
                "Based on the weather conditions, agree on a flight pattern "
                "and maximum safe altitude",
                "Create the waypoints mission on Mission Planner and send it "
                "to the UAS",
                "Check flight mode on controller",
                "Review flight plan - verbal and on Mission Planner",
                "Test audio communications among participants",
                "Check if all participants ready for flight",
                "Press the safety button on the vehicle until solid red - now "
                "live and armed",
                "Check the LED for status of the vehicle. Should see a "
                "blinking green light indicating GPS lock",
                "Arm motors, call clear props, and proceed to execute "
                "the mission"]
        else:
            checklist = [
                "Check current wind speed and humidity at the location, "
                "decide if flight safe",
                "Perform visual inspection of the vehicle - props not damaged, "
                "props tight, \ncenter of gravity, orientation and connection of "
                "RH, GPS, data transfer antennas, \nmechanical check ",
                "Check Mission planner laptop battery charge ",
                "Turn on controller and check voltage ",
                "Confirm a fresh battery is on the UAS",
                "Plug in the UAV's battery and let it boot up stationary "
                "for 20 seconds ",
                "Launch CASS live data streaming software",
                "Confirm real-time plotter is running and data is showing up "
                "and in correct range",
                "Run Mission Planner",
                "Connect telemetry (TCP connection, confirm heartbeat) ",
                "Confirm no error messages with Mission Planner ",
                "BATTERY",
                "Confirm GPS fix type (outdoors must get 3D fix) ",
                "Check flight data logging in Mission Planner",
                "Place vehicle at launch point",
                "Check flight mode on controller",
                "Review flight plan - verbal and on Mission Planner",
                "Test audio communications among participants",
                "Check if all participants ready for flight",
                "Press the safety button on the vehicle until solid red - now"
                " live and armed",
                "Check the LED for status of the vehicle. Should see a "
                "blinking green light indicating GPS lock",
                "Arm motors, call clear prop and proceed to execute the mission"
            ]
        for i in range(len(checklist)):
            if checklist[i] in "BATTERY":
                self.battery()
            else:
                print("\n")
                input(f">> {checklist[i]}")

    def battery(self):
        # launch time, battery num, voltage
        if "launch_time" not in self.flight_info.keys() or self.overwrite:

            self.flight_info["battery_id"] = \
                self.no_commas("\n\n>> Battery number (enter unknown if unknown)")
            self.flight_info["battery_voltage_initial"] = self.no_commas(
                "Battery voltage: Enter only the battery voltage before takeoff"
                " in volts without units.")

    def start_info(self):
        print("\n\nEnter takeoff time as 24-hr UTC HHMM")
        self.flight_info["launch_time_utc"] = self.get_time(self.dt_today)

        print("Finished with pre-takeoff checklist.\n\n"
              "----------------------------------------\n"
              "------------------FLIGHT----------------\n"
              "----------------------------------------\n\n")

    def end_info(self):
        if "max_achieved_alt" not in self.flight_info.keys() or self.overwrite:
            self.flight_info["battery_voltage_final"] = self.no_commas(
                "Battery voltage: Enter only the battery voltage after landing "
                "in volts without units.")
            print("Enter landing time as 24-hr UTC HHMM.")
            self.flight_info["land_time_utc"] = self.get_time(self.dt_today)
            self.flight_info["max_achieved_alt"] = \
                self.no_commas("Enter maximum altitude achieved in meters AGL.")

    def emergency(self):
        if "emergency_landing" not in self.flight_info.keys() or self.overwrite:
            emergency = \
                self.no_commas("---Emergency landing required? y/n---\n"
                               "This includes landing for airspace incursion "
                               "purposes,\n"
                               "critical battery RTL, or loss of control of "
                               "aircraft.")
            while emergency not in ["y", "n"]:
                emergency = self.no_commas("Enter y or n")

            if emergency == "y":
                print("---EMERGENCY CAUSED BY VISUAL AND FLIGHT CONDITION---")
                print("If Flight conditions turned unsafe (wind excess, sudden "
                      "fog or rain, lost sight or communication)")
                print("or Mission planner shows out of range parameters, "
                      "perform the following:")
                print("-Trigger RTL mode")
                print("-Confirm safe landing and shut off")
                print("")
                print("---EMERGENCY CAUSED BY GPS ERRORS---")
                print("If Mission planners shows GPS errors, DO NOT TRIGGER "
                      "RTL. Perform the following:")
                print("-Change to stabilize mode")
                print("-Return to base by pilot's flight skills")
                print("-Confirm safe landing and shut off")
                print("")
                error_str = self.no_commas("Take note of error messages in "
                                           "Mission Planner and what triggered "
                                           "emergency:")
                print("Continuing with post-flight checklist.")
            else:
                error_str = ""

            self.flight_info["emergency_landing"] = emergency
            self.flight_info["emergency_remarks"] = error_str

    def postflight_checks(self):
        checklist = ["Notify observers and participants that mission complete",
                     "Disarm vehicle",
                     "Perform PPK (if applicable)",
                     "Disconnect battery",
                     "Inspect vehicle"]
        for i in range(len(checklist)):
            print("\n")
            input(f">> {checklist[i]}")

        print("\n\nFinished with post_landing checklist.\n")

    def comment(self):
        if "private_remarks" not in self.flight_info.keys() or self.overwrite:
            self.flight_info["private_remarks"] = \
                self.no_commas("Additional remarks or "
                               "comments (for CASS only):")
            self.flight_info["remarks"] = \
                self.no_commas("Additional remarks or comments:")

    def recover(self):
        backupfile = open("backup.log", "r")
        try:
            last_status = backupfile.readlines()[-1]
        except IndexError:
            return
        backupfile.close()
        inp = input("A recovery file has been found for a checklist that was "
                    "not completed. Would you like to \n1) Resume, or "
                    "\n2) Start over?\n>> ")
        while inp not in "12":
            inp = input("Please enter \'1\' or \'2\':\n>> ")
        if inp in "2":
            return

        self.flight_info = \
            json.loads(last_status[last_status.index("{"):].replace("\'", "\""))
        self.step_index = \
            int(last_status[len("INFO:backup:"):last_status.index(" ")])
        print("Checklist recovery sucessful! Resuming where you left off...")
        self.step()

    def nextcloud(self):

        self.flight_info["launch_time_utc"] = \
            self.flight_info['launch_time_utc'].strftime('%Y%m%d_%H%M')
        self.flight_info["land_time_utc"] = \
            self.flight_info['land_time_utc'].strftime('%Y%m%d_%H%M')
        self.flight_info["timestamp"] = self.dt_now.strftime("%Y%m%d_%H%M%S")

        #
        # Header
        #
        if self.is_first:
            f_header = f"{self.flight_info['timestamp']}" + \
                       self.flight_info["platform_id"] + "_log_header.csv"
            f_header_path = os.path.join(self.log_dir, f_header)
            headers = ("timestamp", "operator", "location_id", "location_name",
                         "surface_altitude", "mesonet_id", "region",
                         "pilots_on_site", "objective", "authorization_type",
                         "platform_id", "scoop_id")
            fw = open(f_header_path, "w")
            writer = csv.writer(fw, delimiter=",")
            writer.writerow(headers)
            data = []
            for i in range(len(headers)):
                data.append(self.flight_info[headers[i]])
            writer.writerow(data)
            fw.close()

        #
        # Flight
        #

        f_flight = f"{self.flight_info['launch_time_utc']}" + \
                   self.flight_info["platform_id"] + "_flight_log.csv"
        f_flight_path = os.path.join(self.log_dir, f_flight)

        headers = ("timestamp", "operator", "PIC", "battery_id", "cloud",
                   "rain", "battery_voltage_initial", "max_planned_alt",
                   "launch_time_utc", "max_achieved_alt", "land_time_utc",
                   "battery_voltage_final", "emergency_landing",
                   "emergency_remarks", "private_remarks", "remarks")

        data = []
        for i in range(len(headers)):
            data.append(self.flight_info[headers[i]])
        fw = open(f_flight_path, "w")
        writer = csv.writer(fw, delimiter=",")
        writer.writerow(headers)
        writer.writerow(data)

        fw.close()

        if not self.localNextcloud:
            is_done = input("Is this your last flight?\n>>")
            if is_done.capitalize() in "YES":
                print("Copy this link into your browser and upload the "
                      "contents of " +
                      os.path.join(self.log_dir)
                      + ":\n https://10.197.13.220/s/qXjandWWu26v4hO")


class Admin(UI):

    def __init__(self):
        UI.__init__(self)
        self.step_index = 0
        self.to_do = ['choose_list']
        print("Welcome to the Admin menu! To return to the flight checklist, \n"
              "restart the program. If you make a mistake, just enter \"!\" \n"
              "to go back a step.")
        while self.step_index < len(self.to_do):
            with suppress(ExitException):
                self.step()

    def step(self):
        self.__getattribute__(self.to_do[self.step_index])()
        self.step_index += 1

    def choose_list(self):
        options = {'Platforms (i.e. N###UA_Colloqiual_Name)': "platforms",
                   'General Locations (i.e. Colorado)': "groups",
                   'Specific Locations (i.e. ABC City Park)': "locations",
                   'Objectives (i.e. Photogrametry)': "objectives"}
        message = "What would you like to edit?"
        option = self.get_index(list(options.keys()), message=message,
                                free_response=False)
        self.to_do.append(options[option])

    def platforms(self):
        options = {'Add': "platforms_add",
                   'Remove': "platforms_remove",
                   'Reorder': "platforms_reorder"}
        message = "What would you like to do?"
        option = self.get_index(list(options.keys()), message=message,
                                free_response=False)
        self.to_do.append(options[option])

    def platforms_add(self):
        old_dict = pickle.load(open(self.ndict_path, "rb"))
        print(list(old_dict.keys()))
        add = self.no_commas("Is your platform in this list? (y/n)")
        while add.lower() not in ["y", "n"]:
            add = self.no_commas("Enter y or n")
        if add in "Yesyes":
            self.back()

        name = self.no_commas("Enter the name of your platform in the format "
                              "N###UA_Colloqiual_Name")
        scoop = self.no_commas("Does this platform have an interchangeable "
                               "scoop?")
        while scoop.lower() not in ["y", "n"]:
            scoop = self.no_commas("Enter y or n")

        if scoop in "Yesyes":
            scoop = True
        else:
            scoop = False

        old_dict[name] = scoop
        pickle.dump(old_dict, open(self.ndict_path, "wb"))
        print("Platform " + name + " has been added.")
        self.back()

    def platforms_remove(self):
        old_dict = pickle.load(open(self.ndict_path, "rb"))
        to_remove = self.get_index(list(old_dict.keys()),
                                   message="Which platform would you like to "
                                           "remove?", free_response=False)
        old_dict.pop(to_remove)
        pickle.dump(old_dict, open(self.ndict_path, "wb"))
        print("Platform " + to_remove + " has been removed.")
        self.back()

    def platforms_reorder(self):
        old_dict = pickle.load(open(self.ndict_path, "rb"))
        keys = list(old_dict.keys())
        print("Here is the current order of the platforms: ")
        for i in range(len(keys)):
            print(str(i+1), keys[i])
        print("\nEnter the numbers shown on the left one at a time, starting "
              "with the platform you want listed first and ending with the "
              "one you want listed last.")
        new_dict = {}
        while len(old_dict.keys()) > 0:
            print("\tRemaining: " + str(list(old_dict.keys())))
            next_elem = self.no_commas("")
            while not next_elem.isnumeric():
                next_elem = self.no_commas("Enter an integer.")
            next_elem = int(next_elem)

            new_dict[keys[next_elem-1]] = old_dict.pop(keys[next_elem-1])

        pickle.dump(new_dict, open(self.ndict_path, 'wb'))
        self.back()

    def groups(self):
        options = {'Remove': "groups_remove",
                   'Reorder': "groups_reorder"}
        message = "What would you like to do?"
        option = self.get_index(list(options.keys()), message=message,
                                free_response=False)
        self.to_do.append(options[option])

    def groups_remove(self):
        old_dict = pickle.load(open(self.locations_path, "rb"))
        message = "Which set of locations would you like to remove?\n" \
                  "WARNING: ALL DATA STORED WITHIN THIS AREA WILL BE " \
                  "PERMANENTLY DELETED!"
        option = self.get_index(list(old_dict.keys()), message=message,
                                free_response=False)
        old_dict.pop(option)
        pickle.dump(old_dict, open(self.locations_path, "wb"))
        print("All locations in " + option + " have been deleted.")
        self.back()

    def groups_reorder(self):
        old_dict = pickle.load(open(self.locations_path, "rb"))
        keys = list(old_dict.keys())
        print("Here is the current order of the location groups: ")
        for i in range(len(keys)):
            print(str(i + 1), keys[i])
        print("\nEnter the numbers shown on the left one at a time, starting "
              "with the group you want listed first and ending with the "
              "one you want listed last.")
        new_dict = {}
        while len(old_dict.keys()) > 0:
            print("\tRemaining: " + str(list(old_dict.keys())))
            next_elem = self.no_commas("")
            while not next_elem.isnumeric():
                next_elem = self.no_commas("Enter an integer.")
            next_elem = int(next_elem)

            new_dict[keys[next_elem - 1]] = old_dict.pop(keys[next_elem - 1])

        pickle.dump(new_dict, open(self.locations_path, 'wb'))
        self.back()

    def locations(self):
        options = {'Add': "locations_add",
                   'Remove': "locations_remove",
                   'Reorder': "locations_reorder"}
        message = "What would you like to do?"
        option = self.get_index(list(options.keys()), message=message,
                                free_response=False)
        self.to_do.append(options[option])

    def locations_add(self):
        old_dict = pickle.load(open(self.locations_path, "rb"))
        group = self.get_index(list(old_dict.keys()), message="What country or"
                                                              " US state are "
                                                              "you in?")
        if group in old_dict.keys():
            region = old_dict[group] \
                [list(old_dict[group].keys())[0]]["region"]
        else:
            choice = self.no_commas("Are you in North America? [y/n]")
            if choice in "yesYESYes":
                region = "north_america"
            else:
                region = self.no_commas("What region from this list are you"
                                        " in?\n"
                                        "http://cfconventions.org/"
                                        "Data/standardized-region-list/"
                                        "standardized-region-list.html")

        long_name = self.no_commas("What is the full name of your location?")
        location_id = self.no_commas("What 4-5 character ID would you like "
                                     "to assign to " + long_name + "?")

        lat = self.no_commas("What your latitude?")
        lon = self.no_commas("What is your longitude?")
        alt = self.no_commas("What is your altitude in meters?")
        choice = self.no_commas("Is there a Mesonet station nearby? [y/n]")
        if choice in "yesYesYES":
            mesonet_id = self.no_commas("Enter the station's 4-letter "
                                        "identifier.")
        else:
            mesonet_id = None

        if group not in old_dict.keys():
            old_dict[group] = {}

        old_dict[group][location_id] = \
            {"location_name": long_name, "lat": lat,
             "lon": lon, "surface_altitude": alt,
             "region": region, "mesonet_id": mesonet_id}

        pickle.dump(old_dict, open(self.locations_path, "wb"))
        print(long_name + " has been added to the list of known locations.")
        self.back()

    def locations_remove(self):
        old_dict = pickle.load(open(self.locations_path, "rb"))
        group = self.get_index(list(old_dict.keys()),
                               message="Where is the location you want to "
                                       "delete?", free_response=False)
        loc = self.get_index(list(old_dict[group].keys()),
                             message="Which location would you like to delete?",
                             free_response=False)
        old_dict[group].pop(loc)
        if len(old_dict[group].keys()) < 1:
            del_group = self.no_commas("There are now no saved locations "
                                       "within " + group + ". Would you like "
                                                           "to delete " + group
                                       + "? [y/n]")
            while del_group.lower() not in ["y", "n"]:
                del_group = self.no_commas("Enter y or n")
            if del_group in "Yesyes":
                old_dict.pop(group)

        pickle.dump(old_dict, open(self.locations_path, "wb"))
        print(loc + " has been removed from the list of saved locations.")
        self.back()

    def locations_reorder(self):
        old_dict = pickle.load(open(self.locations_path, "rb"))
        keys = list(old_dict.keys())
        group = self.get_index(keys, message="Which set of locations would you "
                                             "like to reorder?",
                               free_response=False)
        keys = list(old_dict[group].keys())
        print("Here is the current order of the locations in " + group + ": ")
        for i in range(len(keys)):
            print(str(i + 1), keys[i])
        print("\nEnter the numbers shown on the left one at a time, starting "
              "with the location you want listed first and ending with the "
              "one you want listed last.")
        new_sub_dict = {}
        while len(old_dict[group].keys()) > 0:
            print("\tRemaining: " + str(list(old_dict[group].keys())))
            next_elem = self.no_commas("")
            while not next_elem.isnumeric():
                next_elem = self.no_commas("Enter an integer.")
            next_elem = int(next_elem)

            new_sub_dict[keys[next_elem - 1]] = old_dict[group].pop(keys[next_elem - 1])

        old_dict[group] = new_sub_dict
        pickle.dump(old_dict, open(self.locations_path, 'wb'))
        self.back()

    def objectives(self):
        options = {'Add': "objectives_add",
                   'Remove': "objectives_remove",
                   'Reorder': "objectives_reorder"}
        message = "What would you like to do?"
        option = self.get_index(list(options.keys()), message=message,
                                free_response=False)
        self.to_do.append(options[option])

    def objectives_add(self):
        objectives = pickle.load(open(self.objectives_path, "rb"))
        print(objectives)
        add = self.no_commas("Is your objective in this list? (y/n)")
        while add.lower() not in ["y", "n"]:
            add = self.no_commas("Enter y or n")

        if add in "Yesyes":
            self.back()

        new_objective = self.no_commas("What is the name of the objective you'd"
                                       " like to add?")
        objectives.append(new_objective)
        pickle.dump(objectives, open(self.objectives_path, "wb"))
        print(new_objective + " has been added to the saved objectives.")
        self.back()

    def objectives_remove(self):
        objectives = pickle.load(open(self.objectives_path, "rb"))
        to_remove = self.get_index(objectives, free_response=False,
                                   message="Which item would you like to "
                                           "remove?")
        objectives.remove(to_remove)
        pickle.dump(objectives, open(self.objectives_path, "wb"))
        print(to_remove + " has been removed from the list of objectives.")
        self.back()

    def objectives_reorder(self):
        objectives = pickle.load(open(self.objectives_path, "rb"))
        print("Here is the current order of the objectives: ")
        for i in range(len(objectives)):
            print(str(i + 1), objectives[i])
        print("\nEnter the numbers shown on the left one at a time, starting "
              "with the objective you want listed first and ending with the "
              "one you want listed last.")
        new_order = []
        remaining = objectives.copy()
        while len(objectives) - len(new_order) > 0:
            print("\tRemaining: " + str(remaining))
            next_elem = self.no_commas("")
            while not next_elem.isnumeric():
                next_elem = self.no_commas("Enter an integer.")
            next_elem = int(next_elem)

            new_order.append(objectives[next_elem - 1])
            remaining.remove(objectives[next_elem - 1])

        pickle.dump(new_order, open(self.objectives_path, 'wb'))
        self.back()


@click.command()
def cli():
    Checklist()


def main():
    cli()


if __name__ == '__main__':
    main()
