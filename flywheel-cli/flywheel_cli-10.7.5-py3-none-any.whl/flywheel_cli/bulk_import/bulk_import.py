"""Provides BulkImport class."""

import csv
import datetime
import logging
import os
import signal
import stat
import sys
import tempfile
import time
from abc import ABC, abstractmethod

import crayons

from .. import util
from ..importers.container_factory import ContainerFactory, ContainerNode
from ..sdk_impl import SdkUploadWrapper, create_flywheel_client
from .db import create_ingest_factory
from .db.models import DiscoverTask, IngestOperation, IngestStage, PrivateTag, SubjectMap, TaskStatus, WorkTask
from .deid import get_subjects_mapping_config, get_deid_profile_config
from .discover import DiscoverQueue
from .executor import BulkImportExecutor
from .importers.config import create_config_from_dict
from .process import ProcessQueue
from .reporter import BulkImportProgressReporter, TerminalSpinnerThread
from .scan import ScanQueue

log = logging.getLogger(__name__)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('s3transfer').setLevel(logging.CRITICAL)

class BulkImport:  # pylint: disable=too-few-public-methods
    """Creating and controlling bulk imports."""

    def __init__(self, config, importer_config=None):
        self.config = config
        self.context = Context(config, importer_config)
        self.stage = InitializeStage(self.context)
        if not self.context.worker_mode:
            self._init_interrupt_handler()

    def run(self):
        """Run all stages"""
        stage = self.stage

        while stage:
            self.stage = stage
            stage.run()
            stage = stage.next()

    def _init_interrupt_handler(self):
        """Init interrupt handling"""
        original_handler = signal.getsignal(signal.SIGINT)
        def _interrupt_handler(*_):
            """Handle SIGINT"""
            self.context.reporter.suspend()
            if stat.S_ISREG(self.context.reporter.mode) or not self.config.remote_host:
                self.abort()
            else:
                choices = ["1", "2"]
                messages = ["\n", "1. Abort import", "2. Continue import and disconnect progress monitoring"]
                message = str(crayons.red("\n".join(messages) + "\n"))
                sys.stdout.write(message)
                sys.stdout.flush()

                try:
                    while True:
                        choice = input(str(crayons.red("Enter option number: ", bold=True)))
                        if choice == "1":
                            sys.stdout.write(str(crayons.red("Aborting...\n")))
                            sys.stdout.flush()
                            self.abort()
                            return
                        if choice == "2":
                            sys.stdout.write(str(crayons.green((
                                f"Current import ingest ID: {self.context.current_ingest.ingest_id}\n"
                                f"To resume import monitoring, run\n"
                                f"  fw bulk-import watch {self.context.current_ingest.ingest_id}\n"
                            ))))
                            sys.stdout.flush()
                            self.context.reporter.shutdown()
                            sys.exit()
                        else:
                            sys.stdout.write(str(crayons.red("Please choose from " + ", ".join(choices) + "\n")))
                            sys.stdout.flush()
                except RuntimeError:
                    signal.signal(signal.SIGINT, original_handler)
                return
        signal.signal(signal.SIGINT, _interrupt_handler)


    @classmethod
    def watch(cls, ingest_id, config):
        """Start watching the given ingest operation"""
        log.debug("Create BulkImport object")
        ingest_factory = create_ingest_factory(config.db_connection_str)
        ingest_mapper = ingest_factory.create_mapper()
        ingest_operation = ingest_mapper.find(ingest_id)
        importer_config = create_config_from_dict(ingest_operation.config["importer_config"])
        bulk_import_obj = cls(config, importer_config=importer_config)
        log.debug("Set BulkImport obj attributes from ingest operation")
        bulk_import_obj.context.current_ingest = ingest_operation
        bulk_import_obj.stage = STAGE_MAP[ingest_operation.stage](bulk_import_obj.context)
        bulk_import_obj.context.reporter.process_start_time = datetime.datetime.now()
        log.debug("Watching...")
        return bulk_import_obj

    def abort(self):
        """Abort the current ingest operation"""
        log.debug("Start aborting...")
        self.stage.abort()
        self.stage.next()


class Context:  # pylint: disable=too-few-public-methods
    """Bulk import context class.

    Holds the config, current importer, database mapper instances, current ingest and the executer.
    If running in slave mode, importer and current ingest won't be set.
    """
    def __init__(self, config, importer_config=None):
        self.config = config
        self.importer_config = importer_config
        self.ingest_factory = create_ingest_factory(config.db_connection_str)
        self.discover_queue_mapper = self.ingest_factory.create_discover_queue_mapper()
        self.deid_log_mapper = self.ingest_factory.create_deid_log_mapper()
        self.ingest_mapper = self.ingest_factory.create_mapper()
        self.items_mapper = self.ingest_factory.create_ingest_items_mapper()
        self.private_tags_mapper = self.ingest_factory.create_private_tags_mapper()
        self.scan_queue_mapper = self.ingest_factory.create_scan_queue_mapper()
        self.subjects_mapping_mapper = self.ingest_factory.create_subjects_mapping_mapper()
        self.work_queue_mapper = self.ingest_factory.create_work_queue_mapper()
        self.audit_log_mapper = self.ingest_factory.create_audit_log_mapper()
        self.current_ingest = None
        self.executor = None
        self.worker_mode = not importer_config
        self.reporter = BulkImportProgressReporter(self)
        self.container_factory = None


class Stage(ABC):
    """Provides the abstract interface of a Stage. Every concrete stage should implement this interface"""

    def __init__(self, context):
        self.context = context
        self._aborted = False

    def run(self):
        """Run this stage"""
        self._run()

    @abstractmethod
    def _run(self):
        """Run next stage. Should implement in descendant classes"""

    @abstractmethod
    def _next(self):
        """Get next stage. Should implement in descendant classes"""

    def next(self):
        """Get next stage"""
        if self._aborted:
            return AbortedStage(self.context)
        return self._next()

    def abort(self):
        """Abort pipeline"""
        self._aborted = True

    def wait_while_truthy(self, func, *args, **kwargs):
        """Wait while the given func returns true, or aborted is not set"""
        while not (func(*args, **kwargs) or self._aborted):
            time.sleep(1)

    def save_audit_log(self):
        """Save audit log"""
        if self.context.importer_config.no_audit_log:
            return

        project = self.context.current_ingest.config.get("target_project")
        if not project or not project["_id"]:
            log.debug("Skipped saving audit. No target project found")
            return
        project = ContainerNode(
            "project",
            cid=project["_id"],
            label=project["label"],
        )

        path = self.context.importer_config.audit_log_path
        if not path:
            path = f"audit_log-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.csv"

        logs = self.context.audit_log_mapper.get_logs(self.context.current_ingest.ingest_id)

        if self.context.importer_config.save_audit_locally:
            if os.path.dirname(path) and not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            with open(path, "w") as log_file:
                self._write_logs_to_file(logs, log_file)
            self._upload_audit_log(project, path)
        else:
            with tempfile.TemporaryDirectory() as tmp_dir:
                path = os.path.join(tmp_dir, os.path.basename(path))
                with open(path, "w") as log_file:
                    self._write_logs_to_file(logs, log_file)
                self._upload_audit_log(project, path)

    @staticmethod
    def _write_logs_to_file(logs, log_file):
        """Write logs to log file"""
        headers = ["Source Path", "Flywheel Path", "Failed", "Message"]
        csv_writer = csv.DictWriter(log_file, fieldnames=headers)
        csv_writer.writeheader()
        for entry in logs:
            csv_writer.writerow({
                "Source Path": entry.src_path,
                "Flywheel Path": entry.fw_path,
                "Failed": entry.failed,
                "Message": entry.message
            })

    @staticmethod
    def _upload_audit_log(project, path):
        """Upload audit log file to the target project"""
        fw = create_flywheel_client()
        uploader = SdkUploadWrapper(fw)

        if not project:
            log.debug('No project found for import, skipping audit-log upload')
            return

        try:
            log_name = os.path.basename(path)
            with open(path, 'rb') as f:
                uploader.upload(project, log_name, f)
        except Exception:  # pylint: disable=broad-except
            log.error('Error uploading audit-log', exc_info=True)
        else:
            log.debug(f'{log_name} uploaded to the "{project.label}" project.')


class InitializeStage(Stage):
    """Initialize the database stage"""

    def _run(self):
        log.debug("Initializing database...")
        self.context.ingest_mapper.initialize()
        log.debug("Initializing database... done")

    def _next(self):
        if self.context.worker_mode:
            return StartWorkersStage(self.context)

        return CreateIngestStage(self.context)


class StartWorkersStage(Stage):
    """Start worker processes stage"""

    def _run(self):
        log.debug("Start worker processes...")
        executor = BulkImportExecutor()
        executor.add_queue("discover", DiscoverQueue(self.context))
        executor.add_queue("scan", ScanQueue(self.context))
        executor.add_queue("process", ProcessQueue(self.context))
        executor.start(self.context.config.cpu_count)
        self.context.executor = executor
        log.debug("Start worker processes... done")

        if self.context.worker_mode:
            log.info("Waiting for tasks...")
            executor.join()

    def _next(self):
        if self.context.worker_mode:
            return ShutdownStage(self.context)

        return WaitForDiscoverStage(self.context)


class CreateIngestStage(Stage):
    """Create new ingest stage"""

    def _run(self):
        log.debug("Creating new ingest operation...")
        ingest = IngestOperation(
            name="Ingest",  # TODO: get name from config
            stage=IngestStage.scan,
            fs_path=self.context.importer_config.folder,
            created=datetime.datetime.now(),
            config=self.get_config(),
        )
        ingest.ingest_id = self.context.ingest_mapper.insert(ingest)
        self.context.current_ingest = ingest
        self.context.reporter.start()
        # load subject mappings
        subjects_mapping_config = get_subjects_mapping_config(
            self.context.importer_config.deid_profile,
            self.context.importer_config.deid_profiles,
        )
        if subjects_mapping_config and subjects_mapping_config.get("load-from"):
            load_subject_mappings_from_csv_to_db(
                subjects_mapping_config.get("load-from"),
                self.context.subjects_mapping_mapper,
                ingest.ingest_id,
            )

        discover_task = DiscoverTask(
            ingest_id=ingest.ingest_id,
            status=TaskStatus.waiting,
        )
        self.context.discover_queue_mapper.insert(discover_task)

        log.debug("Creating new ingest operation... done")

    def get_config(self):
        """Get config that relevants for the workers."""
        return {
            "importer_config": self.context.importer_config.to_dict(),
        }

    def _next(self):
        if self.context.config.db_connection_str.startswith("sqlite"):
            return StartWorkersStage(self.context)
        return WaitForDiscoverStage(self.context)


class WaitForDiscoverStage(Stage):
    """Discover filesystem stage"""

    def _run(self):
        log.debug("Wait for discover to finish...")
        self.wait_while_truthy(
            self.context.discover_queue_mapper.is_complete_ingest,
            self.context.current_ingest.ingest_id,
        )
        log.debug("Wait for discover to finish... done")

    def _next(self):
        return WaitForScanStage(self.context)


class WaitForScanStage(Stage):
    """Wait until scan finishes stage"""

    def _run(self):
        log.debug("Scanning items...")
        self.wait_while_truthy(
            self.context.scan_queue_mapper.is_complete_ingest,
            self.context.current_ingest.ingest_id
        )
        log.debug("Scanning items... done")

    def _next(self):
        self.context.reporter.suspend()
        return ReviewStage(self.context)


class ReviewStage(Stage):
    """Review stage"""

    def _run(self):
        log.debug("Review...")

        fw = create_flywheel_client()
        uploader = SdkUploadWrapper(fw)
        self.context.container_factory = ContainerFactory(uploader)
        spinner = TerminalSpinnerThread("Resolving containers")
        spinner.start()
        ingest_items = self.context.items_mapper.get_all_item_for_ingest(self.context.current_ingest.ingest_id)
        for item in ingest_items:
            self.context.container_factory.resolve(item.context)
        spinner.stop("Resolved containers")

        project = None
        self.context.reporter.report_review_summary(self.context.container_factory)
        self.context.ingest_mapper.update(self.context.current_ingest.ingest_id, stage=IngestStage.review)
        if self.context.config.assume_yes or util.confirmation_prompt("Confirm upload?"):
            spinner = TerminalSpinnerThread("Creating containers")
            spinner.start()
            self.context.container_factory.create_containers()
            spinner.stop("Created containers")

            self.context.reporter.before_review = False
            self.context.reporter.resume()
            self.context.ingest_mapper.update(self.context.current_ingest.ingest_id, processing_start=datetime.datetime.now())
            for item in self.context.items_mapper.get_all_item_for_ingest(self.context.current_ingest.ingest_id):
                container_node = self.context.container_factory.resolve(item.context)
                if not container_node:
                    errors = item.errors or []
                    errors.append("Couldn't figure out the target conatainer")
                    self.context.items_mapper.update(item.item_id, errors=errors)
                    continue
                if not project:
                    project = self.context.container_factory.get_first_project()
                    if project:
                        self.context.current_ingest.config["target_project"] = {
                            "_id": project.id,
                            "label": project.label,
                        }
                        self.context.ingest_mapper.update(
                            self.context.current_ingest.ingest_id,
                            config=self.context.current_ingest.config
                        )

                item.context["target"] = {
                    "container_type": container_node.container_type,
                    "_id": container_node.id,
                    "label": container_node.label
                }
                self.context.items_mapper.update(item.item_id, context=item.context)
                self.context.work_queue_mapper.insert(WorkTask(
                    item_id=item.item_id,
                    ingest_id=self.context.current_ingest.ingest_id,
                    status=TaskStatus.waiting
                ))
        else:
            self.abort()

        log.debug("Review... done")

    def _next(self):
        return ProcessStage(self.context)


class ProcessStage(Stage):
    """Process stage"""

    def _run(self):
        log.debug("Processing items...")
        self.context.reporter.before_review = False
        self.context.reporter.resume()
        self.context.ingest_mapper.update(self.context.current_ingest.ingest_id, stage=IngestStage.processing)
        self.wait_while_truthy(
            self.context.work_queue_mapper.is_complete_ingest,
            self.context.current_ingest.ingest_id
        )
        log.debug("Processing items... done")

    def _next(self):
        self.context.ingest_mapper.update(self.context.current_ingest.ingest_id, processing_end=datetime.datetime.now())
        self.context.reporter.report_process_summary()
        self.context.reporter.shutdown()
        return CompletedStage(self.context)


class CompletedStage(Stage):
    """Completed stage"""

    def _run(self):
        log.debug("Ingest operation completed")
        self.save_audit_log()
        self.context.ingest_mapper.update(self.context.current_ingest.ingest_id, stage=IngestStage.complete)

        # save subject mapping
        subjects_mapping_config = get_subjects_mapping_config(
            self.context.importer_config.deid_profile,
            self.context.importer_config.deid_profiles,
        )
        if subjects_mapping_config and subjects_mapping_config.get("save-to"):
            save_subject_mappings_to_csv(
                subjects_mapping_config["save-to"],
                self.context.subjects_mapping_mapper,
                self.context.current_ingest.ingest_id,
                subjects_mapping_config.get("fields"),
            )
        deid_profile_config = get_deid_profile_config(
            self.context.importer_config.deid_profile,
            self.context.importer_config.deid_profiles,
        )
        if deid_profile_config and deid_profile_config.get("deid-log-path"):
            save_deid_log_to_csv(
                deid_profile_config["deid-log-path"],
                self.context.deid_log_mapper,
                self.context.current_ingest.ingest_id,
            )

    def _next(self):
        return ShutdownStage(self.context)


class AbortedStage(Stage):
    """Aborted stage"""

    def _run(self):
        log.debug("Aborting import...")
        if self.context.current_ingest:
            self.context.ingest_mapper.update(self.context.current_ingest.ingest_id, stage=IngestStage.aborted)
            self.save_audit_log()
        log.debug("Aborting import... done")

    def _next(self):
        return ShutdownStage(self.context)


class ShutdownStage(Stage):
    """Shutdown stage"""

    def _run(self):
        if self.context.executor:
            log.debug("Shutdown workers...")
            self.context.executor.shutdown()
            log.debug("Shutdown workers... done")
        if self.context.reporter.is_running():
            log.debug("Shutdown reporter...")
            self.context.reporter.shutdown()
            log.debug("Shutdown reporter... done")

    def _next(self):
        return None


def load_private_tags_from_csv_to_db(path, mapper, ingest_id):
    """Load private dicom tags from csv file into database.

    Csv format:
    PrivateCreator,Tag,VR,Description,VM
    Custom Creator,0x111021b0,UN,An unknown property,1

    Args:
        path (str): Path to input csv file
        mapper (PrivateTagsMapper): Private tags mapper
        ingest_id (int): Ingest id
    """
    with open(path, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            private_tag = PrivateTag(
                ingest_id=ingest_id,
                private_creator=row["PrivateCreator"],
                tag=row["Tag"],
                vr=row["VR"],
                description=row["Description"],
                vm=row.get("VM", 1),
            )
            mapper.insert(private_tag)


def load_subject_mappings_from_csv_to_db(path, mapper, ingest_id):
    """Load subject maps from csv

    Args:
        path (str): Path to input csv file
        mapper (SubjectsMappingMapper): Subjects mappings mapper
        ingest_id (int): Ingest id

    """
    with open(path, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            dicom_fields = filter(lambda item: item[0] not in ["SubjectCode", "SubjectId"], row.items())
            subject_map = SubjectMap(
                ingest_id=ingest_id,
                subject_id=row["SubjectId"],
                subject_code=row["SubjectCode"],
                field_values=list(map(lambda item: item[1], dicom_fields))
            )
            mapper.insert(subject_map)


def save_subject_mappings_to_csv(path, mapper, ingest_id, fields):
    """Export subject maps to csv

    Args:
        path (str): Path to the output csv file
        mapper (SubjectsMappingMapper): Subjects mappings mapper
        ingest_id (int): Ingest id

    """
    subject_maps = mapper.get_all_item_for_ingest(ingest_id)
    if not subject_maps:
        return
    fieldnames = ["SubjectId", "SubjectCode"] + fields
    with open(path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)

        for subject_map in subject_maps:
            writer.writerow(
                [subject_map.subject_id, subject_map.subject_code] + subject_map.field_values)


def save_deid_log_to_csv(path, mapper, ingest_id):
    """Export deid log to csv file

    Args:
        path (str): Output csv file path
        mapper (DeidLogMapper): Deid log mapper
        ingest_id (int): Ingest id

    """

    deid_logs = mapper.get_all_item_for_ingest(ingest_id)
    if not deid_logs:
        return

    fieldnames = ["path", "type"]
    with open(path, "w") as f:
        writer = None
        for log_entry in deid_logs:
            if not writer:
                fieldnames.extend(log_entry.field_values.keys())
                writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow({
                "path": log_entry.path,
                "type": log_entry.log_type,
                **log_entry.field_values,
            })


STAGE_MAP = {
    IngestStage.scan: WaitForDiscoverStage,
    IngestStage.review: ReviewStage,
    IngestStage.processing: ProcessStage,
    IngestStage.complete: CompletedStage,
    IngestStage.aborted: AbortedStage,
}
