
from django.db import models

class MedicineChangping(models.Model):
    code = models.CharField(verbose_name="昌平数据库中的商品编码",
                            max_length=127, null=True)
    name = models.CharField(verbose_name="药品通用名称", max_length=255, null=True)
    prod_name = models.CharField(
        verbose_name="商品名称", max_length=255, null=True)
    spec = models.CharField(verbose_name="药品规格", max_length=255, null=True)
    approval_number = models.CharField(
        verbose_name="批准文号", max_length=255, null=True)
    manufacture = models.CharField(
        verbose_name="生产厂家", max_length=255, null=True)
    origin = models.TextField(verbose_name="产地", null=True)
    barcode = models.CharField(verbose_name="条形码", max_length=255, null=True)
    brand = models.CharField(verbose_name="品牌", max_length=255, null=True)
    storage = models.CharField(verbose_name="储存条件", max_length=127, null=True)
    related_id = models.UUIDField(verbose_name="关联主库药品id", null=True)
    data_source = models.CharField(
        verbose_name="数据来源", max_length=255, null=True)

    class Meta:
        abstract = True