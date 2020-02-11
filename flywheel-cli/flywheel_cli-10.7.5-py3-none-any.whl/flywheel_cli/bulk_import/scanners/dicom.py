"""Provides DicomScanner class."""

import copy
import datetime
import gzip
import itertools
import logging
import os

import fs
from flywheel_migration.dcm import DicomFile
from pydicom.datadict import tag_for_keyword
from pydicom.tag import Tag

from ... import util
from ...walker import create_walker
from ..db.models import IngestItem, TaskStatus, IngestStage
from ..deid import get_subjects_mapping_config, load_deid_profile
from ..importers.config import create_config_from_dict
from .abstract_scanner import AbstractScanner

log = logging.getLogger(__name__)
SUBJECT_CODE_KEY = 'SubjectCode'

# Specifying just the list of tags we're interested in speeds up dicom scanning
DICOM_TAGS = [
    "Manufacturer",
    "AcquisitionNumber",
    "AcquisitionDate",
    "AcquisitionTime",
    "SeriesDate",
    "SeriesTime",
    "SeriesInstanceUID",
    "ImageType",
    "StudyDate",
    "StudyTime",
    "StudyInstanceUID",
    "OperatorsName",
    "PatientName",
    "PatientID",
    "StudyID",
    "SeriesDescription",
    "PatientBirthDate",
    "SOPInstanceUID",
]


class DicomScanner(AbstractScanner):
    """Scanner class to scan dicom files and create appropriate ingest items."""

    scanner_type = "dicom"
    # The session label dicom header key
    session_label_key = "StudyDescription"

    def __init__(self, scan_task, ingest_factory, config):
        self.config = config
        self.scan_task = scan_task
        self.ingest_factory = ingest_factory
        self.related_acquisitions = False
        self.sessions = {}
        self.deid_profile = None
        self.ingest_mapper = self.ingest_factory.create_mapper()
        self.items_mapper = self.ingest_factory.create_ingest_items_mapper()
        self.scan_queue_mapper = self.ingest_factory.create_scan_queue_mapper()
        self.subjects_mapping_mapper = self.ingest_factory.create_subjects_mapping_mapper()
        self.current_ingest = None
        self.subjects_mapping_config = None

    def execute(self):
        """Execute the scan and create ingest items."""
        try:
            self.current_ingest = self.ingest_mapper.find(self.scan_task.ingest_id)
            if self.current_ingest.stage == IngestStage.aborted:
                self.scan_queue_mapper.update(self.scan_task.task_id, status=TaskStatus.failed)
                return
            importer_config = create_config_from_dict(self.current_ingest.config["importer_config"])
            walker = create_walker(
                self.current_ingest.fs_path,
                **importer_config.generate_walker_kwargs()
            )
            tags = [Tag(tag_for_keyword(keyword)) for keyword in DICOM_TAGS]
            if importer_config.de_identify:
                self.deid_profile = load_deid_profile(
                    importer_config.deid_profile,
                    importer_config.deid_profiles,
                ).get_file_profile("dicom")
                self.subjects_mapping_config = get_subjects_mapping_config(
                    importer_config.deid_profile,
                    importer_config.deid_profiles,
                )
            for root, _, files in walker.walk(subdir=self.scan_task.path):
                for file_info in files:
                    prefix_path = walker.get_prefix_path(root)
                    path = walker.combine(prefix_path, file_info.name)

                    with walker.open(path, "rb", buffering=self.config.buffer_size) as f:
                        self.scan_dicom_file(self.scan_task.path, path, f, tags, walker, size=file_info.size)
            walker.close()
            self.create_ingest_items(self.current_ingest.ingest_id)
            # finally mark the task as complete
            self.scan_queue_mapper.update(self.scan_task.task_id, status=TaskStatus.complete)
        except Exception as exc:  # pylint: disable=broad-except
            log.exception(exc)
            self.scan_queue_mapper.update(self.scan_task.task_id, status=TaskStatus.failed)

    def scan_dicom_file(self, parent_dir, path, fp, tags, walker, size=0):
        """Scan a single dicom file

        Args:
            parent_dir (str): Parent dir
            path   (str): File path
            fp     (BinaryIO): File like object
            tags   (list): Dicom tags
            walker (AbstractWalker): Filesystem walker object

        """
        _, ext = os.path.splitext(path)
        if ext.lower() == ".gz":
            fp = gzip.GzipFile(fileobj=fp)

        # Don't decode while scanning, stop as early as possible
        # TODO: will we ever rely on fields after stack id for subject mapping
        dcm = DicomFile(
            fp,
            parse=False,
            session_label_key=self.session_label_key,
            decode=self.related_acquisitions,
            stop_when=_at_stack_id(self.related_acquisitions),
            update_in_place=False,
            specific_tags=tags,
            force=util.is_dicom_file(path),
        )

        acquisition = self.resolve_acquisition(self.scan_task.context, dcm)
        series_uid = self.get_value(dcm, "SeriesInstanceUID", required=True)
        sop_uid = self.get_value(dcm, "SOPInstanceUID", required=True)
        if sop_uid in acquisition.files.setdefault(series_uid, {}):
            orig_path, _ = acquisition.files[series_uid][sop_uid]
            if not util.files_equal(walker, path, orig_path):
                message = (
                    "DICOM conflicts with {}! Both files have the "
                    "same IDs, but contents differ!"
                ).format(orig_path)
                log.warning(message)
                # TODO: log to audit logs
        else:
            acquisition.files[series_uid][sop_uid] = (fs.path.frombase(
                fs.path.abspath(parent_dir),
                fs.path.abspath(path),
            ), size)

        if series_uid not in acquisition.filenames:
            acquisition_timestamp = self.determine_acquisition_timestamp(
                dcm
            )
            series_label = self.determine_acquisition_label(
                acquisition.context,
                dcm,
                series_uid,
                timestamp=acquisition_timestamp,
            )
            filename = DicomScanner.determine_dicom_zipname(
                acquisition.filenames, series_label
            )
            acquisition.filenames[series_uid] = filename

    def create_ingest_items(self, current_ingest_id):
        """Create ingest items that this scan discovered

        Args:
            current_ingest_id (int): Id of the current ingest that the scan task relates to

        """
        for session in self.sessions.values():
            session_context = copy.deepcopy(self.scan_task.context)
            session_context.update(session.context)

            for acquisition in itertools.chain(session.acquisitions.values(), session.secondary_acquisitions.values()):

                acquisition_context = copy.deepcopy(session_context)
                acquisition_context.update(acquisition.context)

                for series_uid, files in acquisition.files.items():
                    files = list(files.values())
                    size = sum(map(lambda f: f[1], files))
                    files = list(map(lambda f: f[0], files))
                    filename = acquisition.filenames.get(series_uid)

                    packfile_context = copy.deepcopy(acquisition_context)
                    packfile_context["packfile"] = {
                        "name": filename,
                        "file_count": len(files),
                        "type": "dicom",
                        "flatten": True,
                    }
                    # insert the ingest item
                    self.items_mapper.insert(IngestItem(
                        ingest_id=current_ingest_id,
                        subdir=self.scan_task.path,
                        files=files,
                        size=size,
                        item_type="packfile",
                        context=packfile_context,
                        mtime=datetime.datetime.now()
                    ))

    @staticmethod
    def determine_dicom_zipname(filenames, series_label):
        """Return a filename for the dicom series that is unique to a container

        Args:
            filenames (dict): A map of series uids to filenames
            series_label (str): The base to use for the filename

        Returns:
            str: The filename for the zipped up series
        """
        filename = series_label + ".dicom.zip"
        duplicate = 1
        while filename in filenames.values():
            filename = series_label + f"_dup-{duplicate}.dicom.zip"
        return filename

    def resolve_session(self, context, dcm):
        """Find or create a sesson from a dcm file. """
        session_uid = self.get_value(dcm, "StudyInstanceUID", required=True)
        if session_uid not in self.sessions:
            subject_label = context.get("subject", {}).get("label")
            # Map subject
            if subject_label:
                subject_code = subject_label
            elif self.subjects_mapping_config:
                key = [self.extract_field(dcm, field) for field in self.subjects_mapping_config["fields"]]
                code_formatter = lambda subject_id: self.subjects_mapping_config["format"].format(**{SUBJECT_CODE_KEY: subject_id})
                subject_map = self.subjects_mapping_mapper.get(self.current_ingest.ingest_id, key, code_formatter)
                subject_code = subject_map.subject_code
            else:
                subject_code = self.get_value(dcm, "PatientID", "")

            session_timestamp = self.get_timestamp(dcm, "StudyDate", "StudyTime")

            # Create session
            self.sessions[session_uid] = DicomSession(
                {
                    "session": {
                        "uid": session_uid.replace(".", ""),
                        "label": self.determine_session_label(
                            context, dcm, session_uid, timestamp=session_timestamp
                        ),
                        "timestamp": session_timestamp,
                        "timezone": str(util.DEFAULT_TZ),
                    },
                    "subject": {"label": subject_code},
                }
            )
        return self.sessions[session_uid]

    def resolve_acquisition(self, context, dcm):
        """Find or create an acquisition from a dcm file. """
        session = self.resolve_session(context, dcm)
        series_uid = self.get_value(dcm, "SeriesInstanceUID", required=True)
        primary_acquisition_file = True

        if self.related_acquisitions and dcm.get("ReferencedFrameOfReferenceSequence"):
            # We need to add it to the acquisition of the primary series uid
            try:
                series_uid = (
                    dcm.get("ReferencedFrameOfReferenceSequence")[0]
                    .get("RTReferencedStudySequence")[0]
                    .get("RTReferencedSeriesSequence")[0]
                    .get("SeriesInstanceUID")
                )
                primary_acquisition_file = False
            except (TypeError, IndexError, AttributeError):
                log.warning(
                    "Unable to find related series for file {}. Uploading into its own acquisition"
                )

        if series_uid not in session.acquisitions:
           # full acquisition doesn't exists
            if (not primary_acquisition_file and series_uid in session.secondary_acquisitions):
                # The secondary acquisition exists
                return session.secondary_acquisitions[series_uid]

            acquisition_timestamp = self.determine_acquisition_timestamp(dcm)
            acquisition = DicomAcquisition(
                {
                    "acquisition": {
                        "uid": series_uid.replace(".", ""),
                        "label": self.determine_acquisition_label(
                            context, dcm, series_uid, timestamp=acquisition_timestamp
                        ),
                        "timestamp": acquisition_timestamp,
                        "timezone": str(util.DEFAULT_TZ),
                    }
                }
            )

            if primary_acquisition_file:
                # Check for a secondary and add it the files and filenames to the primary
                if series_uid in session.secondary_acquisitions:
                    acquisition.files = session.secondary_acquisitions.get(
                        series_uid
                    ).files
                    acquisition.filenames = session.secondary_acquisitions.pop(
                        series_uid
                    ).filenames

                session.acquisitions[series_uid] = acquisition
                return session.acquisitions[series_uid]
            session.secondary_acquisitions[series_uid] = acquisition
            return session.secondary_acquisitions[series_uid]

        # Acquisition already exists
        return session.acquisitions[series_uid]

    def determine_session_label(self, context, _dcm, uid, timestamp=None):  # pylint: disable=no-self-use
        """Determine session label from DICOM headers"""
        session_label = context.get("session", {}).get("label")
        if session_label:
            return session_label

        if timestamp:
            return timestamp.strftime("%Y-%m-%d %H:%M:%S")

        return uid

    def determine_acquisition_label(self, context, dcm, uid, timestamp=None):
        """Determine acquisition label from DICOM headers"""
        acquisition_label = context.get("acquisition", {}).get("label")
        if acquisition_label:
            return acquisition_label

        name = self.get_value(dcm, "SeriesDescription")
        if not name and timestamp:
            name = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        if not name:
            name = uid
        return name

    def determine_acquisition_timestamp(self, dcm):
        """Get acquisition timestamp (based on manufacturer)"""
        # Create the acquisition because the acqusition doesn't exist
        if dcm.get_manufacturer() == "SIEMENS":
            timestamp = self.get_timestamp(dcm, "SeriesDate", "SeriesTime")
        else:
            timestamp = self.get_timestamp(dcm, "AcquisitionDate", "AcquisitionTime")
        return timestamp

    def get_timestamp(self, dcm, date_key, time_key):
        """Get a timestamp value"""
        date_value = self.get_value(dcm, date_key)
        time_value = self.get_value(dcm, time_key)

        return DicomFile.timestamp(date_value, time_value, util.DEFAULT_TZ)

    def get_value(self, dcm, key, default=None, required=False):
        """Get a transformed value"""
        if self.deid_profile:
            result = self.deid_profile.get_value(None, dcm.raw, key)
            if not result:
                result = default
        else:
            result = dcm.get(key, default)

        if result is None and required:
            raise ValueError(f"DICOM is missing {key}")

        return result

    @staticmethod
    def extract_field(record, fieldname):
        """Extract field from record, and normalize it (by converting to lowercase and stripping whitespace)

        Args:
            record: A dictionary-like object
            fieldname (str): The field to extract

        Returns:
            str: The normalized value
        """
        value = record.get(fieldname, '')
        return str(value).strip().lower()


class DicomSession:
    """Dicom session class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, context):
        """Helper class that holds session properties and acquisitions"""
        self.context = context
        self.acquisitions = {}
        self.secondary_acquisitions = {}  # Acquisitions that we don't have all
        # of the info for yet


class DicomAcquisition:
    """Dicom acquisition class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, context):
        """Helper class that holds acquisition properties and files"""
        self.context = context
        self.files = (
            {}
        )  # Map of primary_series_uids to maps of series uids to filepaths
        # So that the primary series uid can be used to group multiple dicom series into one acquisition
        self.filenames = {}  # A map of series uid to filenames


def _at_stack_id(related_acquisitions):
    if related_acquisitions:
        stop_tag = (0x3006, 0x0011)
    else:
        stop_tag = (0x0020, 0x9056)

    def f(tag, *args):  # pylint: disable=unused-argument
        return tag == stop_tag

    return f
