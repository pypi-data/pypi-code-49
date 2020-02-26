from dworm.meta import MedicineBaseModel
from django.db import models


class Medicine(MedicineBaseModel):
    pass

    class Meta(MedicineBaseModel.Meta):
        app_label = "collection"
        db_table = "medicine_base"
        verbose_name = "基础药品数据库"
        verbose_name_plural = "基础药品数据库"
        

