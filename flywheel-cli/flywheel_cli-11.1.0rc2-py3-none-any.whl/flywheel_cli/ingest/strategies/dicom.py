"""Provides the DicomImporter class."""

from pydantic import Field, validator

from ... import util
from ..template import create_scanner_node
from ..config import BaseIngestConfig
from .abstract import AbstractIngestStrategy


class DicomIngestStrategyConfig(BaseIngestConfig):
    """Config class for dicom ingest strategy"""
    strategy_type: str = Field("dicom", const=True, argparse_opts={
        "skip": True,
    })
    group: str = Field(..., argparse_opts={
        "positional": True,
        "nargs": "?",
        "metavar": "GROUP_ID",
        "help": "The id of the group",
    })
    project: str = Field(..., argparse_opts={
        "positional": True,
        "nargs": "?",
        "metavar": "PORJECT_LABEL",
        "help": "The label of the project",
    })
    subject: str = Field(None, argparse_opts={
        "metavar": "LABEL",
        "help": "Override value for the subject label"
    })
    session: str = Field(None, argparse_opts={
        "metavar": "LABEL",
        "help": "Override value for the session label"
    })
    # Hide the following config options since these are not relevant for the
    # dicom ingest strategy
    no_subjects: bool = Field(False, argparse_opts={
        "skip": True,
    })
    no_sessions: bool = Field(False, argparse_opts={
        "skip": True,
    })

    @validator("group")
    def validate_group_id(cls, val):  # pylint: disable=no-self-argument, no-self-use
        """Validate group id"""
        return util.group_id(val)


class DicomIngestStrategy(AbstractIngestStrategy):
    """Strategy class to ingest only DICOM files."""
    help_text = "Ingest dicom files"
    config_cls = DicomIngestStrategyConfig

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.config.subject:
            util.set_nested_attr(self.context, "subject.label", self.config.subject)
        if self.config.session:
            util.set_nested_attr(self.context, "session.label", self.config.session)

    def initialize(self):
        """Initialize the importer."""
        self.add_template_node(create_scanner_node("dicom"))
