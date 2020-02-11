"""Provides AuditLog model class."""

from flywheel_cli import util


class AuditLog:
    """Represents an audit log entry

    Attributes:
        log_id (int): Unique ID of the audit log entry.
        ingest_id (int): The ID of the ingest operation thid belongs to.
        src_path (str): The source path of the file.
        fw_path (str): The flywheel path of the file.
        failed (bool): Whether there was a failure.
        message (str): Message about the event.
    """

    def __init__(self, log_id=None, ingest_id=None, src_path=None, fw_path=None, failed=False, message=None):
        """Create an AuditLog entry"""
        self.log_id = log_id
        self.ingest_id = ingest_id
        self.src_path = src_path
        self.fw_path = fw_path
        self.failed = failed
        self.message = message

    @staticmethod
    def map_field(key, value):  # pylint: disable=unused-argument
        """Convert from object to map for serialization"""
        return value

    @staticmethod
    def from_map(kwargs):
        """Deserialize kwargs into AuditLog.

        Args:
            kwargs (dict): The constructor arguments

        Returns:
            AuditLog: The deserialized audit log entry
        """
        return AuditLog(**kwargs)

    @staticmethod
    def get_container_resolver_path(ingest_item, container):
        """Utility function for getting container's resolver path"""
        context = ingest_item.context
        path = []
        if context is None:
            return ""
        for key, value in context.items():
            if key == "group":
                path.append(value["_id"])
            else:
                path.append(value.get("label") or value.get("_id") or "")
            if key == "acquisition":
                break
        if "packfile" in context:
            path.append(util.create_packfile_name(context, container))
        else:
            path.append(ingest_item.files[0])
        return "/".join(path)

    def __repr__(self):
        return f"AuditLog(log_id={self.log_id},ingest_id={self.ingest_id},src_path={self.src_path},message={self.message})"
