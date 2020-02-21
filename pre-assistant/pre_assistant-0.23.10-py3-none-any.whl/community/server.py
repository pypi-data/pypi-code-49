import logging
import os
from multiprocessing import Process

from rasax.community.services.git_service import GitService
from rasax.community.constants import DEFAULT_RASA_ENVIRONMENT
from sqlalchemy.orm import Session

import rasa.cli.utils
import rasax.community.initialise as initialise
import rasax.community.jwt
import rasax.community.metrics
import rasax.community.sql_migrations as sql_migrations
import rasax.community.utils as rasa_x_utils
from rasax.community import config, metrics, scheduler
from rasax.community.api.app import configure_app, initialize_app
from rasax.community.database.utils import session_scope
from rasax.community.services.model_service import ModelService
from rasax.community.services.settings_service import SettingsService

logger = logging.getLogger(__name__)


def main():
    app = configure_app(local_mode=False)
    rasax.community.jwt.initialise_jwt_keys()
    initialize_app(app)
    with session_scope() as session:
        sql_migrations.run_migrations(session)
        initialise.create_community_user(session, app)

        configure_for_server_mode(session)

    setup_metrics()

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


def setup_metrics() -> None:
    rasax.community.metrics.set_metrics_config_from_env()
    metrics.track(metrics.SERVER_START_EVENT)


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
    rasax.community.metrics.set_metrics_config_from_env()

    from rasax.community.services.event_service import main as event_service_main

    event_service_main(should_run_liveness_endpoint=False)


def launch_event_service() -> None:
    """Start the event service in a multiprocessing.Process if
    `EVENT_CONSUMER_SEPARATION_ENV` is `True`, otherwise do nothing."""

    from rasax.community.constants import EVENT_CONSUMER_SEPARATION_ENV

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
