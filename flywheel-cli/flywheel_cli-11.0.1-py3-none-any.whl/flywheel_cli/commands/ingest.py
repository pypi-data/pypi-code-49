"""ingest subcommand"""

import atexit
import binascii
import logging
import os
import tempfile

from pydantic import ValidationError

from .. import util
from ..ingest.ingest_api import IngestApi
from ..ingest.config import ManageIngestConfig, WorkerIngestConfig
from ..ingest.ingest_db import IngestDB
from ..ingest.strategies.factory import STRATEGIES_MAP
from ..ingest.reporter import IngestFollower
from ..ingest.worker import IngestWorkerPool, IngestWorker
from ..ingest import models

log = logging.getLogger(__name__)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('s3transfer').setLevel(logging.CRITICAL)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)


def add_commands(subparsers):
    """Add command to a given subparser"""

    # Expose all ingest strategies as a subcommand
    for strategy_name, strategy_cls in STRATEGIES_MAP.items():
        strategy_parser = subparsers.add_parser(
            strategy_name, help=strategy_cls.help_text
        )
        # add config arguments to the parser
        strategy_cls.config_cls.add_arguments(strategy_parser)
        # set defaults
        strategy_parser.set_defaults(strategy_cls=strategy_cls)
        strategy_parser.set_defaults(config_cls=strategy_cls.config_cls)
        strategy_parser.set_defaults(func=ingest_cmd)
        strategy_parser.set_defaults(parser=strategy_parser)
        strategy_parser.set_defaults(config=load_config)

    # add worker subcommand
    worker_parser = subparsers.add_parser(
        "worker", add_help=False
    )
    # add help argument manually because add_help set to False
    # at the end the worker subcommand won't be visible in the help of the ingest subcommand
    # but can print help text of the worker subcommand using worker --help
    worker_parser.add_argument("-h", "--help", action="store_true", help="show this help message and exit")
    WorkerIngestConfig.add_arguments(worker_parser)
    worker_parser.set_defaults(config_cls=WorkerIngestConfig)
    worker_parser.set_defaults(func=worker_cmd)
    worker_parser.set_defaults(parser=worker_parser)
    worker_parser.set_defaults(config=load_config)

    # add follow subcommand
    follow_parser = subparsers.add_parser(
        "follow", help="Follow the progress of a cluster managed ingest operation"
    )
    ManageIngestConfig.add_arguments(follow_parser)
    follow_parser.set_defaults(config_cls=ManageIngestConfig)
    follow_parser.set_defaults(func=follow_cmd)
    follow_parser.set_defaults(parser=follow_parser)
    follow_parser.set_defaults(config=load_config)

    # add abort subcommand
    abort_parser = subparsers.add_parser(
        "abort", help="Abort a cluster managed ingest operation"
    )
    ManageIngestConfig.add_arguments(abort_parser)
    abort_parser.set_defaults(config_cls=ManageIngestConfig)
    abort_parser.set_defaults(func=abort_cmd)
    abort_parser.set_defaults(parser=abort_parser)
    abort_parser.set_defaults(config=load_config)

    return subparsers


def ingest_cmd(args):
    """Ingest command"""
    if args.config.cluster:
        _run_cluster_ingest(args.config)
    else:
        _run_local_ingest(args.config)

def worker_cmd(args):
    """Start an ingest worker"""
    if args.help:
        args.parser.print_help()
        return
    ingest_worker = IngestWorker(args.config)
    ingest_worker.run()


def follow_cmd(args):
    """Follow the progress of an ingest operation"""
    ingest_api = IngestApi(args.config.ingest_id, args.config)
    _follow_ingest(ingest_api)


def abort_cmd(args):
    """Abort an ingest operation"""
    ingest_api = IngestApi(args.config.ingest_id, args.config)
    ingest = ingest_api.get_ingest()
    if models.Ingest.is_terminal(ingest.status):
        print(f"Ingest already {ingest.status}")
        return
    msg = "Are you sure you want to abort the ingest?"
    if args.config.assume_yes or util.confirmation_prompt(msg):
        ingest_api.abort_ingest()


def _run_cluster_ingest(config):
    ingest_api = IngestApi.create(config)
    _load_subjects(ingest_api, config)
    ingest_url = config.save_ingest_operation_url(ingest_api.ingest_id)

    print(f"Your ingest's url: {ingest_url}")
    print("Use `fw ingest follow` to follow the progress of the ingest")
    print("Use `fw ingest abort` to abort the ingest")

    ingest_api.start_ingest()

    if not config.follow and config.cluster:
        return

    _follow_ingest(ingest_api)


def _run_local_ingest(config):
    random_part = binascii.hexlify(os.urandom(16)).decode("utf-8")
    db_filepath = os.path.join(tempfile.gettempdir(), f"flywheel_cli_ingest_{random_part}.db")
    config.db_url = f"sqlite:///{db_filepath}"
    # delete db file on exit
    atexit.register(delete_file, db_filepath)
    # create db tables
    IngestDB.create_tables(config.db_url)
    # essetial to start workers before initiating flywheel client anywhere
    worker_pool = IngestWorkerPool(config)
    worker_pool.start()
    ingest_db = IngestDB.create(config)
    _load_subjects(ingest_db, config)
    ingest_db.start_ingest()

    try:
        _follow_ingest(ingest_db)
    except KeyboardInterrupt:
        print("\nAborting ingest")
        ingest_db.abort_ingest()
    finally:
        log.debug("Gracefully shutdown worker")
        worker_pool.shutdown()


def _load_subjects(ingest_backend, config):
    if config.load_subjects:
        with open(config.load_subjects, "r") as fp:
            ingest_backend.load_subject_csv(fp)


def _follow_ingest(ingest_manager):
    """Follow the progress of the ingest operation until it completes"""
    log.debug("Start progress reporter")
    follower = IngestFollower(ingest_manager)
    follower.run()


def load_config(args):
    """Load config from cli args"""
    if not hasattr(args, "config_cls") or getattr(args, "help", None):
        args.config = None
        return
    try:
        args.config = args.config_cls.parse_arguments(args)
    except ValidationError as err:
        errors = "\n".join(f"{e['loc'][0]}: {e['msg']}" for e in err.errors())
        args.parser.error(f"The following errors found during parsing configuration:\n{errors}")
    args.config.startup_initialize()


def delete_file(filepath):
    """Delete a given file if exists"""
    if os.path.exists(filepath):
        log.debug(f"Clean up file: {filepath}")
        os.remove(filepath)
