from django.db import models
from markdownx.models import MarkdownxField


class TabElement(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='タブの見出し'
    )
    content = MarkdownxField(
        verbose_name='タブの中身',
        help_text='Markdown、HTMLでの記述が可能です。ドラッグアンドドロップで画像の配置もできます。'
    )

    class Meta:
        verbose_name = 'タブ要素'
        verbose_name_plural = 'タブ要素'

    def __str__(self):
        return self.title
