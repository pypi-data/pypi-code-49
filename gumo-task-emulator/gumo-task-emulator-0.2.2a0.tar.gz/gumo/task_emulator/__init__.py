from logging import getLogger

import os
import flask.views

from gumo.task_emulator._configuration import configure
from gumo.task_emulator.domain.configuration import TaskEmulatorConfiguration
from gumo.task_emulator.presentation.cli.worker import BackgroundWorker


def task_emulator_flask_blueprints():
    from gumo.task_emulator.presentation.restapi import emulator_api_blueprint
    from gumo.task_emulator.presentation.ui import emulator_ui_blueprint

    return [
        emulator_api_blueprint,
        emulator_ui_blueprint,
    ]


def task_emulator_app():
    flask_app = flask.Flask(__name__)
    flask_app.config['JSON_AS_ASCII'] = False

    for blueprint in task_emulator_flask_blueprints():
        flask_app.register_blueprint(blueprint)

    @flask_app.route('/')
    def root():
        return flask.redirect('/task_emulator/dashboard')

    return flask_app, BackgroundWorker.get_instance()


__all__ = [
    configure.__name__,
    TaskEmulatorConfiguration.__name__,
    BackgroundWorker.__name__,
    task_emulator_app.__name__,
    task_emulator_flask_blueprints.__name__,
]

logger = getLogger('gumo.task_emulator')
