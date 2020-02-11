from django.db import models


class Product(models.Model):
    icon = models.CharField(
        max_length=100,
        verbose_name='icon class',
        help_text='https://icofont.com/icons 参照',
        default='icofont icofont-light-bulb',
    )
    name = models.CharField(
        max_length=30,
        verbose_name='サービス名',
    )
    description = models.TextField(
        verbose_name='説明',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '紹介する系'
        verbose_name_plural = '紹介する系'
