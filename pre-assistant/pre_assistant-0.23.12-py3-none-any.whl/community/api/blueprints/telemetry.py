from sanic import Blueprint, response
from sanic.request import Request
from sanic.response import HTTPResponse

from rasax.community.api.decorators import rasa_x_scoped, validate_schema
from rasax.community import metrics


def blueprint() -> Blueprint:
    telemetry_endpoints = Blueprint("telemetry_endpoints")

    @telemetry_endpoints.route("/telemetry", methods=["POST"])
    @validate_schema("telemetry_event")
    async def telemetry_event(request: Request) -> HTTPResponse:
        """Attempts to track a telemetry event. The event will only be tracked
        if telemetry is enabled.

        Args:
            request: Received HTTP request.

        Returns:
            HTTP 204 response.
        """

        rj = request.json
        metrics.track(rj["event_name"], rj.get("properties"), rj.get("context"))
        return response.text("", 204)

    return telemetry_endpoints
