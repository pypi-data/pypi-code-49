from markdownx.admin import MarkdownxModelAdmin
from django_press.models import PageContent, PageText, ImageSlider, Service, Tab, ContactContent
from polymorphic.admin import StackedPolymorphicInline, PolymorphicInlineSupportMixin


class PageContentInline(StackedPolymorphicInline):
    class PageTextInline(StackedPolymorphicInline.Child):
        model = PageText

    class ImageSliderInline(StackedPolymorphicInline.Child):
        model = ImageSlider

    class ServiceInline(StackedPolymorphicInline.Child):
        model = Service

    class TabInline(StackedPolymorphicInline.Child):
        model = Tab

    class ContactInline(StackedPolymorphicInline.Child):
        model = ContactContent

    model = PageContent
    child_inlines = (
        PageTextInline,
        ImageSliderInline,
        ServiceInline,
        TabInline,
        ContactInline,
    )


class PageAdmin(PolymorphicInlineSupportMixin, MarkdownxModelAdmin):
    inlines = [PageContentInline, ]
    pass
