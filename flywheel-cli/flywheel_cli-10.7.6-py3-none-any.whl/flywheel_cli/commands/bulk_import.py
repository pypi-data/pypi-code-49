"""bulk-import sub command"""

from ..bulk_import import BulkImport
from ..bulk_import.config.config import BulkImportConfig
from ..bulk_import.importers.config import get_config_cls
from ..bulk_import.importers.factory import IMPORTER_MAP

def add_command(subparsers):
    """Add command to a given subparser"""
    parser = subparsers.add_parser(
        "bulk-import", help="Bulk import"
    )

    import_subparsers = parser.add_subparsers(title="Available commands", metavar="")
    add_worker_command(import_subparsers)
    for importer_type, importer_cls in IMPORTER_MAP.items():
        add_importer_command(import_subparsers, importer_type, importer_cls)
    add_watch_command(import_subparsers)

    parser.set_defaults(func=bulk_import)
    parser.set_defaults(config=get_config)  # prevent to load the old global config
    parser.set_defaults(parser=parser)
    return parser


def add_importer_command(subparsers, importer_type, importer_cls):
    """Add importer specific sub-command"""
    parser = subparsers.add_parser(
        importer_type, help=importer_cls.help_text
    )
    BulkImportConfig.add_arguments(parser)
    get_config_cls(importer_type).add_arguments(parser)
    parser.set_defaults(importer_type=importer_type)

def add_worker_command(subparser):
    """Add worker subparser"""
    parser = subparser.add_parser(
        "worker", help="Start importer in worker mode"
    )
    BulkImportConfig.add_arguments(parser)
    parser.set_defaults(importer_type="worker", worker_mode=True)


def add_watch_command(subparsers):
    """Add watch subparser"""
    parser = subparsers.add_parser(
        "watch", help="Start watching an ingest operation"
    )
    parser.add_argument("ingest_id", help="The id of an ingest operation")
    BulkImportConfig.add_arguments(parser)
    parser.set_defaults(importer_type="watch")


def bulk_import(args):
    """Bulk import"""
    config = args.config

    if args.importer_type == "watch":
        config = BulkImportConfig(args=args)
        ingest_id = getattr(args, "ingest_id", None)
        bulk = BulkImport.watch(ingest_id, config)
    elif args.importer_type != "worker":
        importer_raw_config = (config.raw_config or {}).get("importer", {}).get(args.importer_type)
        importer_config = get_config_cls(args.importer_type).from_multi_src([args, importer_raw_config, config.raw_config])
        bulk = BulkImport(config, importer_config)
    else:
        bulk = BulkImport(config)
    bulk.run()


def get_config(args):
    """Initialize config object"""
    args.config = BulkImportConfig(args)
