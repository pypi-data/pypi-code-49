from starlette.requests import Request
from starlette.responses import *
from royalnet.constellation import *
from royalnet.utils import *
from royalnet.backpack.tables import *
from royalnet.constellation.api import *


class ApiUserListStar(ApiStar):
    path = "/api/user/list/v1"

    async def api(self, data: ApiData) -> dict:
        users: typing.List[User] = await asyncify(data.session.query(self.alchemy.get(User)).all)
        return [user.json() for user in users]
