import logging

from aiohttp import web

from . import tracking
from . import utils

logger = logging.getLogger(__name__)


async def redirect(request):
    deeplink_id = request.match_info.get("deeplink_id")
    deeplink_s = request.app["deeplink_s"]

    sig_okay, deeplink = deeplink_s.loads_unsafe(deeplink_id)

    if not sig_okay:
        raise web.HTTPNotFound()

    url = deeplink.get("url")

    if not url:
        raise web.HTTPNotFound()

    tracking_id = deeplink.get("tracking_id") or request.query.get("tid")

    if not tracking_id:
        logger.warn(
            '"{}" does not provide any Tracking ID. '
            "Make sure that the Deeplink is used correctly.".format(request.url)
        )

    campaign_name = deeplink.get("campaign_name") or request.query.get("cn")

    if not campaign_name:
        logger.warn(
            '"{}" does not provide any Campaign Name. '
            "Make sure that the Deeplink is used correctly.".format(request.url)
        )

    client_id = await tracking.get_client_id(request, tracking_id, campaign_name)
    await tracking.send_event(request=request, tid=tracking_id, cid=client_id, dl=deeplink.get("url"), cn=campaign_name)

    # Provide GET params - tid and cid
    for p_name, p_value in (
        ("cid", client_id),
        ("tid", tracking_id),
        ("cn", campaign_name),
    ):
        if "{{{}}}".format(p_name) in deeplink["url"]:
            url = url.replace("{{{}}}".format(p_name), p_value)
        else:
            url = utils.set_query_parameter(url, p_name, p_value)

    # Provide GET params - external params excluding deeplink reserved
    for p_name in request.query:
        if p_name not in ("tid", "cid", "cn", "cf1", "cf2", "cf3", "cf4", "cf5"):
            p_value = request.query.get(p_name)
            url = utils.set_query_parameter(url, p_name, p_value)

    # Redirect
    raise web.HTTPFound(url)


async def marker(request):
    gif = b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff"
    gif += b"!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00;"

    tracking_id = request.GET.get("tid")

    if not tracking_id:
        logger.warn("The marker does not provide any Tracking ID.")

    tracking.send_event(
        request=request, tid=tracking_id, cid=await tracking.get_client_id(request, tracking_id), dl=request.url
    )

    return web.Response(body=gif, headers={"Content-Type": "image/gif"})
