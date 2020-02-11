"""CLI Bulk Import Verify Config"""


class ConfigVerificationError(Exception):
    """Handle Config Verification Errors"""

    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return self.msg


class VerifyGlobalConfigMixin:
    """Global Config Verification Mixin"""
    # pylint: disable=too-few-public-methods

    def verify_config(self):
        """Verify global scope config"""


class VerifyBulkImportConfigMixin:
    """Bulk Import Config Verification Mixin"""
    # pylint: disable=too-few-public-methods

    def verify_config(self):
        """Verify bulk import config"""
        if hasattr(self, 'de_identify') and hasattr(self, 'deid_profile_name') and self.de_identify and self.deid_profile_name is not None:
            raise ConfigVerificationError('De-identify and (deid-)profile are mutually exclusive')


class VerifyParrecConfigMixin:
    """Parrec Config Verification Mixin"""
    # pylint: disable=too-few-public-methods

    def verify_specific_config(self):
        """Verify parrec importer specific config"""


class VerifyBrukerConfigMixin:
    """Bruker Config Verification Mixin"""
    # pylint: disable=too-few-public-methods

    def verify_specific_config(self):
        """Verify bruker importer specific config"""
