from royalnet.utils import *
from royalnet.backpack.tables import *
from royalnet.constellation.api import *
from ..utils import find_user_api


class ApiBioGetStar(ApiStar):
    path = "/api/bio/get/v1"

    async def api(self, data: ApiData) -> dict:
        user = await find_user_api(data["id"], self.alchemy, data.session)
        if user.bio is None:
            raise NotFoundError("User has no bio set.")
        return user.bio.json()
