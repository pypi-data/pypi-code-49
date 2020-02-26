from django.db import models
from dworm.meta import OldMetaModel as BaseMetaModel


class Diseases(BaseMetaModel):
    symptom = models.TextField(verbose_name="疾病症状", null=True)
    detailed_description = models.TextField(verbose_name="详细描述", null=True)
    classification = models.CharField(
        verbose_name="疾病分类", max_length=127, null=True)

    class Meta:
        abstract = True


class CheckUp(BaseMetaModel):
    check_up_name = models.CharField(
        verbose_name="检查项名称", max_length=255, null=True)
    classification = models.TextField(verbose_name="检查类别", null=True)
    price = models.FloatField(verbose_name="检查参考费用", null=True)

    class Meta:
        abstract = True


class Medicines(BaseMetaModel):
    """常用药品
    """
    name = models.CharField(verbose_name="药品名称", max_length=255, null=True)
    related_id = models.TextField(verbose_name="相关药品ID", null=True)

    class Meta:
        abstract = True


class DCM(BaseMetaModel):
    """疾病-检查-药品
    """
    symptom = models.CharField(verbose_name="疾病症状", max_length=255, null=True)
    check_up = models.CharField(
        verbose_name="辅助检查项", max_length=255, null=True)
    medicines = models.TextField(verbose_name="治疗药品", null=True)

    class Meta:
        abstract = True
