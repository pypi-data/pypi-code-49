from django.db import models


class DQA(models.Model):

    target = models.CharField(verbose_name="质量评估对象",
                              max_length=255, unique=True)
    total = models.IntegerField(verbose_name="数据总数")
    verfied_count = models.IntegerField(verbose_name="已校验数据条数")
    completed = models.IntegerField(verbose_name="基础信息完整度=1")
    riched = models.IntegerField(verbose_name="数据丰富度 优")
    coverage = models.FloatField(verbose_name="业务数据覆盖度")
    update_time = models.DateTimeField(verbose_name="最后评估时间", auto_now=True)

    class Meta:
        abstract = True
