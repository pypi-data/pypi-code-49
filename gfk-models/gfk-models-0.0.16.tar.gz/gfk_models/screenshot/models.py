from django.db import models
from gfk_models.gfk_base.models import GFKModel
from sorl.thumbnail import ImageField


class Screenshot(GFKModel):
    src = ImageField(upload_to="screenshots/", height_field="height", width_field="width")
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Скриншот'
        verbose_name_plural = 'Скриншоты'

    def __str__(self):
        return str(self.src)
