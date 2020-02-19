import datetime
import logging
import uuid

from aiohttp_session import get_session

from . import settings

logger = logging.getLogger(__name__)


def _get_client_user_ip(request):
    remote_host = None

    peername = request.transport.get_extra_info("peername")
    if peername is not None:
        remote_host, _ = peername

    remote_host = request.headers.get(settings.IP_ADDRESS_META_FIELD, remote_host)
    return remote_host.split(",")[0].strip() if remote_host else None


def _prepare_request_data(request):
    client_user_ip = _get_client_user_ip(request)
    client_user_agent = request.headers.get("User-Agent", None)
    document_referer = request.headers.get("Referer", None)

    return {
        "t": "pageview",
        "dr": document_referer,
        "uip": client_user_ip,
        "uua": client_user_agent,
        "utt": str(datetime.datetime.utcnow()),
        "cf1": request.query.get("cf1", None),
        "cf2": request.query.get("cf2", None),
        "cf3": request.query.get("cf3", None),
        "cf4": request.query.get("cf4", None),
        "cf5": request.query.get("cf5", None),
    }


async def get_client_id(request, tracking_id=None, campaign_name=None):
    if "cid" in request.query:
        return request.query["cid"]

    session = await get_session(request)

    # Build a key name to avoid statistics data collision. Client ID has to be unique for
    # Tracking ID and Campaign Name pair.
    key = "client_id"

    if tracking_id:
        key = f"{key}_{tracking_id}"

    if campaign_name:
        key = f"{key}_{campaign_name}"

    if key not in session or not session[key]:
        session[key] = uuid.uuid4().hex

    return session[key]


async def send_event(request, **kwargs):
    request_data = dict()
    request_data.update(**kwargs)
    request_data.update(_prepare_request_data(request))

    client_session = request.app["client_session"]
    url = f"{settings.EVENTS_API_URL}/event/"

    resp = await client_session.post(url, json=request_data)

    if resp.status != 200:
        logger.error(
            "Request to {} returned status code {}: {}"
            "in {span} milliseconds.".format(url, resp.status, await resp.json())
        )
