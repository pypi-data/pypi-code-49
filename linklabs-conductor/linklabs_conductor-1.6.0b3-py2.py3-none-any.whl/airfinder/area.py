""" Represents an Airfinder Area. """

from conductor.airfinder.base import AirfinderSubject
from conductor.airfinder.zone import Zone


class Area(AirfinderSubject):
    """ Represents an Airfinder Area inside of an Airfinder Site. """
    subject_name = 'Area'

    ###########################################################################
    # Private Methods
    ###########################################################################

    def _get_registered_asset_by_area(self, subject_name, subject_id):
        """ Base function for getting a registered asset from the Network Asset API. """
        url = ''.join([self._af_network_asset_url, '{}/{}'.format(subject_name, subject_id)])
        params = {'siteId': self.parent_site.subject_id, 'areaId': self.subject_id}
        resp = self.session.get(url, params=params)
        resp.raise_for_status()
        return resp.json()

    def _get_registered_assets_by_area(self, asset_name):
        """ Base function for getting list of registered assets from the
        Network Asset API.

        Args:
            asset_name (str): Asset name.

        Returns:
            (dict) json data
        """
        url = ''.join([self._af_network_asset_url, asset_name])
        params = {
                'siteId': self.parent_site.subject_id,
                'areaId': self.subject_id
        }
        resp = self.session.get(url, params=params)
        resp.raise_for_status()
        return resp.json()

    ###########################################################################
    # Manage Zones
    ###########################################################################

    def create_zone(self, name):
        """ Add a zone to the Area. """
        url = ''.join([self._af_network_asset_url, 'zones'])
        params = {
            "siteId": self.parent_site.subject_id,
            "configType": "Zone",
            "configValue": name,
            "properties": "object",
        }
        resp = self.session.post(url, params=params)
        resp.raise_for_status()
        x = resp.json()
        return Zone(self.session, x.get('id'), self, _data=x)

    def get_zone(self, zone_id):
        """ Get a Zone within the Area. """
        x = self._get_registered_asset_by_area('zone', zone_id)
        return Zone(self.session, x.get('id'), self, _data=x)

    def get_zones(self):
        """ Get all the Zones within the Area. """
        return [Zone(self.session, x.get('id'), self, _data=x) for x in
                self._get_registered_assets_by_area('zones')]

    def delete_zone(self, zone_id):
        """ Remove a Zone from an Area. """
        url = ''.join([self._af_network_asset_url, 'zones'])
        params = {"zoneId": zone_id}
        resp = self.session.delete(url, params=params)
        resp.raise_for_status()
        return resp.json()

    ###########################################################################
    # Properties
    ###########################################################################

    @property
    def area_location(self):
        """ The issuance ID is the subject ID from the ConductorSubject base class. """
        return self.metadata.get('areaLocation')

    # TODO
    def get_area_location(self):
        """ Get the location of the area; Outdoor will return coordinates, Indoor will return a mapping. """
        if 'Outdoor' == self.area_location:
            return self.metadata.get('points')
        elif 'Indoor' == self.area_location:
            return self.metadata.get('indoorMapping')

    def get_parent_site(self):
        """ Get the Site that the area is within. """
        return self.parent_site
