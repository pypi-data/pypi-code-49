from datetime import datetime

import dateutil.parser
import utm
from aiohttp import ClientConnectorError, ClientResponse, ClientSession

ENDPOINT_LIST = "https://roads-steckbrief.hamburg/api/steckbriefeweb/list"
ENDPOINT_INFO = "https://roads-steckbrief.hamburg/api/steckbriefeweb/id"


class Baustellen:
    """Baustellen in Hamburg."""

    def __init__(self, session=None):
        self.session = session

    async def get_baustellen(self, date=datetime.now()):
        """Get a list of all construction sites."""

        try:
            d = date.strftime("%Y-%m-%d")
            response = await self.session.request("get", f"{ENDPOINT_LIST}?date={d}")

            baustellen = []
            data = await response.json()

            for baustelle in data:

                coordinates = utm.to_latlon(
                    baustelle["koordinaten"]["easting"],
                    baustelle["koordinaten"]["northing"],
                    32,
                    "U",
                )

                baustellen.append(
                    Baustelle(baustelle["id"], coordinates, baustelle["hotspot"])
                )

            return baustellen
        except ClientConnectorError as error:
            raise CannotConnect(error)

    async def get_informationen(self, id):
        """Get information about a specific construction site."""

        try:
            response = await self.session.request("get", f"{ENDPOINT_INFO}/{id}")

            data = await response.json()

            interval = (
                datetime.strptime(data["bauintervall"]["start"], "%Y-%m-%d"),
                datetime.strptime(data["bauintervall"]["end"], "%Y-%m-%d"),
            )

            last_update = dateutil.parser.isoparse(data["updateDatetime"])

            informationen = Informationen(
                data["titel"],
                data["organisationId"],
                data["anlass"],
                data["umfang"],
                interval,
                last_update,
                data["einschraenkungsbegruendung"],
                data["mehrwert"],
                data["oepnvEinschraenkungen"],
                data["parkraumEinschraenkungen"],
                data["umleitungsbeschreibung"],
                data["internetLink"],
            )

            return informationen
        except ClientConnectorError as error:
            raise CannotConnect(error)


class Baustelle:
    def __init__(self, id, coordinates, hotspot):
        self.id = id
        self.coordinates = coordinates
        self.hotspot = hotspot


class Informationen:
    def __init__(
        self,
        title,
        organisation,
        reason,
        scope,
        interval,
        last_update,
        reason_of_constraints,
        added_value,
        public_transportation_constraints,
        parking_constraints,
        redirection_description,
        link,
    ):
        self.title = title
        self.organisation = organisation
        self.reason = reason
        self.scope = scope
        self.interval = interval
        self.last_update = last_update
        self.reason_of_constraints = reason_of_constraints
        self.added_value = added_value
        self.public_transportation_constraints = public_transportation_constraints
        self.parking_constraints = parking_constraints
        self.redirection_description = redirection_description
        self.link = link


class CannotConnect(Exception):
    """Exception raised if connection could not be established to host."""

    pass
