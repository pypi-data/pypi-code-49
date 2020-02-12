import requests
import base64
import gzip
import json
import datetime
import uuid
from dataclasses import dataclass
from typing import Tuple, List
from mashumaro import DataClassJSONMixin

__all__ = ["LoginException", "News", "Tile", "get_DSB_info"]


class LoginException(Exception):
    """Fehler für falsche Logindaten"""

    pass


@dataclass
class News(DataClassJSONMixin):
    """Ein DSB-News Objekt, bspw. 'Heute ab der sechsten Stunde für alle frei'"""

    title: str
    text: str
    date: datetime.datetime


@dataclass
class Tile(DataClassJSONMixin):
    """Ein DSB-Aushang"""

    title: str
    urls: List[str]
    date: datetime.datetime


def get_DSB_info(
    username: str, password: str, mock=False
) -> Tuple[List[str], List[News], List[Tile]]:
    """gibt einen Tuple aus der Liste der Vertretungsplan-URLs,
    der News und der Aushänge zurück.
    """
    # ein JSON-Objekt der Anfrage wird erstellt

    current_time = datetime.datetime.now().isoformat()

    creds = "{{'UserId': '{}', 'UserPw': '{}', 'AppVersion': '2.5.9', 'Language': 'de', 'OsVersion': '27 8.1.0', 'AppId': '{uuid}', 'Device': 'SM-G935F', 'BundleId': 'de.heinekingmedia.dsbmobile', 'Date': '{date}', 'LastUpdate': '{date}'}}".format(
        username, password, uuid=uuid.uuid4(), date=current_time
    )
    encodedCreds = base64.b64encode(gzip.compress(creds.encode())).decode()
    request = '{"req":{"Data":"' + encodedCreds + '","DataType":1}}'

    headers = {
        "Content-Type": "application/json;charset=utf-8",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "x",
        "UserAgent": "Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nexus 4 Build/OPM7.181205.001)",
    }
    # die Anfrage wird ausgeführt
    r = requests.post(
        "https://app.dsbcontrol.de/JsonHandler.ashx/GetData",
        data=request,
        headers=headers,
    )

    if r.status_code == 200:
        # die Antwort wird verarbeitet und dekodiert.
        d = json.loads(r.content.decode())["d"]
        response = json.loads(gzip.decompress(base64.b64decode(d)).decode())
    else:
        # sollte nicht passieren, dsb gibt eine unerwartete antwort
        raise Exception("dsb response invalid")

    # falls die login-daten falsch waren
    if response["Resultcode"] != 0:
        raise LoginException("invalid login: '{}':'{}'".format(username, password))

    # sammele alle relevante daten in drei arrays:
    timetableurls = []
    news = []
    tiles = []  # type: List[Tile]

    nids = []  # type: List[str]
    for method in response["ResultMenuItems"][0]["Childs"]:
        for item in method["Root"]["Childs"]:
            if method["MethodName"] == "timetable":
                timetableurls.append(item["Childs"][0]["Detail"])
            elif method["MethodName"] == "news":
                # ignoriere doppelte news (nach id)
                if not (item["Id"] in nids):
                    nn = News(
                        item["Title"], item["Detail"], _parse_datetime(item["Date"])
                    )
                    nids.append(item["Id"])
                    news.append(nn)
            elif method["MethodName"] == "tiles":
                urls = map(
                    lambda child: child["Detail"], item["Childs"]
                )  # mappe JSON-Objekte zu ihrem "Detail"-Feld
                tile = Tile(item["Title"], list(urls), _parse_datetime(item["Date"]))
                # ignoriere doppelte tiles (nach titel)
                if tile.title not in map(lambda t: t.title, tiles):
                    tiles.append(tile)

    return (timetableurls, news, tiles)


def _parse_datetime(datestr: str) -> datetime.datetime:
    return datetime.datetime.strptime(datestr, "%d.%m.%Y %H:%M")
