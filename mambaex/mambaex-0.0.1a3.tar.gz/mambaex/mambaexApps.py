from .mambaexApp import MambaexApp

class MambaexApps:
    """
    A class to maintain the multiple port listner servers

    """
    _servers = {}

    @classmethod
    def getOrCreateApp(cls, name=''):
        """
        Create and Returns a server intance

        :param string name: Name of the server
        :return: server instance of it.
        :rtype: MambaexApp_
        :example:
            >>> xyzServer = MambaexApps.getOrCreateApp('XYZ')

        """
        try :
            if not isinstance(name,(str)):
                raise NameShouldBeString(name)
            return cls._servers[name]
        except KeyError as e:
            cls._servers[name] = MambaexApp(name)
            return cls._servers[name]

class NameShouldBeString(Exception):
    """Exception raised for errors in the input.

    :param any name: name of server
    """

    def __init__(self, name):
        self.name = name
        self.message =  "{} is not an instance of str instead it is {}".format(str(name), type(name).__name__)
        Exception.__init__(self,self.message)
