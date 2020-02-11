from polymorphic.models import PolymorphicModel


class BaseInquiry(PolymorphicModel):
    class Meta:
        verbose_name = '問い合わせ関連'
        verbose_name_plural = '問い合わせ関連'

    @classmethod
    def create_form(cls):
        raise NotImplementedError()
