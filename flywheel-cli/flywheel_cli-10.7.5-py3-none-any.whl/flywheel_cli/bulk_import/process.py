"""Provides WorkQueue class."""

import logging
import os
import tempfile
from multiprocessing import current_process

import fs
import pydicom
from flywheel import create_drone_client
from flywheel_migration import dcm

from .. import util
from ..importers.container_factory import ContainerNode
from ..importers.packfile import create_zip_packfile
from ..sdk_impl import SdkUploadWrapper, create_flywheel_client, load_config
from ..walker import create_walker
from .db.models import AuditLog, TaskStatus, IngestStage
from .deid import DeidLogger, load_deid_profile
from .executor import AbstractQueue, Task
from .importers.config import create_config_from_dict

log = logging.getLogger(__name__)

MAX_IN_MEMORY_XFER = 32 * (2 ** 20) # Files under 32mb send as one chunk


class ProcessQueue(AbstractQueue):  # pylint: disable=too-few-public-methods
    """Class that wraps a WorkQueueMapper object and provides methods that necessary for the MultiQueueConsumer."""

    def __init__(self, context):
        self.context = context
        self.completed_task_count = 0
        # initialize an uploader only once in a thread
        sdk_conf = load_config()
        if sdk_conf and sdk_conf.get("key"):
            fw = create_flywheel_client()
        else:
            core_host = os.environ.get("FLYWHEEL_RUNTIME_HOST")
            drone_secret = os.environ.get('FLYWHEEL_CORE_DRONE_SECRET')
            fw = create_drone_client(core_host, drone_secret, "service", "bulk-import")
        self.uploader = SdkUploadWrapper(fw)

    def get(self):
        """Get an item from the scan queue table.

        Returns:
            Task -- Task object that can be executed.
        """
        worker_id = current_process().name
        task_item = self.context.work_queue_mapper.get(worker_id)
        if task_item is not None:
            return ProcessingTask(task_item, self.context.ingest_factory, self.uploader, self.context.config)
        return None


class ProcessingTask(Task):
    """Processing task that wraps a work task from the work queue.

    According to type the work task prepare/create the file that needs to be uploaded
    and finally upload the file.
    """

    def __init__(self, work_task, ingest_factory, uploader, config):
        self.work_task = work_task
        self.uploader = uploader
        self.config = config
        self.ingest_factory = ingest_factory
        self.ingest_mapper = self.ingest_factory.create_mapper()
        self.items_mapper = self.ingest_factory.create_ingest_items_mapper()
        self.work_queue_mapper = self.ingest_factory.create_work_queue_mapper()
        self.audit_log_mapper = self.ingest_factory.create_audit_log_mapper()
        self.private_tags_mapper = self.ingest_factory.create_private_tags_mapper()
        self.deid_log_mapper = self.ingest_factory.create_deid_log_mapper()

    def execute(self):
        """Execute the task"""
        ingest_item = self.items_mapper.find(self.work_task.item_id)
        current_ingest = self.ingest_mapper.find(ingest_item.ingest_id)
        if current_ingest.stage == IngestStage.aborted:
            self.work_queue_mapper.update(self.work_task.task_id, status=TaskStatus.failed)
            return
        importer_config = create_config_from_dict(current_ingest.config["importer_config"])
        walker = create_walker(current_ingest.fs_path)
        container = ContainerNode(
            ingest_item.context["target"]["container_type"],
            cid=ingest_item.context["target"]["_id"],
            label=ingest_item.context["target"]["label"]
        )
        try:
            metadata = None

            deid_profile = None
            if importer_config.de_identify:
                private_tags = self.private_tags_mapper.get_all_item_for_ingest(
                    current_ingest.ingest_id
                )
                self.load_private_tags(private_tags)
                deid_profile = load_deid_profile(
                    importer_config.deid_profile,
                    importer_config.deid_profiles,
                )
                deid_profile.initialize()
                for file_profile in deid_profile.file_profiles:
                    file_profile.set_log(DeidLogger(self.deid_log_mapper, current_ingest.ingest_id))
            if importer_config.ignore_unknown_tags:
                dcm.global_ignore_unknown_tags()

            if ingest_item.item_type == "packfile":
                log.debug("Creating packfile")
                file_obj, metadata = self.create_packfile(
                    container, walker, ingest_item.context,
                    ingest_item.files, ingest_item.subdir,
                    importer_config.get_compression_type(),
                    self.config.max_spool,
                    deid_profile,
                )
                file_name = metadata["name"]
            else:
                file_obj = walker.open(fs.path.join(ingest_item.subdir, ingest_item.files[0]))
                file_name = ingest_item.files[0]

            self.upload_file(container, file_name, file_obj, metadata)
            walker.close()

            log_entry = AuditLog(ingest_id=ingest_item.ingest_id,
                                 src_path=fs.path.join(ingest_item.subdir, file_name),
                                 fw_path=AuditLog.get_container_resolver_path(ingest_item, container),
                                 message="Completed")
            self.audit_log_mapper.insert(log_entry, importer_config.no_audit_log)

            self.work_queue_mapper.update(self.work_task.task_id, status=TaskStatus.complete)
        except Exception as exc:  # pylint: disable=broad-except
            log.exception(exc)

            log_entry = AuditLog(ingest_id=ingest_item.ingest_id,
                                 src_path=ingest_item.subdir,
                                 fw_path=AuditLog.get_container_resolver_path(ingest_item, container),
                                 failed=True,
                                 message=f"Error while uploading: {exc}")
            self.audit_log_mapper.insert(log_entry, importer_config.no_audit_log)

            # always set the task status to failed if some exception happened
            self.work_queue_mapper.update(self.work_task.task_id, status=TaskStatus.failed)

    @staticmethod
    def load_private_tags(tags):
        """Load private dicom tags.

        Args:
            tags (list): List of private tags

        """
        for tag in tags:
            _tag = pydicom.tag.Tag(tag.tag)
            pydicom.datadict.add_private_dict_entry(tag.private_creator, _tag, tag.vr,
                                                    tag.description, tag.vm)

    @staticmethod
    def create_packfile(container, walker, context, files, subdir, compression, max_spool=None, deid_profile=None):
        """Create packfile"""
        if max_spool:
            tmpfile = tempfile.SpooledTemporaryFile(max_size=max_spool)
        else:
            tmpfile = tempfile.TemporaryFile()

        file_name = util.create_packfile_name(context, container)

        paths = list(map(lambda f_name: fs.path.join(subdir, f_name), files))
        zip_member_count = create_zip_packfile(
            tmpfile, walker, packfile_type=context["packfile"]["type"],
            paths=paths, subdir=subdir, compression=compression,
            flatten=context["packfile"].get("flatten", False),
            deid_profile=deid_profile,
        )

        log.debug(f"zipped {zip_member_count} files")

        tmpfile.seek(0)

        metadata = {
            'name': file_name,
            'zip_member_count': zip_member_count,
            'type': context["packfile"]["type"]
        }


        return tmpfile, metadata

    def upload_file(self, container, file_name, file_obj, metadata=None):
        """Upload a file to a target container"""
        upload_file = UploadFileWrapper(file_obj)
        if upload_file.len < MAX_IN_MEMORY_XFER:
            _data = upload_file.read(upload_file.len)
            self.uploader.upload(container, file_name, _data, metadata=metadata)
        else:
            self.uploader.upload(container, file_name, upload_file, metadata=metadata)


class UploadFileWrapper:
    """Wrapper around file that measures progress"""
    def __init__(self, fileobj):
        """Initialize a file wrapper"""
        self.fileobj = fileobj
        self._sent = 0
        self._total_size = None
        self.name = fileobj.name

    def read(self, size=-1):
        """Read chunk from file"""
        chunk = self.fileobj.read(size)
        self._sent = self._sent + len(chunk)
        return chunk

    def reset(self):
        """Reset file offset"""
        self.fileobj.seek(0)
        self._sent = 0

    def close(self):
        """Close file"""
        self.fileobj.close()
        self.fileobj = None

    @property
    def len(self):
        """Get remaining size"""
        return self.total_size - self._sent

    @property
    def total_size(self):
        """Get total size"""
        if self._total_size is None:
            self.fileobj.seek(0, 2)
            self._total_size = self.fileobj.tell()
            self.fileobj.seek(0)
        return self._total_size

    @property
    def get_bytes_sent(self):
        """Get bytes sent"""
        return self._sent
