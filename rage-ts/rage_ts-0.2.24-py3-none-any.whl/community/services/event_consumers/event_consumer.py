import json
import logging
import os
import typing
from contextlib import ExitStack
from typing import Text, Optional, Union

from sanic.response import HTTPResponse

from ragex.community import utils
from ragex.community.database.utils import session_scope
from ragex.community.services.analytics_service import AnalyticsService
from ragex.community.services.event_service import EventService
from ragex.community.services.logs_service import LogsService

if typing.TYPE_CHECKING:
    from multiprocessing import Process  # type: ignore

logger = logging.getLogger(__name__)


class EventConsumer:
    """Abstract base class for all event consumers."""

    type_name = None

    def __init__(self, should_run_liveness_endpoint: bool = False) -> None:
        """Abstract event consumer that implements a liveness endpoint.

        Args:
            should_run_liveness_endpoint: If `True`, runs a Sanic server as a
                background process that can be used to probe liveness of this service.
                The service will be exposed at a port defined by the
                `SELF_PORT` environment variable (5673 by default).

        """
        self.liveness_endpoint: Optional["Process"] = None
        self.start_liveness_endpoint_process(should_run_liveness_endpoint)

        # Assign to the three services placeholder `None` values. They
        # are properly intialised in the `initalise_services()` method.
        self.logs_service: Optional[LogsService] = None
        self.event_service: Optional[EventService] = None
        self.analytics_service: Optional[AnalyticsService] = None
        self.initialise_services()

    def initialise_services(self) -> None:
        # Create services and give them separate db sessions so that they don't
        # affect each other.
        with ExitStack() as context_stack:
            # create three `session_scope()` contexts
            scopes = [context_stack.enter_context(session_scope()) for _ in range(3)]

            # these three services commit frequently due to using different sessions
            self.event_service = EventService(scopes[0])
            self.analytics_service = AnalyticsService(scopes[1])
            self.logs_service = LogsService(scopes[2])

    @staticmethod
    def _liveness_endpoint_process(consumer_type: Text) -> "Process":
        """Get Sanic app as a multiprocessing.Process.

        Args:
            consumer_type: Event consumer type.

        Returns:
            Sanic endpoint app as a multiprocessing.Process.

        """
        from multiprocessing import Process  # type: ignore

        def run_liveness_app(_port: int) -> None:
            from sanic import Sanic
            from sanic import response

            app = Sanic(__name__)

            @app.route("/health")
            async def health(_) -> HTTPResponse:
                return response.text(f"{consumer_type} consumer is running.", 200)

            app.run(host="0.0.0.0", port=_port, access_log=False)

        port = int(os.environ.get("SELF_PORT", "5673"))

        p = Process(target=run_liveness_app, args=(port,), daemon=True)
        logger.info(f"Starting Sanic liveness endpoint at port '{port}'.")

        return p

    def start_liveness_endpoint_process(
        self, should_run_liveness_endpoint: bool
    ) -> None:
        """Start liveness endpoint multiprocessing.Process if
        `should_run_liveness_endooint` is `True`, else do nothing."""

        if should_run_liveness_endpoint:
            self.liveness_endpoint = self._liveness_endpoint_process(self.type_name)
            self.liveness_endpoint.start()

    def kill_liveness_endpoint_process(self) -> None:
        """Kill liveness endpoint multiprocessing.Process if it is active."""

        if self.liveness_endpoint and self.liveness_endpoint.is_alive():
            self.liveness_endpoint.terminate()
            logger.info(
                f"Terminated event consumer liveness endpoint process "
                f"with PID '{self.liveness_endpoint.pid}'."
            )

    def log_event(
        self,
        data: Union[Text, bytes],
        sender_id: Optional[Text] = None,
        event_number: Optional[int] = None,
        origin: Optional[Text] = None,
    ) -> None:
        """Handle an incoming event forwarding it to necessary services and handlers."""

        event = self.event_service.save_event(
            data, sender_id=sender_id, event_number=event_number, origin=origin
        )
        self.logs_service.save_nlu_logs_from_event(data, event.id)
        self.analytics_service.save_analytics(data, sender_id=event.conversation_id)

        if utils.is_enterprise_installed():
            from ragex.enterprise import reporting  # pytype: disable=import-error

            reporting.report_event(json.loads(data), event.conversation_id)

    def consume(self):
        """Consume events."""
        raise NotImplementedError(
            "Each event consumer needs to implement the `consume()` method."
        )
