from typing import Optional, Dict, List, Any, Union

import json
from ldap3 import Connection, Server, SUBTREE


class Ldap:
    def __init__(self, host: str, base_dn: str, ldap3_args: Any = {}):
        """ Creates an ldap3 Server Object that will be used for the authentication

        Args:
            host (string): The URL of the the LDAP server.
            base_dn (string): The base dn of the LDAP server (e.g. DC=example,DC=com).
            ldap3_args (dict): Optional parameters that are used by the ldap3 Server function.
        
        Returns:
            No value
        """

        self.server = Server(host, **ldap3_args)
        self.base_dn = base_dn
        self.__authenticated = False

    def authenticate(
        self, user: str, password: str, member_of: Optional[str] = None
    ) -> bool:
        """ Authenticates the user and if member_of has been provided checks if the user is a member of the group.

        Args:
            user (string): Username
            password (string): Password.
            ldap3_args (dict): Optional parameter that, if provided, is used to validate if the user is a member of the provided group.
        
        Returns:
            __authenticated (bool): True is the user was successfully authenticated (and is in the provided group). Otherwise False. 
        """

        self.user = user
        self.connection = Connection(self.server, user=user, password=password)

        if self.connection.bind():
            if member_of:
                self.connection.search(
                    search_base=self.base_dn,
                    search_filter="(&(mail={})(memberOf={}))".format(user, member_of),
                    search_scope=SUBTREE,
                )
                if self.connection.entries:
                    self.__authenticated = True
                else:
                    self.__authenticated = False
            else:
                self.__authenticated = True
        else:
            self.__authenticated = False

        return self.__authenticated

    def get_attributes(
        self, attributes: Optional[Union[List[str], str]] = "*"
    ) -> Dict[str, Any]:
        """ Gets attributes for the user (successful authentication is required)

        Args:
            attributes (list(str) or str): Optional parameter that defaults to * (meaning all). 
                                           It can be used to specify the attributes that should be returned.

        Returns:
            user_attributes (dict): Values of the attributes requested for the user. Empty if the user hasn't been authenticated previously.
        """

        if self.__authenticated:
            self.connection.search(
                search_base=self.base_dn,
                search_filter="(mail={})".format(self.user),
                search_scope=SUBTREE,
                attributes=attributes,
            )

            entry = json.loads(self.connection.entries[0].entry_to_json())["attributes"]
            user_attributes = {}
            for key, val in entry.items():
                if len(val) == 1:
                    user_attributes[key] = val[0]
                else:
                    user_attributes[key] = val

            return user_attributes
        else:
            return {}
