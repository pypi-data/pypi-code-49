"""Provides UploadTask class."""

import logging
import tempfile

import fs
import fs.copy
import fs.path
from fs.zipfs import ZipFS
from flywheel_migration import dcm

from .. import deid
from .abstract import AbstractTask

log = logging.getLogger(__name__)


class UploadTask(AbstractTask):
    """Process ingest item (deidentify, pack, upload)
    Used configuration variables:
        src_fs_url
        de_identify
        deid_profile
        deid_profiles
        ignore_unknown_tags
        max_spool
    Used configuration methods:
        create_walker
        get_compression

    """
    can_retry = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.walker = None
        self.deid_profile = None

    def _initialize(self):
        self.walker = self.config.create_walker(self.config.src_fs_url)
        if self.config.de_identify:
            self.deid_profile = deid.load_deid_profile(
                self.config.deid_profile,
                self.config.deid_profiles,
            )
            # setup deid logging
            deid_logger = deid.DeidLogger(self.ingest_db)
            for file_profile in self.deid_profile.file_profiles:
                file_profile.set_log(deid_logger)
            self.deid_profile.initialize()
        if self.config.ignore_unknown_tags:
            dcm.global_ignore_unknown_tags()

    def _after_complete(self):
        self.ingest_db.finalize_ingest_after_upload()

    def _after_failed(self):
        self.ingest_db.finalize_ingest_after_upload()

    def _execute(self):
        item = self.ingest_db.get_item(self.task.item_id)
        metadata = None
        container = self.ingest_db.get_container(item.container_id)
        if item.type == "packfile":
            log.debug("Creating packfile")
            file_obj, metadata = self.create_packfile(
                item.context,
                item.filename,
                item.files,
                item.dir,
            )
            file_name = metadata["name"]
        else:
            file_obj = self.walker.open(fs.path.join(item.dir, item.files[0]))
            file_name = item.files[0]
        self.fw.upload(
            container.level.name,
            container.dst_context.get("_id"),
            file_name,
            file_obj,
            metadata
        )
        # TODO: cache scanned files and reuse during upload
        self.walker.close()

    def create_packfile(self, context, filename, files, subdir):
        """Create packfile"""
        max_spool = self.config.max_tempfile * (1024 * 1024)
        if max_spool:
            tmpfile = tempfile.SpooledTemporaryFile(max_size=max_spool)
        else:
            tmpfile = tempfile.TemporaryFile()

        packfile_type = context["packfile"]["type"]
        paths = list(map(lambda f_name: fs.path.join(subdir, f_name), files))
        flatten = context["packfile"].get("flatten", False)
        compression = self.config.get_compression_type()
        if compression is None:
            import zipfile  # pylint: disable=import-outside-toplevel
            compression = zipfile.ZIP_DEFLATED

        with ZipFS(tmpfile, write=True, compression=compression) as dst_fs:
            # Attempt to de-identify using deid_profile first
            processed = False
            if self.deid_profile:
                processed = self.deid_profile.process_packfile(packfile_type, self.walker, dst_fs, paths)
            if not processed:
                # Otherwise, just copy files into place
                for path in paths:
                    # Ensure folder exists
                    target_path = path
                    if subdir:
                        target_path = self.walker.remove_prefix(subdir, path)
                    if flatten:
                        target_path = fs.path.basename(path)
                    folder = fs.path.dirname(target_path)
                    dst_fs.makedirs(folder, recreate=True)
                    with self.walker.open(path, 'rb') as src_file:
                        dst_fs.upload(target_path, src_file)

        zip_member_count = len(paths)
        log.debug(f"zipped {zip_member_count} files")

        tmpfile.seek(0)

        metadata = {
            'name': filename,
            'zip_member_count': zip_member_count,
            'type': context["packfile"]["type"]
        }

        return tmpfile, metadata
