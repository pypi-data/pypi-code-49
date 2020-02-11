from django.db import models
import importlib
from markdownx.models import MarkdownxField
from polymorphic.models import PolymorphicModel

from django_press.models.Inquiry.base import BaseInquiry
from django_press.models.page.componets.files import ImageFile
from django_press.models.page.componets.service import Product
from django_press.models.page.componets.tab import TabElement
from django_press.models.page.page import Page


class PageContent(PolymorphicModel):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE, related_name='contents')
    priority = models.PositiveSmallIntegerField(
        verbose_name='ページ内の表示順(昇順)',
        default=1,
        help_text='同じページ内では数値の重複を避けてください。\n'
                  '0~32767の整数値で入力してください。\n'
                  '小さい数字ほど上に来ます'
    )

    class Meta:
        ordering = ('priority',)
        verbose_name = 'ページの構成要素'
        verbose_name_plural = 'ページの構成要素'


class PageText(PageContent):
    template_name = 'django_press/fields/content.html'
    content = MarkdownxField(
        verbose_name='本文',
        help_text='Markdown、HTMLでの記述が可能です。ドラッグアンドドロップで画像の配置もできます。'
    )

    class Meta:
        verbose_name = '文章と画像に最適'


class ImageSlider(PageContent):
    template_name = 'django_press/fields/featured.html'
    content = models.ManyToManyField(
        to=ImageFile,
        verbose_name='画像',
    )

    class Meta:
        verbose_name = '画像のスライドショー'

    @property
    def images(self):
        return self.content.all()


class Service(PageContent):
    template_name = 'django_press/fields/service.html'
    title = models.CharField(
        max_length=30,
        verbose_name='見出し',
    )
    abstract = models.TextField(
        verbose_name='概要',
        help_text='Markdown、HTMLでの記述が可能です。2,3行ぐらいが好ましいです。'
    )

    products = models.ManyToManyField(
        to=Product,
        verbose_name='サービス',
    )

    class Meta:
        verbose_name = 'サービスなどを伝える'

    @property
    def products_all(self):
        return self.products.all()


class Tab(PageContent):
    template_name = 'django_press/fields/tab.html'
    name = models.CharField(max_length=50, null=True)
    tabs = models.ManyToManyField(
        to=TabElement,
        verbose_name='タブ要素',
    )

    class Meta:
        verbose_name = 'タブを使う'

    def __str__(self):
        return self.name

    @property
    def tabs_all(self):
        return self.tabs.all()


class ContactContent(PageContent):
    template_name = 'django_press/fields/contact.html'

    form = models.CharField(
        max_length=100,
        choices=((inquiry.__module__, inquiry.__name__) for inquiry in BaseInquiry.__subclasses__())
    )

    success_page = models.ForeignKey(
        to='Page',
        on_delete=models.PROTECT,
        default=1
    )

    def get_inquiry_model(self):
        module = importlib.import_module(self.form)
        return getattr(module, self.get_form_display())

    def get_inquiry_form_class(self):
        return self.get_inquiry_model().create_form()

    @property
    def form_instance(self):
        return self.get_inquiry_form_class()()

    class Meta:
        verbose_name = '問い合わせを使う'
