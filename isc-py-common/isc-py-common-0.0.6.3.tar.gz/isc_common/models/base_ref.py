import logging

from isc_common.fields.code_field import CodeField
from isc_common.fields.description_field import DescriptionField
from isc_common.fields.name_field import NameField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditModel

logger = logging.getLogger(__name__)


class Hierarcy(AuditModel):
    parent = ForeignKeyProtect("self", null=True, blank=True)

    class Meta:
        abstract = True


class BaseRef(AuditModel):
    code = CodeField()
    name = NameField()
    description = DescriptionField()

    class Meta:
        abstract = True

class BaseRefHierarcy(Hierarcy):
    code = CodeField()
    name = NameField()
    description = DescriptionField()

    class Meta:
        abstract = True


class BaseRefShort(AuditModel):
    code = CodeField()
    name = NameField()

    class Meta:
        abstract = True


class BaseRefShort1(AuditModel):
    code = CodeField()
    description = DescriptionField()

    class Meta:
        abstract = True


class BaseRef2(AuditModel):
    name = NameField()
    description = DescriptionField()

    class Meta:
        abstract = True
