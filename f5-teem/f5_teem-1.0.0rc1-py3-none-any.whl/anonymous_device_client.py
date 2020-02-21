""" Anonymous Device Client (calls Anonymous TEEM API) """

class AnonymousDeviceClient(object):
    """Anonymous Device Client Class

    Attributes
    ----------

    Methods
    -------
    """

    def __init__(self, client_info, **kwargs):
        """Class initialization

        Parameters
        ----------
        client_info : str
            client information
        **kwargs :
            optional keyword arguments

        Keyword Arguments
        -----------------
        api_key : str
            the api key to use

        Returns
        -------
        None
        """

        self.client_info = client_info
        self._api_key = kwargs.pop('api_key', None)

        self._telemetry_type = None
        self.telemetry_type_version = None

    def report(self, telemetry, **kwargs):
        """Class initialization

        Parameters
        ----------
        telemetry : dict
            telemetry record to send
        **kwargs :
            optional keyword arguments

        Keyword Arguments
        -----------------
        telemetry_type : str
            the telemetry type to use
        telemetry_type_version : str
            the telemetry type version to use

        Returns
        -------
        None
        """

        self._telemetry_type = kwargs.pop('telemetry_type', None)
        self.telemetry_type_version = kwargs.pop('telemetry_type_version', None)

        return telemetry
