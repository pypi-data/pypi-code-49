import royalnet.utils as ru
from royalnet.backpack.tables import *
from royalnet.constellation.api import *
from ..tables import Bio


class ApiBioSetStar(ApiStar):
    path = "/api/bio/set/v1"

    methods = ["POST"]

    async def api(self, data: ApiData) -> ru.JSON:
        contents = data["contents"]
        BioT = self.alchemy.get(Bio)
        user = await data.user()
        bio = user.bio
        if bio is None:
            bio = BioT(user=user, contents=contents)
            data.session.add(bio)
        else:
            bio.contents = contents
        await data.session_commit()
        return bio.json()
