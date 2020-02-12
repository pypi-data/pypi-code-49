###############################
###### nbforms Python API #####
###############################

# TODO: change from tabs to vboxes

from .widgets import *

import datascience as ds
import pandas as pd
import requests
import os
import json
from io import StringIO
from getpass import getpass
from ipywidgets import interact, Button, VBox, HBox, interactive_output, Label, Tab
from IPython.display import display, HTML

class Form:
    """nbforms class for interacting with an nbforms server
    
    The Form class sends requests to the nbforms server that records users'
    resposnes. It provides auth so that users can be differentiated on the server,
    stores users' responses from widgets, generates and displays the necessary
    widgets, and pulls data from the server for analysis.

    Args:
        config_path (str): Path to your nbforms config file

    """

    def __init__(self, config_path="nbforms_config.json"):
        # check that config_path exists
        assert os.path.exists(config_path) and os.path.isfile(config_path), \
        "{} is not a valid config path".format(config_path)

        # load in config file
        with open(config_path) as f:
            self._config = json.load(f)

        # check that config file has required info
        assert all([i in self._config for i in ["server_url", "questions", "notebook"]]), \
        "config file missing required information"

        # assign instance vars
        self._server_url = self._config["server_url"]
        self._notebook = self._config["notebook"]

        self._auth_url = os.path.join(self._server_url, "auth")
        self._submit_url = os.path.join(self._server_url, "submit")
        self._data_url = os.path.join(self._server_url, "data")
        self._login_url = os.path.join(self._server_url, "login")

        self._questions = self._config["questions"]
        
        self._identifiers = []
        self._widgets = {}
        self._widget_instances = {}
        self._responses = {}
        self._updated_since_last_post = {}

        for q in self._questions:
            # check that each question has the required keys
            assert all([t in q.keys() for t in ["identifier", "type", "question"]]), "a question is missing a required key"
            
            self._identifiers += [q["identifier"]]
            widget = TYPE_MAPPING[q["type"]](q)
            self._widgets[q["identifier"]] = widget

        # set up attendance if applicable
        if "attendance" in self._config:
            self._attendance = True
            self._attendance_url = os.path.join(self._server_url, "attendance")

        # check to see if there's already a key in the environment from another
        # Notebook instance
        try:
            global __NBFORMS_API_KEY__
            if __NBFORMS_API_KEY__:
                self._api_key = __NBFORMS_API_KEY__
            else:
                self._auth()

        except NameError:
            self._auth()

        # create global API key
        __NBFORMS_API_KEY__ = self._api_key
            

    def _auth(self):
        # have users authenticate with OAuth
        if "auth" in self._config and self._config["auth"] != "default":
            assert self._config["auth"] in ["google", "none"], "invalid auth provider"

            if self._config["auth"] == "google":
                # send them to login page
                display(HTML(f"""
                <p>Please <a href="{self._login_url}" target="_blank">log in</a> to the 
                nbforms server and enter your API key below.</p>
                """))

                self._api_key = input()
            
            else:
                # send request to get API key
                auth_response = requests.post(self._auth_url)

                # check that sign in was OK, store API key
                assert auth_response.text != "INVALID USERNAME", "Was not able to get API key"
                self._api_key = auth_response.text

        # else have them auth with default auth
        else:
            # ask user for a username and password
            print("Please enter a username and password for nbforms.")
            username = input("Username: ")
            password = getpass("Password: ")

            # auth to get API key
            auth_response = requests.post(self._auth_url, {
                "username": username,
                "password": password
            })

            # check that sign in was OK, store API key
            assert auth_response.text != "INVALID USERNAME", "Incorrect username or password"
            self._api_key = auth_response.text

    def _save_current_response(self, identifier, response):
        """Saves responses from widgets"""
        self._responses[identifier] = response
        self._updated_since_last_post[identifier] = True

    def _was_updated(self, identifier):
        return identifier in self._updated_since_last_post and self._updated_since_last_post[identifier]

    def _send_response(self):
        """Sends responses to the nbforms server"""
        for identifier in self._identifiers:
            if identifier in self._responses and self._was_updated(identifier):
                response = requests.post(self._submit_url, {
                    "identifier": identifier,
                    "api_key": self._api_key,
                    "notebook": str(self._notebook),
                    "response": str(self._responses[identifier]),
                })
                assert response.text != "SUBMISSION UNSUCCESSFUL" and response.text == "SUBMISSION SUCCESSFUL", \
                "submission was not sent successfully"
                self._updated_since_last_post[identifier] = False

    def _get_data(self, identifiers, user_hashes=False):
        """Get data from the server"""
        response = requests.get(self._data_url, {
            "questions": ",".join(identifiers),
            "notebook": str(self._notebook),
            "user_hashes": (0, 1)[user_hashes]
        })
        return response.text

    # def _confirm_submission(self, identifier):
    #     self._widget_instances

    def _create_submit_button(self): # , identifier):
        """Create the submit button for a widget"""

        # create the Button instance
        button = Button(
            description="Submit",
            update=True
        )

        # create the function that will be called when the button is clicked
        def send(b):
            self._send_response()
            b.button_style = 'success'
        
        button.on_click(send)
        return button

    def _arrange_single_widget(self, identifier):
        """Set up a single widget with label and button"""

        # create the label, widget typle
        label, widget = self._widgets[identifier].to_widget_tuple()

        # set up the interactive part of the widget
        interactive = interactive_output(lambda response: self._save_current_response(identifier, response),
                                 {"response": widget})

        # # create the button
        # button = self._create_submit_button(identifier)

        # create the UI with VBoxes and return the ui, interactive tuple
        ui = VBox([label, widget]) # VBox([VBox([label, widget]), button])
        return ui, interactive

    def ask(self, *identifiers):
        """Ask any or all questions in the config file and display widgets
        
        Args:
            identifiers: question identifiers to be asked in the widget; defaults to all
        
        """
        # extract all questions that have been updated before this ask all
        previously_updated_questions = [identifier for identifier in self._updated_since_last_post \
            if self._updated_since_last_post[identifier] and identifier in identifiers]
        
        # restore any previous responses that would be overwritten
        previous_responses = {identifier : self._responses[identifier] for identifier in self._responses \
            if identifier in previously_updated_questions}

        # check that all identifiers are valid
        assert all([i in self._identifiers for i in identifiers]), "one or more questions do not exist"
        
        # default to asking all questions
        if len(identifiers) == 0:
            identifiers = self._identifiers

        # capture all widgets in list of VBoxes
        displays = []
        for identifier in identifiers:
            displays += [VBox(self._arrange_single_widget(identifier))]

        # create submit button
        displays += [self._create_submit_button()]

        # # create the Tab that will display all the widgets
        # t = Tab()
        # t.children = displays

        # create VBox to display
        t = VBox(displays)

        # # set tab titles to identifiers
        # for i in range(len(identifiers)):
        #     t.set_title(i, identifiers[i])

        # display the widget
        display(t, display_id="widget" + "-".join(identifiers), update=True)

        # clear the None values that are autoselected
        for identifier in identifiers:
            if identifier not in previously_updated_questions:
                self._updated_since_last_post[identifier] = False

        # restore previous responses for those overwritten by new widget
        for identifier in previous_responses:
            self._responses[identifier] = previous_responses[identifier]

    def to_table(self, *identifiers, user_hashes=False):
        """Get data from the server and return a datascience Table
        
        Args:
            identifiers: which questions to include in the table, defaults to all
            user_hashes (bool): whether to include hashes of usernames
        
        """
        
        # get a pandas DataFrame and return that turned into a Table
        df = self.to_df(*identifiers, user_hashes=user_hashes)
        return ds.Table.from_df(df)

    def to_df(self, *identifiers, user_hashes=False):
        """Get data from the server and return a pandas DataFrame
        
        Args:
            identifiers: which questions to include in the table, defaults to all
            user_hashes (bool): whether to include hashes of usernames
        
        """
        
        # check that all identifiers are valid
        assert all([i in self._identifiers for i in identifiers]), "one or more questions do not exist"

        # default to getting all questions
        if len(identifiers) == 0:
            identifiers = self._identifiers

        # send request to server and get the CSV string
        csv_string = self._get_data(identifiers, user_hashes=user_hashes)

        # check that we have unlocked questions
        assert csv_string != "NO UNLOCKED QUESTIONS", "No unlocked questions were requested from the server"

        # send to pandas DataFrame and return
        df = pd.read_csv(StringIO(csv_string))
        return df

    def take_attendance(self):
        """Log attendance on the nbforms server"""

        # check that this notebook tracks attendance
        assert self._attendance, "this notebook does not record attendance"

        # send request to the server
        response = requests.post(self._attendance_url, {
            "api_key": self._api_key,
            "notebook": self._notebook,
        })

        # check that there wasn't a server rror
        assert response.text != "ATTENDANCE NOT RECORDED", "attendance not recorded successfully"
        assert response.text == "ATTENDANCE RECORDED", "attendance not recorded successfully"

        # confirm that attendance was recorded
        print("Your attendance has been recorded.")
