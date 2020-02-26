from conductor.devices.module import Module
from conductor.subject import UplinkSubject, DownlinkSubject
from conductor.tokens import AppToken, NetToken


# TODO: Unit test functionality.
# TODO: Format Documenation.

class AssetGroup(UplinkSubject, DownlinkSubject):
    subject_name = 'assetGroup'

    @property
    def name(self):
        return self._data['name']

    def __repr__(self):
        return '{}({}: {})'.format(self.__class__.__name__, self.name, self)

    def rename(self, new_name):
        """ Rename the user-friendly Asset Group Name.

        Args:
            new_name(str): The new name of the Asset Group.

        Returns:

        """
        url = '{}/{}/{}/{}'.format(self.network_asset_url,
                                   self.subject_name,
                                   self.subject_id,
                                   new_name)
        self._put(url)
        self.update_data()

    def add_node(self, node):
        """ Add a tag to the asset group. """
        url = '{}/{}/{}/nodes'.format(self.network_asset_url,
                                      self.subject_name,
                                      self.subject_id)
        data = {
            "href": str(node),
            "desc": ""
        }
        return self._patch(url, json=data)

    def remove_node(self, node):
        """ Remove a tag from the Asset Group. """
        url = '{}/{}/{}/nodes'.format(self.network_asset_url,
                                      self.subject_name,
                                      self.subject_id)
        data = {
            "href": node,
            "desc": ""
        }
        return self._delete(url, data)

    def get_nodes(self):
        """ Get a list of tags in the asset group. """
        url = '{}/{}/{}/nodes'.format(self.network_asset_url,
                                      self.subject_name,
                                      self.subject_id)
        data = {'subjectId': self.subject_id}
        return [Module(self.session, x['desc'], _data=x)
                for x in self._get(url, json=data)]

    def get_application_tokens(self):
        """ Get the Application Tokens in the Asset Group. """
        url = '{}/{}/{}/applicationTokens'.format(self.network_asset_url,
                                                  self.subject_name,
                                                  self.subject_id)
        data = {'subjectId': self.subject_id}
        return [AppToken(self.session, x['desc'], _data=x)
                for x in self._get(url, json=data)]

    def add_application_token(self, appToken):
        """ Add an Application Token to the Asset Group. """
        url = '{}/{}/{}/applicationTokens'.format(self.network_asset_url,
                                                  self.subject_name,
                                                  self.subject_id)
        data = {
            "href": appToken,
            "desc": ""
        }
        return self._patch(url, json=data)

    def remove_application_token(self, appToken):
        """ Remove an Application Token from the Asset Group. """
        url = '{}/{}/{}/applicationTokens'.format(self.network_asset_url,
                                                  self.subject_name,
                                                  self.subject_id)
        data = {
            "href": appToken,
            "desc": ""
        }
        return self._delete(url, data)

    def get_network_tokens(self):
        """ Get the Network Tokens in the Asset Group. """
        url = '{}/{}/{}/nodes'.format(self.network_asset_url,
                                      self.subject_name,
                                      self.subject_id)
        data = {'subjectId': self.subject_id}
        return [NetToken(self.session, x['desc'], _data=x)
                for x in self._get(url, json=data)]

    def add_network_token(self, netToken):
        """ Add a Network Token in the Asset Group. """
        url = '{}/{}/{}/networkTokens'.format(self.network_asset_url,
                                              self.subject_name,
                                              self.subject_id)
        data = {
            "href": netToken,
            "desc": ""
        }
        return self._patch(url, json=data)

    def remove_network_tokens(self, netToken):
        """ Remove a Network Token in the Asset Group. """
        url = '{}/{}/{}/networkTokens'.format(self.network_asset_url,
                                              self.subject_name,
                                              self.subject_id)
        data = {
            "href": netToken,
            "desc": ""
        }
        return self._delete(url, json=data)
