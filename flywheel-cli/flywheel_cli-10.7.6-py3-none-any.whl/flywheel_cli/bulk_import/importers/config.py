"""Importers config classes"""

from ... import util
from ..config.config import BaseImporterConfig, BulkImportConfigError
from ..config.verify_config import ConfigVerificationError

class DicomImporterConfig(BaseImporterConfig):
    """Dicom Importer Configuration"""
    def __init__(self, group=None, project=None, subject=None, session=None, **kwargs):
        super().__init__(**kwargs)
        self.importer_type = "dicom"
        self.group = group
        self.project = project
        self.subject = subject
        self.session = session
        self.verify()

    def verify(self):
        """Verify dicom importer specific config"""
        super().verify()
        if not getattr(self, 'group', None) or not getattr(self, 'project', None):
            raise ConfigVerificationError('Missing required parameters: group, project')

    @staticmethod
    def add_arguments(parser):
        """Add dicom importer arguments"""
        super(DicomImporterConfig, DicomImporterConfig).add_arguments(parser)
        parser.add_argument('group', nargs='?', metavar='group_id', help='The id of the group', type=util.group_id)
        parser.add_argument('project', nargs='?', metavar='project_label', help='The label of the project')
        parser.add_argument('--subject', metavar='subject_label', help='Override value for the subject label')
        parser.add_argument('--session', metavar='session_label', help='Override value for the session label')
        return parser

    @staticmethod
    def get_public_attrs():
        super_attrs = super(DicomImporterConfig, DicomImporterConfig).get_public_attrs()
        return ["group", "project", "subject", "session"] + super_attrs



class FolderImporterConfig(BaseImporterConfig):
    """Folder Importer Configuration"""
    # pylint: disable=too-many-arguments
    def __init__(self, group=None, project=None, root_dirs=None, repack=None, dicom=None,
                 pack_acquisitions=None, no_subjects=None, no_sessions=None, **kwargs):
        super().__init__(**kwargs)
        self.importer_type = "folder"
        self.group = group
        self.project = project
        self.root_dirs = root_dirs or 0
        self.repack = repack or False
        self.dicom = dicom
        self.pack_acquisitions = pack_acquisitions
        self.no_subjects = no_subjects
        self.no_sessions = no_sessions
        self.verify()

    def verify(self):
        """Verify that configuration is valid"""
        super().verify()
        if getattr(self, 'dicom', None) and getattr(self, 'pack_acquisitions', None):
            raise ConfigVerificationError('Dicom and pack-acquisitons arguments are mutually exclusive')

        if getattr(self, 'no_subjects', None) and getattr(self, 'no_sessions', None):
            raise ConfigVerificationError('No-subjects and no-sessions arguments are mutually exclusive')

    @staticmethod
    def add_arguments(parser):
        """Add folder importer arguments to a given parser"""
        super(FolderImporterConfig, FolderImporterConfig).add_arguments(parser)
        parser.add_argument('--group', '-g', metavar='<id>', help='The id of the group, if not in folder structure', type=util.group_id)
        parser.add_argument('--project', '-p', metavar='<label>', help='The label of the project, if not in folder structure')

        # Cannot specify dicom folder name with dicom-acquistions, or bruker-acquisitions with either
        acq_group = parser.add_mutually_exclusive_group()
        acq_group.add_argument('--dicom', metavar='name', help='The name of dicom subfolders to be zipped prior to upload (default: dicom)')
        acq_group.add_argument('--pack-acquisitions', metavar='type',
                               help='Acquisition folders only contain acquisitions of <type> and are zipped prior to upload')

        #parser.add_argument('--repack', action='store_true', help='Whether or not to validate, de-identify and repackage zipped packfiles')

        no_level_group = parser.add_mutually_exclusive_group()
        no_level_group.add_argument('--no-subjects', action='store_true', help='no subject level (create a subject for every session)')
        no_level_group.add_argument('--no-sessions', action='store_true', help='no session level (create a session for every subject)')

        parser.add_argument('--root-dirs', type=int, default=0, help='The number of directories to discard before matching')
        return parser

    @staticmethod
    def get_public_attrs():
        super_attrs = super(FolderImporterConfig, FolderImporterConfig).get_public_attrs()
        return ["group", "project", "root_dirs", "repack", "dicom", "pack_acquisitions",
                "no_subjects", "no_sessions"] + super_attrs


class TemplateImporterConfig(BaseImporterConfig):
    """Template Importer Configuration"""
    def __init__(self, template=None, group=None, project=None, repack=None,
                 no_subjects=None, no_sessions=None, set_vars=None, **kwargs):
        super().__init__(**kwargs)
        self.importer_type = "template"
        self.template = template
        self.group = group
        self.project = project
        self.repack = repack or False
        self.no_subjects = no_subjects
        self.no_sessions = no_sessions
        self.set_vars = set_vars or []
        self.verify()

    def verify(self):
        """Verify that configuration is valid"""
        super().verify()
        if getattr(self, 'no_subjects', None) and getattr(self, 'no_sessions', None):
            raise ConfigVerificationError('No-subjects and no-sessions arguments are mutually exclusive')

    @staticmethod
    def add_arguments(parser):
        """Add template importer arguments"""
        super(TemplateImporterConfig, TemplateImporterConfig).add_arguments(parser)
        parser.add_argument('template', nargs='?', help='The template string')
        parser.add_argument('--group', '-g', metavar='<id>', help='The id of the group, if not in folder structure', type=util.group_id)
        parser.add_argument('--project', '-p', metavar='<label>', help='The label of the project, if not in folder structure')

        # parser.add_argument('--repack', action='store_true', help='Whether or not to validate, de-identify and repackage zipped packfiles')

        no_level_group = parser.add_mutually_exclusive_group()
        no_level_group.add_argument('--no-subjects', action='store_true', help='no subject level (create a subject for every session)')
        no_level_group.add_argument('--no-sessions', action='store_true', help='no session level (create a session for every subject)')

        parser.add_argument('--set-var', '-s', metavar='key=value', action='append', default=[],
                            type=util.split_key_value_argument, help='Set arbitrary key-value pairs')

        return parser

    @staticmethod
    def get_public_attrs():
        super_attrs = super(TemplateImporterConfig, TemplateImporterConfig).get_public_attrs()
        return ["group", "project", "template", "repack", "no_subjects", "no_sessions", "set_vars"] + super_attrs

CONFIG_MAP = {
    'dicom': DicomImporterConfig,
    'folder': FolderImporterConfig,
    'template': TemplateImporterConfig,
}


def create_config_from_dict(config):
    """Create an importer config instance from dict"""
    importer_type = config.get("importer_type")
    config_cls = get_config_cls(importer_type)
    return config_cls.from_dict(config)

def get_config_cls(importer_type):
    """Get config class for a given importer"""
    config_cls = CONFIG_MAP.get(importer_type)
    if not config_cls:
        raise BulkImportConfigError("Invalid type")

    return config_cls
