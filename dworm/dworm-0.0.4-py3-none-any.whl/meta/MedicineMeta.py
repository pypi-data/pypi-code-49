from dworm.meta.BasicalMeta import BaseMetaModel
from django.db import models


class MedicineBaseModel(BaseMetaModel):
    """基础药品信息描述 
    基础字段 不可或缺: 名规厂号类码功图书
    """
    mid = models.UUIDField(verbose_name="药品ID")
    name = models.CharField(verbose_name="通用名称", max_length=255, blank=False)
    # 商品名称往往是 通用名称+品牌名称 的组合, 或者 奇怪的自定义名字
    prod_name = models.CharField(
        verbose_name="商品名称", max_length=255, null=True)
    abbreviation = models.CharField(
        verbose_name="首字母缩写", max_length=255, blank=True)
    spec = models.CharField(verbose_name="规格", max_length=255, null=True)

    # 最小规格理论上是可计算的, 可以由spec生成
    spec_min = models.CharField(verbose_name="最小规格", max_length=255, null=True)

    drug_type = models.CharField(verbose_name="剂型", max_length=255, null=True)
    pack_unit = models.CharField(
        verbose_name="包装单位", max_length=255, null=True)
    storage = models.CharField(verbose_name="储藏", max_length=255, null=True)
    brand = models.CharField(verbose_name="品牌", max_length=255, null=True)

    approval_number = models.CharField(
        verbose_name="批准文号", max_length=255, null=True)
    barcode = models.CharField(verbose_name="条形码", max_length=255, null=True)

    manufacture = models.CharField(
        verbose_name="生产厂家", max_length=255, null=True)
    origin = models.CharField(
        verbose_name="产地", max_length=255, null=True)
    # 药品的分类标签, 用逗号分隔
    tag = models.TextField(verbose_name="分类标签", null=True)
    # 处方与非处方分类
    ro = models.CharField(verbose_name="处方分类", max_length=64,
                          choices=(('rx', '处方'), ('otc', '非处方'), ('--', '未定义')), null=True)

    function = models.TextField(verbose_name="功能主治")

    # 说明书存字典转字符串
    manual = models.TextField(verbose_name="说明书")

    # 药品图片多张以逗号间隔
    img = models.TextField(verbose_name="药品图片")

    def compute_completion(self):
        """计算基础信息完整度及丰富度
        """
        # 计算数据完整度
        keys = ('name', 'spec', 'manufacture',
                'approval_number', 'ro', 'barcode', 'img', 'function', 'manual')

        empty_key = 0
        for key in keys:
            value = self.__dict__.get(key, None)
            if not value:
                empty_key += 1

        completion = 1 - empty_key/len(keys)

        self.data_completion = completion

        # 计算数据丰富度
        options = ('prod_name', 'drug_type', 'pack_unit',
                   'storage', 'brand', 'origin', 'tag')
        empty_option = 0
        for option in options:
            value = self.__dict__.get(option, None)
            if not value:
                empty_option += 1

        richness = 1 - empty_option/len(options)

        self.data_richness = richness

        self.save()

    class Meta:
        abstract = True
        constraints = [models.UniqueConstraint(
            fields=["name", "spec", "approval_number", "manufacture"], name='unique_medicine')]