from django.core.validators import RegexValidator
from django.db import models
from django import forms
from django.forms.utils import ErrorList

from django_press.models.Inquiry.base import BaseInquiry


class Contact(BaseInquiry):
    class Meta:
        verbose_name = '問い合わせフォーム'
        verbose_name_plural = '問い合わせフォーム'

    @classmethod
    def create_form(cls):
        class Form(forms.ModelForm):
            class Meta:
                model = cls
                exclude = (
                    'created_at',
                    'update_at',
                )

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for name, field in self.fields.items():
                    field.widget.attrs['placeholder'] = field.label
                    field.widget.attrs['class'] = 'form-control'
                    pass

        return Form

    category = models.CharField(
        'お問い合わせカテゴリー',
        max_length=10,
        choices=(
            ('取引について', '取引について'),
            ('資料請求', '資料請求'),
            ('その他', 'その他')
        ),
    )
    name = models.CharField(
        'お名前',
        max_length=20,
    )
    furigana_validator = RegexValidator(
        regex=r'^[ｱ-ﾝア-ン\s・]+$',
        message='カタカナで入力してください。'
    )
    furigana = models.CharField(
        'フリガナ',
        validators=(furigana_validator,),
        max_length=50,
    )
    email = models.EmailField()
    phone_number_validator = RegexValidator(
        regex=r'^[0-9]+$',
        message="ハイフンなしで入力してください"
    )
    phone_number = models.CharField(
        validators=(phone_number_validator,),
        max_length=15,
        verbose_name='電話番号'
    )
    age = models.PositiveSmallIntegerField(
        '年齢',
    )
    body = models.TextField(
        '内容'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:20]
