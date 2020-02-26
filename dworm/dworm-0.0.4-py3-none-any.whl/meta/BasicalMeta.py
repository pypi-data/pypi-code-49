from django.db import models


class OldMetaModel(models.Model):
    """兼容旧的表
    
    Args:
        models ([type]): [description]
    """
    data_source = models.TextField(verbose_name="数据来源", null=True)
    download_time = models.DateTimeField(verbose_name="数据更新时间", auto_now=True)
    data_completion = models.FloatField(
        verbose_name="数据完整度", default=0, null=True)
   

    class Meta:
        abstract = True


class BaseMetaModel(models.Model):
    """基础元数据描述
    """
    data_source = models.TextField(verbose_name="数据来源", null=True)
    update_time = models.DateTimeField(verbose_name="数据更新时间", auto_now=True)
    data_completion = models.FloatField(
        verbose_name="数据完整度", default=0, null=True)
    data_richness = models.FloatField(
        verbose_name="数据丰富度", default=0, null=True)
    verified = models.BooleanField(verbose_name="已核对", default=False)
    verified_by = models.CharField(
        verbose_name="核对人员", max_length=10, null=True)
    verified_time = models.DateTimeField(verbose_name="核对时间", null=True)

    class Meta:
        abstract = True
