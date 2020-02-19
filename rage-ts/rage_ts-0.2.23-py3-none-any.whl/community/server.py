import logging
import os
from multiprocessing import Process  # type: ignore

from ragex.community.services.git_service import GitService
from ragex.community.constants import DEFAULT_RASA_ENVIRONMENT
from sqlalchemy.orm import Session

import rasa.cli.utils
from ragex.community import initialise  # pytype: disable=import-error
import ragex.community.jwt
import ragex.community.metrics
import ragex.community.sql_migrations as sql_migrations
import ragex.community.utils as rasa_x_utils
from ragex.community import config, metrics, scheduler
from ragex.community.api.app import configure_app, initialize_app
from ragex.community.database.utils import session_scope
from ragex.community.services.model_service import ModelService
from ragex.community.services.settings_service import SettingsService
from ragex.community.services.config_service import ConfigService

logger = logging.getLogger(__name__)


def main():
    app = configure_app(local_mode=False)
    ragex.community.jwt.initialise_jwt_keys()
    initialize_app(app)
    with session_scope() as session:
        sql_migrations.run_migrations(session)
        initialise.create_community_user(session, app)

        configure_for_server_mode(session)

        # Initialize database with default configuration values so that they
        # can be read later.
        config_service = ConfigService(session)
        config_service.initialize_configuration()

        # Configure telemetry
        ragex.community.metrics.initialize_configuration_from_db(session)

    metrics.track(metrics.SERVER_START_EVENT)

    rasa_x_utils.update_log_level()

    rasa_x_utils.check_for_updates()

    rasa_x_utils.run_operation_in_single_sanic_worker(
        app, metrics.track_status_periodically
    )

    rasa.cli.utils.print_success("Starting Rasa X server... 🚀")
    app.run(
        host="0.0.0.0",
        port=config.self_port,
        auto_reload=os.environ.get("SANIC_AUTO_RELOAD"),
        workers=4,
    )


def configure_for_server_mode(session: Session) -> None:
    # Initialize environments before they are used in the model discovery process
    settings_service = SettingsService(session)
    settings_service.inject_environments_config_from_file(
        config.project_name, config.default_environments_config_path
    )

    model_service = ModelService(
        config.rasa_model_dir, session, DEFAULT_RASA_ENVIRONMENT
    )
    model_service.discover_models_on_init()

    # Start background scheduler in separate process
    scheduler.start_background_scheduler()


def _event_service() -> None:
    # Update metrics config for this new process

    from ragex.community.services.event_service import main as event_service_main

    event_service_main(should_run_liveness_endpoint=False)


def launch_event_service() -> None:
    """Start the event service in a multiprocessing.Process if
    `EVENT_CONSUMER_SEPARATION_ENV` is `True`, otherwise do nothing."""

    from ragex.community.constants import EVENT_CONSUMER_SEPARATION_ENV

    if config.should_run_event_consumer_separately:
        logger.debug(
            f"Environment variable '{EVENT_CONSUMER_SEPARATION_ENV}' "
            f"set to 'True', meaning Rasa X expects the event consumer "
            f"to run as a separate service."
        )
    else:
        logger.debug("Starting event service from Rasa X.")
        p = Process(target=_event_service)
        p.daemon = True
        p.start()


if __name__ == "__main__":
    rasa_x_utils.update_log_level()

    launch_event_service()

    logger.debug("Starting API service.")
    main()
