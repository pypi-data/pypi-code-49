from starlette.responses import *
from royalnet.constellation.api import *
from royalnet.utils import *
from ..tables import *


class ApiDiarioListStar(ApiStar):
    path = "/api/diario/list/v1"

    async def api(self, data: ApiData) -> dict:
        page_str = data["page"]
        try:
            page = int(page_str)
        except ValueError:
            raise InvalidParameterError("'page' is not a valid int.")
        if page < 0:
            page = -page-1
            entries: typing.List[Diario] = await asyncify(
                data.session
                    .query(self.alchemy.get(Diario))
                    .order_by(self.alchemy.get(Diario).diario_id.desc()).limit(500)
                    .offset(page * 500)
                    .all
            )
        else:
            entries: typing.List[Diario] = await asyncify(
                data.session
                    .query(self.alchemy.get(Diario))
                    .order_by(self.alchemy.get(Diario).diario_id)
                    .limit(500)
                    .offset(page * 500)
                    .all
            )
        response = [entry.json() for entry in entries]
        return response
