from django.db import models
from dworm.meta import OldMetaModel as BaseMetaModel


class Medicine315Summary(BaseMetaModel):
    name = models.CharField(verbose_name="药品名称", max_length=255, null=True)
    spec = models.CharField(verbose_name="药品规格", max_length=63, null=True)
    approval_number = models.CharField(
        verbose_name="批准文号", max_length=127, null=True)
    manufacture = models.CharField(
        verbose_name="生产厂家", max_length=255, null=True)
    img_small = models.TextField(verbose_name="缩略图", null=True)
    page = models.IntegerField(verbose_name="数据所在页", null=True)
    index = models.IntegerField(verbose_name="所在页位置", null=True)
    detail_url = models.TextField(verbose_name="详情页", null=True)

    class Meta:
        abstract = True


class Medicine315(BaseMetaModel):
    mid = models.UUIDField(verbose_name="mid")
    name = models.CharField(verbose_name="药品名称", max_length=255, null=True)
    spec = models.CharField(verbose_name="药品规格", max_length=63, null=True)
    approval_number = models.CharField(
        verbose_name="批准文号", max_length=127, null=True)
    manufacture = models.CharField(
        verbose_name="生产厂家", max_length=255, null=True)
    classification = models.CharField(
        verbose_name="药品分类", max_length=127, null=True)
    full_name = models.CharField(
        verbose_name="药品名称(带厂家名称)", max_length=255, null=True)
    is_otc = models.BooleanField(verbose_name="是否为非处方药", null=True)
    price = models.FloatField(verbose_name="建议零售价", null=True)
    wholesale_price = models.FloatField(verbose_name="批发价格", null=True)
    barcode = models.CharField(verbose_name="条形码", max_length=127, null=True)
    abbreviation = models.CharField(
        verbose_name="拼音缩写", max_length=63, null=True)
    img = models.TextField(verbose_name="大图", null=True)
    drug_type = models.CharField(verbose_name="剂型", max_length=63, null=True)
    pack_unit = models.CharField(
        verbose_name="包装单位", max_length=63, null=True)
    function = models.TextField(verbose_name="主治疾病", null=True)
    manual = models.TextField(verbose_name="说明书", null=True)
    min_spec = models.CharField(verbose_name="最小规格", max_length=31, null=True)

    class Meta:
        abstract = True


class MedicineMarked(BaseMetaModel):
    name = models.CharField(verbose_name="药品名称", max_length=255, null=True)
    spec = models.CharField(verbose_name="药品规格", max_length=63, null=True)
    approval_number = models.CharField(
        verbose_name="批准文号", max_length=127, null=True)
    manufacture = models.CharField(
        verbose_name="生产厂家", max_length=255, null=True)
    barcode = models.CharField(verbose_name="条形码", max_length=127, null=True)
    related_id = models.IntegerField(verbose_name="药品库所在ID", null=True)
    img = models.TextField(verbose_name="图片", null=True)

    class Meta:
        abstract = True
