from dotenv import load_dotenv
load_dotenv()
import requests
from requests.exceptions import HTTPError
import json
import datetime
import os


class GetMetadata:
    """ Makes requests to the AIS Metadata API, which fetches vessel data from the AIS Metadata Database, and returns
    those responses as json dictionaries.

    Methods
    -------
    get_current_attributes(mmsi)
        Returns the most current vessel attributes for a given MMSI
    get_timestamps(mmsi)
        Returns vessel attributes for a given MMSI with most recent timestamp for each attribute
    get_changelog(mmsi, attribute, date_start, date_end)
        Returns a list of records for each time a given attribute for a MMSI changed within the defined date range
    """

    def __init__(self):
        """
        Parameters
        ----------
        access_key : str
            AWS access key for the TA Solutions Alpha account
        secret_access_key : str
            AWS secret access key for the TA Solutions Alpha account
        auth : <class 'requests_aws4auth.aws4auth.AWS4Auth'>
            authorizes requests to AIS Metadata API
        attributes_endpoint : str
            API endpoint to get current vessel attributes
        timestamps_endpoint: str
            endpoint to get most recent timestamps for each attribute for a vessel
        changelog_endpoint : str
            API endpoint to get a log of all changes to an attribute for a vessel
        """

        self.attributes_endpoint = 'https://zyqxnexqnf.execute-api.us-east-1.amazonaws.com/dev/vessels'
        self.timestamps_endpoint = 'https://zyqxnexqnf.execute-api.us-east-1.amazonaws.com/dev/timestamps'
        self.changelog_endpoint = 'https://zyqxnexqnf.execute-api.us-east-1.amazonaws.com/dev/changelog'

        # get api key from .olive_env file
        try:
            api_key = os.environ['OLIVE_API_KEY']
        except KeyError:
            msg = "Could not find Olive API Key in .olive_env file, please refer to section 'configuring the Olive API Key'" \
                  "in README"
            raise KeyError(msg)

        self.headers = {
            'Content-type': 'application/json',
            'x-api-key': api_key
        }

    # Request 1: Get the current attributes for a specific Vessel
    def get_current_attributes(self, mmsi):
        """ Gets the most recent vessel attributes for a given mmsi from the AIS Metadata API and returns those
         attributes in a json dictionary.

        Parameters
        ----------
        mmsi : str
            mmsi, or Maritime Mobile Service Identity, for vessel of interest

        Returns
        -------
        json dictionary
        """
        # validate mmsi is string argument
        if not isinstance(mmsi, str):
            raise TypeError('Please provide mmsi as a string argument')

        try:
            # build url using endpoint and mmsi
            url = '{endpoint}/{mmsi}'.format(endpoint=self.attributes_endpoint, mmsi=mmsi)

            # get results from api endpoint using specified parameters
            current_attributes = requests.get(url, headers=self.headers)

            # raise if call doesn't return status code 200
            current_attributes.raise_for_status()

            # load response string as json dict
            json_response = json.loads(current_attributes.content.decode())

            # must check if api response is dictionary or list containing dictionary, and return just the dictionary
            if isinstance(json_response, dict):
                return json_response

            else:
                return json_response[0]

        except HTTPError as err:
            # get status code
            status = err.response.status_code

            if status == 400:
                # bad request, return API response to user with clarifying message, load message and return with error
                msg = json.loads(current_attributes.content.decode())
                raise HTTPError(msg)

            elif status == 403:
                # client error, user needs to checks their credentials
                raise HTTPError("Please check that you are using Alpha account credentials")

            else:
                raise

    # Request 2: Get the timestamps associated with the current attributes for a specific vessel
    def get_timestamps(self, mmsi):
        """Gets the most recent timestamps for each attribute for a vessel and returns them in a json dictionary, where
        the key is the attribute and the value is the timestamp.

        Parameters
        ----------
        mmsi : str
            mmsi, or Maritime Mobile Service Identity, for vessel of interest

        Returns
        -------
        json dictionary
        """
        # validate mmsi is string argument
        if not isinstance(mmsi, str):
            raise TypeError('Please provide mmsi as a string argument')

        try:
            # get results from api endpoint using specified parameters
            url = requests.get('{endpoint}/{mmsi}'.format(endpoint=self.timestamps_endpoint, mmsi=mmsi))

            timestamps = requests.get(url, headers=self.headers)

            # raise if call doesn't return status code 200
            timestamps.raise_for_status()

            # load response string as json dict
            json_response = json.loads(timestamps.content.decode())

            # must check if api response is dictionary or list containing dictionary, and return just the dictionary
            if isinstance(json_response, dict):
                return json_response

            else:
                return json_response[0]

        except HTTPError as err:
            # get status code
            status = err.response.status_code

            if status == 400:
                # bad request, return API response to user with clarifying message, load message and return with error
                msg = json.loads(timestamps.content.decode())

                raise HTTPError(msg)

            elif status == 403:
                # client error, user needs to checks their credentials
                raise HTTPError("Please check that you are using Alpha account credentials")

            else:
                raise

    # Request 3: Get the change log* for a specific attribute of a specific vessel, within a specified date/time range
    def get_changelog(self, mmsi, attribute, date_start=None, date_end=None):
        """Returns a record for each time a selected attribute changed for a vessel within a given date/time range (if
        it changed). The changes will be returned as a list of of dictionaries, with the selected attribute as the key
        and the timestamp that the attribute changed as the value.

        Parameters
        ----------
        mmsi : str
            mmsi, or Maritime Mobile Service Identity, for vessel of interest
        attribute : str
            vessel attribute of interest, valid attributes: 'msg_type', 'imo', 'flag', 'vessel_name', 'vendor_id',
            'callsign', 'length', 'width', 'transponder_type', 'cargo_description'
        date_start : str, optional
            date/time to begin search for changes to an attribute, required format: %Y-%m-%dT%H:%M:%S
            (see http://strftime.org/), ex. '2019-09-10T10:00:00'
        date_end : str, optional
            date/time to end search for changes to an attribute, required format: %Y-%m-%dT%H:%M:%S
            (see http://strftime.org/), ex. '2019-09-10T10:00:00'
        Returns
        -------
        list of json dictionaries
        """
        args = [mmsi, attribute, date_start, date_end]

        # validate all arguments are string
        for arg in args:
            if arg:
                if not isinstance(arg, str):
                    raise TypeError('Please provide {argument} as a string argument'.format(argument=arg))

        if date_start and date_end:
            # convert dates to datetime objects so can do comparisons
            start = datetime.datetime.strptime(date_start, "%Y-%m-%dT%H:%M:%S")
            end = datetime.datetime.strptime(date_end, "%Y-%m-%dT%H:%M:%S")

            # validate start date not same as end date
            assert start != end, "Please enter different values for start and end dates"

            # validate start date before end date
            assert start < end, "Start date must be before end date"

            # build endpoint with both dates
            date_endpoint = 'from={date_start}&to={date_end}'.format(date_start=date_start,
                                                                     date_end=date_end)

        elif date_start:
            # build endpoint with just start date
            date_endpoint = 'from={date_start}'.format(date_start=date_start)

        elif date_end:
            # build endpoint with just end date
            date_endpoint = 'to={date_end}'.format(date_end=date_end)

        else:
            # don't include dates in query
            date_endpoint = None

        try:
            # build full endpoint
            changelog_url = '{endpoint}/{mmsi}/{attribute}?{date_endpoint}'.format(endpoint=self.changelog_endpoint,
                                                                                   mmsi=mmsi,
                                                                                   attribute=attribute,
                                                                                   date_endpoint=date_endpoint)

            # get results from api endpoint using specified parameters
            changelog = requests.get(changelog_url, headers=self.headers)

            # raise if call doesn't return status code 200
            changelog.raise_for_status()

            # load response string as json dict
            json_response = json.loads(changelog.content.decode())

            if json_response:
                # not an empty list, return to user
                return json_response

            else:
                # empty list, let user know that nothing to report
                print("No changes to report for attribute: {attribute}, for specified time range: {start} to "
                      "{end}".format(attribute=attribute, start=date_start, end=date_end))

                return json_response

        except HTTPError as err:
            # get status code
            status = err.response.status_code

            if status == 400:
                # bad request, return API response to user with clarifying message, load message and return with error
                msg = json.loads(changelog.content.decode())

                raise HTTPError(msg)

            elif status == 403:
                # client error, user needs to checks their credentials
                raise HTTPError("Please check that you are using Alpha account credentials")

            else:
                raise
