from dworm.meta import OldMetaModel as BaseMetaModel
from django.db import models


class MedicineKzj(BaseMetaModel):
    name = models.CharField(verbose_name="药品名称", max_length=255, null=True)
    spec = models.CharField(verbose_name="药品规格", max_length=255, null=True)
    approval_number = models.CharField(
        verbose_name="批准文号", max_length=255, null=True)
    manufacture = models.CharField(
        verbose_name="生产厂家", max_length=255, null=True)
    classification = models.CharField(
        verbose_name="药品分类", max_length=127, null=True)
    full_name = models.CharField(
        verbose_name="药品名称(带厂家名称)", max_length=255, null=True)
    is_otc = models.BooleanField(verbose_name="是否为非处方药", null=True)
    price = models.FloatField(verbose_name="建议零售价【原价】", null=True)
    sale_price = models.FloatField(verbose_name="批发价格", null=True)
    img = models.TextField(verbose_name="药品图片", null=True)
    function = models.TextField(verbose_name="主治疾病", null=True)
    manual = models.TextField(verbose_name="说明书", null=True)
    profile = models.TextField(verbose_name="商品信息", null=True)
    brand = models.CharField(verbose_name="商品品牌", max_length=127, null=True)

    class Meta:
        abstract = True
