from starlette.requests import Request
from starlette.responses import *
from royalnet.constellation import *
from royalnet.utils import *
from ..tables import *
import uuid
from royalnet.constellation.api import *


class ApiWikiGetStar(ApiStar):
    path = "/api/wiki/get/v1"

    async def api(self, data: ApiData) -> dict:
        wikipage_id_str = data["id"]
        try:
            wikipage_id = uuid.UUID(wikipage_id_str)
        except (ValueError, AttributeError, TypeError):
            raise InvalidParameterError("'id' is not a valid UUID.")
        wikipage: WikiPage = await asyncify(data.session.query(self.alchemy.get(WikiPage)).get, wikipage_id)
        if wikipage is None:
            raise NotFoundError("No such page.")
        return wikipage.json_full()
