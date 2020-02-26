from dworm.meta import OldMetaModel as BaseMetaModel
from django.db import models


class MedicineHayo(BaseMetaModel):
    name = models.CharField(verbose_name="药品名称", max_length=255, null=True)
    full_name = models.CharField(
        verbose_name="药品全称", max_length=255, null=True)
    related_id = models.BigIntegerField(verbose_name="相关药品ID", null=True)
    img = models.TextField(verbose_name="图片url", null=True)
    spec = models.CharField(verbose_name="药品规格", max_length=127, null=True)
    approval_number = models.CharField(
        verbose_name="批准文号", max_length=127, null=True)
    manufacture = models.CharField(
        verbose_name="生产厂家", max_length=255, null=True)
    barcode = models.CharField(verbose_name="条形码", max_length=127, null=True)
    manual = models.TextField(verbose_name="说明书")

    class Meta:
        abstract = True
